from flask import Flask, request, jsonify
from game_engine import StoryEngine

app = Flask(__name__)
engine = StoryEngine("/path/to/pretrained/model")

@app.route('/generate', methods=['POST'])
def generate_story():
    data = request.json
    result = engine.generate_story(
        data.get('input', ''),
        data.get('story_type', 1),
        data.get('character', 1)
    )
    return jsonify(result)

@app.route('/save', methods=['POST'])
def save_game():
    engine.save_state()
    return jsonify({"status": "success"})

@app.route('/load', methods=['GET'])
def load_game():
    engine.load_state()
    return jsonify(engine.game_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)