#    ▄████████    ▄█   ▄█▄    ▄████████   ▄▄▄▄███▄▄▄▄   ███▄▄▄▄   ▄██   ▄      ▄████████ 
#   ███    ███   ███ ▄███▀   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███▀▀▀██▄ ███   ██▄   ███    ███ 
#   ███    █▀    ███▐██▀     ███    ███ ███   ███   ███ ███   ███ ███▄▄▄███   ███    █▀  
#   ███         ▄█████▀     ▄███▄▄▄▄██▀ ███   ███   ███ ███   ███ ▀▀▀▀▀▀███   ███        
# ▀███████████ ▀▀█████▄    ▀▀███▀▀▀▀▀   ███   ███   ███ ███   ███ ▄██   ███ ▀███████████ 
#          ███   ███▐██▄   ▀███████████ ███   ███   ███ ███   ███ ███   ███          ███ 
#    ▄█    ███   ███ ▀███▄   ███    ███ ███   ███   ███ ███   ███ ███   ███    ▄█    ███ 
#  ▄████████▀    ███   ▀█▀   ███    ███  ▀█   ███   █▀   ▀█   █▀   ▀█████▀   ▄████████▀  
#                ▀           ███    ███                                                  
from termcolor import colored
import telebot
from telebot import types
from beluconfig import *
import asyncio
import time
start_timer = time.time()
print(colored(f"\nОбратите внимание ниже!\n", "green"))
print("Создали бота - Константин/Лев, идея их. Копирование бота и функционал подобный этому - Запрещен.")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['admin'])
def admin(message):
    msg = bot.send_message(message.chat.id, "Введите пароль:")
    bot.register_next_step_handler(msg, admin_password)
def admin_password(message):
    if message.text == "0QDyvyHdN_":
        keyboard1 = types.InlineKeyboardMarkup()
        keyboard1.row_width = 2
        menu2 = types.InlineKeyboardButton(text="👥 Рассылка", callback_data="spam")
        menu3 = types.InlineKeyboardButton(text="📊 Статистика", callback_data = "stat")
        keyboard1.add(menu2, menu3)
        bot.send_message(message.chat.id, "Админ панель успешно активированна!", reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, "Упс! Неверный пароль.")
@bot.message_handler(commands=['start'])
def start(message):
  users = open("users.txt", "r")
  if not str(message.chat.id) in users.read():
      users.close()
      users = open("users.txt", "w")
      users.write(str(message.chat.id) + "\n")
      users.close()
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton('⭐ Портфолио', url='https://t.me/beguginkartinka'))
  markup.add(types.InlineKeyboardButton('❤️ Стикер Пак', url='https://t.me/addstickers/belugadmin'))
  bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! ❤️ \n\nЯ - Белуга, ваш виртуальный и неповторимый! \n\nЯ готов помочь вам разобраться в вопросах и предложить различные варианты действий. \n\nЯ не являюсь заменой человеческому общению, но могу предоставить вам полезную информацию и сэкономить ваше время. \n\nИспользуйте команду /menu, чтобы увидеть полный список моих возможностей. \n\nВерсия бота - {version}', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def inline_key(a):
    if a.text == "/menu":
        mainmenu = types.InlineKeyboardMarkup()
        obomne = types.InlineKeyboardButton(text='ℹ️ FAQ', callback_data='obomne')
        rekvizit = types.InlineKeyboardButton(text='💸 Помощь', callback_data='rekvizit')
        kontacty = types.InlineKeyboardButton(text='👥 Сотрудники', callback_data='kontacty')
        mainmenu.add(obomne, rekvizit, kontacty)
        bot.send_message(a.chat.id, 'Вы находитесь в управлении функционалом бота, нажмите то, что интересует! :3', reply_markup=mainmenu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        obomne = types.InlineKeyboardButton(text='ℹ️ FAQ', callback_data='obomne')
        rekvizit = types.InlineKeyboardButton(text='💸 Помощь', callback_data='rekvizit')
        kontacty = types.InlineKeyboardButton(text='👥 Сотрудники', callback_data='kontacty')

        mainmenu.add(obomne, rekvizit, kontacty)
        bot.edit_message_text('Вы находитесь в управлении функционалом бота, нажмите то, что интересует! :3', call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "kontacty":
        next_menu = types.InlineKeyboardMarkup()
        spic = types.InlineKeyboardButton('✅ Написать мне', url='https://t.me/belugadmin')
        back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='mainmenu')
        next_menu.add(spic, back)
        bot.edit_message_text(f'Чтобы написать мне, нажмите кнопочку ниже и начинайте интересный диалог! :3 \n\nСписок сотрудников: \n{yhactniki}', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
    elif call.data == "obomne":
        next_menu = types.InlineKeyboardMarkup()
        spic = types.InlineKeyboardButton('ℹ️ Мой личный канал', url='https://t.me/beluginisapozhki')
        portf = types.InlineKeyboardButton('⭐ Портфолио', url='https://t.me/beguginkartinka')
        back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='mainmenu')
        next_menu.add(spic, back, portf)
        bot.edit_message_text('Я графический дизайнер с опытом в создании ярких и запоминающихся визуальных решений. \n\nСпециализируюсь на двух направлениях: роспись одежды, превращая ее в носимое искусство, и пиксель-арт на заказ. \n\nМогу воплотить любую вашу идею в пикселях - от графических интерфейсов и спрайтов для Minecraft, до милых котиков на аватарки. \n\nЕсли вам нужен уникальный дизайн, заходите в мой Telegram-канал (по кнопке ниже "Портфолио") - там вы найдете больше примеров моих работ!', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
    elif call.data == "rekvizit":
        next_menu = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='mainmenu')
        next_menu.add(back)
        bot.edit_message_text('Если вам захочется отблагодарить меня, вот номер карты: \n\n5228600544067020 (Александр П.). \n\nВаша поддержка будет очень кстати! Спасибо! 😉', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
    elif call.data == "stat":
        next_menu = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='🔙 В админ панель', callback_data='admin_menu')
        next_menu.add(back)
        elapsed_seconds = time.time() - start_timer
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_seconds))
        users = open("users.txt", "r")
        users_count = len(users.readlines())
        users.close()
        bot.edit_message_text(f'Статистика бота: \n\nВремя работы: {formatted_time} \n\nКоличество пользователей: {users_count}', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
    elif call.data == "admin_menu":
        keyboard1 = types.InlineKeyboardMarkup()
        keyboard1.row_width = 2
        menu2 = types.InlineKeyboardButton(text="👥 Рассылка", callback_data="spam")
        menu3 = types.InlineKeyboardButton(text="📊 Статистика", callback_data = "stat")
        keyboard1.add(menu2, menu3)
        bot.edit_message_text(f'Вы вернулись в админ панель!', call.message.chat.id, call.message.message_id, reply_markup=keyboard1)
    elif call.data == "spam":
        msg = bot.send_message(call.message.chat.id, "Введите текст рассылски:")
        bot.register_next_step_handler(msg, spamer)
def spamer(message):
    users = open("users.txt", "r")
    users_list = users.read().splitlines()
    users.close()
    for user in users_list:
        try:
            bot.send_message(user, message.text)
        except:
            pass
    bot.send_message(message.chat.id, "Рассылка завершена!")
bot.infinity_polling(none_stop=True)
