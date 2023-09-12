import sys
# Code Number One
print('Self Identification')
name = input('Enter your name:')
age = input('Enter your age:')
country = input('Country: ')
country = country.lower()
country_codes = {
    'america': '+1',
    'philippines': '+63',
    'united kingdom': '+44',
    'canada': '+1',
    'australia': '+61',
    'india': '+91',
    'germany': '+49',
    'france': '+33',
    'china': '+86',
    'japan': '+81',
    'brazil': '+55',
    'south korea': '+82',
    'spain': '+34',
    'italy': '+39',
    'mexico': '+52',
    'russia': '+7',
    'south africa': '+27',
    'egypt': '+20',
    'nigeria': '+234',
    'kenya': '+254',
    'argentina': '+54',
    'chile': '+56',
    'new zealand': '+64',
    'singapore': '+65',
    'malaysia': '+60',
    'thailand': '+66',
    'vietnam': '+84',
    'greece': '+30',
    'sweden': '+46',
    'norway': '+47',
    'denmark': '+45',
    'netherlands': '+31',
    'belgium': '+32',
    'switzerland': '+41',
    'austria': '+43',
    'poland': '+48',
    'turkey': '+90',
    'morocco': '+212',
    'tunisia': '+216',
    'saudi arabia': '+966',
    'uae': '+971',
    'qatar': '+974',
    'kuwait': '+965',
    'iran': '+98',
    'iraq': '+964',
    'syria': '+963',
    'lebanon': '+961',
    'jordan': '+962',
    'pakistan': '+92',
    'bangladesh': '+880',
    'sri lanka': '+94',
    'nepal': '+977',
    'bhutan': '+975',
    'afghanistan': '+93',
    'papua new guinea': '+675',
    'fiji': '+679',
    'new caledonia': '+687',
    'samoa': '+685',
    'tonga': '+676',
    'solomon islands': '+677',
    'vanuatu': '+678',
    'french guiana': '+594',
    'peru': '+51',
    'colombia': '+57',
    'venezuela': '+58',
    'ecuador': '+593',
    'bolivia': '+591',
    'paraguay': '+595',
    'uruguay': '+598',
    'costa rica': '+506',
    'panama': '+507',
    'honduras': '+504',
    'el salvador': '+503',
    'nicaragua': '+505',
    'guatemala': '+502',
    'belize': '+501',
    'jamaica': '+1',
    'haiti': '+509',
    'dominican republic': '+1',
    'cuba': '+53',
    'puerto rico': '+1',
    'bahamas': '+1',
    'trinidad and tobago': '+1',
    'barbados': '+1',
    'grenada': '+1',
    'saint lucia': '+1',
    'antigua and barbuda': '+1',
    'saint vincent and the grenadines': '+1',
    'dominica': '+1',
    'st. kitts and nevis': '+1',
    'aruba': '+297',
    'curacao': '+599',
    'bonaire': '+599',
    'suriname': '+597',
    'guyana': '+592',
    'french polynesia': '+689',
    'tahiti': '+689',
    'wallis and futuna': '+681',
    'palau': '+680',
    'marshall islands': '+692',
    'kiribati': '+686',
    'nauru': '+674',
    'tuvalu': '+688',
    'northern mariana islands': '+1',
    'guam': '+1',
    'american samoa': '+1',
    'cook islands': '+682',
    'niue': '+683',
    'tokelau': '+690',
    'pitcairn islands': '+872',
    'antarctica': '+672',
    'heard island and mcdonald islands': '+672',
    'norfolk island': '+672',
    'cocos islands': '+61',
    'christmas island': '+61',
    'australian antarctic territory': '+672',
}
countcode = country_codes.get(country, 'Undefined')
address = input('Please enter your current address:')
contact = int(input('Please enter your mobile number:' + countcode))
print('Hello ' + name + ', You are ' + age + ' years old ' + 'and currently residing at ' +
      address + ' and your contact number is ' + countcode + str(contact) + '.')
# Code Number two
print('Calculator')
while True:
    try:
        operation = input(
            'Select an operation'
            '\n1.Addition'
            '\n2.Subtraction'
            '\n3.Multiplication'
            '\n4.Division'
            '\nYour selection: ')

        if operation == '1':
            c1 = input(
                'Please put 2 if 2 digits and 3 if 3 digits \nYour Answer: ')
            if c1 == '2':
                x = input('Enter first number: ')
                y = input('Enter second number: ')
                sum1 = int(x) + int(y)
                print('The sum of ' + x + ' and ' +
                      y + ' is ' + str(sum1) + '.')
            elif c1 == '3':
                x = input('Enter first number: ')
                y = input('Enter second number: ')
                z = input('Enter third number: ')
                sum2 = int(x) + int(y) + int(z)
                print('The sum of ' + x + ', ' + y +
                      ' and ' + z + ' is ' + str(sum2) + '.')
            else:
                print("You've entered a wrong choice.")
        elif operation == '2':
            x = input('Enter first number: ')
            y = input('Enter second number: ')
            difference = int(x) - int(y)
            print('The difference of ' + x + ' and ' +
                  y + ' is ' + str(difference))
        elif operation == '3':
            x = input('Enter first number: ')
            y = input('Enter second number: ')
            product = int(x) * int(y)
            print('The product of ' + x + ' and ' + y + ' is ' + str(product))
        elif operation == '4':
            x = input('Enter first number: ')
            y = input('Enter second number: ')
            if y == '0':
                print("Division by zero is not allowed.")
            else:
                quotient = int(x) / int(y)
                print('The quotient of ' + x + ' and ' +
                      y + ' is ' + str(quotient))
        else:
            print("You've entered a wrong choice")

        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break  # Exit the loop if the user doesn't want to continue.
    except ValueError:
        print("Invalid input. Please enter valid numbers and choices.")
