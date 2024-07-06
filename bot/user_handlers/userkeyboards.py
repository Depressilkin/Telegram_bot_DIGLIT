from telebot import types,telebot

markup_admin = telebot.types.ReplyKeyboardMarkup()
btn1 = telebot.types.KeyboardButton('Добавить преподавателя')
#btn2 = telebot.types.KeyboardButton('Удалить преподавателя')
btn2 = telebot.types.KeyboardButton('Добавить ученика')
#btn4 = telebot.types.KeyboardButton('Удалить ученика')
btn3 = telebot.types.KeyboardButton('Список преподавателей')
btn4 = telebot.types.KeyboardButton('Список учеников')
btn5 = telebot.types.KeyboardButton('Добавить занятие')
btn6 = telebot.types.KeyboardButton('Расписание')
markup_admin.row(btn1, btn2)
markup_admin.row(btn3, btn4)
markup_admin.row(btn5,btn6)

