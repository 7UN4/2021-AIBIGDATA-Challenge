import csv
import json
import event_util

clear_data_list = []
csv_id_list = []
match_data_list = []

# Extract data from CSV file
with open('p0_SCENARIO_APT29_v1.0.1.csv', 'r') as file:
    csv_datas = csv.reader(file)
    for csv_data in csv_datas:
        clear_data_list.append(csv_data)
    del clear_data_list[0]

# Extract _id from extracted csv data
for clear_data in clear_data_list:
    if clear_data[5] != "":
        if '\n' in clear_data[5]:
            csv_id_list.extend(clear_data[5].split('\n'))
        else:
            csv_id_list.append(clear_data[5])

# Extract json file data && Find matched id's data
with open('p0_SCENARIO_APT29_v1.0.1.json', 'r') as file:
    json_data_list = json.loads(file.read())
    for json_data in json_data_list:
        for csv_id in csv_id_list:
            if json_data['_id'] == csv_id:
                match_data_list.append(json_data)

# Print match data
for match_data in match_data_list:
    print(match_data)

# Print match data's event string
for match_data in match_data_list:
    print(event_util.event_to_str(match_data['event_id']))