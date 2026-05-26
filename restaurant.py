def restaurant():
    available=["rice", "sambar","curd","vada"]
    for all_items in available:
        print(all_items)
        available=open("menu.txt","a")
        available.write((all_items)+'|')
        available.close()
restaurant()