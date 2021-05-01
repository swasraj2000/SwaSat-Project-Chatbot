from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import os

# Creating a chatbot Instance
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

# locate training folder
directory = 'training_data'

for filename in os.listdir(directory):
    
        print('\n Chatbot training with '+os.path.join(directory, filename)+' file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(bot) # bot training
        trainer.train(training_data)
    


trainer_corpus = ChatterBotCorpusTrainer(bot)
trainer_corpus.train('chatterbot.corpus.english')