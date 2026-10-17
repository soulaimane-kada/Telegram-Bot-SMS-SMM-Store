from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonCallback
from telethon.tl.types import KeyboardButtonUrl

import ast, json, requests, asyncio, datetime, time

from change_lan import get_user_lang


# READ CONFIGS
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


sms_api_key = config["SMS_API_KEY"]
bot_lang = json.load(open("lang.json", encoding='UTF-8'))


# function to register the current time
async def register_time():
    return datetime.datetime.now().time()


async def check_time_registered(reg_Time, time_to_wait):
    reg_time = datetime.datetime.strptime(str(reg_Time).split('.')[0], '%H:%M:%S')
    curr_time = datetime.datetime.now().time()
    time_diff = datetime.datetime.combine(datetime.date.today(), curr_time) - datetime.datetime.combine(datetime.date.today(), reg_time.time())
    time_left = datetime.timedelta(seconds=time_to_wait) - time_diff
    if time_left <= datetime.timedelta(0):
        return True
    else:
        minutes, seconds = divmod(time_left.seconds, 60)
        if len(str(minutes)) == 1:
            minutes = f'0{minutes}'
        if len(str(seconds)) == 1:
            seconds = f'0{seconds}'
        return f"{minutes}:{seconds} minutes"


# view all pages
async def all_pages_section_1(event, cursor):
    all_groups = cursor.execute(f"SELECT * FROM service_groups").fetchall()
    user_lang = await get_user_lang(event, None, cursor)
    
    row_buttons = []
    buttons_group = []
    for group_name in all_groups:
        buttons_group.append(KeyboardButtonCallback(text=f"🚀 ➨ {bot_lang[user_lang]['message16']} {(group_name[0]).replace('group_','').zfill(2)}", data=f"go_to_{group_name[0]}"))
        if len(buttons_group) == 3:
            row_buttons.append(KeyboardButtonRow(buttons=buttons_group))
            buttons_group = []
    
    scroll_buttons = ReplyInlineMarkup(rows=row_buttons)
    await event.edit(f'__➨ {bot_lang[user_lang]["message17"]}__', buttons=scroll_buttons)


async def go_to_page(event, cursor, database, page_group_id, CommitDatabase):
    total_services = cursor.execute(f"SELECT * FROM service_groups").fetchall()
    services = cursor.execute(f"SELECT * FROM service_groups WHERE group_code = '{page_group_id}'").fetchall()
    services_ = ast.literal_eval(services[0][1])
    current_index = str(page_group_id).replace("group_","")
    await update_index(event, database, cursor, CommitDatabase, current_index)

    rows = await get_services_rows(services_, database, cursor)
    await show_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], "send", current_index, len(total_services), cursor)

######################### show numbers stocks #########################
async def update_index2(event, database, cursor, new_index, service_id):
    services_idxs = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][8]
    convert_to_json = json.loads(str(services_idxs))
    convert_to_json[f"{str(service_id)}_index"] = str(new_index)
    
    query = "UPDATE bot_users SET current_index2 = ? WHERE user_id = ?"
    cursor.execute(query, (str(convert_to_json).replace("'", '"'), event.chat_id))
    database.commit()

async def get_rows(result, index, database, cursor):
    row_1, row_2, row_3, row_4, row_5, row_6 = [], [], [], [], [], []
    
    for idx, group in enumerate(result[index], start=1):
        flag = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = {group[1]}").fetchall()[0][2]
        country_name = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = {group[1]}").fetchall()[0][1]
        if idx == 1:
            row_1.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
        elif idx == 2:
            row_2.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
        elif idx == 3:
            row_3.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
        elif idx == 4:
            row_4.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
        elif idx == 5:
            row_5.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
        elif idx == 6:
            row_6.append(KeyboardButtonCallback(text=f'{flag} {country_name} ( {group[7]} Credit ~ {group[8]} )', data=f'buy_{group[0]}_{group[1]}'))
            
    return row_1, row_2, row_3, row_4, row_5, row_6

async def get_numbers(event, service_id, database, cursor, idx=None):

    services_idxs = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][8]
    convert_to_json = json.loads(str(services_idxs))
    current_index = convert_to_json.get(f"{str(service_id)}_index")
    
    if current_index == None:
        json_idx = str(idx).replace("'", '"')
        cursor.execute(f"UPDATE bot_users SET current_index2 = '{json_idx}' WHERE user_id = {event.chat_id}")
        database.commit()

        services_idxs = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][8]
        convert_to_json = json.loads(str(services_idxs))
        current_index = convert_to_json.get(f"{str(service_id)}_index")
    
    services = cursor.execute(f"SELECT * FROM numbers_store_lists WHERE service_id = '{service_id}'").fetchall()
    return [services, int(current_index)]


async def show_numbers(event, service_id, database, cursor, idx):
    data = await get_numbers(event, service_id, database, cursor, idx=idx)
    result = [data[0][i:i+5] for i in range(0, len(data[0]), 5)]
    
    lst, index = data[0], data[1] - 1
    lst = sorted(lst, key=lambda x: float(x[7]))
    result = [lst[i:i+5] for i in range(0, len(lst), 5)]
    
    rows = await get_rows(result, index, database, cursor)
    await show_numbers_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], "send", index+1, len(result), service_id, database, cursor)
        
async def show_numbers_next(event, service_id, database, cursor):
    data = await get_numbers(event, service_id, database, cursor)
    result = [data[0][i:i+5] for i in range(0, len(data[0]), 5)]
    new_index = await check_index(data[1], len(result), "next")
    await update_index2(event, database, cursor, new_index[0], service_id)
    
    if new_index[1] != "stop":
        lst, index = data[0], new_index[0] - 1
        lst = sorted(lst, key=lambda x: float(x[7]))
        result = [lst[i:i+5] for i in range(0, len(lst), 5)]
        
        rows = await get_rows(result, index, database, cursor)
        await show_numbers_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], "edit", index+1, len(result), service_id, database, cursor)
    else:
        await event.answer("No more pages")
        
async def show_numbers_back(event, service_id, database, cursor):
    data = await get_numbers(event, service_id, database, cursor)
    result = [data[0][i:i+5] for i in range(0, len(data[0]), 5)]
    new_index = await check_index(data[1], len(result), "back")
    await update_index2(event, database, cursor, new_index[0], service_id)
    
    if new_index[1] != "stop":
        lst, index = data[0], new_index[0] - 1
        lst = sorted(lst, key=lambda x: float(x[7]))
        result = [lst[i:i+5] for i in range(0, len(lst), 5)]
        
        rows = await get_rows(result, index, database, cursor)
        
        await show_numbers_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], "edit", index+1, len(result), service_id, database, cursor)
    else:
        await event.answer("No more pages")

async def show_numbers_list(event, row_1, row_2, row_3, row_4, row_5, row_6, type, current_index, total_pages, service_id, database, cursor):
    user_lang = await get_user_lang(event, None, cursor)

    services_buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=row_1),
        KeyboardButtonRow(buttons=row_2),
        KeyboardButtonRow(buttons=row_3),
        KeyboardButtonRow(buttons=row_4),
        KeyboardButtonRow(buttons=row_5),
        #KeyboardButtonRow(buttons=row_6),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message100']}", f"countrySearch_{service_id}")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"« {bot_lang[user_lang]['btn13']}", f"section2_back_{service_id}"), KeyboardButtonCallback(f"{bot_lang[user_lang]['message16']} {current_index}/{total_pages}", f"section2_{service_id}_current_page"), KeyboardButtonCallback(f"{bot_lang[user_lang]['btn14']} »", f"section2_next_{service_id}")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn15']}", b"back_to_services_list")])
    ])

    service_name = await get_service(service_id, database, cursor)
    if len(str(service_name).split(' ')) > 2:
        service_stock = f"({service_name})'s"
    else:
        service_stock = f"{service_name}'s"
    user_balance = await get_user_balance(event, cursor)
    menu_message = f"__{bot_lang[user_lang]['message18']}\n\n➨ {service_stock} {bot_lang[user_lang]['message19']} {user_balance}__"
    
    if type == "send":
        send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)
    elif type == "edit":
        send_to_user = await event.edit(text=menu_message, buttons=services_buttons)

async def get_user_balance(event, cursor):
    user_balance = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][2]
    return f"{user_balance} Credits ~ {round(user_balance / 10, 2)} $"
    
############################# show services list ###############################
async def check_index(current_index, end, direction):
    if direction == "next":
        if current_index >= end:
            return [end, "stop"]
        else:
            return [(current_index + 1), "moved"]
    elif direction == "back":
        if current_index == 1:
            return [1, "stop"]
        else:
            return [(current_index - 1), "moved"]
        
async def get_service(service_id, database, cursor):
    service_name = cursor.execute(f"SELECT * FROM services WHERE service_id = '{service_id}'").fetchall()[0][2]
    return f"🔥 {service_name}"

async def get_services(event, database, cursor):
    current_index = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][7]
    services = cursor.execute(f"SELECT * FROM service_groups WHERE group_code = 'group_{current_index}'").fetchall()
    return [services, current_index]

async def update_index(event, database, cursor, CommitDatabase, new_index):
    current_index, commit = cursor.execute(f"UPDATE bot_users SET current_index1 = {new_index} WHERE user_id = {event.chat_id}").fetchall(), await CommitDatabase(database)

async def show_list(event, row_1, row_2, row_3, row_4, row_5, type, current_index, total_pages, cursor):
    user_lang = await get_user_lang(event, None, cursor)

    services_buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=row_1),
        KeyboardButtonRow(buttons=row_2),
        KeyboardButtonRow(buttons=row_3),
        KeyboardButtonRow(buttons=row_4),
        KeyboardButtonRow(buttons=row_5),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message96']}", "services_search")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"« {bot_lang[user_lang]['btn13']}", "section1_back"), KeyboardButtonCallback(f"{bot_lang[user_lang]['message16']} {current_index}/{total_pages}", "section1_current_page"), KeyboardButtonCallback(f"{bot_lang[user_lang]['btn14']} »", "section1_next")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message20']}", b"close_this_list")])
    ])

    menu_message = f"__{bot_lang[user_lang]['message21']}__"
    if type == "send":
        send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)
    elif type == "edit":
        send_to_user = await event.edit(text=menu_message, buttons=services_buttons)

async def get_services_rows(services, database, cursor):
    row_1, row_2, row_3, row_4, row_5 = [], [], [], [], []
    for idx, service in enumerate(services, start=1):
        if idx == 1:
            for item in service:
                service_name = await get_service(item, database, cursor)
                row_1.append(KeyboardButtonCallback(text=str(service_name), data=f'service_{item}'))
        elif idx == 2:
            for item in service:
                service_name = await get_service(item, database, cursor)
                row_2.append(KeyboardButtonCallback(text=str(service_name), data=f'service_{item}'))
        elif idx == 3:
            for item in service:
                service_name = await get_service(item, database, cursor)
                row_3.append(KeyboardButtonCallback(text=str(service_name), data=f'service_{item}'))
        elif idx == 4:
            for item in service:
                service_name = await get_service(item, database, cursor)
                row_4.append(KeyboardButtonCallback(text=str(service_name), data=f'service_{item}'))
        elif idx == 5:
            for item in service:
                service_name = await get_service(item, database, cursor)
                row_5.append(KeyboardButtonCallback(text=str(service_name), data=f'service_{item}'))
    return [row_1, row_2, row_3, row_4, row_5]

async def Services_List(event, database, cursor, CommitDatabase):
    total_services = cursor.execute(f"SELECT * FROM service_groups").fetchall()
    display_data = await get_services(event, database, cursor)
    services = ast.literal_eval(list(display_data[0][0])[1])
    current_index = display_data[1]

    rows = await get_services_rows(services, database, cursor)
    await show_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], "send", current_index, len(total_services), cursor)

async def next_page(event, database, cursor, CommitDatabase):
    total_services = cursor.execute(f"SELECT * FROM service_groups").fetchall()
    display_data = await get_services(event, database, cursor)
    current_index = await check_index(display_data[1], len(total_services), "next")
    UPDATE_index = await update_index(event, database, cursor, CommitDatabase, current_index[0])
    display_data = await get_services(event, database, cursor)
    services = ast.literal_eval(list(display_data[0][0])[1])

    if current_index[1] != "stop":
        rows = await get_services_rows(services, database, cursor)
        await show_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], "edit", current_index[0], len(total_services), cursor)
    else:
        await event.answer("No more pages")
    
async def back_page(event, database, cursor, CommitDatabase):
    total_services = cursor.execute(f"SELECT * FROM service_groups").fetchall()
    display_data = await get_services(event, database, cursor)
    current_index = await check_index(display_data[1], len(total_services), "back")
    UPDATE_index = await update_index(event, database, cursor, CommitDatabase, current_index[0])
    display_data = await get_services(event, database, cursor)
    services = ast.literal_eval(list(display_data[0][0])[1])
                
    if current_index[1] != "stop":
        rows = await get_services_rows(services, database, cursor)
        await show_list(event, rows[0], rows[1], rows[2], rows[3], rows[4], "edit", current_index[0], len(total_services), cursor)
    else:
        await event.answer("No more pages")


###################################### selected number ################################
async def update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, user_balance, country_name, country_flag, country_phone_code, phone_number, order_status, timeleft):
    user_lang = await get_user_lang(event, None, cursor)

    if timeleft == True:
        timeleft = "expired"
    if order_status == "Canceled ( No SMS received )" or order_status == "Canceled ( Technical Issue )":
        hint = f"🛑 **{bot_lang[user_lang]['message22']}.** __{bot_lang[user_lang]['message23']}__"
    elif order_status.startswith("->"):
        hint = f"✅ **{bot_lang[user_lang]['message24']}.** __{bot_lang[user_lang]['message25']}__"
    else:
        hint = f"__{bot_lang[user_lang]['message26']}__"
        
    message_details = f'''
**{bot_lang[user_lang]['message27']}** __{order_id}__

➨ **{bot_lang[user_lang]['message28']}** __{service_name} __
➨ **{bot_lang[user_lang]['message29']}** __{service_price} Credits ~ {service_price_dollar}__
➨ **{bot_lang[user_lang]['message30']}** __{user_balance} Credits ~ {round(float(user_balance / 10), 2)} $__

➨ **{bot_lang[user_lang]['message31']}** __{country_name} {country_flag}__
➨ **{bot_lang[user_lang]['message32']}** __`{country_phone_code}`__
➨ **{bot_lang[user_lang]['message33']}** __`+{phone_number}`__

➨ **{bot_lang[user_lang]['message34']}** __{timeleft}__
➨ **{bot_lang[user_lang]['message35']}** __{order_status}__


{hint}
'''
    return message_details

async def make_inline_button(text, data):
    buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text, data)])
    ])
    return buttons
    
async def update_user_credits(event, new_credits, database, cursor):
    update_credits = cursor.execute(f"UPDATE bot_users SET credits = {new_credits} WHERE user_id={event.chat_id};"), database.commit()

async def selected_number(event, service_id, country_code, database, cursor, purchased_at):
    user_lang = await get_user_lang(event, database, cursor)

    # get needed information
    action_info = cursor.execute(f"SELECT * FROM numbers_store_lists WHERE country_code = '{country_code}' AND service_id = '{service_id}'").fetchall()[0]
    country_data = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = '{country_code}'").fetchall()[0]
    service_name, service_price, service_price_dollar, country_name, country_flag, country_phone_code = await get_service(action_info[0], database, cursor), action_info[7], action_info[8], country_data[1], country_data[2], country_data[3]
    
    user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{event.chat_id}'").fetchall()[0]
    user_balance = user_info[2]
    cancels = user_info[9]
    
    bot_settings_data = cursor.execute('SELECT * FROM bot_settings WHERE setting_id = 1')
    bot_settings_data = cursor.fetchone()
    cancels_limit = int(bot_settings_data[2])

    # check to buy a number
    if user_balance >= service_price:
        if cancels < cancels_limit:
            # buy this number
            inform_user = await event.reply(f"⌛️ __{bot_lang[user_lang]['message36']}__")
            
            # take the credits from the user
            new_credits = round(float(user_balance) - float(service_price), 2)
            await update_user_credits(event, new_credits, database, cursor)
            
            # buy a number for him
            website_hostname = "https://hero-sms.com"
            get_numberAPI = f"{website_hostname}/stubs/handler_api.php?api_key={sms_api_key}&action=getNumber&service={service_id}&country={country_code}"
            session = requests.Session()
            number_data, delete = session.get(get_numberAPI), await inform_user.delete()
            
            # check the response
            if (number_data.text).startswith("ACCESS_NUMBER"):
                # we got a number successfully
                clear_number_data = (str(number_data.text).replace('ACCESS_NUMBER:', '')).split(':')
                order_id, phone_number = clear_number_data[0], clear_number_data[1]
                
                # start time left
                reg_time = await register_time()
                add_timer, commit = cursor.execute(f"INSERT INTO orders_reg_time VALUES (?,?,?)", (order_id, str(reg_time.strftime('%H:%M:%S')), 0)), database.commit()
                timeleft = await check_time_registered(reg_time, 120)
                
                # show information to user
                message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message42']}", timeleft)
                buttons = await make_inline_button(f"{bot_lang[user_lang]['message41']} ( 1 Credits ~ 0.1 $ )", f"MoreTime_{order_id}")
                updating_message = await event.reply(message_details, buttons=buttons)
                
                await check_for_activation_code(event, cursor, database, order_id, service_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, purchased_at, updating_message, session, user_balance, country_code)
            

            elif (number_data.text).startswith("NO_NUMBERS"):
                # no numbers for that service/country
                await order_not_complete(event, user_balance, database, cursor, service_id, f"📢 __{bot_lang[user_lang]['message37']} ( {country_flag} {country_name} )\n\n➨ {bot_lang[user_lang]['message38']}__")
                record = await record_order(event, cursor, database, None, service_price, service_price_dollar, "Failed", "Out of stock", service_id, service_name, country_name, None, None, purchased_at)
            elif (number_data.text).startswith("NO_BALANCE"):
                # no balance in my account
                await order_not_complete(event, user_balance, database, cursor, service_id, f"🔧 __{bot_lang[user_lang]['message39']}__")
                record = await record_order(event, cursor, database, None, service_price, service_price_dollar, "Failed", "API has no balance", service_id, service_name, country_name, None, None, purchased_at)
            else:
                print (number_data.text)
                # something wrong happened
                await order_not_complete(event, user_balance, database, cursor, service_id, f"⚠️ __{bot_lang[user_lang]['message40']}__")
                record = await record_order(event, cursor, database, None, service_price, service_price_dollar, "Failed", f"Error : {number_data.text}", service_id, country_name, country_name, None, None, purchased_at)
        else:
            # user did 10 cancels this day
            inform_user = await status_reached_limit(event, service_id, cursor)
            record = await record_order(event, cursor, database, None, service_price, service_price_dollar, "Failed", "Daily limit reached", service_id, service_name, country_name, None, None, purchased_at)
    else:
        # not enough credits
        inform_user = await status_Insufficient_credits(event, service_id, cursor)
        record = await record_order(event, cursor, database, None, service_price, service_price_dollar, "Failed", "Insufficient credits", service_id, service_name, country_name, None, None, purchased_at)


async def request_another_sms(event, database, cursor, order_id, service_id, service_name, service_price, service_price_dollar, user_balance, country_name, country_flag, country_phone_code, phone_number, timeleft, country_code, record_an_error):
    user_lang = await get_user_lang(event, database, cursor)

    try:
        session = requests.Session()
        
        website_hostname = "https://hero-sms.com"
        NewRequestAPI = f"{website_hostname}/stubs/handler_api.php?api_key={sms_api_key}&action=setStatus&status=3&id={order_id}"
        another_request_data = session.get(NewRequestAPI)
        
        if another_request_data.text == "ACCESS_RETRY_GET":
            new_credits = round(float(user_balance) - float(1), 2)
            await update_user_credits(event, new_credits, database, cursor)
            
            message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message42']}", timeleft)
            updating_message = await event.reply(message_details)
            
            while True:
                time_to_wait = 180
                reg_time = cursor.execute(f"SELECT * FROM orders_reg_time WHERE order_id = {order_id}").fetchall()[0][1]
                timeleft = await check_time_registered(reg_time, time_to_wait)
                message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message43']}", timeleft)
                await updating_message.edit(message_details)
                
                check_statusAPI = f"{website_hostname}/stubs/handler_api.php?api_key={sms_api_key}&action=getStatus&id={order_id}"
                check_data = session.get(check_statusAPI)
                
                if timeleft == True:
                    # timeout - cancel it
                    cancel, action_status, verification_code = await change_number_status(order_id, 8), "Timeout", None
                    
                if (check_data.text).startswith("STATUS_OK"):
                    activation_code = str(check_data.text).replace("STATUS_OK:", "")
                    message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"-> `{activation_code}`", timeleft)
                    buttons = ReplyInlineMarkup(rows=[
                        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"✅ {bot_lang[user_lang]['message44']} ( 1 Credit )", f"RequestAnother_{order_id}_{service_id}_{country_code}")]),
                        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")])
                    ])
                    inform_user = await updating_message.edit(message_details)
                    break
                elif (check_data.text).startswith("STATUS_WAIT_CODE") or (check_data.text).startswith("STATUS_WAIT_RETRY") or (check_data.text).startswith("STATUS_WAIT_RESEND"):
                    # timeout for this number
                    message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message42']}", timeleft)
                    inform_user = await updating_message.edit(message_details)
                elif (check_data.text).startswith("STATUS_CANCEL"):
                    cancel = await change_number_status(order_id, 8)
                    buttons = await make_inline_button(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")
                    message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, "Canceled ( No SMS received )", timeleft)
                    inform_user = await updating_message.edit(message_details)
                    break
                    
                if timeleft != True:
                    await asyncio.sleep(10)
            
        else:
            buttons = await make_inline_button(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")
            await event.reply(f"__{bot_lang[user_lang]['message46']}__", buttons=buttons)
        
    except Exception as error: # ERROR ACTION: #005
        record = await record_an_error(f'[ NEW ERROR RECORD ] -- [ USER_ID : {event.query.user_id} ] -- [ ERROR ACTION : #005 ] -- [ RECORDED ERROR : {error} ]')


# check for activation code
async def check_for_activation_code(event, cursor, database, order_id, service_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, purchased_at, updating_message, session, user_balance, country_code):
    user_lang = await get_user_lang(event, database, cursor)

    # checking for activation code
    action_status, time_to_wait = 0, 180
    while True:
        reg_time = cursor.execute(f"SELECT * FROM orders_reg_time WHERE order_id = {order_id}").fetchall()[0][1]
        timeleft = await check_time_registered(reg_time, time_to_wait)
        message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message43']}", timeleft)
        await updating_message.edit(message_details)
        
        website_hostname = "https://hero-sms.com"
        check_statusAPI = f"{website_hostname}/stubs/handler_api.php?api_key={sms_api_key}&action=getStatus&id={order_id}"
        check_data = session.get(check_statusAPI)
        
        if timeleft == True:
            # timeout - cancel it
            cancel, action_status, verification_code = await change_number_status(order_id, 8), "Timeout", None
        
        if (check_data.text).startswith("STATUS_OK"):
            # number received activation code
            activation_code = str(check_data.text).replace("STATUS_OK:", "")
            message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"-> `{activation_code}`", timeleft)
            buttons = ReplyInlineMarkup(rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"✅ {bot_lang[user_lang]['message44']} ( 1 Credit )", f"RequestAnother_{order_id}_{service_id}_{country_code}")]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")])
            ])
            inform_user, action_status, verification_code = await updating_message.edit(message_details, buttons=buttons), "Success", activation_code
            
            get_user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.query.user_id}").fetchall()[0]
            new_successful_sales = int(get_user[11]) + 1
            update_successful_sales = cursor.execute(f"UPDATE bot_users SET successful_sales = {new_successful_sales} WHERE user_id={event.query.user_id};")
            break
        
        elif (check_data.text).startswith("STATUS_CANCEL"):
            message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, "Canceled ( No SMS received )", timeleft) #Canceled ( No SMS received )
            buttons, update_credits = await make_inline_button(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}"), await update_user_credits(event, user_balance, database, cursor)
            inform_user, action_status, verification_code, update_cancels = await updating_message.edit(message_details, buttons=buttons), "Canceled ( No SMS received )", None, await AddCancel(event, database, cursor)
            
            get_user = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.query.user_id}").fetchall()[0]
            new_unsuccessful_sales = int(get_user[12]) + 1
            update_unsuccessful_sales = cursor.execute(f"UPDATE bot_users SET unsuccessful_sales = {new_unsuccessful_sales} WHERE user_id={event.query.user_id};")
            break
        
        elif (check_data.text).startswith("STATUS_WAIT_CODE") or (check_data.text).startswith("STATUS_WAIT_RETRY"):
            # timeout for this number
            message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, f"⏳ {bot_lang[user_lang]['message42']}", timeleft)
            inform_user = await updating_message.edit(message_details)
        else:
            # something happened
            message_details = await update_message(event, cursor, order_id, service_name, service_price, service_price_dollar, new_credits, country_name, country_flag, country_phone_code, phone_number, "Canceled ( Technical Issue )", timeleft)
            cancel = await change_number_status(order_id, 8)
            if cancel == True:
                buttons, update_credits = await make_inline_button(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}"), await update_user_credits(event, user_balance, database, cursor)
                inform_user, action_status, verification_code = await updating_message.edit(message_details, buttons=buttons), f"Canceled ( Technical Issue ) -- Error : {check_data.text}", None
                break
        
        if timeleft != True:
            await asyncio.sleep(10)

    # record the order
    record = await record_order(event, cursor, database, order_id, service_price, service_price_dollar, action_status, None, service_id, service_name, country_name, f"+{phone_number}", verification_code, purchased_at)




# add cancels
async def AddCancel(event, database, cursor):
    current_cancels = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = {event.chat_id}").fetchall()[0][9]
    new_cancels = int(current_cancels) + 1
    update_cancels = cursor.execute(f"UPDATE bot_users SET cancels = {new_cancels} WHERE user_id={event.chat_id};"), database.commit()


# change status for this number
async def change_number_status(order_id, status_code):

    website_hostname = "https://hero-sms.com"
    statusAPI = f"{website_hostname}/stubs/handler_api.php?api_key={sms_api_key}&action=setStatus&status={status_code}&id={order_id}"
    ChangeStatus = requests.get(statusAPI)
    if str(ChangeStatus).startswith("ACCESS_CANCEL"):
        return True
    else:
        return False


# record this order
async def record_order(event, cursor, database, OrderID, cost, service_price_dollar, action_status, cancel_reason, service_id, service_name, phone_number_country, phone_number, verification_code, purchased_at):
    RecordOrder = cursor.execute(f"INSERT INTO orders_recorded VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (OrderID, event.chat_id, cost, service_price_dollar, action_status, cancel_reason, service_id, service_name, phone_number_country, phone_number, verification_code, purchased_at))
    database.commit()


# order did not complete for some unknown reason
async def order_not_complete(event, user_balance, database, cursor, service_id, message_to_user):
    user_lang = await get_user_lang(event, database, cursor)

    update, buttons = await update_user_credits(event, user_balance, database, cursor), await make_inline_button(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")
    await event.reply(message_to_user, buttons=buttons)


# if user has reached his daily limit
async def status_reached_limit(event, service_id, cursor):
    user_lang = await get_user_lang(event, None, cursor)

    message_details = f"__{bot_lang[user_lang]['message48']}__"
    details_buttons = ReplyInlineMarkup(rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message47']}", b"request_reset")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")])
    ])
    send_to_user = await event.client.send_message(entity=event.chat_id, message=message_details, buttons=details_buttons)


# if user dont have enough credits
async def status_Insufficient_credits(event, service_id, cursor):
    user_lang = await get_user_lang(event, None, cursor)
    
    message_details = f"💳 **{bot_lang[user_lang]['message49']}** __{bot_lang[user_lang]['message50']}__"
    details_buttons = ReplyInlineMarkup(rows=[
        #KeyboardButtonRow(buttons=[KeyboardButtonCallback("Purchase Credits ( Automated )", b"add_credits")]),
        # KeyboardButtonRow(buttons=[KeyboardButtonUrl("Purchase Credits ( FromAdmin )", b"https://t.me/zkada")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn1']}", f"btn5")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn15']}", f"service_{service_id}")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['btn2']}", "back_to_menu")])
    ])
    send_to_user = await event.client.send_message(entity=event.chat_id, message=message_details, buttons=details_buttons)


async def Search_Services_List(event, database, cursor, CommitDatabase, search_text):
    chunk_size, user_lang = 3, await get_user_lang(event, None, cursor)
    found_services = cursor.execute(f"SELECT * FROM services WHERE service_name_normal LIKE '%{search_text}%'").fetchall()

    # No services found
    if len(found_services) == 0:
        services_buttons = ReplyInlineMarkup(rows=[
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message99']}", 'no_data_found')]),
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message96']}", "services_search")]),
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message98']}", b"back_to_services")])
        ])

        menu_message = f"__{bot_lang[user_lang]['message21']}__"
        send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)

        return

    # Services found
    rows, grouped = [], [found_services[i:i+chunk_size] for i in range(0, len(found_services), chunk_size)]

    for row in grouped[:10]:
        buttons_row = []
        for service in row:
            buttons_row.append(
                KeyboardButtonCallback(
                    text=str(service[1]),
                    data=f"service_{service[0]}"
                )
            )
        rows.append(buttons_row)

    services_buttons = ReplyInlineMarkup(rows=[
        *[KeyboardButtonRow(buttons=row) for row in rows],
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message96']}", "services_search")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message98']}", b"back_to_services")])
    ])

    menu_message = f"__{bot_lang[user_lang]['message21']}__"
    send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)


async def Search_numbers_List(event, database, cursor, CommitDatabase, service_id, search_text):
    chunk_size, user_lang = 1, await get_user_lang(event, None, cursor)
    found_numbers = cursor.execute(f"SELECT * FROM numbers_store_lists WHERE service_id = '{service_id}' AND country_name LIKE '%{search_text}%'").fetchall()

    # No numbers found
    if len(found_numbers) == 0:
        services_buttons = ReplyInlineMarkup(rows=[
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message99']}", 'no_data_found')]),
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message100']}", f"countrySearch_{service_id}")]),
            KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message102']}", f"backToCountriesList_{service_id}")])
        ])

        service_name = await get_service(service_id, database, cursor)
        if len(str(service_name).split(' ')) > 2:
            service_stock = f"({service_name})'s"
        else:
            service_stock = f"{service_name}'s"
        user_balance = await get_user_balance(event, cursor)
        menu_message = f"__{bot_lang[user_lang]['message18']}\n\n➨ {service_stock} {bot_lang[user_lang]['message19']} {user_balance}__"
        
        send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)

        return

    # numbers found
    rows, grouped = [], [found_numbers[i:i+chunk_size] for i in range(0, len(found_numbers), chunk_size)]

    for row in grouped[:10]:
        buttons_row = []
        for country in row:
            flag = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = {country[1]}").fetchall()[0][2]
            country_name = cursor.execute(f"SELECT * FROM country_numbes WHERE country_code = {country[1]}").fetchall()[0][1]

            buttons_row.append(
                KeyboardButtonCallback(
                    text=f'{flag} {country_name} ( {country[7]} Credit ~ {country[8]} )',
                    data=f'buy_{country[0]}_{country[1]}'
                )
            )
        rows.append(buttons_row)

    services_buttons = ReplyInlineMarkup(rows=[
        *[KeyboardButtonRow(buttons=row) for row in rows],
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message100']}", f"countrySearch_{service_id}")]),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(f"{bot_lang[user_lang]['message102']}", f"backToCountriesList_{service_id}")])
    ])

    service_name = await get_service(service_id, database, cursor)
    if len(str(service_name).split(' ')) > 2:
        service_stock = f"({service_name})'s"
    else:
        service_stock = f"{service_name}'s"
    user_balance = await get_user_balance(event, cursor)
    menu_message = f"__{bot_lang[user_lang]['message18']}\n\n➨ {service_stock} {bot_lang[user_lang]['message19']} {user_balance}__"
    
    send_to_user = await event.client.send_message(entity=event.chat_id, message=menu_message, buttons=services_buttons)
