# input: 578378923
# o/p: 3
#Explanation: The repeated digits in the data are 7, 8 and 3. So, the security key is 3

mylist = [5,7,8,3,7,8,9,2,3]
newlist=[]

for i in range(len(mylist)):
    count = 0 
    key = mylist[i]       #key = 5 then # =7 then=8 then =3     ,then on another 7 to check but it is not a key
    j = i+1               #j=0,then after j+1 j=1 (index num) =2 ,then finds key on j =3
    while j<len(mylist):             #^
        if key == mylist[j]:         #|
            newlist.append(key)      #|
        j = j+1                      #|
print(len(newlist))

