# Riddle:
# There are 100 prisoners in a prison and they are assigned with numbers, starting form 1 to 100.
# There is a room with 100 boxes in it. Each box is assigned a number from 1 to 100 and each box contains a slip with a number on it. 
# The numbers on slip are the numbers of prisoners and they are randomly put into the 100 boxes.  
# Each prisoner can go inside, one at a time and open 50 boxes. 
# If all 100 prisoners finds the slip with their number within the 50 boxes they open, they will be released. 
# They cannot communicate with each other and they are only allowed to open the box and look inside, they cannot change the slips.


import random

def search(prisoner, count = 0, box = 0, number_of_prisoners = 100):
    if count == 0:
        box = prisoner 

    if count == number_of_prisoners//2:
        print(f"Prisoner {prisoner}, Box = {box}")
        return False

    slip = boxes[box-1][1]

    if prisoner == slip:
        print(count+1, boxes[box-1][0], slip)
        print(f"Prisoner {prisoner}, Box = {box}")
        return True
    else:
        print(count+1, boxes[box-1][0] , slip)
        return search(prisoner, count+1, boxes[slip-1][0])


number_of_prisoners = 100 # Increasing prisoners makes it even intersting, try it!

prisoners, boxes = [i for i in range(1,number_of_prisoners + 1)], [[i] for i in range(1,number_of_prisoners + 1)]
random.shuffle(boxes)

boxes = [[i, boxes[i-1][0]] for i in range(1,number_of_prisoners + 1)]

for i in range(0, 100):
    if search(prisoners[i], number_of_prisoners= number_of_prisoners):
        print(f"Prisoner {i+1} found his number")
        continue
    else:
        print(f"Prisoner {prisoners[i]} failed to find the box with his number.")
        break

    print("\nAll Prisoners Released")

# Code by Argish Abhangi