import math 
import time 

print ("\n Welcome to the MYSTERY DIARIES........\n")

name = input("Enter your name : ")

print (f"\n Welcome Dr. {name} !!")

print ("\n\n----- A Murder Was Occured at birmingham high Library......")

def menu():
    print("\n--- Options ---")
    print("\n1. Examine body ")
    print("\n2. Search Library ")

    print("\n3. Questions Suspects ")
    menu = int(input("\nChoose the no. to continue : "))

    if menu == 1:
        victim()
    elif menu == 2:
        library()
    elif menu == 3:
        suspect()

    else:
        print("\n Option not found ")
        return menu
    
def menu1():
    print("\n--- Options ---\n")
    print("1. Examin body")
    print("\n2. Search library\n")

    print("3. Question the suspects.")
    print("\n4. Announce the culprit..")

    choice = int(input("\n Choose the no. to cotinue : "))

    if choice == 1:
        pass
    elif choice == 2:
        library()
    elif choice == 3:
        suspect()
    elif choice == 4:
        final()

    else :
        print("\nOption not found. Enter a proper number.. \n")
        time.sleep(2)
        menu1()
def setting():
    print ("\n\n ---- Crime Scene ----")
    print("\n Year: 1987\n")
    time.sleep(2)
    print(" Location: Blackwood manor! an old mansion isolated in apalachians mounutians.. \n")
    time.sleep(2)

    print(" A storm has knocked. out the phone lines and everyone inside is trapped for a night .\n")
    time.sleep(2)
    print(" At 11:47, milliomaire business man Edward blackwood found dead in his libraby ")
    time.sleep(2)
    print("\nThe doors are locked.. ")
    time.sleep(2)

    print("\nNo One can leave...")
    time.sleep(2)
    
    print("\nMurderer is still inside the Manor...")
    time.sleep(2)
    menu()

def final():
    print("\n--- Reveal the Culprit ---\n")

    print("1. Emily harris")
    print("\n2. Michael Stone")

    print("\n3. James Carter")
    print("\n4. Sarah blackwood")

    choice = int(input("\nChoose the murderer (number) : "))
    if choice == 1:
        print("\nWrong person . Murderer escaped")
        print("\n Mission failed")
        time.sleep(2)
        print("\n--- Game End -- ")

    elif choice == 2:
        print("\nFound it ")
        time.sleep(2)
        print("\n How that bastard making calls when phone lines are cut\n")
        time.sleep(2)
        print("\n---- Game finished ---")

    elif choice == 3:
        print("\n Wrong person")
        time.sleep(2)
        print("\nKiller escaped\n")
        time.sleep(2)
        print("--- Game end ---")
    elif choice == 4:
        print("\nWrong person")
        time.sleep(2)
        print("\nKiller expscaped the mansion \n")
        time.sleep(2)
        print("--- Game End ---")

    else:
        print("\n Option not found try again with proper no.")
        time.sleep(3)
        final()

    


def library():
    print("\n--- Crime Scene ---\n")
    print("Blood is everywhere \n")

    print("There is Knife without fingerprints . cleaned")

    print("\nEdward's dead body ")

    time.sleep(5)
    menu()
def victim():
    print("\n--- VICTIM ---")

    print("\n>>> Edward Blackwood ")
    print("\nAge : 68")

    print("\nOwner of Blackwood Industries")

    print("\nKnown for rich, secretive adn hated by Many..")
    print("\nCause of Death : @ Stab wound")

    choose = str(input("\n return to menu (y/n) : "))
    if choose == "y":
        menu()
    else :
        print("\n Enter a proper answer ")
        time.sleep(3)
        victim()



def emily():
    print("\n>>> Emily Harris \n")

    print ("Aeg : 44")
    print("\nQuiet and Observant..")
     
    print("\n>> Secret : She Overheard something important")

    print("\n>> Alibi : Claims she was cleaning the kitchen ...")
    
    main = input("return to options (y/n) : ")

    if main == "y":
        menu1()
    

def james():
    print("\n>>> James Carter <<<")
    print("\nAge : 59")
    print("\nWorked for the family for 30 years")

    print("\nKnown to be loyal")

    print("\n>> Secret : Edward was planning to fire him")
    print("\n>> Alibi : Claims he was making tea.")

    main = str(input("return to the menu? (y/n) : "))

    if main == "y":
        menu1()

def sarah():
    print("\n>>> Sarah Blackwood (Daugther) <<<")

    print("\nDeeply in debt ")
    print("\n Recently got a heated argument with his dad(Victim)")

    print("\n>> Secret : Edward changed his will and removed her from his inheritance ...")
    print("\n>> Alibi : Claims she was in her bedroom.")
    main =str(input("return to the menu? (y/n) : "))
    if main== "y":
        menu1()
def michael():
    print("\n >>> Michael Stone <<<")
    print("\nAge : 52")

    print("\nCo-Founder of the company..")

    print("\n>> Secret : Edward discovered michael had stolen millions..\n")
    print(">> Alibi : Claims he was making phone calls..")

    main = str(input("\n return to the menu? (y/n) : "))
    if main == "y" :
         menu1()
    



def suspect():
    print("\n--- SUSPECTS --- \n")

    print("1. James Carter (butler)\n")
    print("2. Sarah Blackwood \n")

    print("3. Michael Stone  \n")

    print("4. Emily Harris \n")

    choice_sus = int(input("Select suspect to investigate (no.) : "))

    if choice_sus == 1:
        james()

    elif choice_sus == 2:
        sarah()
    elif choice_sus == 3:
        michael()

    elif choice_sus == 4:
        emily()


    else:
        print ("\n Error finding Suspect . Choose the proper number. ")
        time.sleep(1)
        return suspect()


    

setting()





