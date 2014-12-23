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
    }.get(name, "")

def GetBuyEditMsg(name):
    return {
        "buy_edit_ok": "Изменения успешно сохранены",
    }.get(name, "")

def GetBackmsgMsg(name):
    return {
        "message_is_empty": "Нельзя отправить пустое сообщение",
        "empty_answer_email": "Пустой email для ответа"
    }.get(name, "")
