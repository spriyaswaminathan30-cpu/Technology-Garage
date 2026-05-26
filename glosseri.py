def montly():
    rice=int(input("Enter the price of the rice: "))
    dal=int(input("Enter the price of the dal: "))
    spices=int(input("Enter the price of the spices: "))
    milk=int(input("Enter the price of the milk: "))
    curd=int(input("Enter the price of the curd: "))
    glossery=[rice,dal,spices,milk,curd]
    print(glossery)
    total=0
    for items in glossery:
        total=total+items
        print(total)
    bill=open("montly.txt","a")
    bill.write(str(rice)+'|')
    bill.write(str(dal)+'|')
    bill.write(str(spices)+'|')
    bill.write(str(milk)+'|')
    bill.write(str(curd)+"\n")
    bill.close

    home=open("montly.txt",'r')
    read=(home.read)
    print(read)
    home.close
montly()