def GetSysMsg(name):
    return {
        "wrong_login_or_password": "Неправильный логин или пароль",
    }.get(name, "")
