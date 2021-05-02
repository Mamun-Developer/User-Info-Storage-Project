#What you want to update? (seperate them with comma, if all then *)
def option_validator(option,updatables,separator = ","):
    confirmed_updates = []
    if option == "*":
        return updatables,False # False means option is validated and can proceed futher
    else:
        sep_options = option.split(separator)
        for op in sep_options:
            if op.strip() in updatables:
                confirmed_updates.append(op.strip())
            else:
                print("Wrong updatable selected")
                return None,True # True means try again - wrong updatable option selected
        
        return confirmed_updates,False