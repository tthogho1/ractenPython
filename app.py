import os
import json
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from component.lib import get_assistant
from pinecone_plugins.assistant.models.chat import Message
from flask_socketio import SocketIO, emit

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json['message']
        assistant = get_assistant()
        msg = Message(content=message)
        
        #result = assistant.chat(messages=[msg])
        chanks = assistant.chat(messages=[msg],stream=True)
        
        for chunk in chanks:
            #json_data = chunk.split("data:")[1]
            print(chunk)
            if chunk.type == "content_chunk" :
                socketio.emit('message', chunk.delta.content)
            elif chunk.type == "message_start" :
                socketio.emit('message', "$$start$$")
            elif chunk.type == "message_end" :
                socketio.emit('message', "$$stop$$")
        
        # 回答
        answer = "end" #esult['message']['content']
                
        return jsonify({
            'answer': answer,
        })

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
