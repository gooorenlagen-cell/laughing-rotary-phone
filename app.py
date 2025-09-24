from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)

greetings = [
    "Привет!",
        "Здарова!"
    ]

@app.route("/")
def index():
    greeting = random.choice(greetings)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_number = random.randint(1, 100)
    return f"{greeting} Сейчас: {now}. Случайное число: {random_number}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)