from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot(
    'StudyBOT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3_eng',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            "import_path": "chatterbot.logic.BestMatch",
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
preprocessors=
    [
    'chatterbot.preprocessors.clean_whitespace',
    'chatterbot.preprocessors.unescape_html',
    'chatterbot.preprocessors.convert_to_ascii'
    ]
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return str(bot.get_response(user_input))


if __name__ == "__main__":
    app.run()