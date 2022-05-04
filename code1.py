def convert(string):
    li=string.split("\n")
    i=1
    while(i<=len(li)-1):        
        res=[]
        res.append(li[0])
        res.append(li[i])
        i=i+1
        res.append(li[i])
        ans =yield res
        i=i+1
    return ans
        
a_string ="""first line 
second line 
third line
fourth line
fifth line"""

print(list(convert(a_string)))
