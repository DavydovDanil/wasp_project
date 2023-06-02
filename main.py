import telebot
import sqlite3
from telebot import types

def databasecreation():
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_create_table_query = '''CREATE TABLE student_info(
                                    id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                    name TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    patronymic TEXT,
                                    email TEXT NOT NULL,
                                    phone_number INTEGER NOT NULL,
                                    first_stage_result TEXT,
                                    second_stage_result TEXT,
                                    school TEXT NOT NULL,
                                    city TEXT NOT NULL,
                                    status TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def databasefill_studentinfo(a):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_insert_query = """INSERT INTO student_info
                              (id, name, surname,patronymic,email,phone_number,first_stage_result)
                              VALUES (""" + a + """, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""

bot = telebot.TeleBot('6047835028:AAHha2Rn-1_THc9tEpSwvRaVn4N65qDZohI')

@bot.message_handler(commands=['start'])

def start(message):
    databasecreation()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    organizer = types.KeyboardButton('Я организатор')
    uchenik = types.KeyboardButton('Я ученик')
    zachem = types.KeyboardButton('Зачем нужен бот?')
    markup.add(organizer, uchenik, zachem)
    msg = bot.send_message(message.chat.id, 'Здравствуйте, это бот WASP Academy, выберите категорию запроса',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, user_answer)

#exponation menu
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
        bot.register_next_step_handler(msg, step2)
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
def ImStudent(message):
    msg = bot.send_message(message.chat.id,
                           'Вы были перенесены на этап регистрации. Введите фамилию, имя, отчество (Пример: Кисляков Антон Юрьевич)')
    bot.register_next_step_handler(msg, step22)


#exception if user made a mistake
def step1(message):
    if (message.text == 'Назад'):
        start(message)
    else:
        bot.send_message(message.chat.id, 'Вы нажали нечто не то')
        start(message)


#exception in name menu
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


#confirmation after name menu
def step22(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваши имя, фамилия, отчество: {message.text}, вы уверены?",
                           reply_markup=markup)


    bot.register_next_step_handler(msg, step23)


#just exception
def step23(message):
    if message.text == 'Да':
        gorod(message)
    elif message.text == 'Нет':
        ImStudent(message)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Вы вернулись в меню")
    else:
        msg = bot.send_message(message.chat.id, "Вы написали что-то не то и вас перебросило в начальное меню")
        start(message)


#user chooses city
def gorod(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    msg = bot.send_message(message.chat.id,
                           'В каком городе ты живёшь? \nНапример: Москва \n(Обрати внимание, что курс проходит очно в Москве)')
    bot.register_next_step_handler(msg, proverka_goroda)


#city exception
def proverka_proverki_goroda(message):
    if message.text == 'Нет':
        gorod(message)
    elif message.text == 'Да':
        phone(message)
    elif message.text == 'Назад':
        ImStudent(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        gorod(msg)


#city exception exception
def proverka_goroda(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваш город: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_goroda)


def phone(message):
    msg = bot.send_message(message.chat.id, 'Введите номер телефона \n(Например "88005553535" или \n"+78005553535")')
    bot.register_next_step_handler(msg, proverka_phone)


def proverka_phone(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваш город: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_phone)


def proverka_proverki_phone(message):
    if message.text == 'Нет':
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
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваша почта: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_pochtu)


def proverka_proverki_pochtu(message):
    if message.text == 'Нет':
        vvedite_pochtu(message)
    elif message.text == 'Да':
        Vvedenie_K_Testu(message)
    elif message.text == 'Назад':
        phone(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        vvedite_pochtu(msg)


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


conn = sqlite3.connect('kislyakov.db', check_same_thread=False)

bot.polling(none_stop=True)
