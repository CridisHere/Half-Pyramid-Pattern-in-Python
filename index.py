#WAP in Python to print the following pattern
#1 
#2     2 
#3     3     3 
#4     4     4     4 
#5     5     5     5     5 

def pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=' ')
        print()

pattern(5)  # prints the pattern for n=5