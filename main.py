#Max and Leaf lab 4
#assignment due 11/7

#Goal of lab is to calculate monthly cost of users payment based on data used, the package type, and if they can use a coupon
package_type = input('Enter package type green, blue, or purple: ')
package_type = package_type.lower()
#sets values for the package types
if package_type == ('green'):
    monthly_payment = 49.99
    provided_data = 2
    extra_data = 15
elif package_type == ('blue'):
    monthly_payment = 70
    provided_data = 4
    extra_data = 10
elif package_type == ('purple'):
    monthly_payment = 99.95
else:
    print('Invalid package type: please pick either green, blue, or purple')

#calculates monthly cost for green and blue package type
if package_type == ('green') or package_type == ('blue'):
    used_data = input("enter amount of gigabytes used a month: ")
    used_data = int(used_data)
    data = used_data - provided_data
    if (data > 0):
        monthly_payment = (monthly_payment + (data * extra_data))

# checks if coupon is appliable and takes it into account if so applies it
if package_type == ('green') and monthly_payment >= 75:
    coupon = input('Do you have a coupon? yes or no: ')
    coupon = coupon.lower()
    if coupon == 'yes':
        monthly_payment = monthly_payment - 20
print(f'Your monthly payment is {monthly_payment:.2f} dollars.')

