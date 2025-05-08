# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it

def numberOfSteps(num: int) -> int:

    nr_of_steps = 0

    number = num

    while number > 0:
        if number % 2 == 0:
            number /= 2
            nr_of_steps += 1

        elif number % 2 != 0:
            number -= 1
            nr_of_steps += 1

    return nr_of_steps

print(numberOfSteps(123))
