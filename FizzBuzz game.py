#Wou are going to write a program that automatically prints the solution to the FizzBuzz game.
#Rules
#Your program should print each number from 1 to 100 in turn.
#1. When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#2. When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#3. And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
