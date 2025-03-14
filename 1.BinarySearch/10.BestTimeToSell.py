

# 121. Best Time to Buy and Sell Stock

def calMaxProfit(prices):
    min_val = float('inf')
    max_val = 0
    for i in range(len(prices)):
        if prices[i]<min_val:
            min_val = prices[i]
        elif prices[i] - min_val > max_val:
            max_val = prices[i]-min_val
    return max_val


prices = [7,1,5,3,6,4]
maxProfit = calMaxProfit(prices)
print(maxProfit)