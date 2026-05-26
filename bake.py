def bakes():
    cake=int(input("Enter the price of cake: "))
    donut=int(input("Enter the price of donut: "))
    puff=int(input("Enter the price of puff: "))
    chocolate=int(input("Enter the price of chocolate: "))
    desert=int(input("Enter the price of desert: "))
    items=[cake,donut,puff,chocolate,desert]
    print(items)

    bill=open("billbook.txt", 'a')
    bill.write(str(cake)+'|')
    bill.write(str(donut)+'|')
    bill.write(str(puff)+'|')
    bill.write(str(chocolate)+'|')
    bill.write(str(desert)+'\n')
    bill.close()

def tom():
    priya=("billbook.txt", 'r')
    readvalue=priya.read()
    print(readvalue)



bakes()
tom()