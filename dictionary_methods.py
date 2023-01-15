def get(a):
    print("Input of enter the key : ",end = "")
    k = input()
    if k.isdigit():
        j = int(k)
    if k in a:
        print('Key found\nValue of ',k,' is : ',a[k],sep='')
    elif j in a:
        print('Key found\nValue of ',j,' is : ',a[j],sep='')
    else:
        print("Key not found")
def items(d):
    l = tuple()
    t=list()
    for i in d:
        x = d[i]
        l = (i,x)
        t = t + [l]
    print("Contents of dictionary : dict_items(",t,')',sep='')
def keys(d):
    l = list()
    for i in d:
        l += [i]
    print("Keys : dict_keys(",l,')',sep='')
def values(d):
    l = list()
    for i in d:
        l += [d[i]]
    print('Values : dict_values(',l,')',sep='')
def update(d):
    n = eval(input('Enter second dictionary : '))
    di = dict()
    for j in n:
        for i in d:
            if i == j:
                print('Dictionary cannot be created.',i,'is common in both dictionary')
                break ;
            else:
                di[i] = d[i]
        else:
            di[j] = n[j]
    print("Updated dictionary : ",di)
def popitem(d):
    l = list(d.keys())
    leng = len(l)-1
    x = l[leng]
    d.pop(x)
    print("Modified list : ",d)
print("\t\tMENU\n1. get()\n2. items()\n3. keys()\n4. values()\n5. update()\n6. popitem()")
a = 'Y'
while a == 'y' or a == 'Y':
    d = eval(input("Enter dictionary "))
    print("Enter your choice [1/2/3/4/5/6] : ",end = "")
    ch = int(input())
    if ch==1:
        get(d)
    elif ch==2:
        items(d)
    elif ch==3:
        keys(d)
    elif ch==4:
        values(d)
    elif ch==5:
        update(d)
    elif ch==6:
        popitem(d)
    else:
        print('Invalid Input')
    a = input('Do you wish to continue : [y/N] ')
else:
    print('Program Ends! ')
