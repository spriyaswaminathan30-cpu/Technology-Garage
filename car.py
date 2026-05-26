car1=int(input("enter the value of car1: "))
car2=int(input("enter the value of car2: "))
car3=int(input("enter the value of car3: "))
if(car1>car2 and car1>car3):
    print("car1 is the winner")
elif(car2>car1 and car2>car3):
    print("car2 is the winner")
else:
    print("car3 is the winner")
