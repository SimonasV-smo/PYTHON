
# 0task

# import datetime
#
# print(datetime)
#
# dt_res = datetime.today()
# print(dt_res)

# 1task

# dt_res = datetime.datetime.today()
# print(dt_res)
# print(dt_res.year)
# print(dt_res.month)
# print(dt_res.day)
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
#
# print(f'Dabar yra {dt_res.hour}:{dt_res.minute},'
#       f' {dt_res.day}-{dt_res.month}-{dt_res.year} ')

# # 2task
#
# print('-' * 50)
#
# dt_object = datetime.datetime(year=1995, month=7, day=14, hour=15, minute=30, second=00)
# print(dt_object)
#
# print('-' * 50)
#
# dt_object1 = datetime.date(year=2023, month=1, day=1)
# print(dt_object1)
#
# print('-' * 50)
#
# # 3task
#
# siandien = datetime.datetime.today()
# tukstantmetis = datetime.datetime(2000, 1, 1)
#
# skirtumas = siandien - tukstantmetis
# print(f'Nuo {tukstantmetis.date()} praejo: {skirtumas.days} dienu. ')
#
# print('-' * 50)

# # 5task
#
import datetime


user_input = input('Iveskite data formatu "YYYY-MM-DD": ')

date_time= datetime.datetime.strptime(user_input, '%Y-%m-%d')

print(date_time)

# 6task

import locale

locale.setlocale(locale.LC_TIME, 'lt_LT.utf8')

ivestis = '2022-12-31, 23:59:59'
date_time = datetime.datetime.strptime(ivestis, '%Y-%m-%d, %H:%M:%S')

formated_date_time_1 = date_time.strftime('%d/%m/%Y, %H:%M:%S')
print(formated_date_time_1)

formated_date_time_2 = date_time.strftime('%Y metu %B, %d diena')
print(formated_date_time_2)