from user import User
if __name__ == "__main__":
    user = User("01735774127","Abdllah Al Mamun",1,"Male")
    user._name = "Hridoy"
    # print(user.get_name())
    # print(user.is_gender_correct("MALE"))
    print(user.is_age_correct(14))
    print(user.is_name_correct("Abdullah Al Mamun"))
    print("Phone",user.is_phone_correct("+8801735774127"))