# Core
from flask import Flask, request

# Repositories
from src.repositories.users import UserRepository

# Libs
from dotenv import load_dotenv
import os


# Config App
load_dotenv()
app = Flask(__name__)

# Routes
@app.route("/", methods=["GET"])
def hello_word():
    return f'Hello, ${os.getenv("POSTGRES_USER")}'

@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepository()
    body = request.json
    userRepo.insert_user(body["name"])

    return "OK"

