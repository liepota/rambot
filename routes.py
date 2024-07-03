from flask import Blueprint, request, jsonify
from app.game_logic import process_click

main = Blueprint('main', __name__)

users = {}

@main.route('/')
def index():
    return "Hello, this is Ramble Coin!"

@main.route('/click', methods=['POST'])
def click():
    user_id = request.json.get('user_id')
    if user_id not in users:
        users[user_id] = {"coins": 0, "upgrades": 0}
    
    users[user_id] = process_click(users[user_id])
    
    return jsonify({"success": True, "message": "Coin added!", "coins": users[user_id]["coins"], "upgrades": users[user_id]["upgrades"]})

