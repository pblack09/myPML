            # 37: Symbol Review

list_songs1 = ['Jingle Bells', 'Mary Had a Little Lamb', 'Hot Cross Buns', 'Kentucky 1800', 'Come Sweet Death', 'Adrenaline Engines', 'Variations on a Scarborough Fair', 'The Cave You Fear', 'Japanese Folk Song']
list_songs2 = ['Foundry', 'La Madre de los Gatos', 'Glaciers', 'Khan', '3 Celtic Dances', 'Canarios Fantasia', 'Old Red Mill', 'Satiric Dances', 'This Cruel Moon']
list_songs3 = ['Second Suite in F', 'Sheltering Skies', 'First Suite in Eb', 'Quartets', 'Hounds of Spring', 'Elsa\'s Procession of the Nobles', 'Pas Redouble', 'Lincolnshire Posy', 'La Fiesta Mexicana']


print("""
\tWelcome to myPML!
Where you can find music that fits your ensemble.
Enter your overall Band ability:""")
overall = int(input("> "))

print("Enter your overall Brass ability:")
brass = int(input("> "))

print("Enter your overall Woodwind ability:")
woodwind = int(input("> "))

def list1(brass, woodwind):
    
    if brass == 1:
        
        if woodwind == 1:
            print(list_songs1[0])
            
        elif woodwind == 2:
            print(list_songs1[1])
            
        else:
            print(list_songs1[2])
    
    elif brass == 2:
                  
        if woodwind == 1:
            print(list_songs1[3])
        
        elif woodwind == 2:
            print(list_songs1[4])
        
        else:
            print(list_songs1[5])
    
    else:
        
        if woodwind == 1:
            print(list_songs1[6])
        
        elif woodwind == 2:
            print(list_songs1[7])
        
        else:
            print(list_songs1[8])
            
def list2(brass, woodwind):
    
    if brass <= 4:
        
        if woodwind <= 4:
            print(list_songs2[0])
            
        elif woodwind == 5:
            print(list_songs2[1])
            
        else:
            print(list_songs2[2])
    
    elif brass == 5:
                  
        if woodwind <= 4:
            print(list_songs2[3])
        
        elif woodwind == 5:
            print(list_songs2[4])
        
        else:
            print(list_songs2[5])
    
    else:
        
        if woodwind <= 4:
            print(list_songs2[6])
        
        elif woodwind == 5:
            print(list_songs2[7])
        
        else:
            print(list_songs2[8])
            
def list3(brass, woodwind):
    
    if brass <= 7:
        
        if woodwind <= 7:
            print(list_songs3[0])
            
        elif woodwind == 8:
            print(list_songs3[1])
            
        else:
            print(list_songs3[2])
    
    elif brass == 8:
                  
        if woodwind <= 7:
            print(list_songs3[3])
        
        elif woodwind == 8:
            print(list_songs3[4])
        
        else:
            print(list_songs3[5])
    
    else:
        
        if woodwind <= 7:
            print(list_songs3[6])
        
        elif woodwind == 8:
            print(list_songs3[7])
        
        else:
            print(list_songs3[8])
                  
if overall <= 3:
    list1(brass, woodwind)

elif overall >= 4 and overall <= 6:
    list2(brass, woodwind)

else:
    list3(brass, woodwind)