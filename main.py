from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5225088042:AAEn2gQf5qgRYyWxTbvFHaGKVrnjiSJvk2M", use_context=True)


def main_menu_keyboard():
	keyboard = [[InlineKeyboardButton('join', callback_data='join')],
				[InlineKeyboardButton('schedule', callback_data='schedule')],
				[InlineKeyboardButton('reach us', callback_data='reach')],
				[InlineKeyboardButton('floss 22', callback_data='floss22')]]
	return InlineKeyboardMarkup(keyboard)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		text="Hello sir,\n Welcome to the COEP FLOSSMEET'22.\n Please Choose the option menu",
		reply_markup=main_menu_keyboard())


def schedule(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="Coming Very Soon.",
		reply_markup=main_menu_keyboard())


def join(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="Register for FLOSSMEET'22 => https://www.townscript.com/e/flossmeet22-204311",
		reply_markup=main_menu_keyboard())


def what_is_flossMeet(update: Update, context: CallbackContext):
	update.message.reply_photo(
		photo="https://raw.githubusercontent.com/mr-shitij/TelegramBot_FlossMeet/master/assets/flossmeet.jpeg?token=GHSAT0AAAAAABQYUSJIHLLAR77LVUBQLVXEYRLDG2A",
		caption="It's all about free and open source software",
		reply_markup=main_menu_keyboard())


def flossMeet22(update: Update, context: CallbackContext):
	update.callback_query.message.reply_photo(
		photo="https://raw.githubusercontent.com/mr-shitij/TelegramBot_FlossMeet/master/assets/flossmeet22.jpeg?token=GHSAT0AAAAAABQYUSJIXHFSPQQHIW344PEQYRLDYQA",
		caption="The 4th Edition of COEP FLOSSMeet’22 organized by CoFSUG is almost here!"
				"🤩🔥If you want to witness one of the greatest events held in India for "
				"the spread and awareness of free, libre, and open-source software, this is "
				"the perfect event for you. Our registrations are opening soon make sure "
				"you do not miss out on this amazing opportunity. 💻💯There are no branch "
				"restrictions  or age barriers💫. If you have the desire to learn more and "
				"contribute to the FLOSS world🐧 make sure "
				"to register and join us on the 26th and 27th of March, 2022. 🗓",
		reply_markup=main_menu_keyboard()
	)


def social(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="Linkedin URL => https://www.linkedin.com/company/coep-fossmeet21/, \n"
			 "Website URL => https://foss.coep.org.in/flossmeet/flossmeet22/",
		reply_markup=main_menu_keyboard()
	)


def unknown(update: Update, context: CallbackContext):
	if "floss" in update.message.text and "what" in update.message.text:
		what_is_flossMeet(update, context)

	else:
		update.callback_query.message.reply_text(
			text="Sorry '%s' is not a valid command" % update.message.text,
			reply_markup=main_menu_keyboard()
		)


def error(update, context):
	print(f'Update {update} caused error {context.error}')


def unknown_text(update: Update, context: CallbackContext):
	update.callback_query.message.edit_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(social, pattern="reach"))
updater.dispatcher.add_handler(CallbackQueryHandler(schedule, pattern="schedule"))
updater.dispatcher.add_handler(CallbackQueryHandler(join, pattern="join"))
updater.dispatcher.add_handler(CallbackQueryHandler(flossMeet22, pattern="floss22"))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages and error messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
