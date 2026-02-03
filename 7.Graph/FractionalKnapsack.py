

class Item:
    def __init__(self, profit, weight):
        self.profit=profit
        self.weight=weight
        
        
def fractionalKnapsack(arr,m):
    
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    for item in arr:
        print(item.profit, item.weight)
    max_profit=0.0
    for item in arr:
        if item.weight<m:
            m-=item.weight
            max_profit+=item.profit
        else:
            max_profit+=item.profit*(m/item.weight)
            break
    return max_profit

# Knapsack Problem: Selecting the best combination of items to fit in a container with a weight limit.
M=37
arr=[Item(25,5), Item(75,10), Item(100,12), Item(50,4), Item(45,7), Item(90,9), Item(30,3)]
profit=fractionalKnapsack(arr,M)
print(profit)