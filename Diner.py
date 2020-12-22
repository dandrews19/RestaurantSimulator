#  This class represents one of the diners at the restaurant and keeps tracks of their status and meal.

from MenuItem import MenuItem

class Diner(object):
    #  a list of strings containing the possible statuses a diner might have
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # instance attributes assigned to each diner, a name, their order, and their status
    def __init__(self, dinerNameParam):
        self.name = dinerNameParam
        self.order = []
        self.status = 0

    # input: self
    # output: customer name
    # description: returns the customer's name when called using the Diner class
    def getName(self):
        return self.name

    # input: self
    # output: customer order
    # description: returns the customer's order when called using the Diner class
    def getOrder(self):
        return self.order

    # input: self
    # output: customer status number
    # description: returns the customer's status number when called using the Diner class
    def getStatus(self):
        return self.status

    # input: self
    # output: none
    # description: updates the customers status when called
    def updateStatus(self):
        self.status += 1

    # input: self
    # output: none
    # description: adds to customers order when called
    def addToOrder(self, menuItemParam):
        self.order.append(menuItemParam)

    # input: self
    # output: none
    # description: prints the customers whole order when called
    def printOrder(self):
        print(self.name, "ordered:")
        i = 0
        while i < len(self.order):
            print(self.order[i])
            i += 1

    # input: self
    # output: none
    # description: returns the customer's order cost when called
    def calculateMealCost(self):
        h = 0
        cost = 0
        while h < len(self.order):
            cost += float(self.order[h].getPrice())
            h += 1
        return float(cost)

    # input: self
    # output: customer status
    # description: prints the customers status when called
    def __str__(self):
        msg = "Diner " + self.name + " is currently " + Diner.STATUSES[self.status] + "."
        return msg