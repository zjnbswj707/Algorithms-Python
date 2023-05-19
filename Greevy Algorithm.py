'''
The greedy algorithm generally follows the following steps:

① Establish a mathematical model to describe the problem.

② Divide the solved problem into several sub problems.

③ Solve each subproblem to obtain the local optimal solution of the subproblem.

④ Synthesize the local optimal solution of the subproblem into a solution of the original solution problem.

Although it is necessary to ensure that a local optimal solution can be obtained at each step, the resulting global solution may not necessarily be optimal, so greedy
algorithms should not backtrack.
(This material comes from Baidu)

Example questions
HairCut

There is a barber shop and n customers are coming today. These customers came at the same time, without any order. This barber shop has m hairdressers with the same 
work efficiency, who can cut customers' hair at the same time. Every customer needs to cut their hair It takes a certain amount of time. In order to minimize the 
waiting time, you need to write a program to queue up customers and finally output the captured queue (waiting time=hair cutting time of all customers in front of the
queue+your own hair cutting time)

Input Format

Two rows in total
The first line n, m: represents the number of customers and the number of hairdressers, respectively.
The second line has n numerical values: each represents the time required to complete the haircut for this client's hair.

Output Format

Total m rows
Each row has some numerical values, separated by spaces, indicating the time it takes for each customer in this queue to cut their hair

Sample Input

5 3
1 2 3 4 5

Sample Output

1 4
2 5
3

Data Range
0 < n, m < 100000

Brain Storm

To do this question, we need to use a greedy algorithm to determine which hairdresser will be free at each step, and then ask him to cut the hair for the next client.
1. We need to sort the hair cutting time of customers to ensure that the waiting time is minimized as much as possible
2. Determine which hairdresser will be available and then ask him to cut the hair for the next client
3. Obtain the final queue and output

Let's take a look at the code now
We used a class to manage the queues
'''

class HairCut:
    def __init__(self, line) -> None:
        self._haircut = []
        for i in range(line):
            self._haircut.append([])
            
    def insert(self, line, custom) -> None:
        self._haircut[line-1].append(custom)
        
    def sum(self, line) -> int:
        return sum(self._haircut[line-1])
       
    def get(self, line) -> list[int]:
        return self._haircut[line-1]
    
def min_inlist(lst) -> int:
    _min = 500000
    for i in lst:
        _min = min(_min, i)
    return _min

def get_allsums(obj, line) -> list[int]:
    lst = []
    for i in range(1, line+1):
        lst.append(obj.sum(i))
    return lst

def get_vals() -> list:
    s = input().split()
    for i in range(len(s)):
        s[i] = eval(s[i])
    return s

def main(line, customers):
    haircut = HairCut(line)
    for i in customers:
        lst = get_allsums(haircut, line)
        mininum = min_inlist(lst)
        p = lst.index(mininum)
        haircut.insert(p + 1, i)
    for i in range(1, line + 1):
        t = haircut.get(i)
        for i in t:
            print(t[i], end = ' ')
        print('')

if __name__ == '__main__':
    line = get_vals()[1]
    customers = get_vals()
    main(line, customers)
    
'''
Review

We used greedy algorithms to solve the hair cutting problem, but in fact, there are many places where greedy algorithms can be used, such as the TSP problem and the 
Prim problem. Greedy algorithm is a fundamental algorithm that seeks local optimal solutions with high efficiency and a wide range of applications.

Thank you for watching. Translation reference https://fanyi.baidu.com
(author: zjnbswj707)
'''
