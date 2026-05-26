victim=30
cook=int(input("Enter the Cook Evidence: "))
gardener=int(input("Enter the  Gardener Evidence: "))
maid=int(input("Enter the Maid Evidence: "))
if (cook>=victim):
    print("Cook is the Killer")
elif(gardener>=victim):
    print("Gardener isthe Killer")
elif(maid>=victim):
    print("Maid is the Killer")
else:
    print("Killer is Missing")
    
