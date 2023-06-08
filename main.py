import telebot
import sqlite3
from telebot import types
import random
from random import random, randrange, randint
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

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                                                user_id INTEGER PRIMARY KEY,
                                                task_id_1 INTEGER,
                                                task_id_2 INTEGER,
                                                task_id_3 INTEGER,
                                                task_id_4 INTEGER,
                                                task_id_5 INTEGER,
                                                user_answer_1 TEXT,
                                                user_answer_2 TEXT,
                                                user_answer_3 TEXT,
                                                user_answer_4 TEXT,
                                                user_answer_5 TEXT,
                                                points_1 TEXT,
                                                points_2 TEXT,
                                                points_3 TEXT,
                                                points_4 TEXT,
                                                points_5 TEXT,
                                                answer_1 TEXT,
                                                answer_2 TEXT,
                                                answer_3 TEXT,
                                                answer_4 TEXT,
                                                answer_5 TEXT,
                                                FOREIGN KEY (user_id)  REFERENCES student_info(id)
                                                 );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS organizer_info(
                                        login TEXT PRIMARY KEY,
                                        password TEXT NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS calendar_interview(
                                            date_interview TEXT PRIMARY KEY,
                                            time_interview TEXT,
                                            student_info_id INTEGER UNIQUE
                                            );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS calendar_ochniy_etap(
                                                date_interview TEXT PRIMARY KEY,
                                                time_interview TEXT,
                                                student_info_id INTEGER);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS task_info(
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    taskitself TEXT,
                                                    type_id INTEGER,
                                                    answer INTEGER);''')


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

def insert_test():
    type_1_task_1 = "1.	Определите, в какой минимальной системе счисления может быть записано число 2537." \
                    " Переведите число из этой системы счисления в десятичную."
    type_2_task_1 = "2.	Напишите наименьшее целое число x, для которого истинно следующее высказывание:" \
                    "НЕ ((X < 2) И (X > 5)) ИЛИ (X > 10)"
    type_3_task_1 = "3.	Школьник работал с файлом C:\Documents\Education\Math\Math-Homework1.pdf. " \
                    "Затем он поднялся на уровень вверх, создал там каталог Tasks, а в нем два каталога:" \
                    " Homeworks и Tests. Школьник перенес директорию Math в директорию Homeworks. " \
                    "Каким стало полное имя файла, с которым работал школьник, после сделанных им операций?"
    type_4_task_1 = "4.	Ниже задан алгоритм вычисления значения функции F(n), где n – это натуральное число: " \
                    "\nF(1) = 1; \nF(n) = F(n - 1) * (n + 1) * 2 \n Чему равно значение функции F(4)?"
    type_5_task_1 = "5.	Перед вами программа, записанная на пяти языках программирования." \
                    " Было проведено 10 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:" \
                    " \n(1, 2); (5, 4); (-10, 6); (9, 2); (1, -6); (11, 12); (-11, 12); (-10; 10); (12; -1); (-12; 1)." \
                    "\nСколько было запусков, при которых программа напечатала слово «YES»?"
    #bot.send_photo(message.chat.id, get("https://i0.wampi.ru/2019/11/12/image.png").content)
    type_1_task_2 = "1.	Определите, в какой минимальной системе счисления может быть записано число 7531." \
                   " Переведите число из этой системы счисления в десятичную."
    type_2_task_2 = "2.	Напишите наименьшее целое число x, для которого истинно следующее высказывание:" \
                    "\nНЕ ((X < 5) И (X > 8)) ИЛИ (X > 2)"
    type_3_task_2 = "3.	Сотрудник компании работал с файлом E:\Sheets\Departments\Cloud\Salary.xlsx. " \
                    "Затем он поднялся на два уровня вверх, создал там каталог Accounts, а в нем четыре каталога:" \
                    " Cloud, IT, Sales, Marketing. " \
                    "Сотрудник скопировал файл в директорию Accounts. Каким стало полное имя скопированного файла?"
    type_4_task_2 = "4.	Ниже задан алгоритм вычисления значения функции F(n), где n – это натуральное число:" \
                    "\nF(n) = n при n <= 2; \nF(n) = F(n - 1) * (n + 1) \nЧему равно значение функции F(5)?"
    type_5_task_2 = "5.	Перед вами программа, записанная на пяти языках программирования. " \
                    "Было проведено 10 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел: " \
                    "\n(9, -5); (12, -1); (3, 0); (-9, 2); (1, -6); (11, 12); (-11, 12); (-5; 9); (5; 7); (7; 5)." \
                    "\nСколько было запусков, при которых программа напечатала слово «YES»?"

    type_1_task_3 = "1.	Определите, в какой минимальной системе счисления может быть записано число 5464." \
                    " Переведите число из этой системы счисления в десятичную."
    type_2_task_3 = "2.	Напишите наименьшее целое число x, для которого истинно следующее высказывание:" \
                    "\nНЕ ((X < 0) И (X > 9)) ИЛИ (X > 9)"
    type_3_task_3 = "3.	Программист работал с файлом D:\Application\Source\index.html. " \
                    "Затем он поднялся на два уровня вверх, создал там каталог Pages, а в нем два каталога: " \
                    "Debug, Release. Сотрудник переместил директорию Source в директорию Debug. " \
                    "Каким стало полное имя файла, с которым работал программист, после сделанных им операций?"
    type_4_task_3 = "4.	Ниже задан алгоритм вычисления значения функции F(n), где n – это натуральное число:" \
                    "\nF(n) = n при n <= 3;" \
                    "\nF(n) = F(n - 1) * (n + 1) * n " \
                    "\nЧему равно значение функции F(5)?"
    type_5_task_3 = "5.	Перед вами программа, записанная на пяти языках программирования. " \
                    "Было проведено 10 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел: " \
                    "\n(1, 0); (2, -1); (3, 7); (5, 8); (9, -6); (11, 12); (-11, 12); (-6; 9); (5; 7); (1; 5)." \
                    "\nСколько было запусков, при которых программа напечатала слово «YES»?"

    type_1_task_4 = "1.	Определите, в какой минимальной системе счисления может быть записано число 3421." \
                    " Переведите число из этой системы счисления в десятичную."
    type_2_task_4 = "2.	Напишите наименьшее целое число x, для которого истинно следующее высказывание:" \
                    "\nНЕ ((X < 3) И (X > 4)) ИЛИ (X > 3)"
    type_3_task_4 = "3.	Дизайнер работал с файлом F:\Assets\Project\mockup.ai. " \
                    "Затем он поднялся на два уровня вверх, создал там каталог Mockups, а в нем два каталога: " \
                    "Done, Doing. Сотрудник переместил файл в директорию Doing." \
                    " Каким стало полное имя файла, с которым работал дизайнер, после сделанных им операций?"
    type_4_task_4 = "4.	Ниже задан алгоритм вычисления значения функции F(n), где n – это натуральное число:" \
                    "\nF(n) = n при n <= 1;" \
                    "\nF(n) = F(n - 1) * (n + 1) * n" \
                    "\nЧему равно значение функции F(3)?"
    type_5_task_4 = "5.	Перед вами программа, записанная на пяти языках программирования. " \
                    "Было проведено 10 запусков программы, при которых в качестве значений переменных s и t" \
                    " вводились следующие пары чисел: " \
                    "\n(11, 0); (6, -1); (7, 7); (5, 8); (-8, 5); (11, 12); (-11, 12); (-6; 9); (5; 7); (1; 5)." \
                    "\nСколько было запусков, при которых программа напечатала слово «YES»?"

    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_check_query = """SELECT COUNT(id) FROM task_info"""
    cursor1 = sqlite_connection.cursor()
    cursor1.execute(sqlite_check_query)
    a = cursor1.fetchone()[0]
    if(a==0):
        sqlite_insert_query1 = """INSERT INTO task_info(taskitself,type_id, answer)
                VALUES(\'""" + str(type_1_task_1) + """\', 1, "1375"),(\'""" + str(
            type_1_task_2) + """\', 1, "3929"),(\'""" + str(type_1_task_3) + """\', 1,"1957"),
                (\'""" + str(type_1_task_4) + """\', 1,"486"),(\'""" + str(type_2_task_1) + """\', 2,"2"),(\'""" + str(
            type_2_task_2) + """\', 2,"3"),
                (\'""" + str(type_2_task_3) + """\', 2,"9"),(\'""" + str(type_2_task_4) + """\', 2,"3"),(\'""" + str(
            type_3_task_1) + """\', 3,"C:\Documents\Education\Tasks\Homeworks\Math\Math-Homework1.pdf"),
                (\'""" + str(type_3_task_2) + """\', 3,"E:\Sheets\Accounts\Salary.xlsx"),(\'""" + str(
            type_3_task_3) + """\', 3,"D:\Pages\Debug\index.html"),(\'""" + str(type_3_task_4) + """\', 3,"F:\Mockups\Doing\mockup.ai"),
                (\'""" + str(type_4_task_1) + """\', 4,"480"),(\'""" + str(
            type_4_task_2) + """\', 4,"240"),(\'""" + str(type_4_task_3) + """\', 4,"1800"),
                (\'""" + str(type_4_task_4) + """\', 4,"2"),(\'""" + str(type_5_task_1) + """\', 5,"5"),(\'""" + str(
            type_5_task_2) + """\', 5,"5"),
                (\'""" + str(type_5_task_3) + """\', 5,"5"),(\'""" + str(type_5_task_4) + """\', 5,"7")"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_insert_query1)
        sqlite_connection.commit()
        cursor.close()


def select_random_test_task(task_type):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT id FROM task_info
        WHERE type_id = {task_type};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    if(task_type == 1):
        random_task = randint(1, 4)
    elif (task_type == 2):
        random_task = randint(5, 8)
    elif(task_type == 3):
        random_task = randint(9, 12)
    elif(task_type == 4):
        random_task = randint(13, 16)
    elif(task_type == 5):
        random_task = randint(17, 20)
    sqlite_connection.commit()
    cursor.close()
    return random_task


def select_answer(task_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT answer FROM task_info
            WHERE id = {task_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_instruction_task(task_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT taskitself FROM task_info
                WHERE id = {task_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_sozdanniy_varik1(user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT task_id_1 FROM tasks
                    WHERE user_id = {user_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_sozdanniy_varik2(user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT task_id_2 FROM tasks
                    WHERE user_id = {user_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_sozdanniy_varik3(user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT task_id_3 FROM tasks
                    WHERE user_id = {user_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_sozdanniy_varik4(user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT task_id_4 FROM tasks
                    WHERE user_id = {user_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_sozdanniy_varik5(user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT task_id_5 FROM tasks
                    WHERE user_id = {user_id};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


def select_user_id(id_v_chate):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT id FROM student_info
                        WHERE id_v_chate = {id_v_chate};""")
    rows = cursor.fetchall()
    A = [elt[0] for elt in rows]
    sqlite_connection.commit()
    cursor.close()
    return A[0]


bot = telebot.TeleBot('6047835028:AAHha2Rn-1_THc9tEpSwvRaVn4N65qDZohI')


@bot.message_handler(commands=['start'])
def start(message):
    databasecreation_student()
    insert_test()
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    sqlite_insert_query = """INSERT INTO student_info
    (id_v_chate)
    VALUES(\'""" + str(message.chat.id) + """\')"""
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    sqlite_select_query = """SELECT COUNT(*) as num FROM
    student_info WHERE id_v_chate LIKE \'""" + str(message.chat.id) + """\'"""
    cursor.execute(sqlite_select_query)
    a = cursor.fetchone()[0]
    bot.send_message(message.chat.id, a)
    if a == 1 or a == 0:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        organizer = types.KeyboardButton('Я организатор')
        uchenik = types.KeyboardButton('Я ученик')
        zachem = types.KeyboardButton('Зачем нужен бот?')
        markup.add(organizer, uchenik, zachem)
        msg = bot.send_message(message.chat.id, 'Здравствуйте, это бот WASP Academy, выберите категорию запроса',
                               reply_markup=markup)
        cursor.close()
        bot.register_next_step_handler(msg, user_answer)
    else:
        bot.send_message(message.chat.id, 'У вас больше одного аккаунта')
        sys.exit(0)


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


def step1(message):
    if (message.text == 'Назад'):
        start(message)
    else:
        bot.send_message(message.chat.id, 'Вы нажали нечто не то')
        start(message)


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


def gorod(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    msg = bot.send_message(message.chat.id,
                           'В каком городе ты живёшь? \nНапример: Москва \n(Обрати внимание, что курс проходит очно в Москве)')
    bot.register_next_step_handler(msg, proverka_goroda)


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
        bot.send_message(message.chat.id, 'Поехали!')
        menu_testa(message)
    elif message.text == 'Назад':
        vvedite_pochtu(message)
    else:
        msg = bot.send_message(message.chat.id, "Выбери команду из меню")
        Vvedenie_K_Testu(msg)

def menu_testa(message):
    zadanie1 = select_random_test_task(1)
    zadanie2 = select_random_test_task(2)
    zadanie3 = select_random_test_task(3)
    zadanie4 = select_random_test_task(4)
    zadanie5 = select_random_test_task(5)
    answer1 = select_answer(zadanie1)
    answer2 = select_answer(zadanie2)
    otvet3 = select_answer(zadanie3)
    answer4 = select_answer(zadanie4)
    answer5 = select_answer(zadanie5)
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""INSERT INTO tasks
        (task_id_1, task_id_2, task_id_3, task_id_4, task_id_5, answer_1, answer_2, answer_3, answer_4, answer_5)
        VALUES({zadanie1}, {zadanie2}, {zadanie3}, {zadanie4}, {zadanie5}, {answer1}, {answer2}, {answer4}, {answer4}, {answer5});""")
    sqlite_connection.commit()
    cursor.close()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    zadanie_1 = types.KeyboardButton('Задание 1')
    zadanie_2 = types.KeyboardButton('Задание 2')
    zadanie_3 = types.KeyboardButton('Задание 3')
    zadanie_4 = types.KeyboardButton('Задание 4')
    zadanie_5 = types.KeyboardButton('Задание 5')
    markup.add(zadanie_1, zadanie_2, zadanie_3, zadanie_4, zadanie_5)
    msg = bot.send_message(message.chat.id, 'Тест состоит из 5 заданий, выбери задание и решай его. Если не знаешь, как решить задание, можешь перейти к другому', reply_markup=markup)
    bot.register_next_step_handler(msg, raspredelenie)


def raspredelenie(message):
    if(message.text == 'Задание 1'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        zadanie = select_sozdanniy_varik1(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        bot.send_message(message.chat.id, instruction)
    elif(message.text == 'Задание 2'):
        zadanie = select_sozdanniy_varik2(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        bot.send_message(message.chat.id, instruction)
    elif (message.text == 'Задание 3'):
        zadanie = select_sozdanniy_varik3(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        bot.send_message(message.chat.id, instruction)
    elif (message.text == 'Задание 4'):
        zadanie = select_sozdanniy_varik4(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        bot.send_message(message.chat.id, instruction)
    elif (message.text == 'Задание 5'):
        zadanie = select_sozdanniy_varik5(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        bot.send_message(message.chat.id, instruction)


@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Напишите /start, чтобы использовать бота')


def step_back(message):
    start(message)


@bot.message_handler(func=lambda message: message.text == 'Назад', content_types=['text'])
def step2_back_handler(message):
    start(message)



bot.polling(none_stop=True)