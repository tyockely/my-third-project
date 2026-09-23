while True:
    print("What did you get on the test?")

    choice = input("Enter your score (or type 'exit' to quit): ")
    if choice.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    elif choice.isdigit() and int(choice) > 80:
        print("Congratulations! You did great on the test!")
    elif choice.isdigit() and int(choice) > 60:
        print("Not bad! You passed the test.")
    elif choice.isdigit() and int(choice) >= 50:
        print("You passed, but there's room for improvement.")
    elif choice.isdigit() and int(choice) < 50:
        print("Study a bit more buddy")
    else:
        print("Invalid")
