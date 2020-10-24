class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_data_numbers(cls, date):
        data_list = date.split('/')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        return cls(day, month, year)

    @staticmethod
    def validate_date(self):
        months_dict = {num + 1: month for num, month in enumerate(['January', 'February', 'March', 'April', 'May',
                                                                   'June', 'July', 'August', 'September', 'October',
                                                                   'November', 'December'])}
        days_in_month_1 = {day + 1: days_num for day, days_num in enumerate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31,
                                                                             30, 31])}
        days_in_month_2 = {day + 1: days_num for day, days_num in enumerate([31, 29, 31, 30, 31, 30, 31, 31, 30, 31,
                                                                             30, 31])}
        return "You've entered the wrong month. Max number of months is 12" if self.month not in range(1, 13) else \
            (f"You've entered the wrong day. Max days in {months_dict[self.month]} {self.year} is "
             f"{days_in_month_2[self.month] if self.year % 4 == 0 else days_in_month_1[self.month]}"
             if self.day > (days_in_month_2[self.month] if self.year % 4 == 0 else days_in_month_1[self.month])
             else "You've entered everything correct!")


date_0 = Date.get_data_numbers('29/02/2020')
print(date_0.day)
print(date_0.month)
print(date_0.year)
print(date_0.validate_date(date_0))

date_1 = Date.get_data_numbers('29/02/2019')
print(date_1.validate_date(date_1))

date_2 = Date.get_data_numbers('02/13/2020')
print(date_1.validate_date(date_2))

date_3 = Date.get_data_numbers('31/09/2020')
print(date_1.validate_date(date_3))
