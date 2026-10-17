from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonUrl
from telethon.tl.types import KeyboardButtonCallback

from change_lan import *
from menu import *
import asyncio


async def MyAccount(event, database, cursor):
    user_lang = await get_user_lang(event, database, cursor)
    menu7 = await get_button_lang(database, cursor, "menu7", user_lang)
    menu8 = await get_button_lang(database, cursor, "menu8", user_lang)
    my_account_text = await get_button_lang(database, cursor, "my_account_text", user_lang)
    
    user_info = await get_user_info(event, database, cursor)
    user_referral_link = f'https://t.me/NumbersSeller_Bot?start={user_info[0]}'
    # share_url = f"""https://t.me/share/url?url=☎️%20__Do%20you%20need%20a%20number?__%0A%0A__Easily%20verify%20your%20account%20on%20any%20platform%20with%20**Numbers%20Store's**%20virtual%20numbers__%0A%0A%0A➨%20{user_referral_link}"""
    share_url = f"https://t.me/share/url?url={user_referral_link}"
    
    bot_lang = json.load(open("lang.json", encoding='UTF-8'))

    change_lang_buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonUrl(f'{bot_lang[user_lang]["btn4"]}', share_url)]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(menu7, b"change_lang")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f'{bot_lang[user_lang]["btn2"]}', b"back_to_menu")])
    ])

    bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
    bot_settings_data = cursor.fetchone()
    
    user_info = f'''
💳 __**{bot_lang[user_lang]["btn12"]}** {user_info[2]} Credits ( {round(float(user_info[2] / 10), 2)}$ )__
🪪 __**{bot_lang[user_lang]["btn5"]}** {user_info[0]}__


➨ __{bot_lang[user_lang]["btn6"]} {user_info[11]}__
➨ __{bot_lang[user_lang]["btn7"]} {user_info[12]}__
➨ __{bot_lang[user_lang]["btn8"]} {user_info[9]}/{bot_settings_data[2]}__

➨ __{bot_lang[user_lang]["btn9"]} {user_info[10]}__
➨ __{bot_lang[user_lang]["btn10"]} {user_info[3]}__
➨ __{bot_lang[user_lang]["btn11"]} {user_referral_link}__
'''
    
    
    await hide_keyboard(event), await event.client.send_message(entity=event.chat_id, message=user_info, buttons=change_lang_buttons)
    
    