veg=int(input("Enter the veg:"))
fruits=int(input("Enter the fruit:"))
snack=int(input("Enter the snack:"))
grossery=int(input("Enter the grossery:"))
stationary=int(input("Enter the stationary:"))
items=[veg,fruits,snack,grossery,stationary]
item=0
for all_item in items:
    item=item+all_item
    print(item)