from time import time


def factorial(num: int) -> int:
    if num == 0: 
        return 1
    return num * factorial(num - 1)


num = int(input("Enter an integer you would like to know the factorial of: "))

start_time = time( ) # record the starting time

print(f"{num}! is equal to {factorial(num)}")

end_time = time( ) # record the ending time

elapsed = round(end_time - start_time, 6)
print(f"The algorithm took {elapsed}s to run in total time.")
