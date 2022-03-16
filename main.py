from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5225088042:AAEn2gQf5qgRYyWxTbvFHaGKVrnjiSJvk2M", use_context=True)


def main_menu_keyboard():
	keyboard = [[InlineKeyboardButton('REGISTER', callback_data='register')],
				[InlineKeyboardButton('SCHEDULE', callback_data='schedule')],
				[InlineKeyboardButton('REACH US', callback_data='reach')],
				[InlineKeyboardButton('WHAT IS FLOSS?', callback_data='what_is_floss')],
				[InlineKeyboardButton('FLOSSMeet\'22', callback_data='floss22')]]
	return InlineKeyboardMarkup(keyboard)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		text="Hello " + update.message.from_user.first_name +",\n Welcome to the COEP FLOSSMEET'22.\n Please Choose the option menu",
		reply_markup=main_menu_keyboard())


def schedule(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="Coming Very Soon.",
		reply_markup=main_menu_keyboard())


def register(update: Update, context: CallbackContext):
	update.callback_query.message.reply_photo(
		photo="https://raw.githubusercontent.com/mr-shitij/TelegramBot_FlossMeet/master/assets/register.jpeg?token=GHSAT0AAAAAABQYUSJIJ3FKCBTZ4NRMB6CYYRQ6WLA",
		caption="*IF YOU WANT TO BE THERE FOR EVENT!*\n"
			 "If you wish to be a part of the event and "
			 "enjoy the awesome sessions which we will have conduct,"
			 " register now and stay tuned to get timely updates.\n"
			 " *Click here to register:*\n"
			 " https://www.townscript.com/e/flossmeet22-204311",
		reply_markup=main_menu_keyboard(),
		parse_mode=ParseMode.MARKDOWN)


def what_is_floss(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="Floss in 2 min \n https://youtu.be/MtNcxMuphLc\n\n"
			"FOSS United \n https://www.youtube.com/watch?v=iXL1j_lUUB8\n\n"
			"Read About Open Source \n https://www.gnu.org/philosophy/open-source-misses-the-point.html\n\n"
			"This is the most detailed one in case you wanna dive deeper \n https://youtu.be/n9YDz-Iwgyw\n",
		reply_markup=main_menu_keyboard())


def flossMeet22(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="The 4th Edition of COEP FLOSSMeet’22 organized by CoFSUG is almost here!🤩🔥"
			 "If you want to witness one of the greatest events held in India for the spread and "
			 "awareness of free, libre, and open-source software, this is the perfect event for you."
			 " Our registrations are open now Make sure you do not miss out on this amazing opportunity. "
			 "💻💯There are no branch restrictions  or age barriers💫. If you have the desire to learn more and"
			 " contribute to the FLOSS world🐧 make sure to register and join us on the 26th and 27th of March, 2022. \n\n"
			 "🗓<b>Visit our site for more information:</b>\n\n"
			 "https://foss.coep.org.in/flossmeet/flossmeet22/",
		reply_markup=main_menu_keyboard(),
		parse_mode=ParseMode.HTML
	)


def social(update: Update, context: CallbackContext):
	update.callback_query.message.reply_text(
		text="<b>Follow Us:</b>\n"
			 "🔸 <b>LinkedIn:</b> https://www.linkedin.com/company/coep-fossmeet21\n\n"
			 "🔸 <b>Instagram:</b> https://www.instagram.com/coep_flossmeet/\n\n"
			 "🔸 <b>Telegram:</b> https://t.me/+F6TTbsAfLMU5N2E1\n",
		reply_markup=main_menu_keyboard(),
		parse_mode=ParseMode.HTML
	)


def unknown(update: Update, context: CallbackContext):
	if "floss" in update.message.text and "what" in update.message.text:
		what_is_floss(update, context)

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
updater.dispatcher.add_handler(CallbackQueryHandler(register, pattern="register"))
updater.dispatcher.add_handler(CallbackQueryHandler(flossMeet22, pattern="floss22"))
updater.dispatcher.add_handler(CallbackQueryHandler(what_is_floss, pattern="what_is_floss"))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages and error messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
