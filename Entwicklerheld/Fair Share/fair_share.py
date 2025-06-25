def sum_up_payments(csv_filename):
    people_dict = {}
    amount_of_activities = 0
    with open(csv_filename, "r") as data:

        for line in data:
            amount_of_activities += 1
            entry = line.strip("\n").strip('"').split(';')
            entry[2] = float(entry[2])

            if entry[1] not in people_dict.keys():
                people_dict[entry[1]] = [entry[2], 1]
            else:
                people_dict[entry[1]][0] += entry[2]
                people_dict[entry[1]][1] += 1

    return people_dict, amount_of_activities


def calculate_shares(people_dict, amount_of_activities):
    pass

csv_filename = "data-1-1.csv"
people_dict, amount_of_activities = sum_up_payments(csv_filename)

print(amount_of_activities)
for key, value in people_dict.items():
    print(key, value)

