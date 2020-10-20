import telebot # Подключаем библиотеку
import time  # Подключаем модуль времени

bot = telebot.TeleBot('1186613531:AAF-cnm0kgg2LYc48siWTR9p3cxI3N31-l4')

bad_words = ["жопа", "дурак", "мудак", "durak", "моргенштерн", "всем привет", "шлюха",]

other_lang = ["таблетки", "наркота",
              "палата", "деньги", "дота", "коронавирус"]

# Словарь для фраз на которыем мы будем реагировать стикером

other_bot = ["бухать", "пить", "курить", "травку", "травка", "пиво", "водка", "виски", "вино", "алкаш"]  # Еще один словарь для фраз на которыем мы будем реагировать стикером


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
        try:
            bot.reply_to(message, text='Приветствую тебя, присаживай поудобнее')
            sti=open(r'G:\python\RaznieProject\botdlyatg\mp4.mp4', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id, disable_notification=True)
        except OSError:
            print("SongError - Sending again after 3 seconds!!!")
            time.sleep(3)
            bot.reply_to(message, text='стул вон там!')  # Отвечаем на сообщение
            sti = open(r'G:\python\RaznieProject\botdlyatg\baxagif.mp4','rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id,
                               disable_notification=True)

@bot.message_handler(
    content_types=['left_chat_member'])  # Хендлер описывающий поведение бота при выходе пользователя из чата
def not_greeting(message):  # Запуско основной функции хендлера
    print("User " + message.left_chat_member.first_name + " left")  # Выводим в консоль имя ушедшего пользователя
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='жаль тебя.',
                     disable_notification=True)  # Выводим прощание в чат
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("LeftError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='я буду скучать.',
                     disable_notification=True)  # Выводим прощание в чат


@bot.message_handler(commands=['start'])  # Хендлер описывающий поведение бота при вводе /start
def starting(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  #в/start
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("StartingError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  #  /start


@bot.message_handler(commands=['command1'])  # Хендлер описывающий поведение бота при вводе command1
def bui(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bui_pic = open(r'G:\python\RaznieProject\botdlyatg\bui.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, bui_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("BuiError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bui_pic = open(r'G:\python\RaznieProject\botdlyatg\bui.webp', 'rb')  # О
        bot.send_sticker(message.chat.id, bui_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер


@bot.message_handler(commands=['command2'])  # Хендлер описывающий поведение бота при вводе command2
def zvezda(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        zv_pic = open(r'G:\python\RaznieProject\botdlyatg\zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, zv_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("ZvezdaError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        zv_pic = open(r'G:\python\RaznieProject\botdlyatg\zvezda.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, zv_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер


@bot.message_handler(commands=['command3'])  # Хендлер описывающий поведение бота при вводе command3
def jigurda(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jig_pic = open(r'G:\python\RaznieProject\botdlyatg\jig.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jig_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("JigurdaError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jig_pic = open(r'G:\python\RaznieProject\botdlyatg\jig.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jig_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер


@bot.message_handler(commands=['help'])  # Хендлер описывающий поведение бота при вводе help
def helper(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Чем тебе помочь ?', disable_notification=True) #/he
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("HelperError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Как я могу тебе помочь ?', disable_notification=True)


@bot.message_handler(content_types=['voice'])  # Хендлер описывающий поведение бота при голосовом сообщении в чате
def voice_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open(r'G:\python\RaznieProject\botdlyatg\voice.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open(r'G:\python\RaznieProject\botdlyatg\voice.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер


@bot.message_handler(
    content_types=['pinned_message'])  # Хендлер описывающий поведение бота после того, как было закрепленно сообщение
def pinned_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='И зачем ты закрепил это ?',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PinnedError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='И зачем ты закрепил это ?',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение


@bot.message_handler(content_types=['audio'])  # Хендлер описывающий поведение бота при добавлении аудиофайла в чат
def audio_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open(r'G:\python\RaznieProject\botdlyatg\002.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open(r'G:\python\RaznieProject\botdlyatg\002.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение


@bot.message_handler(content_types=['text'])  # Хендлер описывающий поведение бота на текст в чате
def txt(message):  # Запуско основной функции хендлера
    for i in range(0, len(bad_words)):  # Перебираем все элементы словаря по очереди
        if bad_words[i] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id, )  # Удаляем сообщение
                print(message.text + " delited")  # Выводим удаленное сообщение в консоль
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("BadWordsError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение
                print(message.text + " delited")  # Выводим удаленное сообщение в консоль

    for l in range(0, len(other_lang)):  # Перебираем все элементы словаря по очеред
        if other_lang[l] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                get_pic = open(r'G:\python\RaznieProject\botdlyatg\get_out.webp', 'rb')  # Открывем стикер и присваиваем его переменной
                bot.send_sticker(message.chat.id, get_pic, reply_to_message_id=message.message_id,
                                 disable_notification=True)  # Отправляем стикер
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("LangError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                get_pic = open(r'G:\python\RaznieProject\botdlyatg\get_out.webp', 'rb')  # Открывем стикер и присваиваем его переменной
                bot.send_sticker(message.chat.id, get_pic, reply_to_message_id=message.message_id,
                                 disable_notification=True)  # Отправляем стикер

    for f in range(0, len(other_bot)):  # Перебираем все элементы словаря по очеред
        if other_bot[f] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                pss_pic = open(r'G:\python\RaznieProject\botdlyatg\zbsgif.mp4', 'rb')  # Открывем видео и присваиваем его переменной
                bot.send_animation(message.chat.id, pss_pic, reply_to_message_id=message.message_id,
                                   disable_notification=True)  # Отправляем видео
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("AnimError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                pss_pic = open(r'G:\python\RaznieProject\botdlyatg\zbsgif.mp4', 'rb')  # Открывем видео и присваиваем его переменной
                bot.send_animation(message.chat.id, pss_pic, reply_to_message_id=message.message_id,
                                   disable_notification=True)  # Отправляем видео

    if message.text == 'Абушка':  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='чё надо от хозяина ?!')  # Отвечаем на сообщение
            sti = open(r'G:\python\RaznieProject\botdlyatg\bahagif.mp4', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем гифку
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("SongError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='Ща ебало начищу!')  # Отвечаем на сообщение
            sti = open(r'G:\python\RaznieProject\botdlyatg\bahagif.mp4', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем гифку

    if message.text == 'абушка':  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='занят он, позже ответит')  # Отвечаем на сообщение
            sti = open(r'G:\python\RaznieProject\botdlyatg\baxagif.mp4', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем гифку
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("SongError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='Я не понял ?!')  # Отвечаем на сообщение
            sti = open(r'G:\python\RaznieProject\botdlyatg\baxagif.mp4', 'rb')  # Открывем аудио и присваиваем его переменной
            bot.send_animation(message.chat.id, sti, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем гифку


    elif message.text == "Дима":  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            ver_pic = open(r'G:\python\RaznieProject\botdlyatg\hg.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
            bot.send_photo(message.chat.id, ver_pic, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем изображение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("VerError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            ver_pic = open(r'G:\python\RaznieProject\botdlyatg\hg.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
            bot.send_photo(message.chat.id, ver_pic, reply_to_message_id=message.message_id,
                           disable_notification=True)  # Отправляем изображение


    elif message.text == "Славик":  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='что тебя нужно от него ?', disable_notification=True)  # Отвечаем на сообщение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("Stop_wordError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='что тебя нужно от него ?', disable_notification=True)  # Отвечаем




    elif " бот " in message.text.lower():  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='Я хоть и бот, но всё вижу', disable_notification=True)  # Отвечаем на сообщение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("Stop_wordError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='У меня зоркий глаз', disable_notification=True)  # Отвечаем на сообщение

    elif " бот" in message.text.lower():  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='Не говори ничего про меня', disable_notification=True)  # Отвечаем на сообщение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("Stop_wordError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='Хватит меня упоминать', disable_notification=True)  # Отвечаем



    elif "бот " in message.text.lower():  # Ищем нашу фразу в тексте сообщения
        try:  # Пытаемся выполнить команду приведеную ниже
            bot.reply_to(message, text='я обижен', disable_notification=True)  # Отвечаем на сообщение
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("Stop_wordError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            bot.reply_to(message, text='всё, не разговариваю с тобой', disable_notification=True)  # Отвечаем



    else:  # Если ничего не подошло
        pass  # Идём дальше


if __name__ == '__main__':  # Блок запуска бота
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PollingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(5)  # Делаем паузу в 5 секунд и выполняем команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота