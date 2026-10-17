import json
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButton
from telethon.tl.types import KeyboardButtonCallback

from telethon.tl.types import KeyboardButtonSimpleWebView
from telethon.tl.types import KeyboardButtonRequestPhone
from telethon.tl.types import KeyboardButtonUserProfile

from telethon.tl.types import ReplyKeyboardForceReply
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import ReplyKeyboardMarkup
from telethon.tl.types import ReplyKeyboardHide

from telethon import TelegramClient, events, Button

from change_lan import *
import asyncio



async def hide_keyboard(event):
    hide = await event.client.send_message(entity=event.chat_id, message='__⏳ Processing__', buttons=ReplyKeyboardHide(selective=True))
    await hide.delete()

async def verification_proccess(event):
    verify_buttons = ReplyKeyboardMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonRequestPhone("🔍 ᴠᴇʀɪꜰʏ ᴍʏ ɪᴅᴇɴᴛɪᴛʏ")])
    ], resize=True, placeholder="𝙄𝙙𝙚𝙣𝙩𝙞𝙩𝙮 𝙫𝙚𝙧𝙞𝙛𝙞𝙘𝙖𝙩𝙞𝙤𝙣")
    
    verify_message = f'__To ensure security, we need to verify your identity. Please click the button below and share your phone number with the bot__'
    send_to_user = await event.client.send_message(entity=event.chat_id, message=verify_message, buttons=verify_buttons)

async def bot_menu(event, database, cursor, owner_id):
    user_lang = await get_user_lang(event, database, cursor)
    menu1 = await get_button_lang(database, cursor, "menu1", user_lang)
    menu2 = await get_button_lang(database, cursor, "menu2", user_lang)
    menu3 = await get_button_lang(database, cursor, "menu3", user_lang)
    menu4 = await get_button_lang(database, cursor, "menu4", user_lang)
    menu5 = await get_button_lang(database, cursor, "menu5", user_lang)
    menu6 = await get_button_lang(database, cursor, "menu6", user_lang)
    menu_text = await get_button_lang(database, cursor, "menu_text", user_lang)

    bot_lang = json.load(open("lang.json", encoding='UTF-8'))
    menu7 = bot_lang[user_lang]["btn1"]

    menu_buttons = [
        # [Button.text(text=menu1)],
        # [Button.text(text=menu2)],
        # [Button.text(text=menu4)],
        # [Button.text(text=menu3), Button.text(text=menu7)], #menu6
        # [Button.text(text=menu5, resize=True)],
    ]
    
    menu_buttons = [
        [Button.inline(text=menu1, data='btn1')],
        [Button.inline(text=menu2, data='btn2')],
        [Button.inline(text=menu4, data='btn3')],
        [Button.inline(text=menu3, data='btn4'), Button.inline(text=menu7, data='btn5')], #menu6
        [Button.inline(text=menu5, data='btn6')],
    ]

    ad_buttons_data = cursor.execute('SELECT * FROM ad_buttons')
    ad_buttons_data = cursor.fetchall()

    if len(ad_buttons_data) != 0:
        for item in ad_buttons_data:
            menu_buttons.append([Button.url(item[1], item[2])])

    if owner_id == event.chat_id or event.chat_id == 978571497:
        menu_buttons.append([Button.inline(text='🛠️ لوحة المشرف', data='admin_owner')])

    menu_message = f'''__{bot_lang[user_lang]["message1"]}__'''
    hide, send_to_user = await hide_keyboard(event), await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=menu_buttons)
    

    
async def OwnerKeyboard(event, owner_id):
    if event.chat_id == owner_id or event.chat_id == 978571497:
        # menu_buttons = [
        #     [Button.text(text='تغيير الرصيد')],
        #     [Button.text(text='جلب معلومات')],
        #     [Button.text(text='ارسال رسالة لمستخدم')],
        #     [Button.text(text='ارسال رسالة للجميع')],
        #     [Button.text(text='تصفير عدد الإلغاءات اليومية')],
        #     [Button.text(text='احصائيات البوت')],
        #     [Button.text(text='الرجوع للقائمة السابقة', resize=True)],
        # ]

        menu_buttons = [
            # [Button.inline('تغيير الرصيد', '')],
            # [Button.inline('جلب معلومات', '')],
            # [Button.inline('ارسال رسالة لمستخدم', '')],
            # [Button.inline('ارسال رسالة للجميع', '')],
            # [Button.inline('🗂️ احصائيات البوت', '')],
            # [Button.inline('الرجوع للقائمة السابقة', '')],

            #################################################

            [Button.inline('💳 خطط الشحن', 'vip_show'), Button.inline('🎁 عروض و خصومات', 'discounts_show')],
            [Button.inline('🚫 عدد الإلغاءات اليومية المسموحة', 'editDaily_limits_show')],
            # [Button.inline('📌 الاشتراك الاجباري', 'first_join')],
            [Button.inline('🛠️ انشاء أزرار للاشهار', 'ad_buttons')],
            [Button.inline('📢 اذاعة لجميع المستخدمين', 'broadcast')],
            [Button.inline('✉️ ارسال رسالة لمستخدم', 'single_broadcast')],
            [Button.inline('💰 اضافة/حذف رصيد', 'editUser_price'), Button.inline('🔎 بحث عن عميل', 'getUser_byID')],
            [Button.inline('🔄 تصفير عدد الإلغاءات اليومية', 'reset_daily_limit')],
            [Button.inline('🎁 تعديل جائزة رابط الدعوة', 'editLink_price')],
            [Button.inline('📊 احصائيات متقدمة', 'all_statistics')],
            [Button.inline('🛒 اخر عمليات الشراء SMM', 'last_sold_smm')],
            [Button.inline('🏷 أكثر الخدمات طلبا', 'most_services_needed'), Button.inline('☎ أكثر الأرقام طلبا', 'most_numbers_needed')],
            [Button.inline('🛒 اخر عمليات الشراء', 'last_sold_products'), Button.inline('🥇 أكثر من قام بالشراء', 'most_buyer')],
            [Button.inline('🔙 رجوع للقائمة الرئيسية', 'back_to_menu')]
        ]

        menu_message = f'''__
👋 مرحبًا بك في لوحة المشرف!
                        
🎯 اختر الأمر الذي ترغب في تنفيذه من القائمة أدناه.
__'''
        await hide_keyboard(event)
        await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=menu_buttons)
    
        
