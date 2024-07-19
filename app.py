from flask import Flask, request, jsonify, render_template
from rules import RuleBot

app = Flask(__name__)
bot = RuleBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = bot.chat(user_input.lower())
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
