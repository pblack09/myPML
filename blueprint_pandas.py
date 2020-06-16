from music_library.elsx import *


# Grade 4, piece 1 [total difficulty]
# Grade 4, piece 2
# etc...
piece4_1 = ['Divertimento for Band', 9]
piece4_2 = ['A Drop of Rain', 7]
piece4_3 = ['Ceremonial Dances', 5]


# Below code works for total difficulty
# Function finds which pieces are at or below user's difficulty
# Returns True or False for if a piece meets their criteria
# Does NOT return song name though...
#def suggest(user_input):
    #piece1 = user_input >= piece4_1[1]
    #piece2 = user_input >= piece4_2[1]
    #piece3 = user_input >= piece4_3[1]
    #return piece1, piece2, piece3
#print(suggest(7))

a_drop_of_rain = [6, 6, 6, 6, 6]
user_input = [6, 6, 7, 6, 3]

def suggestion(piece, user):
    if list(a_drop_of_rain) >= list(user_input):
        return True
    else:
        return False

print(suggestion)
