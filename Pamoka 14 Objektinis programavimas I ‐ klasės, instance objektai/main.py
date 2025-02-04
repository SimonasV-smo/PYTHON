

class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

house1 = House(199000, 2025)
house2 = House(165000, 2008)

house1.country = 'LV'

print(
    house1.country, house1.price, house1.year
)
print(
    house2.country, house2.price, house2.year
)