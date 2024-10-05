if __name__ == '__main__':
    d={}
    for i in range(int(input())):

        name = input()
        score = float(input())
        d[name]=score
    first=None
    second=None
    for i in d.values():
        if first is None or i<first:
            second=first
            first=i
        elif (second is None or second>i) and first!=i :
            second=i
    l=[]
    for i,j in d.items():
        if j==second:
            l.append(i)
    l=sorted(l)
    for i in l:
        print(i) 

        



def count_substring(s,t):
    l=[]
    for i in range(0,len(s)):
        if t in s[i:len(t)+i]:
            l.append(t)
    return len(l) 
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
