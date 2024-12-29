class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        if self.month <= 9:
            self.month = '0'+str(self.month)

        if self.day <= 9:
            self.day = '0'+str(self.day)

    def format(self):
        pass

    def iso_format(self):
        pass

class USADate(Date):

    def format(self):
        return f'{self.month}-{self.day}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month}-{self.day}'


class ItalianDate(Date):

    def format(self):
        return f'{self.day}/{self.month}/{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month}-{self.day}'

usa_date = USADate(2024, 12, 9)
italian_date = ItalianDate(2024, 12, 9)

print(usa_date.format())
print(usa_date.iso_format())

print(italian_date.format())
print(italian_date.iso_format())
