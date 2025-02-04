from flask import Flask, jsonify, request, redirect, url_for
import torch
app = Flask(__name__)
import openai
import requests
from openai import OpenAI
import os
# Set the API key directly
#openai.api_key = "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"
openai.api_key ="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"
os.environ["OPENAI_API_KEY"] = "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"
generating_times = 0
SETTING = {}
sentence_history = []
# 示例游戏数据
game_state = {
    "player": {
        "name": "Hero",
        "position": {"x": 0, "y": 0}
    },
    "enemies": [
        {"name": "Goblin", "position": {"x": 5, "y": 5}},
        {"name": "Orc", "position": {"x": 10, "y": 10}}
    ]
}

# 示例用户数据
users = {
    "zzq": "123"
}

@app.route('/game_background', methods=['GET'])
def get_game_state():
    global generating_times
    data = request.json
    prompt = data.get('prompt')
    client = OpenAI()
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1792x1024",
    quality="standard",
    n=1,
    )
    image_data = requests.get(response.data[0].url).content
    with open(str(generating_times)+".png", 'wb') as file:
        file.write(image_data)

    print("图像已成功下载并保存为 'siamese_cat.png'")
    return jsonify(game_state)

# @app.route('/move_player', methods=['POST'])
# def move_player():
#     direction = request.json.get('direction')
#     if direction == 'up':
#         game_state['player']['position']['y'] += 1
#     elif direction == 'down':
#         game_state['player']['position']['y'] -= 1
#     elif direction == 'left':
#         game_state['player']['position']['x'] -= 1
#     elif direction == 'right':
#         game_state['player']['position']['x'] += 1
#     return jsonify(game_state)
@app.route('/story_choosing', methods=['POST'])
def story_choosing1():
    global SETTING
    data = request.json
    username = data.get('choice')
    print(username)
    SETTING['story_choice'] = data.get('choice')
    return jsonify({"status": "Success", "message": "Success"})
@app.route('/setting_choosing', methods=['POST'])
def setting_choosing1():
    global SETTING
    data = request.json
    username = data.get('choice')
    print(username)
    SETTING['setting_choice'] = data.get('choice')
    return jsonify({"status": "Success", "message": "Success"})

@app.route('/character_choosing', methods=['POST'])
def character_choosing1():
    global SETTING
    data = request.json
    username = data.get('choice')
    print(username)
    SETTING['character_choice'] = data.get('choice')
    return jsonify({"status": "Success", "message": "Success"})
@app.route("/model_main",methods = ["POST"])
def model_sentence():
    global sentence_history
    reply = ''
    return jsonify({"reply": reply,"flag":"Y" if len(sentence_history)%3 == 0 and len(sentence_history) != 0 else "N"})
if __name__ == '__main__':
    app.run(debug=True)
