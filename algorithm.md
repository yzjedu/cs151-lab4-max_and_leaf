# Algorithm Document

1. Request package type from user (Green, Blue, or Purple) 
2. convert to lowercase
3. While the package is not currently set to green, blue, or purple, run through steps 4-7
4. If package is green: 
   1. set monthly payment to 49.99
   2. set provided data to 2
   3. set cost of each extra data to 15
5. Otherwise, if package is blue
    1. set monthly payment to 70
    2. set provided data to 4
    3. set cost of extra data to 10
6. Otherwise, if package is purple
    1. set monthly payment to 99.95
   2. you do not need to define provided data or cost of extra data
7. Otherwise, output an error message, telling the user to input specifically green, blue, or purple
8. if the selected package is green OR blue
    1. request the amount of used data expressed in gigabytes from the user 
   2. calculate the difference between the used data and the provided data
   3. if the difference is greater than 0
   4. set the monthly payment to (monthly payment + (difference * cost of extra data))
9. if the package is green AND monthly payment is greater than or equal to 75
   1. Request a yes or no response from the user as to whether or not they have a coupon
   2. if response is yes subtract 20 from monthly payment
10. output monthly payment
      
      
    