from datetime import datetime, timedelta

max_day_month_normal_y = {'1': 31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':
                        31, '9':30, '10':31, '11':30, '12':31}

max_day_month_leap_y = {'1': 31, '2':29, '3':31, '4':30, '5':31, '6':30, '7':31, '8':
                        31, '9':30, '10':31, '11':30, '12':31}

#Оказывается можно было легче решить
# def date_in_future(integer):
#     if type(integer) == int:
#         finally_date = timedelta(days=integer) + datetime.now()
#         return finally_date.strftime('%d-%m-%Y %H:%M:%S')
#     else:
#         return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
def date_in_future(integer):
    if type(integer) == int:
        year = int(datetime.now().strftime('%Y'))
        month = int(datetime.now().strftime('%m'))
        day = int(datetime.now().strftime('%d')) + integer
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #проверка на високосный год
            while day > max_day_month_leap_y[str(month)]:
                day -= max_day_month_leap_y[str(month)]
                month += 1
                if month == 13:
                    year += 1
                    month = 1
            if 1 <= month < 10 and 1 <= day < 10:
                return f"0{day}-0{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            elif 1 <= month < 10:
                return f"{day}-0{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            elif 1 <= day < 10:
                return f"0{day}-{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            else:
                return f"{day}-{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
        else:
            while day > max_day_month_normal_y[str(month)]:
                day -= max_day_month_normal_y[str(month)]
                month += 1
                if month == 13:
                    year += 1
                    month = 1
            if 1 <= month < 10 and 1 <= day < 10:
                return f"0{day}-0{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            elif 1 <= month < 10:
                return f"{day}-0{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            elif 1 <= day < 10:
                return f"0{day}-{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
            else:
                return f"{day}-{month}-{year} {datetime.now().strftime('%H:%M:%S')}"
    else:
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
