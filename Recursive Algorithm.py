'''
Recursive Algorithm
Recursive Algorithm refers to a method of solving problems by repeatedly decomposing them into similar sub problems, similar to divide and conquer. Recursive 
Algorithms can be used to solve many computer science problems, so they are a very important concept in computer science. Most programming languages support 
self calling of functions, in which functions can be recursively implemented by calling themselves. In many functional programming languages, recursion is 
commonly used to implement loops. We can use recursion to solve many problems that loops cannot solve, such as inverting strings, calculating Fibonacci 
sequences, and so on.

Example questions
Hanoi Tower Problem
There are three pillars named A, B, and C. On the A-pillar, there are n disks arranged from top to bottom, from small to large. Each time, only the top disk of
each tower with disks can be moved. When moving, the top disk of the destination pillar needs to be larger than the moving disk. Your goal is to move all the 
disks on the A-pillar to the C-pillar and ensure that the operation is legal during the operation, and finally tell everyone the operation sequence with the 
least number of operations.

Input Format
A positive integer n

Output Format
Assuming there are k rows in the output, with each row formatted as' X ->Y 'indicating that the top disk of the X column moves to the Y column

Sample Input
2

Sample Output
A ->B
A ->C
B ->C

Data Range
0<n<50

Brain Storm
To do this question, we need to use a recursive algorithm,
1. Move n-1 disks from A to B
2. Move the last disk of A to C
3. Next, move the remaining disks of B to C

Let's take a look at the code
'''
def hanoi(A, B, C, n):
    if n == 1:
        print(f"{A}->{C}")
        return 0
    hanoi(A,C,B,n-1)
    print(f"{A}->{C}")
    hanoi(B,A,C,n-1)

def main():
    n = int(input())
    hanoi('A', 'B', 'C', n)

if __name__ == "__main__":
    main()
'''
review

We used a recursive algorithm to solve the Tower of Hanoi problem. We used a bidirectional operation similar to recursion to solve the problem of moving pillars from
A to C. Recursion actually has many other uses, and we hope you can better grasp it.

Thank you for watching. Translation reference https://fanyi.baidu.com
(author: zjnbswj707)
'''
