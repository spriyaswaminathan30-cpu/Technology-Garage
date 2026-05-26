mark1=int(input("Enter the mark1:"))
mark2=int(input("Enter the mark2:"))
mark3=int(input("Enter the mark3:"))
mark4=int(input("Enter the mark4:"))
mark5=int(input("Enter the mark5:"))
marks=[mark1,mark2,mark3,mark4,mark5]
mark=0
for total_marks in marks:
    mark=mark+total_marks
print("PRIYA SCORED "+ str(mark)+" IN HER FINAL EXAM")
