bricksArray1 = [2, 0, 2]
bricksArray2 = [1, 0, 2, 1]
bricksArray3 = [2, 0, 3, 0, 4]
bricksArray4 = [4, 0, 1, 4, 2, 4]
bricksArray5 = [4, 1, 0, 4, 2, 4]
bricksArray6 = [3, 3, 0, 1, 3]
bricksArray7 = [3, 4, 2, 3, 0, 3, 2, 0, 0, 0, 3, 0, 3]
bricksArray8 = [7, 0, 3, 1, 6, 7]


def how_much_water(bricks_array: list) -> int:

    water_bricks_array = []
    index = 0

    for element in bricks_array:
        print("element:", element)
        if index < len(bricks_array) - 1:
            print(f"index: {index}")

            if element > bricks_array[index+1]:
                print(f"element: {element} > element + 1: {bricks_array[index+1]}")

                if bricks_array[index] <= max(set(bricks_array[index+1:])):
                    print(f"element: {bricks_array[index]} <= max(set(bricks_array[index+1:])): {max(set(bricks_array[index+1:]))}")

                    index_max_local = index + 1 + bricks_array[index+1:].index(max(set(bricks_array[index+1:])))
                    print(f"index_max_local: {index_max_local}")

                    water_bricks_array.append(bricks_array[index_max_local] - bricks_array[index])
                    index += 1
                    print(f"added to water_bricks_array: {water_bricks_array}")

                else:
                    index += 1


            elif bricks_array[index] > max(set(bricks_array[index+1:])):
                print(f"{bricks_array[index]} > {max(set(bricks_array[index+1:]))}")
                if bricks_array[index+1] < bricks_array[index]:
                    water_bricks_array.append(max(bricks_array[index+1:]) - bricks_array[index+1])
                    index += 1
                    print(f"water_bricks_array: {water_bricks_array}")
                else:
                    index += 1


        else:
            index += 1


    amount_of_water_bricks = sum(water_bricks_array)
    return amount_of_water_bricks

print(how_much_water(bricksArray4))
