import random

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
import time

time.clock = time.time()

chatbot = ChatBot('HAL', preprocessors=['chatterbot.preprocessors.clean_whitespace'],
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                  'chatterbot.logic.BestMatch'],
                  database_uri='sqlite:///database.db',
                  response_selection_method=get_random_response)

trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english.greetings")
# trainer.train('./places.yml')

resp_list = ["Think you will like", "How about", "Hmmm..."]
print("Hey, my name is Berry, i am loving collecting beautiful places \n"
      "all over the world into my collection! Write down a country, \n"
      "and I`ll answer what places you definitely should visit! :)")
while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        resp = random.choice(resp_list)
        print(resp, bot_response)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break