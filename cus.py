apple=input("Enter the apple cost:")
orange=int(input("Enter the orange cost:"))

fruit=open("bill.txt", "w")
fruit.write(str(apple)+'|')
fruit.write(str(orange)+'|')

fruit.close()

priya=open("bill.txt","r")
read=(priya.read())
print(read)
priya.close()