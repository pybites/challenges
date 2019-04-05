# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from lang_dict import *
from geo_app import *
import logging

# You might need to add your tokens to this file...
from credentials import *


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:
LANG = "EN"
SET_LANG, MENU, SET_STAT, REPORT, MAP, FAQ, ABOUT, LOCATION = range(8)
STATE = SET_LANG


def start(bot, update):
    """
    Start function. Displayed whenever the /start command is called.
    This function sets the language of the bot.
    """
    # Create buttons to slect language:
    keyboard = [['ES', 'EN']]

    # Create initial message:
    message = "Hey, I'm DisAtBot! / ¡Hey, soy DisAtBot! \n\n\
Please select a language to start. / Por favor selecciona un idioma \
para comenzar."

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

    return SET_LANG


def set_lang(bot, update):
    """
    First handler with received data to set language globally.
    """
    # Set language:
    global LANG
    LANG = update.message.text
    user = update.message.from_user

    logger.info("Language set by {} to {}.".format(user.first_name, LANG))
    update.message.reply_text(lang_selected[LANG],
                              reply_markup=ReplyKeyboardRemove())

    return MENU


def menu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [[send_report[LANG], view_map[LANG]],
                [view_faq[LANG], view_about[LANG]]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("Menu command requested by {}.".format(user.first_name))
    update.message.reply_text(main_menu[LANG], reply_markup=reply_markup)

    return SET_STAT


def set_state(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == send_report[LANG]:
        STATE = REPORT
        report(bot, update)
        return LOCATION
    elif update.message.text == view_map[LANG]:
        STATE = MAP
        vmap(bot, update)
        return MENU
    elif update.message.text == view_faq[LANG]:
        STATE = FAQ
        faq(bot, update)
        return MENU
    elif update.message.text == view_about[LANG]:
        STATE = ABOUT
        about_bot(bot, update)
        return MENU
    else:
        STATE = MENU
        return MENU


def report(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("Report requested by {}.".format(user.first_name))
    update.message.reply_text(loc_request[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of {}: ({}, {})".format(
                user.first_name, user_location.latitude,
                user_location.longitude))
    report_map = geo_app()
    report_map.append_data(user_location.latitude, user_location.longitude)
    update.message.reply_text(loc_aquired[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return MENU


def vmap(bot, update):
    """
    View map function. In development...
    """
    user = update.message.from_user
    logger.info("Map requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=map_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])

    # View map locally:
    report_map = geo_app()
    report_map.latlong_to_coords()
    report_map.visualize()
    return


def faq(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("FAQ requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=faq_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def about_bot(bot, update):
    """
    About function. Displays info about DisAtBot.
    """
    user = update.message.from_user
    logger.info("About info requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=about_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def help(bot, update):
    """
    Help function.
    This displays a set of commands available for the bot.
    """
    user = update.message.from_user
    logger.info("User {} asked for help.".format(user.first_name))
    update.message.reply_text(help_info[LANG],
                              reply_markup=ReplyKeyboardRemove())


def cancel(bot, update):
    """
    User cancelation function.
    Cancel conersation by user.
    """
    user = update.message.from_user
    logger.info("User {} canceled the conversation.".format(user.first_name))
    update.message.reply_text(goodbye[LANG],
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    global LANG
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SET_LANG: [RegexHandler('^(ES|EN)$', set_lang)],

            MENU: [CommandHandler('menu', menu)],

            SET_STAT: [RegexHandler(
                        '^({}|{}|{}|{})$'.format(
                            send_report['ES'], view_map['ES'],
                            view_faq['ES'], view_about['ES']),
                        set_state),
                       RegexHandler(
                        '^({}|{}|{}|{})$'.format(
                            send_report['EN'], view_map['EN'],
                            view_faq['EN'], view_about['EN']),
                        set_state)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('menu', menu)]
        },

        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help)]
    )

    dp.add_handler(conv_handler)

    # Log all errors:
    dp.add_error_handler(error)

    # Start DisAtBot:
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process
    # receives SIGINT, SIGTERM or SIGABRT:
    updater.idle()


if __name__ == '__main__':
    main()
