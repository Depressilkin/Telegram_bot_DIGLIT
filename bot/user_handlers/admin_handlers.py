import telebot
from bot.user_handlers.userkeyboards import markup_admin
from bot.config_data import admin
bot = telebot.TeleBot('7062078052:AAHWw9Am8GMAuThzrCOVM_ObDP9T7NJ2AEo')

role = None
theme = ''
last_name = ''
first_name = ''
token = None

@bot.message_handler(commands=['admin'])
def start_admin(message):
    bot.send_message(message.chat.id,'Админ, я готов!', reply_markup=markup_admin)
    if str(message.chat.id) == admin.token:
        bot.register_next_step_handler(message, admin_menu)
def admin_menu(message):
    global role
    if message.text == 'Добавить преподавателя':
        bot.send_message(message.chat.id,f'Добавление преподавателя!')
        role = 't'
        get_first_name(message)
    #elif message.text == 'Удалить преподавателя':
    #    delete_tutor(message)
    elif message.text == 'Добавить ученика':
        bot.send_message(message.chat.id,f'Добавление ученика!')
        role = 's'
        get_first_name(message)
    #elif message.text == 'Удалить ученика':
    #    delete_student(message)
    elif message.text == 'Список преподавателей':
        desplay_tutors(message)
    elif message.text == 'Список учеников':
        desplay_students(message)
    elif message.text == 'Добавить занятие':
        add_slot(message)
    elif message.text == 'Расписание':
        desplay_slots(message)


#ввод данных нового пользователя
def get_first_name(message):
    bot.send_message(message.chat.id,f'Начнем!\nВведи имя')
    bot.register_next_step_handler(message, get_last_name)
def get_last_name(message):
    global first_name
    first_name = message.text
    bot.send_message(message.chat.id,f'Продолжим!\nВведи фамилию')
    bot.register_next_step_handler(message, get_theme)
def get_theme(message):
    global last_name
    last_name = message.text
    bot.send_message(message.chat.id,f'Осталось немного!\nВведи дисциплину')
    bot.register_next_step_handler(message, get_token)
def get_token(message):
    global theme, role
    theme = message.text
    bot.send_message(message.chat.id,f'И последнее!\nВведи токен')
    if role == 't':
        bot.register_next_step_handler(message, add_tutor)
    else:
        bot.register_next_step_handler(message, add_student)
#добавление преподавателя
def add_tutor(message):
    global first_name, last_name, theme, token
    token = int(message.text)
    bot.send_message(message.chat.id,'Готово! Теперь можно установить слот для занятий')
    #logging.info(f'Добавлен преподаватель {first_name} {last_name}')
    tutor = admin.creat_tutor(first_name, last_name, theme, token)
    admin.tutors.append(tutor)
    bot.send_message(admin.token, f'Добавлен преподаватель {tutor.first_name} {tutor.last_name}')
    start_admin(message)
#удаление преподавателя
@bot.message_handler(commands=['deletetutors'])
def delete_tutor(message):
    desplay_tutors(message)
    bot.send_message(admin.token, f'Введите ID перподавателя для удаления')
    bot.register_next_step_handler(message, delete_tutor_complite)
def delete_tutor_complite(message):
    admin.del_tutor(f'{message.text}')
    bot.send_message(admin.token, f'Преподаватель удален!\n')
    desplay_tutors(message)
#добавление ученика
def add_student(message):
    global first_name, last_name, theme, token
    token = int(message.text)
    bot.send_message(message.chat.id,'Готово! Теперь можно установить слот для занятий')
    #logging.info(f'Добавлен преподаватель {first_name} {last_name}')
    student = admin.creat_student(first_name, last_name, theme, token)
    admin.students.append(student)
    bot.send_message(admin.token, f'Добавлен ученик {student.first_name} {student.last_name}')
    start_admin(message)
#удаление преподавателя
@bot.message_handler(commands=['deletetutor'])
def delete_student(message):
    desplay_students(message)
    bot.send_message(admin.token, f'Введите ID перподавателя для удаления')
    bot.register_next_step_handler(message, delete_student_complite)
#удаление ученика
@bot.message_handler(commands=['deletestudent'])
def delete_student_complite(message):
    admin.del_student(f'{message.text}')
    bot.send_message(admin.token, f'Преподаватель удален!\n')
    desplay_students(message)

#вывод списка преподавателей
def desplay_tutors(message):
    desplay = ''
    for tutor in admin.tutors:
        desplay += f'{tutor.first_name} {tutor.last_name} {tutor.id_tutor}\n'
    bot.send_message(message.chat.id, f'Список преподавателей:\n{desplay}')
    start_admin(message)

#вывод списка учеников
def desplay_students(message):
    desplay = ''
    for student in admin.students:
        desplay += f'{student.first_name} {student.last_name} {student.id_student}\n'
    bot.send_message(message.chat.id, f'Список учеников:\n{desplay}')
    start_admin(message)

#добавление занятия
def add_slot(message):
    bot.send_message(message.chat.id, f'Добавим занятие! Введи через пробел:\n ID-ученика, ID-учителя, количество академчасов,\n день недели (понедельник - 0, воскресение - 6), время (чч:мм)')
    bot.register_next_step_handler(message, data_slot)
def data_slot(message):
    data = message.text.split(' ')
    for student in admin.students:
        if student.id_student == data[0]:
            std = student
    for tutor in admin.tutors:
        if tutor.id_tutor == data[1]:
            ttr = tutor
    slot = admin.add_slot(std, ttr, data[2], data[3], data[4])
    admin.slots.append(slot)
    bot.send_message(message.chat.id, f'Ура! Занятие добавлено! Теперь его можно увидеть в расписании, а я за сутки предупрежу о нем.')
    start_admin(message)

#вывод расписания
def desplay_slots(message):
    desplay = ''
    for slot in admin.slots:
        desplay += f'День недели: {slot.day}, время: {slot.time}, ученик: {slot.student.last_name}, учитель: {slot.tutor.last_name}\n'
    bot.send_message(message.chat.id, f'Список учеников:\n{desplay}')
    start_admin(message)


bot.polling()


