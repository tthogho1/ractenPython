from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from component.lib import get_assistant
from pinecone_plugins.assistant.models.chat import Message

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json['message']
        assistant = get_assistant()
        msg = Message(content=message)
        result = assistant.chat(messages=[msg])
        
        # 回答を取得
        answer = result['message']['content']
                
        return jsonify({
            'answer': answer,
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
