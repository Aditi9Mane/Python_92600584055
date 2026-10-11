import random

e_count = 0
dice_face = []
for i in range(5):
    dice = random.randint(1, 6)
    if dice % 2 == 0:
        dice_face.append("Even")
        e_count += 1
    else:
        dice_face.append("Odd")
        e_count += 0
print(dice_face)
print("Number of times even numbered face of dice comes: ", e_count)
    
