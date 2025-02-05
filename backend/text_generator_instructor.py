import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime
import json
import os

class StoryGenerator:
    """
    基于《西游记》主题的AI冒险游戏生成器
    实现类似AI Dungeon的交互式叙事功能
    """
    
    def __init__(self, model_path="/home/gzy/google/pretrain_model/Gemma-2-9B-Chinese-Chat"):
        self.model_path = model_path
        self.history_max_length = 5
        self.session_file = "game_session.json"

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map=self.device,
            torch_dtype=self.dtype
        )

        self.game_state = {
            "background": self.default_background(),
            "history": [],
            "current_scene": None,
            "characters": {
                "孙悟空": {"位置": "火焰山入口", "状态": "准备战斗"},
                "唐僧": {"位置": "安全区域", "状态": "等待"}
            }
        }
        

        self.system_prompt = """
        你是一个专业级的《西游记》叙事引擎，需要根据玩家的输入生成符合以下要求的游戏内容：
        
        1. 叙事风格：
        - 严格保持章回体小说格式
        - 使用明清白话文与现代汉语结合的风格
        - 每段包含环境描写、人物动作和对话
        - 保持情节的戏剧冲突和道教佛教元素
        
        2. 游戏机制：
        - 每次生成400-600字的独立章节
        - 每个章节结尾提供3个可选行动选项，也可以让玩家自己输入如何让游戏如何发展
        - 合理推进故事发展，保持逻辑连贯
        - 根据玩家选择动态调整难度（0.1-0.9）
        
        3. 角色设定：
        - 孙悟空：机智好斗但尊重师父
        - 唐僧：仁慈坚定但易受欺骗
        - 妖怪：各具特色且动机合理
        
        当前故事阶段：火焰山篇
        """

    def default_background(self):
        """默认故事背景"""
        return {
            "location": "火焰山",
            "time": "唐朝贞观年间",
            "objective": "取得芭蕉扇，熄灭火焰山之火",
            "current_challenge": "牛魔王率众妖把守山口",
            "previous_events": ["师徒四人抵达山脚", "土地神告知芭蕉扇情报"]
        }

    def build_prompt(self, user_input):
        """
        构建符合模型要求的输入提示
        包含：系统指令 + 游戏状态 + 历史记录 + 当前输入
        """
        prompt = [{"role": "system", "content": self.system_prompt}]
        
        state_summary = f"""当前游戏状态：
        位置：{self.game_state['background']['location']}
        任务：{self.game_state['background']['objective']}
        角色状态：
        - 孙悟空：{self.game_state['characters']['孙悟空']['状态']}
        - 唐僧：{self.game_state['characters']['唐僧']['位置']}
        """
        prompt.append({"role": "assistant", "content": state_summary})
        
        for entry in self.game_state["history"][-3:]:
            prompt.append({"role": "user", "content": entry["input"]})
            prompt.append({"role": "assistant", "content": entry["response"]})
        
        prompt.append({"role": "user", "content": user_input})
        
        return prompt

    def generate_text(self, user_input, max_length=600, temperature=0.7):
        """
        生成故事内容并更新游戏状态
        """
        try:
            full_prompt = self.build_prompt(user_input)
            
            input_ids = self.tokenizer.apply_chat_template(
                full_prompt,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt"
            ).to(self.device)
            
            generation_config = {
                "max_new_tokens": max_length,
                "do_sample": True,
                "temperature": temperature,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "pad_token_id": self.tokenizer.eos_token_id
            }
            
            outputs = self.model.generate(input_ids, **generation_config)
            
            response = self.tokenizer.decode(
                outputs[0][input_ids.shape[-1]:], 
                skip_special_tokens=True
            )
            
            self.update_game_state(user_input, response)
            
            return response
        
        except Exception as e:
            raise RuntimeError(f"生成失败: {str(e)}")

    def update_game_state(self, user_input, response):
        """更新游戏状态和历史记录"""
        self.game_state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "response": response
        })
        
        if len(self.game_state["history"]) > self.history_max_length:
            self.game_state["history"] = self.game_state["history"][-self.history_max_length:]
        
        # 解析响应中的状态更新（示例）
        if "获得" in response:
            self.game_state["characters"]["孙悟空"]["状态"] = "获得新物品"
        if "受伤" in response:
            self.game_state["characters"]["孙悟空"]["状态"] = "受伤状态"

    def save_game_state(self):
        with open(self.session_file, 'w', encoding='utf-8') as f:
            json.dump(self.game_state, f, ensure_ascii=False, indent=2)

    def load_game_state(self):
        if os.path.exists(self.session_file):
            with open(self.session_file, 'r', encoding='utf-8') as f:
                self.game_state = json.load(f)

class GameInterface:
    """游戏交互界面"""
    
    def __init__(self, generator):
        self.generator = generator
        self.commands = {
            "/save": self.save_game,
            "/load": self.load_game,
            "/status": self.show_status
        }
    
    def start_game(self):
        print("欢迎来到《西游记》AI冒险游戏！")
        print("输入 '/help' 查看可用命令")
        print("\n当前故事背景：")
        print(self.format_background())
        
        while True:
            try:
                user_input = input("\n请输入指令/动作：").strip()
                
                if not user_input:
                    continue
                
                # 处理特殊命令
                if user_input.startswith('/'):
                    self.handle_command(user_input)
                    continue
                
                if user_input.lower() in ['exit', 'end', '退出']:
                    print("游戏结束，期待下次再会！")
                    self.generator.save_game_state()
                    break
                
                # 生成故事内容
                response = self.generator.generate_text(user_input)
                print("\n" + self.format_response(response))
                
                # 自动保存进度
                self.generator.save_game_state()
            
            except Exception as e:
                print(f"发生错误：{str(e)}")

    def format_background(self):
        """格式化背景故事显示"""
        bg = self.generator.game_state["background"]
        return f"""
        🌋 地点：{bg['location']}
        ⏳ 时间：{bg['time']}
        🎯 目标：{bg['objective']}
        🚩 当前挑战：{bg['current_challenge']}
        📜 已发生事件：{" → ".join(bg['previous_events'])}
        """

    def format_response(self, response):
        """美化输出格式"""
        return f"""
        {'='*40}
        📖 故事发展：
        {response}
        {'='*40}
        """

    def handle_command(self, command):
        """处理系统命令"""
        cmd = command.split()[0].lower()
        if cmd in self.commands:
            self.commands[cmd]()
        else:
            print("可用命令：")
            print("/save - 保存当前进度")
            print("/load - 加载上次进度")
            print("/status - 显示当前状态")
            print("/help - 显示帮助信息")

    def save_game(self):
        self.generator.save_game_state()
        print("游戏进度已保存！")

    def load_game(self):
        self.generator.load_game_state()
        print("游戏进度已加载！")
        print(self.format_background())

    def show_status(self):
        print("\n当前角色状态：")
        for char, state in self.generator.game_state["characters"].items():
            print(f"{char}:")
            for k, v in state.items():
                print(f"  {k}: {v}")

if __name__ == "__main__":
    generator = StoryGenerator()
    
    if os.path.exists(generator.session_file):
        choice = input("检测到存档文件，是否加载？(y/n): ")
        if choice.lower() == 'y':
            generator.load_game_state()

    interface = GameInterface(generator)
    interface.start_game()