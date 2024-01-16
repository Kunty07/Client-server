import yaml
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Scopus Bot. Ask me about Scopus data.')

def handle_scopus_request(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    author_name = update.message.text

    # Sending the user's request to the Scopus server
    scopus_server_url = 'https://api.elsevier.com'
    response = requests.post(scopus_server_url, json={'user_id': user_id, 'text': author_name})

    # Processing the Scopus server response and sending it back to the user
    data = response.json()
    last_three_documents = ', '.join(data.get('last_three_documents', []))
    subject_areas = ', '.join(data.get('subject_areas', []))
    metrics = data.get('metrics', {})

    result_message = (
        f"Last three documents: {last_three_documents}\n"
        f"Subject areas: {subject_areas}\n"
        f"Metrics: {metrics}"
    )

    update.message.reply_text(result_message)

def main():
    # Loading configuration
    conffile = "conf.json"
    with open(conffile, 'r') as f:
        conf = yaml.safe_load(f)

    # Initializing the Telegram bot
    updater = Updater(token=conf['telegram']['bot_token'], use_context=True)
    dp = updater.dispatcher

    # Defining command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, handle_scopus_request))

    # Starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
