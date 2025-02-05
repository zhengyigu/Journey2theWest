import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime
import json
import os

class StoryEngine:
    """增强版西游游戏引擎"""
    
    def __init__(self, model_path):
        self.model_path = model_path
        self.history_max_length = 5
        self.session_file = "game_session.json"
        
        # 初始化模型
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map=self.device,
            torch_dtype=self.dtype
        )
        
        # 游戏状态管理
        self.game_state = {
            "current_story": 1,      # 当前故事线
            "selected_character": 1, # 选择角色
            "background": self._default_background(),
            "history": [],
            "inventory": [],
            "difficulty": 0.5
        }

    def _default_background(self):
        """动态生成故事背景"""
        return {
            "locations": ["火焰山", "狮驼岭", "盘丝洞"],
            "current_location": 0,
            "objectives": ["取得芭蕉扇", "降服青狮精", "解救唐僧"],
            "characters": {
                "孙悟空": {"状态": "战斗准备", "技能": ["七十二变", "筋斗云"]},
                "唐僧": {"状态": "等待", "技能": ["紧箍咒"]}
            }
        }

    def generate_story(self, user_input, story_type=1, character=1):
        """生成故事内容"""
        try:
            prompt = self._build_prompt(user_input, story_type, character)
            
            input_ids = self.tokenizer.apply_chat_template(
                prompt,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt"
            ).to(self.device)
            
            outputs = self.model.generate(
                input_ids,
                max_new_tokens=600,
                do_sample=True,
                temperature=0.7 + self.game_state["difficulty"]*0.2,
                top_p=0.9,
                repetition_penalty=1.1
            )
            
            response = self.tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
            self._update_state(user_input, response)
            
            return {
                "status": "success",
                "story": response,
                "options": self._extract_options(response),
                "state": self.game_state
            }
            
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _build_prompt(self, user_input, story_type, character):
        """构建提示词模板"""
        prompt = [
            {"role": "system", "content": self._system_prompt(story_type, character)},
            {"role": "assistant", "content": self._state_summary()}
        ]
        
        # 添加上下文历史
        for entry in self.game_state["history"][-3:]:
            prompt.append({"role": "user", "content": entry["input"]})
            prompt.append({"role": "assistant", "content": entry["response"]})
            
        prompt.append({"role": "user", "content": user_input})
        return prompt

    def _system_prompt(self, story_type, character):
        """动态系统提示词"""
        prompts = {
            1: "火焰山篇 - 重点描写高温环境和与牛魔王的对抗",
            2: "狮驼岭篇 - 强调三魔王的狡诈和团队协作",
            3: "真假美猴王篇 - 注重心理描写和身份谜题"
        }
        return f"""
        你正在创作《西游记》的{prompts[story_type]}章节，需遵循：
        1. 使用章回体格式，包含对仗工整的回目
        2. 每次生成400-600字，包含环境、动作和对话
        3. 结尾提供3个符合角色{character}特性的选项
        4. 难度系数：{self.game_state['difficulty']}/1.0
        5. 当前物品：{', '.join(self.game_state['inventory'])}
        """

    def _update_state(self, user_input, response):
        """更新游戏状态"""
        self.game_state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "response": response
        })
        
        # 状态自动更新规则
        if "获得" in response:
            item = response.split("获得")[1].split("。")[0].strip()
            self.game_state["inventory"].append(item)
        if "受伤" in response:
            self.game_state["difficulty"] = max(0.1, self.game_state["difficulty"]-0.1)
        else:
            self.game_state["difficulty"] = min(0.9, self.game_state["difficulty"]+0.1)

    def save_state(self):
        """保存游戏状态"""
        with open(self.session_file, 'w') as f:
            json.dump(self.game_state, f)

    def load_state(self):
        """加载游戏状态"""
        if os.path.exists(self.session_file):
            with open(self.session_file, 'r') as f:
                self.game_state = json.load(f)