#-*- coding: utf-8 -*-

def GetRegMsg(name):
    return {
        "wrong_login_or_password": "Неправильный логин или пароль",
        "user_is_not_activated": "Ваш аккаунт не активирован. Перейдите по ссылке активации, высланной Вам на почту",
        "username_is_invalid": "Логин может состоять из латинских букв, цифр, знаков ._-",
        "email_is_invalid": "Адрес может состоять из латинских букв, цифр, знаков ._- и @",
        "username_is_too_short": "Логин должен иметь хотя бы 3 символа",
        "username_is_too_long": "Логин должен быть короче 30 символов",
        "username_is_not_unique": "Логин занят",
        "email_is_not_unique": "Email занят",
        "password_is_invalid": "Неверный символ в пароле О_О. Как Вы этого добились!?",
        "bad_password_len": "Пароль должен иметь от 3 до 30 символов",
        "passwords_are_not_equal": "Пароли не совпадают",
        "offer_wasnt_be_agreed": "Вы должны согласиться с положением оферты",
        "required_fields_missed": "Заполнены не все обязательные поля"
    }.get(name, "")

def GetBuyEditMsg(name):
    return {
        "title_is_missing": "Название товара должно быть заполнено",
        "fromcountry_is_invalid": "Указана страна покупки, отсутствующая в базе данных",
        "tocountry_is_empty": "Поле со страной доставки обязательно для заполнения",
        "tocountry_field_is_invalid": "Указана страна доставки, отсутствующая в базе данных",
        "costfr_is_invalid": "Некорректное значение минимальной стоимости",
        "costto_is_missing": "Поле с максимальной стоимостью обязательно для заполнения",
        "costto_is_invalid": "Некорректное значение максимальной стоимости",
    }.get(name, "")

def GetBackmsgMsg(name):
    return {
        "message_is_empty": "Нельзя отправить пустое сообщение",
        "empty_answer_email": "Пустой email для ответа"
    }.get(name, "")

def GetSaleAddMsg(name):
    return {
        "fromdate_field_is_empty": "Поле с датой отправления обязательно для заполнения",
        "fromdate_field_is_invalid": "Поле с датой отправления должно быть в формате дд.мм.гггг",
        "fromcountry_field_is_empty": "Поле со страной отправления обязательно для заполнения",
        "fromcountry_field_is_invalid": "Указана страна отправления, отсутствующая в базе данных",
        "todate_field_is_empty": "Поле с датой прибытия обязательно для заполнения",
        "todate_field_is_invalid": "Поле с датой прибытия должно быть в формате дд.мм.гггг",
        "tocountry_field_is_empty": "Поле со страной прибытия обязательно для заполнения",
        "tocountry_field_is_invalid": "Указана страна прибытия, отсутствующая в базе данных",
        "invalid_deposit": "Некорректное значение депозита"
    }.get(name, "")

def GetEditProfileMsg(name):
    return {
        "firstname_is_missing": "Поле с именем должно быть заполнено",
        "lastname_is_missing": "Поле с фамилией должно быть заполнено",
        "country_is_invalid": "Указана страна, отсутствующая в базе данных",
        "bday_is_missing": "Поле с датой рождения должно быть заполнена",
        "bday_is_invalid": "Поле с датой рождения должно быть в формате дд.мм.гггг",
        "old_pass_is_invalid": "Неверный пароль",
        "passwords_are_not_equal": "Введённые пароли не совпадают",
        "bad_password_len": "Пароль должен иметь от 3 до 30 символов",
    }.get(name, "")

def GetGalleryExcMsg(name):
    return {
        "image_limit_exceeded": "Превышено кол-во изображений для галлереи",
        "image_big_size": "Размер файла не должен превышать 6МБ",
        "image_bad_format": "Неккоректный тип файла",
    }.get(name, "")
