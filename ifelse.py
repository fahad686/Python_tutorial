####################### if else ,elif
name=input("Enter your name : ")
if(name=="fahad" or name=="Fahad"):
    print("Congration Fahad!!!!")
    age = int(input("Please enter your age : "))
    if (age >= 18):
        print("Congratulation you can enter in room")
    elif(age==10):
        print("you are a decade kid")
    else:
        print("sorry, you are teen ager")
else:
    print("sorry! You can't enter the system")



