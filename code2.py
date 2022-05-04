#Parse below output to form dictionary where output should be like {key: []}
#     ex:     input:       in string
# 	            device1   vlan1
# 				device2   vlan2
# 				device3   vlan1
# 				device2   vlan3
# 				device1   vlan4
# 				device2   vlan1
# 				device3   vlan6
			
# 			output: 
# 			    {"device1": ["vlan1", "vlan4"], "device2": ["vlan2", "vlan1", "vlan3"], "device3": ["vlan1", "vlan6"]}


def convert(string):
    dictonary={}
    for subString in string.split("\n"):
        li = list(subString.split("   "))
        if li[0] in dictonary:
            dictonary[li[0]].append(li[1])
        else:
            dictonary[li[0]] = list(li[1].split(" "))
    return dictonary

a_string ="""device1   vlan1
device2   vlan2
device3   vlan1
device2   vlan3
device1   vlan4
device2   vlan1
device3   vlan6 """
print(convert(a_string))
