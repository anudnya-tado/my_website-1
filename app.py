from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Anudnya:anudnya1@anns.cvxkuxx.mongodb.net/loginDB?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)
db = client['loginDB']
users = db['users']  # Make sure your collection is named 'users'

@app.route('/')
def home():
    return render_template('index1.html') # Make sure this file is in the templates folder

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users.find_one({'username': username, 'password': password})
    if user:
        return f"✅ Welcome, {username}!"
    else:
        return "❌ Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True)
