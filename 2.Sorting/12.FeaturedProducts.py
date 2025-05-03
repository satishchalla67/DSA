
def checkFeatured(products):
    
    productDict = {}
    
    for product in products:
        productDict[product] = productDict.get(product, 0)+1
        
    sortedProducts = sorted(productDict.items(), key= lambda x : (-x[1], x[0]))
    
    max_sold = sortedProducts[0][1]
    res = None
    for product, freq in sortedProducts:
        if freq == max_sold:
            res = product
    return res
    
products = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat', 'pinkHat', 'blackShirt', 'yellowShirt', 'greenPants','greenPants','greenPants']

featuredProduct = checkFeatured(products)
print(featuredProduct)