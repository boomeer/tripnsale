def GetSysMsg(name):
    return {
        "wrong_login_or_password": "Неправильный логин или пароль",
        "user_is_not_activated": "Ваш аккаунт не активирован. Перейдите по ссылке активации, высланной Вам на почту",
    }.get(name, "")
