#laptop price on brand

brand= input("Enter the laptop brand: ") .upper()
if brand == "Toshiba".upper():
    print("The price of {} is 80 Doller".format(brand))
elif brand == "HP15".upper():
    print("The price of {} is 210 Dollar")
elif brand == "Tablet".upper():
     print("The price of {} is 90 Doller".format(brand))
elif brand == " HP15 Notebook".upper():
     print("The price of {} is 100 Doller".format(brand))
elif brand == "Apple MacBook Air".upper():
     print("The price of {} is 120 Doller".format(brand))
elif brand == "MacBook Pro".upper():
     print("The price of {} is 20 Doller".format(brand))
elif brand == "HP Spectre x360".upper():
     print("The price of {} is 220 Doller".format(brand))
elif brand == "Newest HP Envy".upper():
      print("The price of {} is 300 Doller".format(brand))

else:
    print('Sorry! We do not have the product you are looking for')
    print('These are the available laptops: Toshiba, HP15, Tablet, HP15 Notebook, Apple MacBook Air, MacBook Pro, HP Spectre x360 and HP Envy')
    
# program to find biggest of tow numbers
    
    num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
if num1>num2:
    print('{} is greater than {}'.format(num1,num2))
elif num1<num2:
    print('{} is greater than {}'.format(num2,num1))
else:
    print(num1 == num2)

    # Program to check whether given number is in between 1 & 90

a = int(input('Enter a number in the ranger of 1-90: '))
if a in range(0,91):
    print('{} is present'.format(a))
else:
    print('The number is not in the specified range')
