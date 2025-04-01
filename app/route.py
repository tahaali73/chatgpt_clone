from app import app
from flask import render_template, request, jsonify

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api',methods=['GET', 'POST'])
def qa():
    if request.method == "POST":  
        question=request.get_json()
        data = {"result":question['question']}
        print(data)
        return jsonify(data)
    
    return jsonify(data)