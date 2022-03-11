from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5225088042:AAEn2gQf5qgRYyWxTbvFHaGKVrnjiSJvk2M", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello sir, Welcome to the COEP FLOSSMEET'22.Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/linkedin - To get the LinkedIn profile URL
	/website - To get the website URL""")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"LinkedIn URL => \
		https://www.linkedin.com/company/coep-fossmeet21/")


def website(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Website URL => \
		https://foss.coep.org.in/flossmeet/flossmeet22/")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('website', website))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
