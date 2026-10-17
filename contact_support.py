from telethon.tl.types import ReplyKeyboardMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButton
from telethon.tl.types import ReplyKeyboardForceReply
from telethon import Button

from change_lan import *
from menu import *
import asyncio


async def ContactSupport(event, cursor, database, CommitDatabase, datetimeNow, owner_id):
    user_lang = await get_user_lang(event, database, cursor)
    support_button1 = await get_button_lang(database, cursor, "support_button1", user_lang)
    support_text = await get_button_lang(database, cursor, "support_text", user_lang)
    support_message = await get_button_lang(database, cursor, "support_message", user_lang)
    support_success = await get_button_lang(database, cursor, "support_success", user_lang)
    support_failed = await get_button_lang(database, cursor, "support_failed", user_lang)
    
    button_to_cancel = ReplyKeyboardMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButton(text=support_button1)])
    ], resize=True, placeholder=support_text)
    try:
        async with event.client.conversation(event.chat_id, timeout=600) as conv:
            user_message = await conv.send_message(f'__{support_message}__', buttons=button_to_cancel)
            user_ticket = await conv.get_response()
            
            if user_ticket.text == support_button1:
                cancel, menu = await conv.cancel_all(), await bot_menu(event, database, cursor, owner_id)
            else:
                reported_at = await datetimeNow()
                # add_report, commit = cursor.execute(f"INSERT INTO reports VALUES (?,?,?)", (event.chat_id, user_ticket.text, str(reported_at))), await CommitDatabase(database)
                buttons = [[Button.inline('Reply On User', f'AdminReply_{event.chat_id}')]]
                await event.client.send_message(entity=owner_id , message=user_ticket, buttons=buttons)
                
                await hide_keyboard(event), await conv.send_message(f"__{support_success}__"), await bot_menu(event, database, cursor, owner_id)
        


    except Exception as error:
        await conv.send_message(f'__{support_failed}__')
        
        