def main():
    n = int(input("Please enter the value to start counting from:"))
    x = n - 1#to ensure the number entered by the user is included in the sum
    sum = 0
    z = int(input("Please enter the value to end counting:")) 
    y = z+1#to ensure the number entered by the user is included in the sum

    while (x<y):
        sum+=x
        
        x+=2#determines the increment of the sum as it goes through the loop
    
    print("The sum of values between 1 and 100 is:",sum)

main()