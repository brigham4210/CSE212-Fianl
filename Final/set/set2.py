set = {1,2,3,4,5,6,7,8,9,10,11}
set2 = {'dog','cat','shark','goose'}
ar = ["none","none","none","none"]
ar2 = ["none","none","none","none"]

def hashing(number):
    a = number % 4
    if ar[a-1] == "none":
        ar[a-1] = number
    elif type(ar[a-1]) == int:
        ar[a-1] = [ar[a-1], number]
    else:
        ar[a-1].append(number)
    print(ar)

for i in set:

    hashing(i)

def hashing2(item):
    a = hash(item) % 4
    if ar2[a-1] == "none":
        ar2[a-1] = item
    elif type(ar[a-1]) == str:
        ar2[a-1] = [ar2[a-1], item]
    else:
        ar2[a-1].append(item)
    print(ar2)


for i in set2:
    
    hashing2(i)


