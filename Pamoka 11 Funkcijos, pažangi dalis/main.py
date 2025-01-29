#
# def print_args(*args):
#     print(args)
#     print(type(args))
#
# print_args('Adomas', 'sausis', 1000)



# def give_hello_to_names(*args):
#     res = ''
#     for name in args:
#         res += f'Hello, {name}!\n'
#     return res
#
# print(give_hello_to_names('Ram', 'Adomas', 'Valdas'))

# def miltiply_all_by_numb(numb, *args):
#     for elem in args:
#         print(numb * elem)
#
# miltiply_all_by_numb(1, 2, 3, 4, 5)

# def take_order(customer_name, *args):
#     """
#     Takes a restaurant order with multiple food items.
#
#     :param customer_name: str
#     :param args: food items
#     :return: None
#     """
#     print(f'Order for {customer_name}')
#     for i in args:
#         print(f'- {i}')
#     print('Thank you for your order!')
#
# take_order('Darius', 'Pizza', 'burger', 'soausage', 'milshake')
#
# def multiply_all_by_numb(numb, *args, text='* daugyba'):
#     """
#     Ši funkcija padaugina kiekvieną skaičių iš pateikto skaičiaus.
#
#     :param numb: int arba float, pagrindinis skaičius
#     :param args: int arba float, skaičiai, kuriuos reikia padauginti
#     :param text: str, pasirinktinė žinutė po rezultato, numatytoji reikšmė '* daugyba'
#     :return: None
#     """
#     for i in args:
#         print(f'{numb} * {i} = {numb * i} {text}')
#
# # Funkcijos iškvietimai
# multiply_all_by_numb(7, 10, 11, 50)
# multiply_all_by_numb(7, 10, 11, 50, text='***')
#
#
# def return_list_of_multiplied_numbs(numb, *args, info=False):
#     multiplied_numbs = [elem * numb for elem in args]
#     if info:
#         print(f'daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}')
#     return multiplied_numbs
#
# # Funkcijos iškvietimai
# res = return_list_of_multiplied_numbs(7, 10, 11, 50)
# print(res)
#
# res = return_list_of_multiplied_numbs(7, 10, 11, 50, info=True)
# print(res)
#
# def print_list(listas, skirtukas=' ', eilutes_pabaiga='\n'):
#     for elem in listas:
#         print(elem, 'men.', sep=skirtukas, end=eilutes_pabaiga)
#
# listas_duom = ['Sausis', 'vasaris', 'kovas']
# print_list(listas_duom)
# print_list(listas_duom, skirtukas='|||', eilutes_pabaiga='***\n')
#
# def print_list(listas, **kwargs):
#     for elem in listas:
#         print(elem, 'men.', **kwargs )
#
# print_list(listas_duom, sep='>>>')
# print_list(listas_duom, sep='>>>', end='---')

darbuotojai = [
    ['Valdas', 'programuotojas', 2000]



]

res = sorted(darbuotojai)

print(res)
