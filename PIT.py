retry = 0

while True:
    selection = input("Select your choice:\n1. Inches to Centimeters\n2. Centimeters to Inches\nYour Choice:")

    if selection == '1':
        inch_to_cm = 2.54
        inches = input("How many inches: ")
        try:
            inches = float(inches)
            conversion1 = inches * inch_to_cm
            print(f"{inches} inches is equal to {conversion1:.2f} centimeters.")
        except ValueError:
            print('Invalid input. Please enter a valid number for inches.')
            retry += 1
            if retry == 5:
                print("Maximum retries reached.\nProgram Ended")
                break
            continue

    elif selection == '2':
        cm_to_inch = 0.3937
        centimeters = input("How many centimeters: ")
        try:
            centimeters = float(centimeters)
            conversion2 = centimeters * cm_to_inch
            print(f"{centimeters} centimeters is equal to {conversion2:.2f} inches.")
        except ValueError:
            print('Invalid input. Please enter a valid number for centimeters.')
            retry += 1
            if retry == 5:
                print("Maximum retries reached.\nProgram Ended")
                break
        continue

    else:
        print('Invalid Selection. Please choose 1 or 2.')
        retry += 1
        if retry == 5:
            print("Maximum retries reached.\nProgram Ended")
            break
        continue

    again = input("Do you want to convert again? (yes/no): ").lower()

    if again == 'yes':
        continue
    elif again == 'no':
        break
    else:
        print('Invalid Selection. Considered as NO.')
        break
