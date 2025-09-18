#print 1 to 30 
# for i in range(30):
# #     print(i+1)
#  ###print list values
# a=[3,4,5,3,7,8,9]
# for item in a:
#     print(item)
# #####printing set values with for loop
# b={55,66,77,88,99}
# for item in b:
#     print("pinting set values",item)
#


    #continure
list=[100,2,59,3,44,55,63,65]

for i in range(len(list)):
    if list[i]==3:
        continue  #to skip below code go to next iteration
    elif list[i]==55:
        break
    print(f'loop {i} -  {list[i]}')
