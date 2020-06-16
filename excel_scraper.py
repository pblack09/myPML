import pandas as pd
excel_file = '~/myPML/music_library.xlsx'
library = pd.read_excel(excel_file)


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
Approximations based on (TX - UIL) 5A/6A and 3C/2C classifications:
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
grade_1 = pd.read_excel(excel_file, sheet_name=1, index_col=2)
grade_2 = pd.read_excel(excel_file, sheet_name=2, index_col=2)
grade_3 = pd.read_excel(excel_file, sheet_name=3, index_col=2)
grade_4 = pd.read_excel(excel_file, sheet_name=4, index_col=2)
grade_5 = pd.read_excel(excel_file, sheet_name=5, index_col=2)



    # Take the search criteria and tell which classes to activate
class Search(object):
# ex) input() = user_search = Search(title, grade, difficulty, composer)
                                        # if variable is empty, then null
    def __init__(self, title, grade, difficulty, composer):
        self.title = title
        self.grade = grade
        self.difficulty = difficulty
        self.composer = composer

    def user_search():
        if not 0 in options:
            Title.search(self.title)
        if not 0 in options:
            Grade.search(self.grade)
        if not 0 in options:
            Difficulty.search(self.difficulty)
        if not 0 in option:
            Composer.search(self.composer)
        else:
            pass
            #return entire spreadsheet



class Title(Search):

    def search(title):
        pd.read_excel(excel_file, index_col=2)
        #search through all sheets (sheet_name = 0)
        #search through title column (index_col = 2)


class Grade(Search):

    def search(grade):
        given_grade = input("What grade level are you searching for? ")
        if given_grade == "1":
            level = grade_1.head()
        elif given_grade == "2":
            level = grade_2.head()
        elif given_grade == "3":
            level = grade_3.head()
        elif given_grade == "4":
            level = grade_4.head()
        elif given_grade == "5":
            level = grade_5.head()
        elif given_grade == "help":
            print(ability_rubric)
        else:
            print("I don't understand that search criteria.")
        return level



class Difficulty(Search):

    def search(difficulty):
        giventotal = input("What is your ensemble's overall ability level?")
        # if only difficulty given:
            # search all sheets for difficulty
        # if grade and difficulty given:
            # search grade_? for difficulty



class Composer(Search):

    def search(composer):
        name = input("Which composer/arranger are you looking for?")
        pd.read_excel(excel_file, index_col=3, index_col=4)
        #search through all sheets (sheet_name = 0)
        #search through composer & arranger columns (index_col = 3 & 4)
            #combine both columns into one?
            #ex)Comp/Arr:
                #Bach/Daehn
                #Grainger/Ragsdale
                #Holst/Fennell


    # User enters their search criteria
search_1 = input("Are you searching for a specific piece? >>")
if search_1 == "yes":
    title = input("What title? >>")
else:
    title = 0
search_2 = input("Are you searching for a specific grade level? >>")
if search_2 == "yes":
    grade = input("Which grade level? >>")
else:
    grade = 0
search_3 = input("Are you searching for a specific difficulty? >>")
if search_3 == "yes":
    difficulty = input("What difficulty from 1-10? >>")
else:
    difficulty = 0
search_4 = input("Are you searching for a specific composer or arranger? >>")
if search_4 == "yes":
    composer = input("Which comp/arr? >>")
else:
    composer = 0


    # User's search criteria submitted through class Search
prompt = Search(title, grade, difficulty, composer)
