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

def how_much_water(bricks_array: list) -> int:

    water_bricks_array = []

# find the first non-zero element
    for index, element in enumerate(bricks_array):

        if element != 0:
            index_start = index
            print(f"index_start: {index_start}")
            break
        else:
            print("All elements are 0")

# find the last non-zero element
    for index in range(len(bricks_array) -1, -1, -1):

        if bricks_array[index] != 0:
            index_end = index
            print(f"index_end: {index_end}")
            break

        else:
            print("All elements are 0")

# find the maximum element and amount
    element_max = max(set(bricks_array))
    count_max = bricks_array.count(element_max)
    print(f"element_max: {element_max}; count_max: {count_max}")

    if count_max == 1 and bricks_array.index(element_max) != 0 and bricks_array.index(element_max) != len(bricks_array) - 2:
        bricks_array.remove(element_max)
        print(type(bricks_array))
        print(bricks_array)

    for index, element in enumerate(bricks_array):
# FEHLERHAFT: sicherstellen, dass nicht beim falschen index weiter gemacht wird
        if index > len(water_bricks_array):
            break
# iterate over the elements, starting from the first non-zero element
        elif index >= index_start and index < len(bricks_array) - 1:
            if element >= bricks_array[index+1]:
                print(f"index: {index}; element: {element} > element + 1: {bricks_array[index+1]}")

                element_local_max = max(set(bricks_array[index+1:]))

                if element <= element_local_max:
                    print(f"element ({element}) <= max local ({element_local_max})")

                    index_local_max = index + 1 + bricks_array[index+1:].index(element_local_max)

                    for sub_index in range(index + 1, index_local_max + 1):
                        print(f"sub_index: {sub_index}, element: {bricks_array[sub_index]}")

                        if bricks_array[sub_index] <= bricks_array[index] and len(water_bricks_array) < len(bricks_array) - 1:
                            water_bricks_array.append(bricks_array[index] - bricks_array[sub_index])
                            print(f"added to water_bricks_array: {water_bricks_array}")

                elif element > element_local_max and element_local_max == bricks_array[index_end]:
                    print(f"element ({element}) > max local ({element_local_max}); end_element: {bricks_array[index_end]}")

                    for sub_index in range(index + 1, index_end + 1):
                        print(f"sub_index: {sub_index}, element: {bricks_array[sub_index]}")

                        if bricks_array[sub_index] <= bricks_array[index_end] and len(water_bricks_array) < len(bricks_array) - 1:
                            water_bricks_array.append(bricks_array[index_end] - bricks_array[sub_index])
                            print(f"added to water_bricks_array: {water_bricks_array}")


            elif index >= index_start and element < bricks_array[index+1]:
                print(f"{bricks_array[index]} < {bricks_array[index+1]}")

    return sum(water_bricks_array)

print(how_much_water(bricksArray11))

