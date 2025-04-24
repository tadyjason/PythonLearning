print("Script Starting")
def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: 
            print(i)
if __name__ == "__main__":
    # Prompt the user only when file is run directly
    n = int(input("Enter a number for FizzBuzz: "))
    fizzbuzz(n)
