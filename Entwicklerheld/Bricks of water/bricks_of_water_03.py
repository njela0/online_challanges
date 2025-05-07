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

    # find the first non-zero element
    for index, element in enumerate(bricks_array):

        if element != 0:
            index_start = index
            print(f"index_start: {index_start}")
            break
        else:
            print(f"index: {index} - element: {element}")

    # find the last relevant element
    for index in range(len(bricks_array) - 1, -1, -1):

        if bricks_array[index] != 0:
            index_end = index
            print(f"index_end: {index_end}")
            break

        else:
            print(f"index: {index} - element: {bricks_array[index]}")

    # slice the array (in case start/end is smaller than the following/reverse following element)
    bricks_array_prepared = bricks_array[index_start:index_end+1]
    print("bricks_array_prepared:", bricks_array_prepared)

    # find the maximum wall-height
    list_set_values_sorted = sorted(list(set(bricks_array_prepared)), reverse=True)
    print(f"list_set_values_sorted: {list_set_values_sorted}")

    for value in list_set_values_sorted:
        count = bricks_array_prepared.count(value)
        print(f"value: {value}; count: {count}")

        if count > 1:
            max_wall_height = value
            print(f"max_wall_height: {max_wall_height}")
            break

    # check if max-walls are on the outside
    if bricks_array_prepared[0] == max_wall_height and bricks_array_prepared[-1] == max_wall_height:
        print("max-walls are on the outside")
        for element in bricks_array_prepared:
            water_bricks_array.append(max_wall_height - element)

    else: # if walls are on the inside
        print("max-walls are on the inside")
        # find the heights of the outer walls
        left_wall_height = bricks_array_prepared[0]
        right_wall_height = bricks_array_prepared[-1]
        index_start_middle = 0
        index_end_middle = 0

        # amount of water for the elements on the left
        for index, element in enumerate(bricks_array_prepared):
            if element < max_wall_height:
                water_bricks_array.append(left_wall_height - element)
                print(f"water_bricks_array: {water_bricks_array}")
            else:
                index_start_middle = index
                print(f"index_start_middle: {index_start_middle}")
                break

        # amount of water for the elements on the right
        for index in range(len(bricks_array_prepared) - 1, -1, -1):
            if bricks_array_prepared[index] < max_wall_height:
                water_bricks_array.append(right_wall_height - bricks_array_prepared[index])
                print(f"water_bricks_array: {water_bricks_array}")
            else:
                index_end_middle = index
                print(f"index_end_middle: {index_end_middle}")
                break

        # amount of water for the middle part
        for index, element in enumerate(bricks_array_prepared):
            if index >= index_start_middle and index < index_end_middle:
                water_bricks_array.append(max_wall_height - element)
                print(f"water_bricks_array: {water_bricks_array}")


    print(f"water_bricks_array: {water_bricks_array}")
    amount_of_water_bricks = sum([x for x in water_bricks_array if x > 0])
    return amount_of_water_bricks

print(how_much_water(bricksArray14))