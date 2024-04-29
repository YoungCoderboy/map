import csv

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = './abc.csv'
output_text_file_path = 'D://Code-Arena//js-samples//output.txt'  # Changed to '.txt' for plain text

# Open the CSV file for reading
with open(csv_file_path, 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)
  output_data = []  # List to store processed data

  # Iterate over each row in the CSV file
  for row in csv_reader:
    # Process each row as needed
      # Assuming longitude is in the second column
    processed_data = f'new google.maps.LatLng({row[0]}, {row[1]}),'
    output_data.append(processed_data)

# Open the output text file for writing (plain text)
with open(output_text_file_path, 'w') as output_file:
  # Write each processed data point to the file with a newline character
  for line in output_data:
    output_file.write(line + "\n")

print(f"Processed data written to: {output_text_file_path}")
