# ####################### if else ,elif
name=input("Enter your name : ")
if name=="fahad" or name=="Fahad":
    print("Congration Fahad!!!!")
    age = int(input("Please enter your age : "))
    if age >= 18:
        print("Congratulation you can enter in room")
    elif age==10:
        print("you are a decade kid")
    else:
        print("sorry, you are teen ager")
else:
    print("sorry! You can't enter the system")



### Check student eligibility criteria  fist should pass eng, then math , then abel to take admission




isPass_english=input('Are you have passed in english subject: (pass/fail)? ')

if isPass_english=='pass':
    isPass_math=input('Are you have passed in math: (pass/fail)? ')
    if isPass_math=='pass':
        print('Congratulation you have to abel the take admission...')
    else:
        print('not abel to move for admission please pass you math subject')
else:
    print("Sorry you are failed in english subject ,, ")
