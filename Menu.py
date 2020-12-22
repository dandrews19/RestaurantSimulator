# This class represents the restaurant’s menu which contains four different categories of
# menu items diners can order from

from MenuItem import MenuItem

class Menu(object):

    # a list of categories of the menu items to be referenced later when taking orders
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # instance attributes for the menu, creates separate lists for each category using the menu file
    def __init__(self, menuParam = "menu.csv"):
        fileIn = open(menuParam, "r")
        appetizerList = []
        drinkList = []
        entreeList = []
        dessertList = []
        for line in fileIn:
            menuItem = line.strip().split(",")
            item = MenuItem(nameParam= menuItem[0], typeParam= menuItem[1], priceParam = menuItem[2], descParam = menuItem[3])
            if menuItem[1] == "Appetizer":
                appetizerList.append(item)
            elif menuItem[1] == "Dessert":
                dessertList.append(item)
            elif menuItem[1] == "Drink":
                drinkList.append(item)
            elif menuItem[1] == "Entree":
                entreeList.append(item)
        self.drinkList = drinkList
        self.appetizerList = appetizerList
        self.entreeList = entreeList
        self.dessertList = dessertList
        fileIn.close()

    # inputs: string representing a type of menu item,  integer representing the index position of a certain menu item
    # output: a MenuItem object from one of the four menuItem lists
    # description: Gets the correct MenuItem from the lists using its type and index position in the list of items
    def getMenuItem(self, typeParam, indexParam):
        menu = Menu()
        if typeParam == menu.MENU_ITEM_TYPES[0]:
            return self.drinkList[indexParam]
        elif typeParam == menu.MENU_ITEM_TYPES[1]:
            return self.appetizerList[indexParam]
        elif typeParam == menu.MENU_ITEM_TYPES[2]:
            return self.entreeList[indexParam]
        elif typeParam == menu.MENU_ITEM_TYPES[3]:
            return self.dessertList[indexParam]

    # inputs: a string representing a type of menu item
    # outputs: None
    # description: Prints a header with the type of menu items, followed by a numbered list of all the menu items of
    # that type.
    def printMenuItemsByType(self, typeParam):
        if typeParam == Menu.MENU_ITEM_TYPES[0]:
            print("-----DRINKS-----")
            i = 0
            while i < len(self.drinkList):
                print(i, str(self.drinkList[i]))
                i += 1
        elif typeParam == Menu.MENU_ITEM_TYPES[1]:
            print("-----APPETIZERS-----")
            c = 0
            while c < len(self.appetizerList):
                print(c, str(self.appetizerList[c]))
                c += 1
        elif typeParam == Menu.MENU_ITEM_TYPES[2]:
            print("-----ENTREES-----")
            h = 0
            while h < len(self.entreeList):
                print(h, str(self.entreeList[h]))
                h += 1
        elif typeParam == Menu.MENU_ITEM_TYPES[3]:
            print("-----DESSERTS-----")
            j = 0
            while j < len(self.dessertList):
                print(j, str(self.dessertList[j]))
                j += 1

    # inputs: a string representing a type of menu item
    # outputs: an integer representing the number of MenuItems of the input type
    # description: this function gets the number of items by type on the menu to be used to error check the user input
    def getNumMenuItemsByType(self, typeParam):
        if typeParam == Menu.MENU_ITEM_TYPES[0]:
            return int(len(self.drinkList))
        elif typeParam == Menu.MENU_ITEM_TYPES[1]:
            return int(len(self.appetizerList))
        elif typeParam == Menu.MENU_ITEM_TYPES[2]:
            return int(len(self.entreeList))
        elif typeParam == Menu.MENU_ITEM_TYPES[3]:
            return int(len(self.dessertList))