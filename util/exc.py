class TsExc(Exception):
    def __init__(self, msg=""):
        super().__init__(msg)

class RedirectExc(TsExc):
    pass
        
class ReqMustBePostErr(TsExc):
    def __init__(self):
        super().__init__("req_must_be_post")
