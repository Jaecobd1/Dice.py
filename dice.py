#dice.py
import random 
# ~~~ App's main code block ~~~
# 1. Get an validate user's input

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_Height = len(DICE_ART[1])
DIE_Width = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    if input_string.strip() in { "1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("please enter a number from 1 to 6.")
        raise SystemExit(1)
def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

num_dice_input = input("how many dice do you want to roll? [1-6]")



num_dice = parse_input(num_dice_input)

roll_results = roll_dice(num_dice)

def generate_dice_faces_diagram(dice_values):

    dice_faces = []

    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    dice_faces_rows = []
    for row_idx in range(DIE_Height):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

dice_face_diagram = generate_dice_faces_diagram(roll_results)
print(f"\n{dice_face_diagram}")


    
print(roll_results)
