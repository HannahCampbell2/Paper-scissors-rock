#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      minim
#
# Created:     03/06/2021
# Copyright:   (c) minim 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def calculate (a, b):
    answer = a + b
    return answer
answer = calculate(5, 10)
print (answer)

friends = []
name = input("Enter your first friends name. Enter x if you have no friends :")
while name.lower() != "x":
    friends.append(name)
    name = input("Enter your next friends name. Enter x if you have no other friends :")
print("{}".format(friends))
for index in range(len(friends)):
  #  print("Friend",index+1, ": ",friends[index])
    print("Friend {} : {}".format(index+1,friends[index]))




food = []
food_list = input("Enter the first item on your shopping list. Enter x if you need nothing :")
while food_list.lower() != "x":
    food.append(food_list)
    food_list = input("Enter your next food. Enter x if you there's nothing else on your list :")
print("{}".format(food))
for index in range(len(food)):
  #  print("Friend",index+1, ": ",friends[index])
    print(" {}) {}".format(index+1,food[index]))



