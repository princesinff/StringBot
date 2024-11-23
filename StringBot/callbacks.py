import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringBot.gen import generate_session, ask_ques, buttons_ques

@Client.on_callback_query(filters.regex(r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon|pyrogram_v3|pyrogram_v2)$"))
async def callback_handler(bot: Client, callback_query: CallbackQuery):
    query = callback_query.data
    try:
        if query == "generate":
            await callback_query.answer()
            await callback_query.message.edit_text(
                ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques)
            )
        elif query == "pyrogram_v3":
            await callback_query.answer("Generating a Pyrogram v3 session.", show_alert=True)
            await generate_session(bot, callback_query.message, pyro_v3=True)
        elif query == "pyrogram_v2":
            await callback_query.answer("Generating a Pyrogram v2 session.", show_alert=True)
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("Generating a Pyrogram Bot session.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer("Generating a Telethon Bot session.", show_alert=True)
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer("Generating a Telethon session.", show_alert=True)
            await generate_session(bot, callback_query.message, telethon=True)
    except Exception as e:
        # Log the error details for debugging and notify the user
        print(traceback.format_exc())
        await callback_query.message.reply(
            ERROR_MESSAGE.format(str(e))
        )
