from flask import Flask
from flask_pymongo import PyMongo
from openai import OpenAI

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://diytech960:Qmobile888@cluster0.q0ffqok.mongodb.net/chatgpt"
mongo = PyMongo(app)
client = OpenAI(api_key="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",base_url="https://openrouter.ai/api/v1")

from app import route
