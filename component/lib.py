import openai
import os
import dotenv
from pinecone import Pinecone

# .envの読み込み
dotenv.load_dotenv()

pinecone_key = os.environ['PINECONE_API_KEY']
pc = Pinecone(api_key=pinecone_key)
pinecone_assistant = os.environ['PINECONE_ASSISTANT']

# OpenAI APIキーを設定
openai.api_key = os.environ['OPENAI_API_KEY']
model = os.environ['EMBEDDING_MODEL']

def get_assistant():
    assistant = pc.assistant.Assistant(
        assistant_name= pinecone_assistant, 
    )    
    return assistant

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    return response['data'][0]['embedding']


