import os

# Define the file paths (must be in .txt format)
input_file = '/home/md/Desktop/UW2Tags/table.txt'
output_file = '/home/md/Desktop/UW2Tags/tags.txt'

# Define the prefix for the parent tag (User dependent: can change to Step 1/Step 2/Step 3)
parent_tag_prefix = 'UWorld::'

# Open the input file for reading
with open(input_file, 'r') as file:
    # Read the content of the file
    content = file.readlines()

# Open the output file for writing
with open(output_file, 'w') as file:
    # Iterate over each line in the content, excluding the header row
    for line in content[1:]:
        # Split the line into columns
        columns = line.strip().split('\t')

        try:
            # Extract the required columns
            id_suffix = columns[0].split('-')[1].strip()
            subjects = columns[1].strip().replace(', ', '_').replace(' ', '_').replace('/', '_')
            systems = columns[2].strip().replace(', ', '_').replace(' ', '_').replace('/', '_')
            categories = columns[3].strip().replace(', ', '_').replace(' ', '_').replace('/', '_')
            topics = columns[4].strip().replace(', ', '_').replace(' ', '_').replace('/', '_')

            # Generate the tags
            id_tag = f'{parent_tag_prefix}QID::{id_suffix} '
            subjects_tag = f'{parent_tag_prefix}Subject::{subjects} '
            systems_tag = f'{parent_tag_prefix}System::{systems} '
            categories_tag = f'{parent_tag_prefix}Category::{categories} '
            topics_tag = f'{parent_tag_prefix}Topic::{topics}\n\n'

            # Write the tags to the output file
            file.write(id_tag)
            file.write(subjects_tag)
            file.write(systems_tag)
            file.write(categories_tag)
            file.write(topics_tag)
        except IndexError:
            print(f"Error processing line: {line}")

print(f'Tags generated and saved to {output_file}')

