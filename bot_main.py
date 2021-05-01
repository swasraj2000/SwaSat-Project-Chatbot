from chatterbot import ChatBot

# Create a new instance of a ChatBot
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

# Get a response for some unexpected input
name = input('Enter Your Name: ')
print('Welcome to Chatbot Service! Let me know how can I help you')
while True:

    request = input(name + ':')

    if request == "Bye" or request == 'bye':
        print('Bot: Bye')
        break
    else:
        response = bot.get_response(request)
        print('Bot: ', response)