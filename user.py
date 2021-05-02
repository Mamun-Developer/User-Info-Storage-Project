class User:
    def __init__(self, phone, name, age, gender):
        self._phone = phone
        self._name = name
        self._age = age
        self._gender = gender
    
    def get_phone(self):
        return self._phone

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def is_gender_correct(self, gender):
        # i.e input = Male,MALE,male
        allowed_genders = ["female", "male", "others"]
        if gender.lower() in allowed_genders:
            return True
        else:
            return False

    def is_age_correct(self, age=1):
        age = int(age)
        allowed_range = (13, 91)
        if type(age) == int:
            if age in range(allowed_range[0], allowed_range[1]):
                return True
            else:
                return False
        else:
            return False

    def is_name_correct(self, name):
        allowed_chars = ("a", "z", " ")     # ASCII 97 to 122
        temp_name = name.lower()
        array_of_allowed_ascii = [i for i in range(
            ord(allowed_chars[0]), ord(allowed_chars[1])+1)]
        array_of_allowed_ascii.append(ord(allowed_chars[2]))
        # for i in range(ord(allowed_chars[0]),ord(allowed_chars[1])+1):
        #   array_of_allowed_ascii.append(i)

        is_allowed = True
        for char in temp_name:
            if ord(char) not in array_of_allowed_ascii:
                is_allowed = False
                break
        return is_allowed

    def is_phone_correct(self, phone):
        if phone[0] == "+":
            phone = phone[1:len(phone)]
        is_valid = True

        allowed_digits_range = ['0', '9']
        # List comprehesion
        allowed_digits_list = [str(dig) for dig in range(
            int(allowed_digits_range[0]), int(allowed_digits_range[1])+1)]

        for char in phone:
            if char not in allowed_digits_list:
                is_valid = False
                return is_valid

        valid_country_codes = {
            "880": 13,
            "91": 12
        }

        is_valid = False
        c_code_found = False
        list_of_country_code = [*valid_country_codes]
        for c_code in list_of_country_code:
            if phone.startswith(c_code):
                c_code_found = True
                if len(phone) == valid_country_codes[c_code]:
                    is_valid = True
                    break
                else:
                    is_valid = False  # just for reference
                    break

        return is_valid

    #Phone,Validators
    USER_INFO_LIST = {
        "Phone": is_phone_correct,
        "Name":is_name_correct,
        "Age":is_age_correct,
        "Gender":is_gender_correct
    }
