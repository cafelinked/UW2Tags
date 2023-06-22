# UW2Tags
A CLI tool based on python3 to generate UWorld Anki Tags from UWorld Block Overview page.

# Setup
Make sure to change path to `input_file` and `output_file` prior to run.
Make sure you have installed the correct dependencies: `python3`

# Run
Open terminal
Type `python3 generate_tags.py`
Let the CLI do the work


https://github.com/cafelinked/UW2Tags/assets/106856406/91b96132-6f8f-4c94-983e-17fd8a412f75

# Using AnKing UWorld QID Add-on
You can do the following within the .py file: (v12 - if you use <v12, modify accordingly to your own AnKing version)
```
    # Define the prefix for the parent tags
      parent_tag_prefix = 'UWorld::'
      qid_parent_tag_prefix = 'AK_Step1_v12::'
      qid_prefix = '#UWorld::'
```
And then adjust the following:
```
            # Generate the tags
            id_tag = f'{parent_tag_prefix}QID::{id_suffix} '
            qid_parent_tag = f'{qid_parent_tag_prefix}{qid_prefix}{id_suffix} '
            subjects_tag = f'{parent_tag_prefix}Subject::{subjects} '
            systems_tag = f'{parent_tag_prefix}System::{systems} '
            categories_tag = f'{parent_tag_prefix}Category::{categories} '
            topics_tag = f'{parent_tag_prefix}Topic::{topics}\n\n'
```
This will add additonal tags for AnKing. 
```#AK_Step1_v12::#UWorld::XXXXXX```

If you wish to remove the ```UWorld::QID::XXXXXX``` tag, you may simply remove the ```id_tag``` line so no duplicate is created.

Rest of the code is as is.


# Known Issues
Fails to ignore the headers, and you will receive an error in terminal. Ignore this error.

# Errors?
Submit your errors in issues.
