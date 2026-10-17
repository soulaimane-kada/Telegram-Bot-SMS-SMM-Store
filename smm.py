from telethon import Button
import json, requests

from change_lan import get_user_lang


# READ CONFIGS
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)



SMM_API_URL = "https://smmai.net/api/v2"
SMM_API_KEY = config["SMM_API_KEY"]


smm_services = json.load(open('smm_services.json', encoding='utf-8'))
bot_lang = json.load(open("lang.json", encoding='UTF-8'))


# Add 50% to the service price ( ex : smmai.net service price 1$ on bot will be 1.50$ )
NetPercentage = 50


# Define table name and columns
table_name = "record_smm_services"
columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "created_by": "INTEGER",
    "service_id": "TEXT",
    "price_in_credits": "TEXT",
    "link": "TEXT",
    "quantity": "TEXT",
    "order_id": "TEXT"
}



subscription_history_columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "user_id": "INTEGER",
    "invoice_id": "TEXT",
    "invoice_link": "TEXT",
    "paid_subscription_at": "DATE",
    "subscription_price": "TEXT"
}


bot_settings_columns = {
    "setting_id": "INTEGER",
    "link_reward": "TEXT",
}


ad_buttons_columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "title": "TEXT",
    "link": "TEXT",
}



limited_offer_columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "offer_name": "TEXT",
    "offer_code": "TEXT",
    "reduce": "FLOAT",
    "valid_days": "INTEGER",
    "created_at": "DATE",
    "end_at": "DATE",
    "status": "TEXT",
    "usage_count": "INTEGER",
}




vip_subscription_columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "price": "FLOAT",
    # "months": "INTEGER",
    "status": "TEXT",
}




# Create the table if it doesn't exist
async def create_table_if_not_existsV2(cursor, database, table_name, columns):
    columns_definitions = ", ".join([f"{column_name} {column_type}" for column_name, column_type in columns.items()])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions})")
    database.commit()
    # print(f"Table '{table_name}' checked or created.")




# Get all orders
def get_orders_from_db(event, cursor):
    cursor.execute(f"SELECT * FROM record_smm_services WHERE created_by = {event.chat_id}")
    orders = cursor.fetchall()
    return orders


# Get order from database
async def GetOrderByOrderId(cursor, order_id):
    order_data = cursor.execute(f"SELECT * FROM record_smm_services WHERE order_id = '{order_id}'").fetchone()
    return order_data


# Get order from database
async def GetOrderById(cursor, id):
    order_data = cursor.execute(f"SELECT * FROM record_smm_services WHERE id = '{id}'").fetchone()
    return order_data


# SMM Record Order
async def smm_record_order(cursor, database, created_by, service_id, price_in_credits, link, quantity, order_id):
    cursor.execute(
        f"INSERT INTO record_smm_services (created_by, service_id, price_in_credits, link, quantity, order_id) VALUES (?,?,?,?,?,?)",
        (created_by, service_id, price_in_credits, link, quantity, order_id)
    )
    database.commit()


# Create the table if it doesn't exist
async def create_table_if_not_exists(cursor, database):
    columns_definitions = ", ".join([f"{column_name} {column_type}" for column_name, column_type in columns.items()])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions})")
    database.commit()
    # print(f"Table '{table_name}' checked or created.")


# Check if a column exists, and if not, add it
async def add_column_if_not_exists(cursor, database, target_table_name, column_name, column_type):
    cursor.execute(f"PRAGMA table_info({target_table_name})")
    existing_columns = [info[1] for info in cursor.fetchall()]
    
    if column_name not in existing_columns:
        cursor.execute(f"ALTER TABLE {target_table_name} ADD COLUMN {column_name} {column_type}")
        print(f"Column '{column_name}' added to '{target_table_name}'.")
        database.commit()

# Add Credits
async def update_user_credits(event, new_credits, database, cursor):
    update_credits = cursor.execute(f"UPDATE bot_users SET credits = {new_credits} WHERE user_id={event.chat_id};"), database.commit()


# Add Percentage
async def add_percentage(number, percentage):
    return number + (percentage / 100) * number

# Create Order
async def CreateOrder(service_id, link, quantity):
    payload = {
        "key": SMM_API_KEY,
        "action": "add",
        "service": service_id,
        "link": link,
        "quantity": quantity
    }
    
    try:
        req = requests.post(SMM_API_URL, params=payload)
        if req.status_code == 200:
            return req.json()
        else:
            return False
    except Exception as error:return False


# Order Info
async def CheckOrder(order_id):
    payload = {
        "key": SMM_API_KEY,
        "action": "status",
        "order": order_id,
    }
    
    try:
        req = requests.post(SMM_API_URL, params=payload)
        if req.status_code == 200:
            if req.json().get('status') != None:
                return req.json()
            else:
                return False
        else:
            return False
    except Exception as error:return False



# Show Services Platform Name
async def SmmServices_List(event, database, cursor, CommitDatabase):
    user_lang = await get_user_lang(event, database, cursor)

    buttons = [
        [Button.inline('Instagram', 'smmShow_instagram'), Button.inline('Tiktok', 'smmShow_tiktok')],
        [Button.inline('Facebook', 'smmShow_facebook'), Button.inline('Twitter', 'smmShow_twitter')],
        [Button.inline('Youtube', 'smmShow_youtube'), Button.inline('Telegram', 'smmShow_telegram')],
        [Button.inline('Threads', 'smmShow_threads'), Button.inline('Twitch', 'smmShow_twitch')],

        # [Button.inline('JACO', 'smmShow_jaco'), Button.inline('Linkedin', 'smmShow_linkedin')],
        # [Button.inline('Soundcloud', 'smmShow_soundcloud')]
        # Button.inline('Kick', 'smmShow_kick')
        # Button.inline('Audiomack', 'smmShow_audiomack')
        # Button.inline('Spotify', 'smmShow_spotify')
    ]

    buttons.append([Button.inline(bot_lang[user_lang]['btn2'], 'back_to_menu')])
    await event.reply(f"__{bot_lang[user_lang]['message51']}__", buttons=buttons)


# Show Services Title Names
async def SmmShowServices(event, smm_type, database, cursor):
    user_lang = await get_user_lang(event, database, cursor)

    buttons = []
    for english_service in smm_services['english']:
        arabic_service = [service for service in smm_services['arabic'] if service['service'] == english_service['service']]
        
        if smm_type in str(english_service['name']).lower() and english_service['type'] == "Default":
            if user_lang == "english":
                buttons.append([Button.inline(english_service['name'], f"smmInfo_{english_service['service']}")])
            else:
                buttons.append([Button.inline(arabic_service[0]['name'], f"smmInfo_{english_service['service']}")])
        
        if len(buttons) == 10:
            break

    buttons.append([Button.inline(bot_lang[user_lang]['btn16'], 'back_to_smmList')])
    await event.reply(f"__{bot_lang[user_lang]['message52']} {smm_type}, {bot_lang[user_lang]['message53']}:__", buttons=buttons)


# Show Service Information Using Its ID
async def SmmShowServiceInfo(event, service_id, database, cursor):
    user_lang = await get_user_lang(event, database, cursor)

    buttons, message = [], bot_lang[user_lang]['message54']
    for english_service in smm_services['english']:
        if service_id == english_service['service']:
            arabic_service = next((service for service in smm_services['arabic'] if service['service'] == english_service['service']), None)

            buttons.append([Button.inline(bot_lang[user_lang]['btn18'], f"smmBuy_{english_service['service']}")])

            if user_lang == "english":
                service_name = english_service['name']
                service_category = english_service['category']
            else:
                service_name = arabic_service['name']
                service_category = arabic_service['category']

            # 🔖 **Type**: {english_service['type']}
            # 🔄 **Dripfeed**: {english_service['dripfeed']}
            # ♻️ **Refill**: {english_service['refill']}
            # ❌ **Cancel**: {english_service['cancel']}
            service_price = await add_percentage(float(english_service['rate']), float(NetPercentage))
            message = f"""
🔢 **{bot_lang[user_lang]['message55']}**: `{english_service['service']}`

🏷️ **{bot_lang[user_lang]['message56']}**: __{service_name}__

💰 **{bot_lang[user_lang]['message57']}**: __{round(service_price, 2)}$ {bot_lang[user_lang]["message69"]} 1000__
🔽 **{bot_lang[user_lang]['message58']}**: __{english_service['min']}__
🔼 **{bot_lang[user_lang]['message59']}**: __{english_service['max']}__

📂 **{bot_lang[user_lang]['message60']}**: __{service_category}__
"""

            break

    buttons.append([Button.inline(bot_lang[user_lang]['btn16'], 'back_to_smmList')])
    await event.reply(message, buttons=buttons)


# Buy Procces
async def SmmBuyService(event, service_id, database, cursor):
    user_lang = await get_user_lang(event, database, cursor)

    await create_table_if_not_exists(cursor, database)
    # add_column_if_not_exists(cursor, database, "quantity", "INTEGER")
    buttons = [
        [Button.inline(bot_lang[user_lang]['btn16'], 'back_to_smmList')]
    ]

    services_data_en = None
    services_data_ar = None
    for english_service in smm_services['english']:
        if service_id == english_service['service']:
            services_data_ar = next((service for service in smm_services['arabic'] if service['service'] == english_service['service']), None)
            services_data_en = english_service
            break

    services_data = None

    if user_lang == 'english':
        services_data = services_data_en
    elif user_lang == 'arabic':
        services_data = services_data_ar

    if services_data == None:
        await event.reply(f'__{bot_lang[user_lang]["message61"]}__', buttons=buttons)
    else:
        user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{event.chat_id}'").fetchone()
        user_balance = user_info[2]
        service_price = await add_percentage(float(services_data['rate']), float(NetPercentage))

        await event.reply(f'''
🏷️ **{bot_lang[user_lang]["message62"]}**: __{services_data['name']}__

💰 **{bot_lang[user_lang]["message57"]}**: __{round(service_price, 2)}$ {bot_lang[user_lang]["message69"]} 1000__
🔽 **{bot_lang[user_lang]["message58"]}**: __{services_data['min']}__
🔼 **{bot_lang[user_lang]["message59"]}**: __{services_data['max']}__

💵 **{bot_lang[user_lang]["message63"]}**: __{round(float(user_balance) * 0.1, 2)}$ ( ~ {round(user_balance, 2)} Credits )__

**‼ {bot_lang[user_lang]["message64"]}:**
__- {bot_lang[user_lang]["message65"]}
- {bot_lang[user_lang]["message66"]}
- {bot_lang[user_lang]["message67"]}
- {bot_lang[user_lang]["message68"]}__
''')

        try:
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message(f'{bot_lang[user_lang]["message70"]}')
                link = (await conv.get_response()).message

                await conv.send_message(f'{bot_lang[user_lang]["message71"]}')
                quantity = (await conv.get_response()).message

            if str(quantity).isdigit():
                quantity = int(quantity)
                if quantity < int(services_data['min']):
                    await event.reply(f"__{bot_lang[user_lang]['message72']}__", buttons=buttons)
                elif quantity > int(services_data['max']):
                    await event.reply(f"__{bot_lang[user_lang]['message73']}__", buttons=buttons)
                else:
                    user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{event.chat_id}'").fetchone()
                    user_balance = user_info[2]

                    total_price = round((quantity / 1000) * float(service_price), 2)
                    total_credits = float(total_price) * 10
                    await event.reply(f'''
🔗 **{bot_lang[user_lang]['message74']}**: {link}
🔢 **{bot_lang[user_lang]['message75']}**: {quantity}

💵 **{bot_lang[user_lang]['message63']}**: {round(user_balance * 0.1, 2)}$ ( ~ {round(user_balance, 2)} Credits )
💰 **{bot_lang[user_lang]['message76']}**: {total_price}$ ( ~ {round(total_credits, 2)} Credits )
''')


                    if user_balance >= total_credits:
                        valid_order = await CreateOrder(service_id, link, quantity)
                        # print (valid_order)
                        if valid_order == False:
                            await event.reply(f"{bot_lang[user_lang]['message77']}", buttons=buttons)
                        else:
                            order_id, error = valid_order.get('order'), valid_order.get('error')

                            if error != None:
                                if error == "Not enough funds on balance" or error == "neworder.error.not_enough_funds":
                                    await event.reply(f"__{bot_lang[user_lang]['message78']}__", buttons=buttons)
                                else:
                                    await event.reply(f"__{bot_lang[user_lang]['message79']}__", buttons=buttons)
                            else:
                                user_info = cursor.execute(f"SELECT * FROM bot_users WHERE user_id = '{event.chat_id}'").fetchone()
                                user_balance = user_info[2]

                                # take the credits from the user
                                new_credits = round(float(user_balance) - float(total_credits), 2)
                                await update_user_credits(event, new_credits, database, cursor)
                                
                                # Record Order
                                await smm_record_order(cursor, database, event.chat_id, str(service_id), str(total_credits), str(link), str(quantity), str(order_id))
                                order_DATA = await GetOrderByOrderId(cursor, order_id)

                                # Send Message To User
                                order_buttons = [
                                    [Button.inline(bot_lang[user_lang]['btn17'], f'smmOrderView_{order_DATA[0]}')],
                                    [Button.inline(bot_lang[user_lang]['btn16'], 'back_to_smmList')]
                                ]
                                await event.reply(f'''
✅ **{bot_lang[user_lang]['message80']}**

🔗 **{bot_lang[user_lang]['message74']}**: {link}
🔢 **{bot_lang[user_lang]['message75']}**: {quantity}

💰 **{bot_lang[user_lang]['message81']}**: {total_price}$ ( ~ {round(total_credits, 2)} Credits )

⏳ __{bot_lang[user_lang]['message82']}__
''', buttons=order_buttons)
                    
                    else:
                        message_details = f"💳 **{bot_lang[user_lang]['message49']}** __{bot_lang[user_lang]['message50']}__"
                        send_to_user = await event.client.send_message(entity=event.chat_id, message=message_details, buttons=buttons)

            else:
                await event.reply(f"__{bot_lang[user_lang]['message83']}__", buttons=buttons)
    

        except Exception as error:pass



# View Order Info
async def SmmViewOrderInfo(event, database, cursor, order_id):
    user_lang = await get_user_lang(event, database, cursor)

    buttons = []
    buttons.append([Button.inline(bot_lang[user_lang]['btn2'], 'back_to_menu')])

    order_data = await GetOrderById(cursor, order_id)
    data = await CheckOrder(order_data[6])
    if data == False:
        await event.reply(f'__{bot_lang[user_lang]["message84"]}__', buttons=buttons)
    else:
        service_id = order_data[2]
        link = order_data[4]
        quantity = order_data[5]
        price_in_credits = order_data[3]

        await event.reply(f'''
🔗 **{bot_lang[user_lang]["message74"]}**: {link}
🔢 **{bot_lang[user_lang]["message75"]}**: {quantity}

💰 **{bot_lang[user_lang]["message81"]}**: {round(float(price_in_credits) * 0.1, 2)}$ ( ~ {round(float(price_in_credits), 2)} Credits )

📊 **{bot_lang[user_lang]["message85"]}**: {data["start_count"]}
⚠️ **{bot_lang[user_lang]["message86"]}**: {data["status"]}
🔢 **{bot_lang[user_lang]["message87"]}**: {data["remains"]}
''', buttons=buttons)



# Function to handle the order pagination
async def ShowSmmRecordOrders(event, database, cursor, order_index):
    await create_table_if_not_exists(cursor, database)

    user_lang = await get_user_lang(event, database, cursor)
    orders = get_orders_from_db(event, cursor)

    if order_index < 0:
        order_index = 0
    elif order_index >= len(orders):
        await event.answer(f"{bot_lang[user_lang]['message88']}", alert=True)
        return

    try:
        await event.delete()
    except:pass

    # Display the current order
    order = orders[order_index]
    message = f'''
🆔 **{bot_lang[user_lang]['message89']}**: {order[0]}

📄 **{bot_lang[user_lang]['message55']}**: {order[2]}
💳 **{bot_lang[user_lang]['message57']}**: {round(float(order[3]) * 0.1, 2)}$ ( ~ {round(float(order[3]), 2)} Credits )

🔗 **{bot_lang[user_lang]['message74']}**: {order[4]}
🔢 **{bot_lang[user_lang]['message75']}**: {order[5]}
🆔 **{bot_lang[user_lang]['message90']}**: {order[6]}
'''
    
    # Send the message with navigation buttons
    await event.reply(
        message,
        buttons=[
            [Button.inline(bot_lang[user_lang]['btn17'], f'smmOrderView_{order[0]}')],
            [Button.inline(f"⬅️ {bot_lang[user_lang]['btn13']}", f"backSmm_{order_index}"), Button.inline(f"{bot_lang[user_lang]['btn14']} ➡️", f"nextSmm_{order_index}")],
            [Button.inline(bot_lang[user_lang]['btn2'], 'back_to_menu')]
        ]
    )
