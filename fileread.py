def fruit():
    apple=int(input("enter the price of apple:"))
    orange=int(input("enter the price of orange:"))
    watermelon=int(input("enter the price of watermelon:"))
    fruitshop=open("fileread.txt","x")
    fruitshop.write(str(apple)+"|")
    fruitshop.write(str(orange)+"|")
    fruitshop.write(str(watermelon)+"\n")
    fruitshop.close()
def readfile():
    priya=open("fileread.txt","r")
    readvalue=priya.read()
    individual=readvalue.split("\n")
    print(individual)
    priya.close()
ape=10
def veggies():
    brinjal=20
    drumstick=30
    potato=40

#fruit()
readfile()
#veggies()
