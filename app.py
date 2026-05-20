from flask import Flask, render_template, request

app = Flask(__name__)


def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to Rhombix AI Assistant 🤖"

    elif "cloud" in user_input:
        return "Cloud computing provides scalable and on-demand computing services over the internet."

    elif "cybersecurity" in user_input:
        return "Cybersecurity helps protect systems, networks, and applications from digital attacks."

    elif "python" in user_input:
        return "Python is widely used in AI, automation, cybersecurity, and cloud development."

    elif "flask" in user_input:
        return "Flask is a lightweight Python framework used to build web applications."

    elif "internship" in user_input:
        return "This chatbot project was developed during the Rhombix Technologies internship program."

    elif "bye" in user_input:
        return "Thank you for visiting! Have a great day 👋"

    else:
        return "I can help you with cloud computing, cybersecurity, Python, and Flask."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
