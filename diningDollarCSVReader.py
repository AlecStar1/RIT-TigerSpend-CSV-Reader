import sys
def matchHelp(inpu, match, toReplace):
    if match in inpu:
        return toReplace
    else:
        return None

def simplifyDH(descript):
    DH = descript
    for match,case in [
                    ["Nathan","Nathan's Soup & Salad"],
                    ["BEVERAGE","Vending Machine Drink"],
                    ["SNACK","Vending Machine Snack"],
                    ["FOOD","Vending Machine Food"],
                    ["Crossroads","Crossroads"],
                    ["Commons","Commons"],
                    ["Corner","The Corner Store"],
                    ["Beanz","Beanz"],
                    ["Brick City", "Brick City"],
                    ["RITZ","RITZ"],
                    ["Cantina","Cantina"],
                    ["Ctrl", "Ctrl Alt Deli"],
                    ["Grind","College Grind"],
                    ["Midnight","Midnight Oil"],
                    ["Campus","Food Truck"],
                    ["Ben","Ben & Jerry's"],
                    ["MICRO","Micro Market"],
                    ["Artesano","Artesano's"],
                    ["Latke","Loaded Latke"],
                    ["Market","The Market at Global Village"]]:
                    out = matchHelp(descript, match, case)
                    if out:
                        DH = out
    return DH
class reader:
    import csv
    import statistics
    file = None
    purchases = []
    diningHall = {}
    days = {}
    
    def __init__(self, filename):
        assert filename[-3:].lower() == "csv"
        with open(filename, newline='') as csvfile:
            self.file = csvfile
            for i in self.csv.DictReader(csvfile):
                self.purchases.append(i)
                DH = simplifyDH(i["Description"])
                self.diningHall.setdefault(DH, 0) 
                self.diningHall[DH] += 1
                self.days.setdefault(i["date"].split(" ")[0], 0)
                self.days[i["date"].split(" ")[0]] += 1
    
    def average(self):
        """
        adds up all the amounts and returns the average of it.\n
        returns: float
        """
        amount = [float(i["Amount"]) for i in self.purchases]
        return self.statistics.fmean(amount)

    def mean(self):
        """
        exactly the same as average.
        returns: float
        """
        return self.average()
    def median(self):
        return self.statistics.median(self.amount)
    
    def averageDiningArea(self):
        return max(self.diningHall.__iter__(), key=(lambda key: self.diningHall[key]))

    def onlineAmount(self):
        return sum("OnDemand" in x["Description"] for x in self.purchases)
   
    def biggestPurchase(self):
        biggest = min(self.purchases, key=lambda i: float(i["Amount"]))
        return [biggest["Amount"], simplifyDH(biggest["Description"]), biggest["Date"]]

    def BiggestAmountSpentOnADay(self):
         return max(self.days.__iter__(), key=(lambda key: self.days[key]))

    def __len__(self):
        return len(self.purchases)

    def __str__(self):
        return f"""\t{len(self)} purchases with a average of {"{:.2f}".format(self.average())} per purchase.
        The biggest purchase was {self.biggestPurchase()[0]} from {self.biggestPurchase()[1]} on {self.biggestPurchase()[2]}.
        Most of those were from {self.averageDiningArea()} with {self.diningHall[self.averageDiningArea()]} purchases.
        Most purchases were made on {self.BiggestAmountSpentOnADay()} with {self.days[self.BiggestAmountSpentOnADay()]} purchases.
        Out of all of the purchases, {self.onlineAmount()} were made with OnDemand.
        """
    
if __name__ == "__main__":
    uhhh = reader(sys.argv[1])
    print(uhhh)

    