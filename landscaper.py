## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "mouth of great teeth", "profit": 1, "cost": 0},
    {"name": "tiny shear", "profit": 5, "cost": 5},
    {"name": "scythe", "profit": 50, "cost": 25},
    {"name": "weed wacker", "profit": 80, "cost": 65},
    {"name": "push mower", "profit": 120, "cost": 90},
    {"name": "ride mower", "profit": 450, "cost": 250}
]

## Game Option Function
def mow_lawn():
    tool = tools[game["tool"]]
    print(f"Go mow that yard with your {tool['name']} and make us ${tool['profit']}")
    game["money"] += tool["profit"]
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using a {tool['name']}")
    
def upgrade():
    if(game["tool"] >= len(tools) - 1):
        print("No more upgrades")
        return 0
    next_tool = tools[game["tool"]+1]
    if(next_tool == None):
        print("There are no more tools")
        return 0
    if(game["money"] < next_tool["cost"]):
        print("Not enough to buy tool.")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    print(f"You upgraded to a {next_tool['name']}! You only have ${game['money']}, now. Go mow more lawns!")

def win_check():
    if(game["tool"] == 5 and game["money"] >= 1000):
        print("Ayyyyy you got ABC a new mower and have made $1000+! Congrats! You get...the end of this...game. Broke the 4th wall. Bye! ")
        return True
    return False
        

## Introduction
print("Hi player! Nice to meet you!")
print("You have just joined ABC Landscaping.")
print("Unfortunately...")
print("We do not have any tools or money, so why don't you start and we will build from there.")


## User's Name
user_name = input("First, what is your name?")

## Response to name
print(f"{user_name}?")
print("I guess that's okay. I see you more as a...")
print("Boss off camera: Stop chit chatten and mow these lawns.")
print("Boss off camera: Time is money and we barely have time!")

## Starting Mow for the first time
print(f"Alright {user_name}, all we have is one pair of scissors and they are for me. So you will have to use your teeth on the first one.")

while (True):
    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    i = int(i)
    if (i == 1):
        mow_lawn()
    if (i == 2):
        check_stats()
    if(i == 3):
        upgrade()
    if(i == 4):
        print("You're Fired! I don't hire quitters!")
        break
    if (win_check()):
        break