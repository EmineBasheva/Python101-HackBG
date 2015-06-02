class Panda:
    def __init__(self, name, email, gender):
        self.__name = str(name)
        if not self.is_valid_email(email):
            raise Exception("Not valid email")
        self.__email = str(email)
        self.__gender = str(gender)

    def name(self):
        return self.__name

    def is_valid_email(self, email):
        return '@' in email and '.' in email and email.index('@') < email.index('.') and ' ' not in email

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender.lower()

    def isMale(self):
        return self.__gender == 'male'

    def isFemale(self):
        return self.__gender == 'female'

    def __str__(self):
        return self.__name
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__name == other.name() and self.__email == other.email() and self.__gender == other.gender()

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()