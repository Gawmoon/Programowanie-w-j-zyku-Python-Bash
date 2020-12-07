#!/usr/bin/env python

path="new_file.txt"
new_lines=[]
file = open(path,'r')
for line in file:
    if " sie " or " i " or "oraz" or " nigdy " or "dlaczego" in line:
        line=line.replace(" i ", " oraz*V* ")
        line=line.replace(" oraz ", " i*V* ")
        line=line.replace(" nigdy", " prawie nigdy ")
        line=line.replace(" dlaczego", " czemu")
        line=line.replace("*V*", "")
        new_lines.append(line)
file.close()
with open("new_text.txt",'w') as file:
    file.writelines([line  for line in new_lines])