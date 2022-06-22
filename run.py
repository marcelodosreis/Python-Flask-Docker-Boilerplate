from crypt import methods
from flask import Flask, request
from src.repositories.users import UserRepository


app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_word():
    return "Hello World!"

@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepository()
    body = request.json
    userRepo.insert_user(body["name"])

    return "OK"