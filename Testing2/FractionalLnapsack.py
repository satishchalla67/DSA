



class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        


def fractionalKnapsack(arr, m):
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    profit=0
    for item in arr:
        if item.weight<m:
            m-=item.weight
            profit+=item.profit
        else:
            profit+=item.profit*(m/item.weight)
            return profit



m=37
arr=[Item(25,5), Item(75,10), Item(100,12), Item(50,4), Item(45,7), Item(90,9), Item(30,3)]
result = fractionalKnapsack(arr, m)
print(result)

