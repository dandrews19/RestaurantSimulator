# This class will be used to get and display a menu item, its price, and description to the interface

class MenuItem(object):

    # inputs: self, name parameter, type parameter, price parameter, and description parameter
    # outputs: none
    # description: this function assigns attributes to the menu item based on information received from another file,
    # it assigns a type, a price, a name, and a description to the menu item
    def __init__(self, nameParam, typeParam, priceParam, descParam):
        self.name = nameParam
        self.type = typeParam
        self.price = priceParam
        self.description = descParam

    # input: self
    # output: name
    # description: this function returns the name of the menu item
    def getName(self):
        return self.name

    # input: self
    # output: type
    # description: this function returns the type of food from the menu item
    def getType(self):
        return self.type

    # input: self
    # output: price
    # description: this function returns the price of the menu item
    def getPrice(self):
        return self.price

    # input: self
    # output: description
    # description: this function returns the name of the menu item
    def getDescription(self):
        return self.description

    # input: none
    # output: string
    # description: this function returns a string containing the name, type, price, and description of a menu item
    def __str__(self):
        msg = "- " + self.getName() + " (" + self.getType() + "): " + "$" + self.getPrice() + "\n\t" + self.getDescription()
        return msg