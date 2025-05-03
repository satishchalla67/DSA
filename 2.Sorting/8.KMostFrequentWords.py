



from heapq import heappush, heappop



#tc = O(nlogn)
def frequentWords(arr, k):
    worddict = {}
    for word in arr:
        worddict[word] = worddict.get(word, 0)+1
    
    heaparr = []
    
    for key, val in worddict.items():
        heappush(heaparr, (-val, key))
    
    return [heappop(heaparr)[1] for _ in range(k)]


#k most frequent words sorted in lexicographical order
arr = ['priya', 'bhatia', 'akshay', 'arpit', 'priya', 'arpit']
k = 3
result = frequentWords(arr, k)
print(result)