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
                                                points_1 INTEGER,
                                                points_2 INTEGER,
                                                points_3 INTEGER,
                                                points_4 INTEGER,
                                                points_5 INTEGER,
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
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            date_interview TEXT ,
                                            time_interview TEXT,
                                            student_info_id INTEGER UNIQUE
                                            );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS calendar_ochniy_etap(
                                                date_interview TEXT,
                                                time_interview TEXT,
                                                student_info_id INTEGER);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS task_info(
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    taskitself TEXT,
                                                    type_id INTEGER,
                                                    answer INTEGER);''')

    sqlite_connection.commit()
    cursor.close()

def selectstudent(studentid):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT * FROM student_info
                WHERE id = {studentid};""")
    row = cursor.fetchall()
    A = [elt[0] for elt in row]
    sqlite_connection.commit()
    cursor.close()
    return A[0]
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
    # bot.send_photo(message.chat.id, get("https://i0.wampi.ru/2019/11/12/image.png").content)
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
    if (a == 0):
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
    if (task_type == 1):
        random_task = randint(1, 4)
    elif (task_type == 2):
        random_task = randint(5, 8)
    elif (task_type == 3):
        random_task = randint(9, 12)
    elif (task_type == 4):
        random_task = randint(13, 16)
    elif (task_type == 5):
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


def select_answer_by_id(answer, user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("""SELECT """ + answer + f""" FROM tasks
                WHERE user_id = {user_id};""")
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


def insert_points(points_tasknumber, value, user_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    sqlite_update_query = f"""UPDATE tasks
     SET {points_tasknumber} = {value}
     WHERE user_id = {user_id}"""
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_update_query)
    sqlite_connection.commit()
    cursor.close()


def select_points(user_id, points_column):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""SELECT """ + points_column + f""" FROM tasks
                            WHERE user_id = {user_id};""")
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
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    organizer = types.KeyboardButton('Я организатор')
    uchenik = types.KeyboardButton('Я ученик')
    zachem = types.KeyboardButton('Зачем нужен бот?')
    markup.add(organizer, uchenik, zachem)
    msg = bot.send_message(message.chat.id, 'Здравствуйте, это бот WASP Academy, выберите категорию запроса',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if message.text == 'Я организатор':
        msg = bot.send_message(message.chat.id,
                               'Введите ваш пароль')
        bot.register_next_step_handler(msg, ImOrganiser)

    elif message.text == 'Я ученик':
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """INSERT INTO student_info
               (id_v_chate)
               VALUES(\'""" + str(message.chat.id) + """\')"""
        cursor.execute(sqlite_insert_query)
        cursor = sqlite_connection.cursor()
        sqlite_connection.commit()
        sqlite_select_query = """SELECT COUNT(*) as num FROM
               student_info WHERE id_v_chate LIKE \'""" + str(message.chat.id) + """\'"""
        cursor.execute(sqlite_select_query)
        a = cursor.fetchone()[0]
        #bot.send_message(message.chat.id, a)
        if (a == 1 or a == 0):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('Назад')
            ready = types.KeyboardButton('Готов(a) регистрироваться!')
            markup.add(ready, back)
            msg = bot.send_message(message.chat.id,
                                   'Поступление на наши курсы состоит из 4-ёх этапов: \n\n1) Заполнение анкеты\n2) Тест в онлайн-формате\n3) Тест в очном формате\n4) Интервью',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, ImStudent1)
        else:
            bot.send_message(message.chat.id, 'У вас больше одного аккаунта')
            sys.exit(0)
        cursor = sqlite_connection.cursor()
        cursor.close()
    elif message.text == 'Зачем нужен бот?':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        msge = bot.send_message(message.chat.id, 'Бот нужен для помощи в регистрации на курсы WASP Academy',
                                reply_markup=markup)
        bot.register_next_step_handler(msge, step1)


def ImOrganiser(message):
    if message.text == '123':
        bot.send_message(message.chat.id, 'Добро пожаловать, Anthony')
        OrganizerMenu1(message)
    else:
        bot.send_message(message.chat.id, 'Неверный пароль')
        start(message)


def vnesti_date(value_date):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("""INSERT INTO calendar_interview(date_interview)
                VALUES(\'""" + str(value_date) + """\')""")
    sqlite_connection.commit()
    cursor.close()


def vnesti_time(value_time,id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    a = """UPDATE calendar_interview SET time_interview = \'""" + str(value_time) + """\'
    WHERE id = \'""" + str(id) + """\'"""
    cursor.execute(a)
    sqlite_connection.commit()
    cursor.close()


def CountDates():
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT COUNT(*) as num FROM calendar_interview """
    cursor.execute(sqlite_select_query)
    a = cursor.fetchone()[0]
    sqlite_connection.commit()
    cursor.close()
    print (a)
    return a

def OrganizerMenu1(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    tasks_quota = types.KeyboardButton('Выбрать квоту зачисленных')
    calendar_changes = types.KeyboardButton('Внести временные слоты в календарь')
    info_about_student = types.KeyboardButton('Узнать информацию об ученике')
    results = types.KeyboardButton('Внести результаты по очному этапу')
    other_buttons = types.KeyboardButton('Другие запросы (2 часть)')
    markup.add(tasks_quota, calendar_changes, info_about_student,results, other_buttons)
    msg = bot.send_message(message.chat.id, 'Выберите категорию запроса', reply_markup=markup)
    bot.register_next_step_handler(msg, OrganizerIf)


def OrganizerMenu2(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    status = types.KeyboardButton('Выбрать статус кандидата')
    etap_dates = types.KeyboardButton('Изменить даты этапов')
    group_message = types.KeyboardButton('Оповестить всех')
    next_etap = types.KeyboardButton('Отправить приглашение на следующий этап')
    other_buttons = types.KeyboardButton('Другие запросы (1 часть)')
    markup.add(status, etap_dates, group_message, next_etap, other_buttons)
    msg = bot.send_message(message.chat.id, 'Выберите категорию запроса',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, OrganizerIf)


def OrganizerIf(message):
    if (message.text == 'Другие запросы (2 часть)'):
        OrganizerMenu2(message)
    elif (message.text == 'Другие запросы (1 часть)'):
        OrganizerMenu1(message)
    elif (message.text == 'Внести временные слоты в календарь'):
        sloty_if(message)
    elif (message.text == 'Выбрать статус кандидата'):
        msg = bot.send_message(message.chat.id, "Введите ID ученика")
        bot.register_next_step_handler(msg, Status)
    elif (message.text == 'Узнать информацию об ученике'):
        msg = bot.send_message(message.chat.id, "Введите ID ученика")
        bot.register_next_step_handler(msg, SelectStudentInfo)
    elif (message.text == 'Внести результаты по очному этапу'):
        msg = bot.send_message(message.chat.id, "Введите ID ученика")
        bot.register_next_step_handler(msg, OchniyEtapRes)


def OchniyEtapRes(message):
    global res
    res = message.text
    msg = bot.send_message(message.chat.id, "Введите результат кандидата за очное тестирование")
    bot.register_next_step_handler(msg, OchniyEtapResIf)

def OchniyEtapResIf(message):
    update_student(message.text, "second_stage_result", res)
    bot.send_message(message.chat.id, "Результат сохранён")
    OrganizerMenu1(message)

def SelectStudentInfo(message):
    studentid = message.text
    selectstudent(message, studentid)


def Status(message):
    global a
    a = message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    cool = types.KeyboardButton('Зачислен')
    notcool = types.KeyboardButton('Не зачислен')
    inprocess = types.KeyboardButton('В ожидании')
    markup.add(cool, notcool, inprocess)
    msg = bot.send_message(message.chat.id,"Выберите статус кандидата",reply_markup=markup)
    bot.register_next_step_handler(msg, StatusIf)


def StatusIf(message):
    update_student(message.text, "status", a)
    OrganizerMenu1(message)


def sloty_if(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    data_answer = types.KeyboardButton('Добавить дату и время')
    data2_answer = types.KeyboardButton('Удалить последнюю запись')
    data3_answer = types.KeyboardButton('Удалить день')
    data4_answer = types.KeyboardButton('Назад')
    markup.add(data_answer,data2_answer,data3_answer,data4_answer)
    msg = bot.send_message(message.chat.id,"Выберите категорию запроса",reply_markup=markup)
    bot.register_next_step_handler(msg,vnesti_sloty_if)


def vnesti_sloty_if(message):
    if message.text == 'Добавить дату и время':
       msg = bot.send_message(message.chat.id, "Введите день, который хотите добавить")
       bot.register_next_step_handler(msg,vnesti_sloty_date)
    elif message.text == 'Удалить последнюю запись':
        delete_last_note(message)
    elif message.text == 'Удалить день':
        msg = bot.send_message(message.chat.id, "Введите день, который хотите удалить")
        bot.register_next_step_handler(msg, delete_full_day)
    elif message.text == 'Назад':
        OrganizerMenu1(message)


def delete_sloty_date(date_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"""UPDATE calendar_interview
    SET date_interview = "null", time_interview = "null"
    WHERE id = {date_id}"""
    cursor.execute(sqlite_select_query)
    sqlite_connection.commit()
    cursor.close()


def delete_sloty_date_full(date_id):
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"""UPDATE calendar_interview
    SET date_interview = "null", time_interview = "null"
    WHERE date_interview = {date_id}"""
    cursor.execute(sqlite_select_query)
    sqlite_connection.commit()
    cursor.close()

def delete_last_note(message):
    day = CountDates()
    delete_sloty_date(day)
    bot.send_message(message.chat.id, "Запись удалена!")
    OrganizerMenu1(message)


def delete_full_day(message):
    day = message.text
    delete_sloty_date_full(day)
    bot.send_message(message.chat.id, "День удалён!")
    OrganizerMenu1(message)

def vnesti_sloty_date(message):
    vnesti_date(message.text)
    msg = bot.send_message(message.chat.id, "Теперь введите время")
    bot.register_next_step_handler(msg, vnesti_sloty_time)
def vnesti_sloty_time(message):
    day = CountDates()
    value_time = message.text
    vnesti_time(value_time,day)
    bot.send_message(message.chat.id, "Время успешно добавлено!")
    OrganizerMenu1(message)


def ImStudent1(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Готов(a) регистрироваться!'):
        msg = bot.send_message(message.chat.id,
                               'Вы были перенесены на этап регистрации. Введите имя (Пример: Антон)')
        bot.register_next_step_handler(msg, ImStudent2)
    else:
        user_answer(message)


def ImStudent2(message):
    remove = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id,
                           'Введите фамилию (Пример: Кисляков)')
    update_student(message.text, "name", message.chat.id)

    bot.register_next_step_handler(msg, ImStudent3)


def ImStudent3(message):
    remove = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id,
                           'Введите отчество (Пример: Юрьевич)')
    update_student(message.text, "surname", message.chat.id)

    bot.register_next_step_handler(msg, step22)


def step1(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        start(message)
    else:
        bot.send_message(message.chat.id, 'Вы нажали нечто не то')
        start(message)


def step2(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    msg = bot.send_message(message.chat.id,
                           'В каком городе ты живёшь? \nНапример: Москва \n(Обрати внимание, что курс проходит очно в Москве)')
    bot.register_next_step_handler(msg, proverka_goroda)


def proverka_proverki_goroda(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'Введите номер телефона \n(Например "88005553535")')
    bot.register_next_step_handler(msg, proverka_phone)


def proverka_phone(message):
    remove = types.ReplyKeyboardRemove()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, f"Ваш номер телефона: {message.text}, вы уверены?", reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_proverki_phone)
    update_student(message.text, "phone_number", message.chat.id)


def proverka_proverki_phone(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'Введите почту \n(Например "kislyakovanton@lit1533.com")')
    bot.register_next_step_handler(msg, proverka_pochtu)


def proverka_pochtu(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id,
                           'Введите название вашего учебного заведения \n(Например "ГБОУ Школа №1488" или НИУ ВШЭ)')
    bot.register_next_step_handler(msg, proverka_school)


def proverka_school(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    no = types.KeyboardButton('Нет')
    yes = types.KeyboardButton('Да')
    back = types.KeyboardButton('Назад')
    markup.add(yes, no, back)
    msg = bot.send_message(message.chat.id, 'Теперь тебе нужно пройти тест, который будет длиться 1 час\nТы готов?',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, proverka_gotovnosti_k_testu)


def proverka_gotovnosti_k_testu(message):
    remove = types.ReplyKeyboardRemove()
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
    remove = types.ReplyKeyboardRemove()
    zadanie1 = select_random_test_task(1)
    zadanie2 = select_random_test_task(2)
    zadanie3 = select_random_test_task(3)
    zadanie4 = select_random_test_task(4)
    zadanie5 = select_random_test_task(5)
    answer1 = select_answer(zadanie1)
    answer2 = select_answer(zadanie2)
    answer4 = select_answer(zadanie4)
    answer5 = select_answer(zadanie5)
    sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""INSERT INTO tasks
        (task_id_1, task_id_2, task_id_3, task_id_4, task_id_5, answer_1, answer_2, answer_3, answer_4, answer_5)
        VALUES({zadanie1}, {zadanie2}, {zadanie3}, {zadanie4}, {zadanie5}, {answer1}, {answer2}, {answer4}, {answer4}, {answer5});""") #ДОДЕЛАТЬ НОРМАЛЬНЫЙ ОТВЕТ ДЛЯ НОМЕРА 3
    sqlite_connection.commit()
    cursor.close()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    zadanie_1 = types.KeyboardButton('Приступить к выполнению задания')
    markup.add(zadanie_1)
    msg = bot.send_message(message.chat.id,
                           'Тест состоит из 5 заданий, выбери задание и решай его. Если не знаешь, как решить задание, можешь перейти к другому',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, raspredelenie)


def raspredelenie(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Задание 1' or message.text == 'Приступить к выполнению задания'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        zadanie = select_sozdanniy_varik1(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        msg = bot.send_message(message.chat.id, instruction, reply_markup=markup)
        bot.register_next_step_handler(msg, zadanie1_acceptage)
    elif (message.text == 'Задание 2'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        zadanie = select_sozdanniy_varik2(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        msg = bot.send_message(message.chat.id, instruction, reply_markup=markup)
        bot.register_next_step_handler(msg, zadanie2_acceptage)
    elif (message.text == 'Задание 3'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        zadanie = select_sozdanniy_varik3(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        msg = bot.send_message(message.chat.id, instruction, reply_markup=markup)
        bot.register_next_step_handler(msg, zadanie3_acceptage)
    elif (message.text == 'Задание 4'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        zadanie = select_sozdanniy_varik4(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        msg = bot.send_message(message.chat.id, instruction, reply_markup=markup)
        bot.register_next_step_handler(msg, zadanie4_acceptage)
    elif (message.text == 'Задание 5'):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        zadanie = select_sozdanniy_varik5(select_user_id(message.chat.id))
        instruction = select_instruction_task(zadanie)
        msg = bot.send_message(message.chat.id, instruction, reply_markup=markup)
        bot.register_next_step_handler(msg, zadanie5_acceptage)
    elif (message.text == 'Я готов сдать (перед тем, как сдать, проверь, все ли задания ты решил)'):
        if (select_answer_by_id("user_answer_1", select_user_id(message.chat.id)) == select_answer_by_id("answer_1",
                                                                                                         select_user_id(
                                                                                                                 message.chat.id))):
            insert_points("points_1", 2, select_user_id(message.chat.id))
        else:
            insert_points("points_1", 0, select_user_id(message.chat.id))
        if (select_answer_by_id("user_answer_2", select_user_id(message.chat.id)) == select_answer_by_id("answer_2",
                                                                                                         select_user_id(
                                                                                                                 message.chat.id))):
            insert_points("points_2", 2, select_user_id(message.chat.id))
        else:
            insert_points("points_2", 0, select_user_id(message.chat.id))
        if (select_answer_by_id("user_answer_3", select_user_id(message.chat.id)) == select_answer_by_id("answer_3",
                                                                                                         select_user_id(
                                                                                                                 message.chat.id))):
            insert_points("points_3", 2, select_user_id(message.chat.id))
        else:
            insert_points("points_3", 0, select_user_id(message.chat.id))
        if (select_answer_by_id("user_answer_4", select_user_id(message.chat.id)) == select_answer_by_id("answer_4",
                                                                                                         select_user_id(
                                                                                                                 message.chat.id))):
            insert_points("points_4", 2, select_user_id(message.chat.id))
        else:
            insert_points("points_4", 0, select_user_id(message.chat.id))
        if (select_answer_by_id("user_answer_5", select_user_id(message.chat.id)) == select_answer_by_id("answer_5",
                                                                                                         select_user_id(
                                                                                                                 message.chat.id))):
            insert_points("points_5", 2, select_user_id(message.chat.id))
        else:
            insert_points("points_5", 0, select_user_id(message.chat.id))
        task1_result = select_points(select_user_id(message.chat.id), "points_1")
        task2_result = select_points(select_user_id(message.chat.id), "points_2")
        task3_result = select_points(select_user_id(message.chat.id), "points_3")
        task4_result = select_points(select_user_id(message.chat.id), "points_4")
        task5_result = select_points(select_user_id(message.chat.id), "points_5")
        itog = task1_result+task2_result+task3_result+task4_result+task5_result
        if(itog>=6):
            bot.send_message(message.chat.id,f"Ты набрал {itog} баллов из 10, поздравляем, ты зачислен")
        elif (itog == 5):
            bot.send_message(message.chat.id,f"Ты набрал {itog} баллов из 10, к сожалению, ты не зачислен")
        elif(itog == 0):
            bot.send_message(message.chat.id, f"Ты набрал {itog} баллов из 10, к сожалению, ты не зачислен")
        else:
            bot.send_message(message.chat.id, f"Ты набрал {itog} балла из 10, к сожалению, ты не зачислен")


def zadanie1_acceptage(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        menu_testa_after_zapolnenie(message)
    else:
        user_id = select_user_id(message.chat.id)
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        sqlite_update_query = """UPDATE tasks
            SET user_answer_1 = \'""" + str(message.text) + """\'
            WHERE user_id = \'""" + str(user_id) + """\'"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()
        cursor.close()
        menu_testa_after_zapolnenie(message)


def zadanie2_acceptage(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        menu_testa_after_zapolnenie(message)
    else:
        user_id = select_user_id(message.chat.id)
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        sqlite_update_query = """UPDATE tasks
            SET user_answer_2 = \'""" + str(message.text) + """\'
            WHERE user_id = \'""" + str(user_id) + """\'"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()
        cursor.close()
        menu_testa_after_zapolnenie(message)


def zadanie3_acceptage(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        menu_testa_after_zapolnenie(message)
    else:
        user_id = select_user_id(message.chat.id)
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        sqlite_update_query = """UPDATE tasks
            SET user_answer_3 = \'""" + str(message.text) + """\'
            WHERE user_id = \'""" + str(user_id) + """\'"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()
        cursor.close()
        menu_testa_after_zapolnenie(message)


def zadanie4_acceptage(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        menu_testa_after_zapolnenie(message)
    else:
        user_id = select_user_id(message.chat.id)
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        sqlite_update_query = """UPDATE tasks
            SET user_answer_4 = \'""" + str(message.text) + """\'
            WHERE user_id = \'""" + str(user_id) + """\'"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()
        cursor.close()
        menu_testa_after_zapolnenie(message)


def zadanie5_acceptage(message):
    remove = types.ReplyKeyboardRemove()
    if (message.text == 'Назад'):
        menu_testa_after_zapolnenie(message)
    else:
        user_id = select_user_id(message.chat.id)
        sqlite_connection = sqlite3.connect('kislyakovdatabase.db')
        sqlite_update_query = """UPDATE tasks
            SET user_answer_5 = \'""" + str(message.text) + """\'
            WHERE user_id = \'""" + str(user_id) + """\'"""
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()
        cursor.close()
        menu_testa_after_zapolnenie(message)


def menu_testa_after_zapolnenie(message):
    remove = types.ReplyKeyboardRemove()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    zadanie_1 = types.KeyboardButton('Задание 1')
    zadanie_2 = types.KeyboardButton('Задание 2')
    zadanie_3 = types.KeyboardButton('Задание 3')
    zadanie_4 = types.KeyboardButton('Задание 4')
    zadanie_5 = types.KeyboardButton('Задание 5')
    ya_gotov = types.KeyboardButton('Я готов сдать (перед тем, как сдать, проверь, все ли задания ты решил)')
    markup.add(zadanie_1, zadanie_2, zadanie_3, zadanie_4, zadanie_5, ya_gotov)
    msg = bot.send_message(message.chat.id, 'Ты в меню', reply_markup=markup)
    bot.register_next_step_handler(msg, raspredelenie)


@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Напишите /start, чтобы использовать бота')


def step_back(message):
    start(message)


@bot.message_handler(func=lambda message: message.text == 'Назад', content_types=['text'])
def step2_back_handler(message):
    start(message)


bot.polling(none_stop=True)