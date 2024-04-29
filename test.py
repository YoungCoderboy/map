import csv
import json
# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = './dog.csv'
output_txt_file_path = './output.json'
# Open the CSV file for reading
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    l = []
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Process each row as needed
        first = f'new google.maps.LatLng({row[0]},{row[1]})'
        final = first+","
        print(final)
        
        # Append the tuple to the list
        l.append(first)

with open(output_txt_file_path, 'w') as output_file:
    # Serialize the list to JSON and write to the output file
    json.dump(l, output_file)
# with open(csv_file_path, 'r') as file:
#     # Create a CSV reader object
#     csv_reader = csv.reader(file)
#     l = []
#     # Iterate over each row in the CSV file
#     for row in csv_reader:
#         # Process each row as needed
#         last_two_elements = tuple(map(float, row[1:]))
        
#         # Append the tuple to the list
#         l.append(last_two_elements)

# with open(output_txt_file_path, 'w') as output_file:
#     # Serialize the list to JSON and write to the output file
#     json.dump(l, output_file)
