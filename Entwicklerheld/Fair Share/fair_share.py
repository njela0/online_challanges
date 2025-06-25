def sum_up_payments(csv_filename):
    """Takes input from csv file and returns a dictionary with the total and parts per person and a variable containing the number of participants"""
    shares_dict = {}
    total_payment = 0
    number_of_participants = 0

    with open(csv_filename, "r") as data:

        for line in data:
            entry = line.strip("\n").strip('"').split(';')
            entry[2] = float(entry[2])
            total_payment += entry[2]

            if entry[1] not in shares_dict.keys():
                shares_dict[entry[1]] = entry[2]
                number_of_participants += 1
            else:
                shares_dict[entry[1]] += entry[2]

    return shares_dict, total_payment, number_of_participants


def calculate_shares(shares_dict, total_payment, number_of_participants):
    shares_list = []

    for key, value in shares_dict.items():
        person_shares_dict = {}
        person_shares_dict["people"] = key
        person_shares_dict["total"] = value
        person_shares_dict["refund"] = round(((total_payment / number_of_participants) - value), 2)
        shares_list.append(person_shares_dict)

    return shares_list

csv_filename = "data-1-1.csv"
shares_dict, total, number_of_participants = sum_up_payments(csv_filename)

print(number_of_participants)
for key, value in shares_dict.items():
    print(key, value)

shares_list = calculate_shares(shares_dict, total, number_of_participants)

print(shares_list)