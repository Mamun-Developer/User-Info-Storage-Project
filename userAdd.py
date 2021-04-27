from user import User

class UserAdd(User):
    def __init__(self):
        super().__init__("","",0,"")
    
    def set_name(self,name):
        self._name = name
    
    def set_age(self,age):
        self._age = age
    
    def set_gender(self,gender):
        self._gender = gender
    
    def set_phone(self,phone):
        self._phone = phone
    