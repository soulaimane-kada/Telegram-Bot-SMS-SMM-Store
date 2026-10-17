from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonCallback
import asyncio



async def pin_animation(event, text):
    await event.answer(text)

async def change_lang(event, user_id):
    change_lan_buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text='English', data=f'lang_english')]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text='العربية', data=f'lang_arabic')])
    ])
    
    send_to_user = await event.client.send_message(user_id, "__⏳ Updating langauge... / ...تحديث اللغة ⏳__", buttons=change_lan_buttons)
    
async def get_user_lang(event, database, cursor):
    user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={event.chat_id}").fetchall()
    user_lang = user_info[0][4]
    return user_lang

async def get_user_info(event, database, cursor):
    user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id={event.chat_id}").fetchall()
    user_info = user_info[0]
    return user_info
    
async def get_button_lang(database, cursor, button_code, user_lang):
    button_text = (cursor.execute(f"SELECT * FROM langs WHERE button_code = '{button_code}' AND button_lang = '{user_lang}';").fetchall())[0][1]
    return button_text
    
