def sum_up_payments(csv_filename):
    people_dict = {}
    amount_of_activities = 0
    with open(csv_filename, "r") as data:

        for line in data:
            amount_of_activities += 1
            entry = line.strip("\n").strip('"').split(';')
            entry[2] = float(entry[2])

            if entry[1] not in people_dict.values():
                people_dict["person"] = entry[1]
                people_dict["total"] = entry[2]
                people_dict["refund"] = 1

            else:
                people_dict["total"] += entry[2]
                people_dict["refund"] += 1

    return people_dict, amount_of_activities


def calculate_shares(people_dict, amount_of_activities):
    pass

csv_filename = "data-1-1.csv"
people_dict, amount_of_activities = sum_up_payments(csv_filename)

print(amount_of_activities)
for key, value in people_dict.items():
    print(key, value)

if [154.0, 4] in people_dict.values():
    print("No more shares")
