bot_api = "5816162831:AAHNRlAhj0VX2b4tmpluGN7jdtOvG7yEID4"

import os
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import re
# from flask import Flask

# Подключение к базе данных
conn = sqlite3.connect("lib/database.db")
# Создание таблиц для каждого курса и группы
for course_num in range(1, 5):
    for group_num in range(1, 10):
        table_name = f"group_{course_num}_{group_num}"
        # Создание таблицы
        conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (day TEXT, number TEXT, lesson TEXT)")
# Закрытие соединения с базой данных
conn.close()

# Путь к папке с базой данных
folder_path = "lib"
# Название файла базы данных
db_name = "database.db"

# Проверяем существует ли файл базы данных
db_path = os.path.join(folder_path, db_name)
if os.path.exists(db_path):
    print("База данных существует")
else:
    # Подключение к базе данных
    conn = sqlite3.connect("lib/database.db")
    # Создание таблиц для каждого курса и группы
    for course_num in range(1, 5):
        for group_num in range(1, 10):
            table_name = f"group_{course_num}_{group_num}"
            # Создание таблицы
            conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (day TEXT, number INT, lesson TEXT)")
    # Закрытие соединения с базой данных
    conn.close()

bot = telebot.TeleBot(bot_api)

hello_text = "Привет"
text_course = 'Выберите курс'
text_groups = "Выберите группу"
text_days = "Выберите день"
text_days_admin = "Выберите день для добавления пар"

course = 0
group = 0
day_edit = 0

# id_admin = 1210146115
id_admin = 922107973

flag_admin = False


# Клавиатуры
btn_return_main = InlineKeyboardButton(text = "Назад", callback_data = 'return_main')
btn_return_group = InlineKeyboardButton(text = 'Назад', callback_data = 'return_course')
btn_return_days = InlineKeyboardButton(text = 'Назад', callback_data = 'return_days')
btn_return_timetable = InlineKeyboardButton(text = 'Назад', callback_data = 'return_timetable')

btn_course = InlineKeyboardButton(text="Выберите курс", callback_data='course')
keyboard_main = InlineKeyboardMarkup(row_width=2)
keyboard_main.add(btn_course)

btn_admin = InlineKeyboardButton(text = "Админ", callback_data = 'admin')

keyboard_main_admin = InlineKeyboardMarkup(row_width = 2)
keyboard_main_admin.add(btn_course, btn_admin)

btn_course1 = InlineKeyboardButton(text = "Первый курс", callback_data = "course1")
btn_course2 = InlineKeyboardButton(text = "Второй курс", callback_data = "course2")
btn_course3 = InlineKeyboardButton(text = "Третий курс", callback_data = "course3")
btn_course4 = InlineKeyboardButton(text = "Четвёртый курс", callback_data = "course4")
keyboard_courses = InlineKeyboardMarkup(row_width = 2)
keyboard_courses.add(btn_course1, btn_course2, btn_course3, btn_course4, btn_return_main)

btn_group_1 = InlineKeyboardButton(text = 'Группа 1', callback_data = 'group1')
btn_group_2 = InlineKeyboardButton(text = 'Группа 2', callback_data = 'group2')
btn_group_3 = InlineKeyboardButton(text = 'Группа 3', callback_data = 'group3')
btn_group_4 = InlineKeyboardButton(text = 'Группа 4', callback_data = 'group4')
btn_group_5 = InlineKeyboardButton(text = 'Группа 5', callback_data = 'group5')
btn_group_6 = InlineKeyboardButton(text = 'Группа 6', callback_data = 'group6')
btn_group_7 = InlineKeyboardButton(text = 'Группа 7', callback_data = 'group7')
btn_group_8 = InlineKeyboardButton(text = 'Группа 8', callback_data = 'group8')
btn_group_9 = InlineKeyboardButton(text = 'Группа 9', callback_data = 'group9')
keyboard_groups = InlineKeyboardMarkup(row_width = 2)
keyboard_groups.add(btn_group_1, btn_group_2, btn_group_3, btn_group_4, btn_group_5, btn_group_6, btn_group_7, btn_group_8, btn_group_9)
keyboard_groups.add(btn_return_group)

btn_day1 = InlineKeyboardButton(text = 'Понедельник', callback_data = 'day1')
btn_day2 = InlineKeyboardButton(text = 'Вторник', callback_data = 'day2')
btn_day3 = InlineKeyboardButton(text = 'Среда', callback_data = 'day3')
btn_day4 = InlineKeyboardButton(text = 'Четверг', callback_data = 'day4')
btn_day5 = InlineKeyboardButton(text = 'Пятница', callback_data = 'day5')
btn_day6 = InlineKeyboardButton(text = 'Суббота', callback_data = 'day6')
btn_week = InlineKeyboardButton(text = 'Неделя', callback_data = 'week')
keyboard_days = InlineKeyboardMarkup(row_width = 2)
keyboard_days.add(btn_day1, btn_day2, btn_day3, btn_day4, btn_day5, btn_day6, btn_week)
keyboard_days.add(btn_return_days)

keyboard_timetable = InlineKeyboardMarkup(row_width=2)
keyboard_timetable.add(btn_return_timetable)

keyboard_days_admin = InlineKeyboardMarkup(row_width = 2)
keyboard_days_admin.add(btn_day1, btn_day2, btn_day3, btn_day4, btn_day5, btn_day6, btn_return_days)

btn_add_lesson = InlineKeyboardButton(text = "Добавить пару", callback_data = 'add_lesson')
btn_clear_lesson = InlineKeyboardButton(text = 'Очистить день', callback_data = 'clear_lesson')
btn_look_lesson = InlineKeyboardButton(text = 'Посмотереть расписание', callback_data = 'look_lesson')
btn_return_edit_lesson = InlineKeyboardButton(text = 'Назад', callback_data = 'return_edit_lesson')
keyboard_edit_lesson = InlineKeyboardMarkup(row_width = 2)
keyboard_edit_lesson.add(btn_add_lesson, btn_look_lesson, btn_clear_lesson)
keyboard_edit_lesson.add(btn_return_edit_lesson)

btn_return_add_lesson = InlineKeyboardButton(text = 'Назад', callback_data = 'return_add_lesson')
keyboard_add_lesson = InlineKeyboardMarkup()
keyboard_add_lesson.add(btn_return_add_lesson)


def add_lesson(message):
    lesson = str(message.text)
    table_name = f'group_{course}_{group}'
    connection = sqlite3.connect("lib/database.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT MAX(number) FROM {table_name} WHERE day = {day_edit}")
    try:
        number = int(cursor.fetchone()[0])
        new_number = number + 1
    except:
        new_number = 1
    cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?)', (day_edit, new_number, lesson))
    connection.commit()
    connection.close()
    bot.send_message(message.chat.id, "Пара успешно добавлена!", reply_markup=keyboard_edit_lesson)



@bot.message_handler(commands=['start'])
def start(message):
    global flag_admin
    flag_admin = False
    if message.chat.id == id_admin:
       bot.send_message(message.chat.id, hello_text, reply_markup=keyboard_main_admin)
    else:
        bot.send_message(message.chat.id, hello_text, reply_markup=keyboard_main)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global course, group, flag_admin, day_edit
    if call.data == 'course':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_course, reply_markup = keyboard_courses)

    if call.data == 'course1':
        course = 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_groups, reply_markup = keyboard_groups)
    if call.data == 'course2':
        course = 2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_groups, reply_markup = keyboard_groups)
    if call.data == 'course3':
        course = 3
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_groups, reply_markup = keyboard_groups)
    if call.data == 'course4':
        course = 4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_groups, reply_markup = keyboard_groups)

    if call.data == 'group1':
        group = 1
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите день', reply_markup = keyboard_days)
    if call.data == 'group2':
        group = 2
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group3':
        group = 3
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group4':
        group = 4
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group5':
        group = 5
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group6':
        group = 6
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group7':
        group = 7
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group8':
        group = 8
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'group9':
        group = 9
        if flag_admin == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days_admin, reply_markup = keyboard_days_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)


    if call.data == 'day1' and flag_admin == False:
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '1'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'day2':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '2'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'day3':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '3'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'day4':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '4'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'day5':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '5'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'day6':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '6'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()
    if call.data == 'week':
        # Подключение к базе данных
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name}"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание списка уникальных дней
        days = []
        for row in result:
            if row[0] not in days:
                days.append(row[0])
        # Создание строки с несколькими строками
        message = ""
        for day in days:
            message += f"\n{day} день\n"
            for row in result:
                if row[0] == day:
                    message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup=keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()


    if (call.data == 'day1') and (flag_admin == True):
        day_edit = 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)
    if (call.data == 'day2') and (flag_admin == True):
        day_edit = 2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)
    if (call.data == 'day3') and (flag_admin == True):
        day_edit = 3
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)
    if (call.data == 'day4') and (flag_admin == True):
        day_edit = 4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)
    if (call.data == 'day5') and (flag_admin == True):
        day_edit = 5
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)
    if (call.data == 'day6') and (flag_admin == True):
        day_edit = 6
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)


    if call.data == 'add_lesson':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите пару", reply_markup = keyboard_add_lesson)
        bot.register_next_step_handler(call.message, add_lesson)

    if call.data == 'look_lesson':
        conn = sqlite3.connect('lib/database.db')
        cursor = conn.cursor()
        # SQL-запрос для получения данных за первый день
        table_name = f'group_{course}_{group}'
        query = f"SELECT * FROM {table_name} WHERE day = '{day_edit}'"
        # Выполнение запроса и получение результатов
        cursor.execute(query)
        result = cursor.fetchall()
        # Создание строки с несколькими строками
        message = ""
        for row in result:
            message += f"{row[1]} пара. Предмет: {row[2]}\n"
        # Отправка сообщения
        if message == '':
            message = "Расписания на этот день нет"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message, reply_markup = keyboard_timetable)
        # Закрытие соединения с базой данных
        conn.close()


    if call.data == 'return_main':
        flag_admin = False
        if call.message.chat.id == id_admin:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=hello_text, reply_markup = keyboard_main_admin)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=hello_text, reply_markup = keyboard_main)
        course = 0
    if call.data == 'return_course':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_course, reply_markup = keyboard_courses)
        group = 0
    if call.data == 'return_days':
        day_edit = 0
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите группу', reply_markup = keyboard_groups)
    if call.data == 'return_timetable':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_days, reply_markup = keyboard_days)
    if call.data == 'return_edit_lesson':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите день, для добавления пар", reply_markup = keyboard_days_admin)
    if call.data == 'return_add_lesson':
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Редактирование дня", reply_markup = keyboard_edit_lesson)



    if call.data == 'admin':
        flag_admin = True
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Панель администратора', reply_markup = keyboard_courses)



def send_start_message():
    bot.send_message(chat_id=1210146115, text="Бот перезапущен!")
send_start_message()
print('Бот запущен...') 

bot.polling()
