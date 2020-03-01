import datetime

class Volleyball_player:
    def __init__(self, date=None, sex=True, name=None, height=None, weight=None, club=None, nation=None):
        self.date = date
        self.sex = sex
        self.name = name
        self.height = height
        self.weight = weight
        self.club = club
        self.nation = nation

        self.items = []

    def show(self):
        if self.sex:
            str_sex = "Male"
        else:
            str_sex = "Female"
        return "Name: " + str(self.name) + ', Date: ' + str(self.date) + ', Sex: ' + str_sex \
                + ', Height: ' + str(self.height) + ', Weight: ' + str(self.weight) + ', Club: ' + str(self.club) \
                + ', Nation: ' + str(self.nation) + ";"
    def add(self):
        self.name = input("Write Name: ")
        self.height = input("Write Height: ")
        self.weight = input("Write Weight: ")
        self.club = input("Write Club: ")
        self.nation = input("Write Nation: ")
        str_sex = input("Write Sex (M/F): ")
        if str_sex == 'F':
            self.sex = False
        else:
            self.sex = True
        year = int(input("Write Year: "))
        month = int(input("Write Month: "))
        day = int(input("Write Day: "))
        self.date = datetime.date(year, month, day)