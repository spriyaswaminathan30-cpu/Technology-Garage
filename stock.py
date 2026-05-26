def stationary():
    pencil=int(input("Enter the total number of pencil: "))
    eraser=int(input("Enter the total number of eraser: "))
    scale=int(input("Enter the total number of scale: "))
    pen=int(input("Enter the total number of pen: "))
    pouch=int(input("Enter the total number of pouch: "))
    stationary_stock=[pencil, eraser, scale, pen, pouch]
    print(stationary_stock)
    for shop in stationary_stock:
        print(shop)
stationary()





 