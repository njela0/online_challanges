bricksArray1 = [2, 0, 2]
bricksArray2 = [1, 0, 2, 1]
bricksArray3 = [2, 0, 3, 0, 4]
bricksArray4 = [4, 0, 1, 4, 2, 4]
bricksArray5 = [4, 1, 0, 4, 2, 4]
bricksArray6 = [3, 3, 0, 1, 3]
bricksArray7 = [3, 4, 2, 3, 0, 3, 2, 0, 0, 0, 3, 0, 3]
bricksArray8 = [7, 0, 3, 1, 6, 7]
bricksArray9 = [2, 0, 3, 0, 2]
bricksArray10 = [4, 0, 3, 4, 1, 7, 4, 4, 2, 4]
bricksArray11 = [3, 2, 3, 0, 3, 2, 0, 0, 0, 3, 0, 3]
bricksArray12 = [0, 0, 1, 3, 2, 3, 0, 3, 2, 0, 0, 0, 3, 0]
bricksArray13 = [0, 0, 1, 3, 2, 3, 0, 3, 2, 0, 0, 0, 3, 1, 0]
bricksArray14 = [0, 0, 1, 0, 3, 2, 3, 0, 3, 2, 0, 0, 0, 3, 1, 0]

def how_much_water(bricks_array: list) -> int:

    water_bricks_array = []

    print("bricks_array:", bricks_array)

    # find the first relevant element
    for index, element in enumerate(bricks_array):

        if element > bricks_array[index+1]:
            index_start = index
            print(f"index_start: {index_start}")
            break
        else:
            print(f"index: {index} - element: {element}")

    # find the last relevant element
    for index in range(len(bricks_array) - 1, -1, -1):

        if bricks_array[index] > bricks_array[index-1]:
            index_end = index
            print(f"index_end: {index_end}")
            break

        else:
            print(f"index: {index} - element: {bricks_array[index]}")

    # slice the array (in case start/end is smaller than the following/reverse following element)
    bricks_array_prepared = bricks_array[index_start:index_end+1]
    print("bricks_array_prepared:", bricks_array_prepared)

    # count amounts of water
    index = 0

    for element in bricks_array_prepared:

        while index < len(bricks_array_prepared) -1 and element >= bricks_array_prepared[index+1]:
            if element <= max(bricks_array_prepared[index+1:]):
                water_bricks_array.append(element - bricks_array_prepared[index+1])
                index += 1
                print(f"added to water_bricks_array: {water_bricks_array}")
            elif element > max(bricks_array_prepared[index+1:]):
                water_bricks_array.append(max(bricks_array_prepared[index+1:]) - bricks_array_prepared[index+1])
                index += 1
                print(f"added to water_bricks_array: {water_bricks_array}")

        else:
            continue


    print(f"water_bricks_array: {water_bricks_array}")
    amount_of_water_bricks = sum([x for x in water_bricks_array if x > 0])
    return amount_of_water_bricks

print(how_much_water(bricksArray9))