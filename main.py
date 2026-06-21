import math 
import time 

print ("\n Welcome to the MYSTERY DIARIES........\n")

name = input("Enter your name : ")

print (f"\n Welcome Dr. {name} !!")

print ("\n\n----- A Murder Was Occured at birmingham high Library......")

def menu():
    print("\n1. Examine body ")
    print("\n2. Search Library ")

    print("\n3. Questions Suspects ")
    menu = int(input("\nChoose the no. to continue : "))

    if menu == 1:
        pass
    elif menu == 2:
        pass
    elif menu == 3:
        suspect()

    else:
        print("\n Option not found ")
        return menu
    

def setting():
    print ("\n\n ---- Crime Scene ----")
    print("\n Year: 1987\n")
    print(" Location: Blackwood manor! an old mansion isolated in apalachians mounutians.. \n")

    print(" A storm has knocked. out the phone lines and everyone inside is trapped for a night .\n")

    print(" At 11:47, milliomaire business man Edward blackwood found dead in his libraby ")
    print("\nThe doors are locked.. ")

    print("\nNo One can leave...")
    
    print("\nMurderer is still inside the Manor...")




def victim():
    print("\n--- VICTIM ---")

    print("\n>>> Edward Blackwood ")
    print("\nAge : 68")

    print("\nOwner of Blackwood Industries")

    print("\nKnown for rich, secretive adn hated by Many..")
    print("\nCause of Death : @ Stab wound")

def emily():
    print("\n>>> Emily Harris \n")

    print ("Aeg : 44")
    print("\nQuiet and Observant..")
     
    print("\n>> Secret : She Overheard something important")

    print("\n>> Alibi : Claims she was cleaning the kitchen ...")
    
    main = input("return to options (y/n) : ")

    if main == "y":
        menu()
    

def james():
    pass

def sarah():
    print("\n>>> Sarah Blackwood (Daugther) <<<")

    print("\nDeeply in debt ")
    print("\n Recently got a heated argument with his dad(Victim)")

    print("\>>")

def michael():
    print("\n >>> Michael Stone <<<")
    print("\nAge : 52")

    print("\nCo-Founder of the company..")

    print("\n>> Secret : Edward discovered michael had stolen millions..\n")
    print(">> Alibi : Claims he was making phone calls..")

    main = str(input("\n return to the menu? (y/n) : "))
    if main == "y" :
         menu()
    


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

victim()
menu()


