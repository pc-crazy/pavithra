import csv


def write_processed_data(user_data, file_name="user_totals.csv", ):
    data = [["user_id", "total_amount"]]
    for key, value in user_data.items():
        data.append([key, value])
    with open(file_name, 'w') as csv_reader:
        writer = csv.writer(csv_reader)
        writer.writerows(data)


def process_csv(file_name=""):
    result_data = {}
    with open(file_name, 'r') as csv_reader:
        reader = csv.reader(csv_reader)
        for x in reader:
            user_id = x[1]
            amount = x[2]

            if user_id and amount and amount.isdigit():

                if user_id in result_data:
                    result_data[user_id] = result_data[user_id] + int(amount)
                else:
                    result_data[user_id] = int(amount)
    return result_data


response = process_csv("paras.csv")
write_processed_data(response)
