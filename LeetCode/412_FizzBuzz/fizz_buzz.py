def fizzBuzz(n: int) -> list[str]:

    solution_array = []

    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            solution_array.append("FizzBuzz")
        elif num % 3 == 0:
            solution_array.append("Fizz")
        elif num % 5 == 0:
            solution_array.append("Buzz")
        else:
            solution_array.append(str(num))

    return solution_array

print(fizzBuzz(15))