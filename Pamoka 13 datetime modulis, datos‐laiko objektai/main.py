
# # datetime klasė ir datos-laiko skaičiavimai
#
# # import datetime
# from datetime import datetime
#
# # print(type(datetime))
#
# # kreipiamės į funkcionalumą aprašytą datetime faile
# # todėl kode 2 kartus kartojam datetime
# # antrasis datetime yra kreipimasis į klasę
# # .today() metodas sukuria šio laiko momento datos-laiko objektą
# # rezultatas yra datetime.datetime objektas
#
# print(datetime)
# print(datetime.today())
# dt_res = datetime.today()
# print(dt_res)


# import datetime
#
# print(f'START - {datetime.datetime.today()}')
# dt_res = datetime.datetime.today()
# print(dt_res)
# print(dt_res.year)
# print(dt_res.month)
# print(dt_res.day)
# for i in range(1, 1000000):
#     a = 123
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
# print(dt_res.microsecond)
# print(f'START - {datetime.datetime.today()}')

# import datetime

# my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
# today_dt = datetime.datetime.today()

# print(my_datetime)

# if my_datetime < today_dt:
#     print('YES')
#
# def is_save_still_valid(start_dt, end_dt) -> bool:
#     today_dt = datetime.datetime.today()
#     if start_dt < today_dt < end_dt:
#         return True
#     return False
#
# sale_start_dt = datetime.datetime(year=2025, month=2, day=2)
# sale_end_dt = datetime.datetime(year=2025, month=4, day=2)
#
# is_still_valid = is_save_still_valid(sale_start_dt, sale_end_dt)
# if not is_still_valid:
#     raise ValueError('Sale is over!')
# print('Aciu kad perkate')

# import datetime
#
# # Sukuriame datetime objektą iš datos string'o
# ivestis = '2020-02-11'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
# print(my_datetime)
#
# # Sukuriame datetime objektą iš datos ir laiko string'o
# ivestis = '2020-02-15, 10:11:59'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d, %H:%M:%S')
# print(my_datetime)
#
# import datetime
# from calendar import month
#
# months= {
#     1: 'Sausis',
#     2: 'Vasaris'
# }
#
# # ivestis = '2020-02-11'
# # my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
# # print(my_datetime)
#
# ivestis = '2020-02-15, 10:11:59'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d, %H:%M:%S')
# # print(my_datetime)
#
# # print(my_datetime)
# # print(type(my_datetime.strftime('%d %m %Y')))
#
# print(months.get((my_datetime.month)))
#
# print(my_datetime.strftime('%d %m %Y'))
# print(my_datetime.strftime('%Y %m %d'))
# print(my_datetime.strftime('%Y %B %d'))

import datetime

dabar = datetime.datetime.today()