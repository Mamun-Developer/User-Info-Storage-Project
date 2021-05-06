
# Interface
# ----------COMMAND LIST----------
# 1. Add
# 2. Update
# 3. Delete
# 4. Search
from user import User
from others import option_validator


class Console:
    def print_home_data(self, title, prety_char="-", padding_len=5):
        print(self.get_title(title, prety_char, padding_len))
        print(self.get_home_commands())

    def get_title(self, title, prety_char="-", padding_len=5):
        res = prety_char * padding_len
        return res+title+res

    home_command_options = {
            "1": "Add",
            "2": "Update",
            "3": "Delete",
            "4": "Search",
            "5": "Exit"
        }

    def get_home_commands(self):
        '''
            Returns a title string that will be printed on the console
        '''

        commands = ""
        for key in self.home_command_options:
            commands = commands + str(key)+". "+self.home_command_options[key]+"\n"
        return commands

    def add_users(self):
        '''
            Returns user data to be inserted in the database as a dictionary
            i.e output: 
            {'Phone': '8801735774127', 'Name': 'jfsd', 'Age': '22', 'Gender': 'male'}
        '''
        inputs = {}
        for key in User.USER_INFO_LIST:
            not_done = True
            while not_done:
                tempInput = input(key+": ")
                if User.USER_INFO_LIST[key](None, tempInput) == True:
                    inputs[key] = tempInput
                    not_done = False
                else:
                    print("Please provide a valid "+key)
        print(inputs)
        return inputs

    def update_user(self):
        '''
            1. Ask user to select columns that will be updated
            2. Show current data of updatable columns
            3. Input new values for updatable columns
            4. Return new values with keys
        '''
        UPDATE_RESTRICTED = []
        UPDATABLE_OPTIONS = list(User.USER_INFO_LIST.keys())
        for restricted in UPDATE_RESTRICTED:
            UPDATABLE_OPTIONS.remove(restricted)

        not_done = True
        user_phone = ""
        while not_done:
            user_phone = input("Phone: ")
            if User.USER_INFO_LIST["Phone"](None, user_phone) == True:
                not_done = False
            else:
                print("Please provide a valid Phone")

        # Collect "user_phone" info from database
        not_done = True
        while not_done:
            print("Options: "+str(UPDATABLE_OPTIONS))
            option = input(
                "What you want to update? (seperate them with comma, if all then *)\nOptions: ")
            req_update, not_done = option_validator(option, UPDATABLE_OPTIONS)
        print(req_update)

        # Show current values of updatable columns to the user
        # Write codes from here
        print("Current value of database will be printed here")

        # Ask user to input new value for the columns

        inputs = {}
        inputs["RealPhone"] = user_phone
        for key in req_update:
            not_done = True
            while not_done:
                tempInput = input(key+": ")
                if User.USER_INFO_LIST[key](None, tempInput) == True:
                    inputs[key] = tempInput
                    not_done = False
                else:
                    print("Please provide a valid "+key)
        print(inputs)
        return inputs

    def delete_user(self):
        '''
            Input phone number and validate it and returns the phone number for deletion
        '''
        user_phone = ""
        while True:
            user_phone = input("Phone: ")
            if User.USER_INFO_LIST["Phone"](None, user_phone) == True:
                break
            else:
                print("Enter valid phone number")
                continue

        return user_phone
    
    def search_user(self):
        '''
            Input phone number and validate it and returns the phone number for searching
        '''
        user_phone = ""
        while True:
            user_phone = input("Phone: ")
            if User.USER_INFO_LIST["Phone"](None, user_phone) == True:
                break
            else:
                print("Enter valid phone number")
                continue

        return user_phone
