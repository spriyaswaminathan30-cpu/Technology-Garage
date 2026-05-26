available_items="dosa", "idly", "pongal", "vada", "poori"
order="masal dosa"
did_you_find_my_order="no"
for everyitem in available_items:
    if everyitem==order:
        did_you_find_my_order="yes"
        if did_you_find_my_order=="yes":
            print("Your order is available")
        else:
            print("your order is not available")
