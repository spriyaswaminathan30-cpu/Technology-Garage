def scorecard():
    name=str(input("Enter the name:"))
    mark1=int(input("Enter the mark1:"))
    mark2=int(input("Enter the mark2:"))
    mark3=int(input("Enter the mark3:"))
    scorecard=open("marksheet.txt","a")
    scorecard.write("name"+"|")
    scorecard.write(str("mark1")+"|")
    scorecard.write(str("mark2")+"|")
    scorecard.write(str("mark3")+"\n")
    scorecard.close()

scorecard()

def scorecards():
    scorecards=("marksheet.txt","r")
    read=(scorecards.read())
    print(read)
    scorecards.close()

scorecards()