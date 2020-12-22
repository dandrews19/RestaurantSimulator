# This class will represent the restaurant’s waiter. The waiter maintains a list of the diners
# it is currently taking care of, and progresses them through the different stages of the
# restaurant. The waiter in the simulation will repeat multiple cycles of attending to the
# diners. In each cycle, the waiter will seat a new diner, if one arrives, take any diners’
# orders if needed, and give diners their bill, according to each diner’s status

from Menu import Menu
from Diner import Diner

class Waiter(object):

    # creates instance attributes, gives the waiter a list of diners and a menu
    def __init__(self, menuObjectParam):
        self.diners = []
        self.menu = menuObjectParam

    # input: self, diner
    # output: none
    # description: adds the diner to the waiter's list of diners
    def addDiner(self, dinerObjectParam):
        self.diners.append(dinerObjectParam)

    # input: self
    # output: number of diners
    # description: returns the number of diners in the restaurant when called
    def getNumDiners(self):
        return int(len(self.diners))

    # input: self
    # output: none
    # description: prints the status of all the diners in the restaurant when called
    def printDinerStatuses(self):
        print("Diners who are seated: ")
        i = 0
        while i < len(self.diners):
            if self.diners[i].getStatus() == 0:
                print("\t" + str(self.diners[i].getName()), "is currently seated.")
            i += 1
        print("Diners who are ordering: ")
        h = 0
        while h < len(self.diners):

            if self.diners[h].getStatus() == 1:
                print("\t" + self.diners[h].getName(), "is currently ordering.")
            h += 1
        print("Diners who are eating: ")
        c = 0
        while c < len(self.diners):

            if self.diners[c].getStatus() == 2:
                print("\t" + self.diners[c].getName(), "is currently eating.")
            c += 1
        print("Diners who are paying: ")
        j = 0
        while j < len(self.diners):

            if self.diners[j].getStatus() == 3:
                print("\t" + self.diners[j].getName(), "is currently paying.")
            j += 1
        print("Diners who are leaving:")
        u = 0
        while u < len(self.diners):
            if self.diners[u].getStatus() == 4:
                print("\t" + str(self.diners[u].getName()), "is currently leaving.")
            u += 1

    # input: self
    # output: none
    # description: takes the customers order ad adds it to their own order list to be used to display later and
    # calculate cost
    def takeOrders(self):
        i = 0
        orderList = []
        while i < len(self.diners):
            if self.diners[i].getStatus() == 1:
                h = 0
                while h < len(Menu.MENU_ITEM_TYPES):

                    self.menu.printMenuItemsByType(typeParam=Menu.MENU_ITEM_TYPES[h])
                    print(self.diners[i].getName() + ", please select a " + str(self.menu.MENU_ITEM_TYPES[h]) + " menu item number.")
                    order = input("> ")
                    while order.isdigit() == False or int(order) >= self.menu.getNumMenuItemsByType(self.menu.MENU_ITEM_TYPES[h]):
                        order = input("> ")
                    orderVar = self.menu.getMenuItem(typeParam=Menu.MENU_ITEM_TYPES[h], indexParam=int(order))
                    orderList.append(orderVar)
                    h += 1
                self.diners[i].addToOrder(orderList[0])
                self.diners[i].addToOrder(orderList[1])
                self.diners[i].addToOrder(orderList[2])
                self.diners[i].addToOrder(orderList[3])
                self.diners[i].printOrder()
            i += 1

    # input: self
    # output: none
    # description: prints the customer's total cost using the calculate meal cost function
    def ringUpDiners(self):
        i = 0
        while i < len(self.diners):
            if self.diners[i].getStatus() == 3:
                print("\n" + str(self.diners[i].getName()) + ", your meal cost $" + str(self.diners[i].calculateMealCost()))
            i += 1

    # input: self
    # output: none
    # description: removes diners from the restaurant when they are done
    def removeDoneDiners(self):
        i = 0
        while i < len(self.diners):
            if self.diners[i].getStatus() == 4:
                print(self.diners[i].getName() + ", thank you for dining with us! Come again soon!")
            i += 1
        for index in range(len(self.diners)-1, -1, -1):
            diner = self.diners[index]
            if diner.getStatus() == 4:
                self.diners.remove(diner)


    # input: self
    # output: none
    # description: prints all the diner's statuses, takes the orders of people ordering, calculates the cost of
    # paying customers, removes the diners who are leaving, and updates the status of all the diners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        i = 0
        while i < len(self.diners):
            self.diners[i].updateStatus()
            i += 1

