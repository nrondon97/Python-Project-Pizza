#------------------------------------------------------------------------------------------------------------------------
# Program name – MoreGuests_NayleneRondon.py
# Written by – Naylene Rondon
# Date – 03/09/17
# Project 3
# Introduction to Lists
#------------------------------------------------------------------------------------------------------------------------
import time

#Start

def main():
    """Main function, calls all the other functions"""
    #Variables
    guests = ["William Shakespeare", "Edgar Allan Poe", "Katherine Johnson",
              "Jane Austen", "Benedict Cumberbatch", "Martin Freeman", "Mary Shelley"]
    #Call Functions
    invite(guests)

    guests = noAttend(guests)
    invite(guests)

    guests = table(guests)
    invite(guests)
    

def invite(guests):
    """Send out the invites to dinner, Part 1 of the project."""
    print("\n\nI am inviting " + str(len(guests)) + " people to dinner.")
    for guest in guests:
        print("\nDear " + guest.title() + ",")
        print("You have been invited to dinner.")
        time.sleep(2)

def noAttend(guests):
    """Will find and POP those who cannot attend, Part 2 of the project."""
    CantAttend = guests.pop(-2)
    NewGuy = "mads mikkelsen"

    print("\n" + CantAttend + " called and cancelled. However, " + NewGuy.title() + " called.")
    print("He's free that evening. I'll invite him.")

    guests.append(NewGuy)

    return guests

def table(guests):
    """Will add three more people, Part 3 of the project."""
    print("\nI have found a larger table. I can invite three more people.")
    person1 = "Carrie-Ann Moss"
    person2 = "Hugh dancy"
    person3 = "Carrie Fisher"

    guests.insert(0, person1)
    guests.insert(-4, person2)
    guests.append(person3)

    return guests
    

main()

#End
