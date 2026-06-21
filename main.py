import math 

print ("\n Welcome to the MYSTERY DIARIES........\n")

name = input("Enter your name : ")

print (f"\n Welcome Dr. {name} !!")

print ("\n\n----- A Murder Was Occured at birmingham high Library......")


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

    print("\n>>> Edward Blackwood")
    print("\nAge : 68")

    print("\nOwner of Blackwood Industries")

    print("\nKnown for rich, secretive adn hated by Many..")
    print("\nCause of Death : @ Stab wound")

def emily():
    print(">>> Emily Harris \n")

    print ("Aeg : 44")

def james():
    pass

def sarah():
    pass

def michael():
    pass


def suspect():
    print("\n--- SUSPECTS --- \n")

    print("1. James Carter (butler)\n")
    print("2. Sarah Blackwood \n")

    print("3. Michael Stone  \n")

    print("4. Emily Harris \n")
    choice_sus = input("Select suspect to investigate (no.) : ")

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
        time.sleep(1s)
        return suspect()


    

setting()

victim()
suspect()


