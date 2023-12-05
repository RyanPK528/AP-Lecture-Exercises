class ShoppingRPK:
    def __init__(self, foodname, amount):
        self.__foodname = foodname.lower()
        self.__amount = amount
        self.__standardPrice = self.__PriceListRPK()
        self.__calcPrice = self.__totalCostRPK()

    def __PriceListRPK(self):
        if self.__foodname == 'dry cured iberian ham':
            return 177.80
        elif self.__foodname == 'wagyu steaks':
            return 450.00
        elif self.__foodname == 'matsutake mushrooms':
            return 272.00
        elif self.__foodname == 'kopi luwak coffee':
            return 306.50
        elif self.__foodname == 'moose cheese':
            return 487.20
        elif self.__foodname == 'white truffles':
            return 3600.00
        elif self.__foodname == 'blue fin tuna':
            return 3603.00
        elif self.__foodname == 'le bonnotte potatoes':
            return 270.81
        else:
            return 0.00

    def __totalCostRPK(self):
        return self.__amount * self.__standardPrice

    def get_food_nameRPK(self):
        return self.__foodname

    def get_amount_orderedRPK(self):
        return self.__amount

    def get_standard_priceRPK(self):
        return self.__standardPrice

    def get_orderPriceRPK(self):
        return self.__calcPrice

    def __str__(self):
        return f"Item: {self.__foodname.capitalize()}\nAmount ordered: {self.__amount:.1f} pounds\nPrice per pound: ${self.__standardPrice:.2f}\nPrice of order: ${self.__calcPrice:.2f}" 

    