#convert string into list of list with first line as first element in all sublist, sublist len is 3
#	ex:    input:        in string
#				first line 
#				second line 
#				third line
#				fourth line
#				fifth line
#				
#			output:
#			    [["first line", "second line", "third line"], ["first line", "fourth line", "fifth line"]]
				
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
