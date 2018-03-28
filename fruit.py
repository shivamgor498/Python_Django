fruits = []
while(1):
    n = int(raw_input("\t1.Enter Fruit\n\t2.Print Fruit in sorted order\n\t3.exit"))
    if(n==1):
        s = raw_input("Enter Fruit")
        fruits.append(s)
    elif(n==2):
        fruits.sort()
        print fruits
    else:
        break
