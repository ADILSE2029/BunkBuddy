import module1 as m1
    ## main function
def main():
    bunkBuddy = m1.Bunkbuddy()
    bunkBuddy.decorator()
    print("\tBUNK BUDDY\t")
 

    while True:
        bunkBuddy.decorator()
        user_choice = input(
            "[M] Mark Attendence\n[A] Add Subject\n[V] View Details\n[R] Reset Data\n[W] Warnings\n[B] Bunk-o-Meter\n[Q] Quit\nChoice:").lower()
        
        if user_choice == "m":
            bunkBuddy.subject_selection()
        
        elif user_choice== "a":
            bunkBuddy.add_subject()

        elif user_choice == "v":
            bunkBuddy.view_details()

        elif user_choice == "r":
            bunkBuddy.reset_data()

        elif user_choice == "q":
            bunkBuddy.decorator()
            print("Thanks for using ")
            break

        elif user_choice == "w":
            bunkBuddy.warnings()

        elif user_choice == "b":
            bunkBuddy.bunkmeter()

        else:
            bunkBuddy.decorator()
            print("Invalid Input")


if __name__ == "__main__":
    main()
