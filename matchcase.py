################################### match case (switch)

# a= int(input("Enter number: "))
# match a:
#     case 5:
#         print('value is 5')
#     case 6:
#         print("value is 6")
#     case 10:
#         print("value is 10")
#     case _:
#         print("Entered value is not found")

#write a python program to print a table of number which lies between 1 and 10
number=int(input("Enter number between 1 and 10 :"))
for i in range(1,11):
 match number:
     case 1:
        print(number,"*",i,"=",number*i)
     case 2:
         print(number,"*",i,"=",number*i)
     case 3:
         print(number,"*",i,"=",number*i)
     case 4:
         print(number,"*",i,"=",number*i)
     case 5:
         print(number,"*",i,"=",number*i)
     case 6:
         print(number,"*",i,"=",number*i)
     case 7:
         print(number,"*",i,"=",number*i)
     case 8:
         print(number,"*",i,"=",number*i)
     case 9:
         print(number,"*",i,"=",number*i)
     case 10:
         print(number,"*",i,"=",number*i)
     case _:
         print("your enter number is not between 1 and 10")




