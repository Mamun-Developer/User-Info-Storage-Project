
# Interface
#----------COMMAND LIST----------
# 1. Add
# 2. Update
# 3. Delete
# 4. Search
from user import User
from others import option_validator
class Console:
    def get_title(self,title,prety_char="-",padding_len=5):
        res = prety_char * padding_len
        return res+title+res

    def get_home_commands(self):
        options = {
            1:"Add",
            2:"Update",
            3:"Delete",
            4:"Search"
        }
        commands  = ""
        for key in options:
            commands = commands + str(key)+". "+options[key]+"\n"
        return commands
    
    def add_users(self):
        inputs = {}
        for key in User.USER_INFO_LIST:
            not_done = True
            while not_done:
                tempInput = input(key+": ")
                if User.USER_INFO_LIST[key](None,tempInput)==True:
                    inputs[key] = tempInput
                    not_done = False
                else:
                    print("Please provide a valid "+key)
        
        return inputs

    def update_user(self):
        UPDATE_RESTRICTED = []
        UPDATABLE_OPTIONS = list(User.USER_INFO_LIST.keys())
        for restricted in UPDATE_RESTRICTED:
            UPDATABLE_OPTIONS.remove(restricted)

        not_done = True
        user_phone = ""
        while not_done:
            user_phone = input("Phone: ")
            if User.USER_INFO_LIST["Phone"](None,user_phone) == True:
                not_done = False
            else:
                print("Please provide a valid Phone")

        # Collect "user_phone" infor from database
        not_done = True
        while not_done:
            print("Options: "+str(UPDATABLE_OPTIONS))
            option = input("What you want to update? (seperate them with comma, if all then *)\nOptions: ")
            req_update,not_done = option_validator(option,UPDATABLE_OPTIONS)
        print(req_update)

# title = Console().get_title(prety_char="*",padding_len=10,title="COMMAND LIST")
# print(title)
# Console().get_home_commands()
# Console().add_users()
Console().update_user()