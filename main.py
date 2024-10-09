#Max and Leaf lab 4
#assignment due 11/7

#Goal of lab is to calculate monthly cost of users payment based on data used, the package type, and if they can use a coupon
passthru1 = "no"
passthru2 = "no"
package_type = input('Enter package type green, blue, or purple: ')
package_type = package_type.lower()
#sets values for the package types
while passthru1 == "no":
    if package_type == ('green'):
        passthru1 = "yes"
        monthly_payment = 49.99
        provided_data = 2
        extra_data = 15
    elif package_type == ('blue'):
        passthru1 = "yes"
        monthly_payment = 70
        provided_data = 4
        extra_data = 10
    elif package_type == ('purple'):
        passthru1 = "yes"
        monthly_payment = 99.95
    else:
        print('Invalid package type. please pick either green, blue, or purple')

#calculates monthly cost for green and blue package type
if package_type == ('green') or package_type == ('blue'):
    used_data = float(input("enter amount of gigabytes used this month: "))
    data_difference = used_data - provided_data
    if (data_difference > 0):
        monthly_payment = (monthly_payment + (data_difference * extra_data))

# checks if coupon is appliable and takes it into account if so applies it

if package_type == ('green') and monthly_payment >= 75:
    while passthru2 == "no":
        coupon_boolean = str.lower(input('Do you have a coupon? yes or no: '))
        if coupon_boolean == 'yes':
            passthru2 = "yes"
            monthly_payment = monthly_payment - 20
        elif coupon_boolean == 'no':
            passthru2 = "yes"
        else:
            print("This is an invalid input. Please put in 'yes' or 'no' only")

print(f'Your monthly payment is {monthly_payment:.2f} dollars.')

