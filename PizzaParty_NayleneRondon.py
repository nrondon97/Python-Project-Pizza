#------------------------------------------------------------------------------------------------------------------------
# Program name – PizzaParty_NayleneRondon.py
# Written by – Naylene Rondon
# Date Began– 03/13/17
# Project 3
# Introduction to Lists
#------------------------------------------------------------------------------------------------------------------------
import random

#Start
def main():
    intro()
    print("Before we continue, make sure you mark a seat for yourself.")
    userName = input("What's your name? ")
    print("Great! Now, let's work out who's being invited.")
    guests = guestList(8)
    guests.append(userName)
    invite(guests)
    guests = cancel(guests)
    guests = LargeTable(guests)
    toppings = pizza()
    topping = pizzachange(guests, toppings)

    print("\n\nHooray! You had a great party.")
    

def intro():
    print("Busy, Busy, Busy, isn't it. You have all your favorite people")
    print("coming over. You have to work hard and make it perfect so it")
    print("doesn't end up like Macbeth's dinner.")

def guestList(number):
    G_list = []
    counter = int(0)
    while counter < number:
        name = input("Who are you inviting to the party? ")
        G_list.append(name)
        counter = counter + 1

    return G_list

def invite(G_List):
    for g in G_List :
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
              "\n  Dear " + g + ",                " +
              "\n        You are invited          " +
              "\n        to a delicious           " +
              "\n          pizza party!           " +
              "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def cancel(G_List):
    numb = int(len(G_List))
    cancelled = random.randint(0,numb-1)
    print("\n Oh no! " + G_List[cancelled] + " can't make it.")
    print("We can't leave the seat empty.")
    G_List[cancelled] = input("\n Who do you want to invite to take their place? ")

    invite(G_List)

    return G_List
    
def LargeTable(G_List):
    print("Hooray! You found a larger table!")
    print("This tables gives you three extra seats.")
    print("So invite three more people!")

    name = input("Who are you inviting to the party? ")
    G_List.insert(0, name)
    name = input("Who are you inviting to the party? ")
    G_List.insert(6, name)
    name = input("Who are you inviting to the party? ")
    G_List.append(name)

        
    invite(G_List)
    return G_List
    
def pizza():
    print("Now it is time to get the pizza. We should have three toppings")
    print("for three different pizzas.")
    Pizza = []
    counter = int(0)
    while counter < 3:
        topping = input("Name a topping: ")
        Pizza.append(topping)
        counter = counter + 1
    print("The toppings are: ")
    for p in Pizza:
        print(p)

    return Pizza

def pizzachange(G_List, pizza):
    numb = int(len(G_List))
    change = random.randint(0,numb-1)
    print(G_List[change] + " wants to add a pizza to the list.")
    print("Tey think there's not enough.")
    topping = input("Name another topping: ")
    pizza.append(topping)

    print("The updated toppings are: ")
    for p in pizza:
        print(p)

        
    return pizza
    

main()

#End
