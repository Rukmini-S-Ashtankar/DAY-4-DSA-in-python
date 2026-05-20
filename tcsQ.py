#input = aaabbbbccceeeee
#output = a3b4c3e5

name = 'aabbbbeeeeffggg'
newname = {}
for i in range(len(name)):
    key = name[i]
    count = 0
    for j in range(len(name)):
        if key ==  name[j]:
            count+=1
    newname[key] = count
# print(newname)
for i, j in newname.items():
    print(i,j,sep='', end='')
