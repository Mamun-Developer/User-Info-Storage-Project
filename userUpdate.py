from userAdd import UserAdd
class UserUpdate(UserAdd):
    
    def construct_user(self,phone):
        name = "Username"
        age = 12
        gender = "male"

        self.set_name(name)
        self.set_age(age)
        self.set_gender(gender)
    
    def update_name(self,name):
        self._name = name
    
    def update_gender(self,gender):
        self._gender = gender
    
    def update_age(self,age):
        self._age = age
    
    


update = UserUpdate()
update.construct_user("213131")
update.update_gender("male")
print(update.get_gender())
