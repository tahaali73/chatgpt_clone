from app import app, mongo, client
from flask import render_template, request, jsonify

@app.route("/")
def home():
    chats = mongo.db.chat.find({})
    mychats = [chat for chat in chats]
    return render_template("index.html", mychats=mychats)

@app.route('/api',methods=['GET', 'POST'])
def qa():
    if request.method == "POST":  
        question=request.json.get("question")
        chat = mongo.db.chat.find_one({"question": question})
        if chat:
            data = {"result":f"{chat['answer']}"}
            return jsonify(data)
        else:
            
            completion = client.chat.completions.create(
            
            model="openai/gpt-4o",
            messages=[
            {
            "role": "user",
            "content": "What is the meaning of life?"
            }])
            print(completion.choices[0].message.content)

            
            mongo.db.chat.insert_one({"question": question, "answer": "answer from open ai"})
            return jsonify(data)
    data = {"result":"this out of db question"}
    
    return jsonify(data)