# Challenge: Write a python function that generates all even numbers from 1 to a given number n (inclusive).
# n=10

def generate_even_numbers(n):
    even_numbers = []
    for i in range(1,n):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(generate_even_numbers(10))