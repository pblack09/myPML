import pandas as pd
data_file = 'music_library.csv'
df = pd.read_csv(data_file)

    # Approximate rubric for difficulty scale
ability_rubric = """
Approximations based on (TX - UIL) 5A/6A and 2C/3C classifications:
10: Top-level HS Varsity
9:  Very strong HS Varsity
8:  Average HS Varsity
7:  Very strong HS Non-Varsity
6:  Average HS Non-Varsity
5:  Top-level MS Varsity
4:  Average HS Sub Non-Varsity
3:  Average MS Non-Varsity
2:  Average MS Sub Non-Varsity
1:  Early MS Sub Non-Varsity
"""

    # User enters their search criteria

# Search for Title:
title = input("What piece are you searching for? ")
given_title = title.lower()

# Search for Grade Level:
print("What grade level are you searching for?")
grade_request = input()
    if grade_request == "":
        given_grade = [1, 2, 3, 4, 5]
    else:
        given_grade = [int(grade_request)]

# Search for Difficulty:
print(ability_rubric)
print("What difficulty are you searching for?")
total_request = input()
    if total_request == "":
        given_total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    else:
        given_total = [int(total_request)]

# Search for Composer/Arranger
name = input("Which composer/arranger are you searching for? ")
given_name = name.lower()

    # Perform search function
    
df[(df['Title'].str.lower().str.contains(given_title)) & (df['Grade'].isin(given_grade)) & (df['Total'].isin(given_total)) & (df['Composer'].str.lower().str.contains(given_name) | df['Arranger'].str.lower().str.contains(given_name))]