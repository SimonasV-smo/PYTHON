
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

import datetime

# my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
# today_dt = datetime.datetime.today()

# print(my_datetime)

# if my_datetime < today_dt:
#     print('YES')

def is_save_still_valid(start_dt, end_dt) -> bool:
    today_dt = datetime.datetime.today()
    if start_dt < today_dt < end_dt:
        return True
    return False

sale_start_dt = datetime.datetime(year=2025, month=2, day=2)
sale_end_dt = datetime.datetime(year=2025, month=4, day=2)

is_still_valid = is_save_still_valid(sale_start_dt, sale_end_dt)
if not is_still_valid:
    raise ValueError('Sale is over!')
print('Aciu kad perkate')
