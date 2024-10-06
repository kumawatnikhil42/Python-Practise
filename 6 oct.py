import textwrap

def wrap(string, max_width):
    w=max_width
    i=0
    end=len(string)
    l=[]
    while i<end:
        l.append(string[i:i+w])
        i+=w
    
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)




# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
for i in range(0,n//2):
    for s in range(m//2-1,3*i,-1):
        
        print("-",end="")
    for j in range(0,2*i+1):
        print(".|.",end="")
    for s in range(m//2-1,3*i,-1):
        
        print("-",end="")
    print()
for i in range(0,(m-7)//2):
    print("-",end="")
print("WELCOME",end="")
for i in range(0,(m-7)//2):
    print("-",end="")
print("")
for i in range(0,n//2):
    for s in range(0,3*(i+1)):
        print("-",end="")
    for j in range(2*(n//2-i-1),-1,-1):
        print(".|.",end="")
    for s in range(0,3*(i+1)):
        
        print("-",end="")
    print("")   
