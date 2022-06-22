# Core
from flask import Flask, request

# Repositories
from src.repositories.users import UserRepository

# Libs
from dotenv import load_dotenv


# Config App
load_dotenv()
app = Flask(__name__)

# Routes
@app.route("/", methods=["GET"])
def hello_word():
    return 'Hello World'

@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepository()
    userRepo.insert_user(request.json["name"])

    return "OK"

