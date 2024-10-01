# import re
# from telegram.ext import Updater, CommandHandler, MessageHandler

# # Set up Telegram connection
# bot_token = "7722973135:AAFmHSTmqT5kQs6Ek4_GrI6lbSILkjw0QA8"
# chat_id = 5789453415

# # Create a Telegram bot instance
# updater = Updater(bot_token)
# # Get the conversation history
# updates = updater.bot.get_updates(chat_id=chat_id, offset=0)

# # Parse the messages to extract text content
# messages = []
# for update in updates:
#     message = update.message
#     if message:
#         text = message.text
#         if text:
#             messages.append(text)

# # Convert the messages to lowercase
# messages_lower = [message.lower() for message in messages]

# # Define the phrases to search for
# phrases = ["playing soccer", "basketball", "tennis", "football"]

# # Use the regular expression pattern to find the phrases
# phrase_patterns = [re.escape(phrase.lower()) for phrase in phrases]
# pattern = re.compile(r'\b(' + '|'.join(phrase_patterns) + r')[.,;:]?\b', re.IGNORECASE)
# found_phrases = [phrase for phrase in phrases if any(pattern.search(message) for message in messages_lower)]

# print("Found phrases:", found_phrases)





from telegram import Bot
import re
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.utils.request import Request
from telegram import Update
from queue import Queue

# Create a Bot object
bot_token = "7722973135:AAFmHSTmqT5kQs6Ek4_GrI6lbSILkjw0QA8"
request = Request(con_pool_size=8)
bot = Bot(bot_token, request)

# Create an update queue
update_queue = Queue()

# Create the Updater object
updater = Updater(bot_token, update_queue)

# Set up Telegram connection
bot_token = "7722973135:AAFmHSTmqT5kQs6Ek4_GrI6lbSILkjw0QA8"
chat_id = 5789453415

try:
    # Create a Telegram bot instance
    updater = Updater(bot_token, update_queue)

    # Get the conversation history
    updates = updater.bot.get_updates(chat_id=chat_id, offset=0)

    # Parse the messages to extract text content
    messages = []
    for update in updates:
        message = update.message
        if message:
            text = message.text
            if text:
                messages.append(text)

    # Convert the messages to lowercase
    messages_lower = [message.lower() for message in messages]

    # Define the phrases to search for
    phrases = ["playing soccer", "basketball", "tennis", "football"]

    # Use the regular expression pattern to find the phrases
    phrase_patterns = [re.escape(phrase.lower()) for phrase in phrases]
    pattern = re.compile(r'\b(' + '|'.join(phrase_patterns) + r')[.,;:]?\b', re.IGNORECASE)
    found_phrases = [phrase for phrase in phrases if any(pattern.search(message) for message in messages_lower)]

    print("Found phrases:", found_phrases)

except Exception as e:
    print("An error occurred:", e)