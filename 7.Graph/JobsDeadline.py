import heapq
class Job:
    def __init__(self, profit, deadline):
        self.profit = profit
        self.deadline = deadline
        
def findMaxProfit(jobs):
    lastDeadline = -1
    
    for job in jobs:
        if job.deadline >lastDeadline:
            lastDeadline = job.deadline
    days = [False]*lastDeadline
    
    jobs.sort(key = lambda x: x.profit, reverse=True)
    maxProfit=0
    
    for job in jobs:
        idx=job.deadline-1
        while idx>=0:
            if not days[idx]:
                print(job.profit, idx+1)
                maxProfit+=job.profit
                days[idx]=True
                break
            idx-=1
    print(days)
    
    return maxProfit
            

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x,y):
        rx = self.find(x)
        ry = self.find(y)
        self.parent[rx] = ry


def findMaxProfitOptimized(jobs):
    
    if not jobs:
        return 0
    
    max_deadline = max(job.deadline for job in jobs)
    dsu = DSU(max_deadline)
    jobs.sort(key=lambda x:x.profit, reverse=True)
    maxProfit=0
    
    for job in jobs:
        
        available = dsu.find(min(job.deadline, max_deadline))
        
        if available>0:
            maxProfit+=job.profit
            dsu.union(available, available-1)
    return maxProfit
        
    
def findMaxUsingHeap(jobs):
    jobs.sort(key = lambda x : x.deadline)
    
    n=[]
    
    for job in jobs:
        heapq.heappush(n, job.profit)
        print("pushing", job.profit, job.deadline)
        if job.deadline < len(n):
            print("poping", heapq.heappop(n))
    return sum(n)

# Job must be submitted before the deadline and max profit should be made
jobs = [Job(55,5), Job(65,2), Job(75,7), Job(60,3), Job(70,2), Job(50,1), Job(85,4), Job(68,5), Job(45,3)]
maxProfit = findMaxUsingHeap(jobs)
print(maxProfit)

# jobs.sort(key=lambda x : x.profit, reverse=True)

# for job in jobs:
#     print(job.profit, job.deadline)
