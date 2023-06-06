import telebot
import sqlite3
from telebot import types
import random
import sys
#    update_student(surname1, "surname", message.chat.id)
  #  update_student(name1, "name", message.chat.id)
   # update_student(patronymic1, "patronymic", message.chat.id)

def databasecreation_student():
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student_info(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_v_chate INTEGER NOT NULL,
                                    name TEXT,
                                    surname TEXT,
                                    patronymic TEXT,
                                    email TEXT ,
                                    phone_number INTEGER ,
                                    first_stage_result TEXT,
                                    second_stage_result TEXT,
                                    school TEXT ,
                                    city TEXT ,
                                    status TEXT );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS organizer_info(
                                        login TEXT PRIMARY KEY NOT NULL,
                                        password TEXT NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS calendar_interview(
                                            date_interview TEXT PRIMARY KEY NOT NULL,
                                            time_interview TEXT,
                                            student_info_id INTEGER);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS calendar_ochniy_etap(
                                                date_interview TEXT PRIMARY KEY NOT NULL,
                                                time_interview TEXT,
                                                student_info_id INTEGER);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                                                variants INTEGER PRIMARY KEY NOT NULL,
                                                student_info_id INTEGER NOT NULL,
                                                task_info_id INTEGER NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS task_info(
                                                    id INTEGER PRIMARY KEY NOT NULL,
                                                    taskitself INTEGER NOT NULL,
                                                    correctanswer INTEGER NOT NULL);''')
    sqlite_connection.commit()
    cursor.close()


def update_student(value, table, idvchate):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_update_query = """UPDATE student_info
    SET \'""" + str(table) + """\' = \'""" + str(value) + """\'
    WHERE id_v_chate = \'""" + str(idvchate) + """\'"""
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_update_query)
    sqlite_connection.commit()
    cursor.close()


bot = telebot.TeleBot('6047835028:AAHha2Rn-1_THc9tEpSwvRaVn4N65qDZohI')


@bot.message_handler(commands=['start'])
def start(message):
    databasecreation_student()
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_insert_query = """INSERT INTO student_info
    (id_v_chate)
    VALUES(\'""" + str(message.chat.id) + """\')"""
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    cursor.close()
    sqliteConnection = sqlite3.connect('kislyakovdatabase.db')
    cursor1 = sqliteConnection.cursor()
    sqlite_select_query = """SELECT COUNT(*) as num FROM
    student_info WHERE id_v_chate LIKE \'""" + str(message.chat.id) + """\'"""
    cursor1.execute(sqlite_select_query)
    a = cursor1.fetchone()[0]
    bot.send_message(message.chat.id, a)
    if a == 1 or a == 0:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        organizer = types.KeyboardButton('Я организатор')
        uchenik = types.KeyboardButton('Я ученик')
        zachem = types.KeyboardButton('Зачем нужен бот?')
        markup.add(organizer, uchenik, zachem)
        msg = bot.send_message(message.chat.id, 'Здравствуйте, это бот WASP Academy, выберите категорию запроса',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, user_answer)
    else:
        bot.send_message(message.chat.id, 'У вас больше одного аккаунта')
        sys.exit(0)


# exponation menu
def user_answer(message):
    if message.text == 'Я организатор':
        bot.send_message(message.chat.id, 'Введите ваш пароль')
        # bot.register_next_step_handler(msgge, ImOrganiser)
    elif message.text == 'Я ученик':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        ready = types.KeyboardButton('Готов(a) регистрироваться!')
        markup.add(ready, back)
        msg = bot.send_message(message.chat.id,
                               'Поступление на наши курсы состоит из 4-ёх этапов: \n\n1) Заполнение анкеты\n2) Тест в онлайн-формате\n3) Тест в очном формате\n4) Интервью',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, ImStudent1)
    elif message.text == 'Зачем нужен бот?':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        msge = bot.send_message(message.chat.id, 'Бот нужен для помощи в регистрации на курсы WASP Academy',
                                reply_markup=markup)
        bot.register_next_step_handler(msge, step1)


# def ImOrganiser(message):
# bot.send_message(chat_id)

# if student menu clicked
def ImStudent1(message):
    msg = bot.send_message(message.chat.id,
                           'Вы были перенесены на этап регистрации. Введите имя (Пример: Антон)')
    bot.register_next_step_handler(msg, ImStudent2)

def ImStudent2(message):
    msg = bot.send_message(message.chat.id,
                           'Введите фамилию(Пример: Кисляков)')
    update_student(message.text,"name",message.chat.id)


    bot.register_next_step_handler(msg, ImStudent3)


def ImStudent3(message):
    msg = bot.send_message(message.chat.id,
                           'Введите отчество(Пример: Юрьевич)')
    update_student(message.text, "surname", message.chat.id)

    bot.register_next_step_handler(msg, step22)
# exception if user made a mistake
def step1(message):
    if (message.text == 'Назад'):
        start(message)
    else:
        bot.send_message(message.chat.id, 'Вы нажали нечто не то')
        start(message)


# exception in name menu
def step2(message):
    if (message.text == 'Назад'):
        start(message)
    elif (message.text == 'Готов(a) регистрироваться!'):

        msg = bot.send_message(message.chat.id,
                               'Вы были перенесены на этап регистрации. Введите фамилию, имя, отчество (Пример: Кисляков Антон Юрьевич)')
        bot.register_next_step_handler(msg, step22)
    else:
        bot.send_message(message.chat.id, 'Вы нажали что-то не то, и вас перебросило')
        start(message)


# confirmation after name menu
def step22(message):
    update_student(message.text, "patronymic", message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Вы уверены, что ввели правильные данные?",
                           reply_markup=markup)

    bot.register_next_step_handler(msg, step23)


# just exception
def step23(message):
    if message.text == 'Да':
        gorod(message)
    elif message.text == 'Нет':
        update_student("null", "surname", message.chat.id)
        update_student("null", "patronymic", message.chat.id)
        update_student("null", "name", message.chat.id)
        ImStudent1(message)
    else:
        msg = bot.send_message(message.chat.id, "Вы написали что-то не то и вас перебросило в начальное меню")
        start(message)


# user chooses city
def gorod(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    msg = bot.send_message(message.chat.id,
                           'В каком городе ты живёшь? \nНапример: Москва \n(Обрати внимание, что курс проходит очно в Москве)')
    bot.register_next_step_handler(msg, proverka_goroda)


# city exception
def proverka_proverki_goroda(message):
    if message.text == 'Нет':
        update_student("null", "city", message.chat.id)
        gorod(message)
    elif message.text == 'Да':
        phone(message)
    elif message.text == 'Назад':
        ImStudent1(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        gorod(msg)


# city exception exception
def proverka_goroda(message):
    check_gorod = message.text
    update_student(check_gorod, "city", message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваш город: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_goroda)


def phone(message):
    msg = bot.send_message(message.chat.id, 'Введите номер телефона \n(Например "88005553535")')
    bot.register_next_step_handler(msg, proverka_phone)


def proverka_phone(message):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваш номер телефона: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_phone)
    update_student(message.text, "phone_number", message.chat.id)

def proverka_proverki_phone(message):
    if message.text == 'Нет':
        update_student("null", "phone_number", message.chat.id)
        phone(message)
    elif message.text == 'Да':

        vvedite_pochtu(message)
    elif message.text == 'Назад':
        gorod(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        phone(msg)


def vvedite_pochtu(message):
    msg = bot.send_message(message.chat.id, 'Введите почту \n(Например "kislyakovanton@lit1533.com")')
    bot.register_next_step_handler(msg, proverka_pochtu)


def proverka_pochtu(message):
    check_email = message.text
    update_student(check_email, "email", message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваша почта: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_pochtu)


def proverka_proverki_pochtu(message):
    if message.text == 'Нет':
        update_student("null", "email", message.chat.id)
        vvedite_pochtu(message)
    elif message.text == 'Да':
        vvedite_school(message)
    elif message.text == 'Назад':
        vvedite_school(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        vvedite_school(msg)


def vvedite_school(message):
    msg = bot.send_message(message.chat.id, 'Введите название вашего учебного заведения \n(Например "ГБОУ Школа №1488" или НИУ ВШЭ)')
    bot.register_next_step_handler(msg, proverka_school)

def proverka_school(message):
    check_school = message.text
    update_student(check_school, "school", message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваше учебное заведение: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_school)


def proverka_proverki_school(message):
    if message.text == 'Нет':
        update_student("null", "school", message.chat.id)
        vvedite_school(message)
    elif message.text == 'Да':
        Vvedenie_K_Testu(message)
    elif message.text == 'Назад':
        vvedite_pochtu(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        phone(msg)


def Vvedenie_K_Testu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, 'Теперь тебе нужно пройти тест, который будет длиться 1 час\nТы готов?',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_gotovnosti_k_testu)


def proverka_gotovnosti_k_testu(message):
    if message.text == 'Нет':
        bot.send_message(message.chat.id, 'Возвращайся, когда будешь готов!')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, 'Теста пока нет')
    elif message.text == 'Назад':
        vvedite_pochtu(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        Vvedenie_K_Testu(msg)


@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Напишите /start, чтобы использовать бота')


def step_back(message):
    start(message)


@bot.message_handler(func=lambda message: message.text == 'Назад', content_types=['text'])
def step2_back_handler(message):
    start(message)



bot.polling(none_stop=True)