import pandas as pd
excel_file = 'music_library.xlsx'


                    # Welcome to myPML!
            # My name is Philip Black and thank you for checking
            # out my program. I hope this is useful to you in
            # some manner.

            # Please let me know if there's anything I can do
            # to help make your experience with this program
            # any better.
                    # Thank you!


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

    # Assign each grade level sheet to a variable
all_grades = pd.read_excel(excel_file)
grade_1 = pd.read_excel(excel_file, sheet_name=1)
grade_2 = pd.read_excel(excel_file, sheet_name=2)
grade_3 = pd.read_excel(excel_file, sheet_name=3)
grade_4 = pd.read_excel(excel_file, sheet_name=4)
grade_5 = pd.read_excel(excel_file, sheet_name=5)



    # Take the search criteria and tell which classes to activate
class Search(object):

    def __init__(self, title, grade, difficulty, composer):
        self.title = title
        self.grade = grade
        self.difficulty = difficulty
        self.composer = composer

    def user_search(self):
        if self.title == 1:
            Title.search()

        if self.grade == 1:
            Grade.search()

        if self.difficulty == 1:
            Difficulty.search()

        if self.composer == 1:
            Composer.search()

        else:
            print(all_grades)
            # Return entire spreadsheet



class Title(Search):

    def search():
        search_title = input("What piece are you looking for? ")
        user_title = (all_grades['Title'].str.lower().str.contains(search_title))
        print (all_grades[user_title])



class Grade(Search):

    def search():
        given_grade = input("What grade level are you searching for? ")
        if given_grade == "1":
            print(grade_1)
        elif given_grade == "2":
            print(grade_2)
        elif given_grade == "3":
            print(grade_3)
        elif given_grade == "4":
            print(grade_4)
        elif given_grade == "5":
            print(grade_5)
        else:
            print("I don't understand that grade level.")
            Grade.search()



class Difficulty(Search):

    def search():
        print(ability_rubric)
        given_total = input("What is your ensemble's overall ability level? ")
        diff_search = (all_grades['Total'] == given_total)
        print (all_grades[diff_search])
        # if only difficulty given:
            # search all sheets for difficulty
        # if grade and difficulty given:
            # search grade_? for difficulty



class Composer(Search):

    def search():
        name = input("Which composers/arrangers are you looking for? ")
        comp_search = (all_grades['Composer'].str.lower().str.contains(name) | (all_grades['Arranger'].str.lower().str.contains(name)))
        print (all_grades[comp_search])



    # User enters their search criteria
search_1 = input("Are you searching for a specific piece? ")
if search_1.lower() == "yes":
    title = 1
else:
    title = 0

search_2 = input("Are you searching for a specific grade level? ")
if search_2.lower() == "yes":
    grade = 1
else:
    grade = 0

search_3 = input("Are you searching for a specific difficulty? ")
if search_3.lower() == "yes":
    difficulty = 1
else:
    difficulty = 0

search_4 = input("Are you searching for a specific composer or arranger? ")
if search_4.lower() == "yes":
    composer = 1
else:
    composer = 0



    # User's search criteria submitted through class Search
prompt = Search(title, grade, difficulty, composer)
prompt.user_search()
