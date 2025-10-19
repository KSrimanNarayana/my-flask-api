# save this as app.py
from flask import Flask, jsonify

app = Flask(__name__)

# define your API endpoint
@app.route("/api/mydata")
def my_data():
    data = {
        "project": "Chatbot",
        "author": "Sriman Narayana",
        "language": "Python",
        "year": 2025
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
