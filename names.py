# Replace 'input_file.txt' with the path to your text file
input_file = './dataset_description.txt'
output_file = 'output_file.csv'

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Replace newlines with commas and write to output file
with open(output_file, 'w') as file:
    for line in lines:
        # Remove the newline character and add a comma
        file.write(line.strip() + ',')

print(f"Data has been processed and saved to {output_file}.")
