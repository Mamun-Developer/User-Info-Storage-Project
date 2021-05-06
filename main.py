from console_interface import Console
from dabase_handler import DatabaseHandler
prety_char = "="
padding_len=20
console = Console()
console.print_home_data(title = "COMMAND LIST",prety_char=prety_char,padding_len = padding_len)
while True:
    command = input("Enter command: ")
    console.get_home_commands
    allowed_commands = list(console.home_command_options.keys())
    print(allowed_commands)
    if command in allowed_commands:
        print("Inside")
        # proceed next
        if console.home_command_options[command]=="Add":
            # Write code for adding user
            user_info = console.add_users()
            db = DatabaseHandler("ourDB.db")
            db.add_users(user_info)
            # Push to database if same user doesnt exit
            
        elif console.home_command_options[command]=="Update":
            # Write code for updating user
            # RealPhone is primary of table
            update_values = console.update_user()
            # Update into database

        elif console.home_command_options[command]=="Delete":
            # Write code for deleting user
            pass
        elif console.home_command_options[command]=="Search":
            # Write code for searching user
            
            
        elif console.home_command_options[command]=="Exit":
            # Write cod for exiting from home
            print("Console exit successful")
            break  # user exit successfull

    else:
        print("Wrong command, Try again")
        continue


