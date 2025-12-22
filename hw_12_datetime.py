import datetime as d


"""Задания 1, 2, 4, 6, 8"""


now = d.datetime.now()
my_birthday = d.datetime(1994, 4, 19)
ten_days_from_now = now + d.timedelta(days=10)

def weekends(date):
    print(f'Дата {date.strftime("%d-%m-%Y")} является '
          f'{"выходным" if date.weekday() >= 5 else "рабочим днем"}')

weekends(d.date(2025, 12, 27))
weekends(now)
weekends(ten_days_from_now)
weekends(my_birthday)

