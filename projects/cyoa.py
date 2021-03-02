"""Python Penguin!"""
__author__: str = "730327440"


import random
todays_forecast = random.choice("weather")
player: str 
points: int = 0
CHILLY = "\U0001F427"


def greet() -> None:
    """Kindly greet the player."""
    global player
    player = input("What is your name? ")
    print(f"Greetings! {player}, welcome to Python's Pet Penguins! {CHILLY}")
    print("Penguin Points:")
    global points
    points += 5
    print(points)


def intro() -> None:
    """Beginning of the game."""
    print("To begin...")
    pet_name = input("What is the name of your pet? ")
    print(f" {pet_name} , what a lovely name!")
    print("Let's Start!")
    print("Penguin Points:")
    global points
    points += 10
    print(points)


def morning() -> None:
    """Good Morning Penguins!"""
    print("Good morning, let's see how the weather is today!")
    # Choose weather to begin day 
    weather: list[str] = ["snowy", "sunny", "rainy", "windy"]
    todays_forecast = random.choice(weather)
    print(f"The weather today is {todays_forecast}!")
    if todays_forecast == "snowy":
        print(f"{CHILLY} wants to know waddle do today.")
        print("Penguin Points:")
        global points
        points += 5
        print(points)
        snow_plans()   
    else:
        if todays_forecast == "sunny": 
            print(f"{CHILLY} wants to know waddle do today.")
            print("Penguin Points:")
            points += 5
            print(points)
            sunny_plans()
        if todays_forecast == "rainy":
            print(f"{CHILLY} wants to know waddle do today.")
            print("Penguin Points:")
            points += 5
            print(points)
            rainy_plans()
        if todays_forecast == "windy":
            print(f"{CHILLY} wants to know waddle do today.")
            print("Penguin Points:")
            points += 5
            print(points)
            windy_plans()


def snow_plans() -> None:
    """What will you do while it is snowing?"""
    todays_forecast == "snowy"
    while True:
        snow_ans = input("Do you want to: A) Build a snowman and drink hot chocolate. B) Pick strawberries. [A/B] ? :")
        if snow_ans in ["A", "B"]:
            # whenever it is equal to A or B, break the loop
            if snow_ans == "A": 
                print("Yay! Great choice!Let's go have fun in the snow!")
                print(f" \u2744 \u2744 \u2744 \u2603 {CHILLY} \u2744 \u2744 \u2744")
                print(f" \u2615 {CHILLY}")
                print("Penguin Points:") 
                global points
                points += 10
                print(points)
            elif snow_ans == "B":
                print("Oh no! It is way too cold for picking strawberries! Not the best choice!")
                print("You tried to go strawberry picking, but ended up with a cold instead.")
                print("Since you now have a cold, you must go see the doctor!")
                print("\U0001F328 \U0001F6AB \U0001F353")
                print("Penguin Points:")
                points -= 10
                print(points)
            break
    

def sunny_plans() -> None:
    """What will you do while it is sunny?"""
    todays_forecast == "sunny"
    while True: 
        sun_ans = input("Do you want to: A) Sleep in. B) Swim at the beach with your friend, Paula Bear.  [A/B] ? :")
        if sun_ans in ["A", "B"]:
            # whenever it is equal, break the loop
            if sun_ans == "A": 
                print("Although sleeping in is great, it has now messed up your sleeping schedule.")
                print("\U0001F6CC \U0001F6AB ")
                print("Penguin Points:") 
                global points
                points -= 10
                print(points)
            elif sun_ans == "B":
                print("What a wonderful idea! The weather was so perfect for riding the waves!")
                print("We also found many cool shells and enjoyed some delicious ice cream too!")
                print(f" \U0001F30A \U0001F30A \U0001F30A \U0001F3D6 \U0001F43B {CHILLY} ")
                print("Penguin Points:")
                points += 10
                print(points)
        break


def windy_plans() -> None:
    """What will you do when it is windy?"""
    todays_forecast == "windy"
    while True:
        windy_ans = input("Do you want to: A) Go fly kites with friends. B) Play badminton with friends. [A/B] ? :")
        if windy_ans in ["A", "B"]:
            # whenever it is equal, break the loop
            if windy_ans == "A": 
                print("Execellent Choice! You are now ready to show your friends your new red kite!")
                print(f"\U0001F332 \U0001F32C \U0001FA81{CHILLY} \U0001F43B \U0001F994 \U0001F415 \U0001F332")
                print("Penguin Points:") 
                global points
                points += 10
                print(points)
            if windy_ans == "B": 
                print("While badminton with friends is a lot of fun, it is not the best choice.")
                print("The wind causes the birdie to fly in the wrong direction. You have lost 2 birdies so far.")
                print(" \U0001F32C \U0001F3F8 \U0001F6AB ")
                print("Penguin Points:")
                points -= 10
                print(points)
            break


def rainy_plans() -> None:
    """What will you do when it is rainy?"""
    todays_forecast == "rainy"
    while True:
        rainy_ans = input("Do you want to: A) Go for a long walk while listening to music. B) Stay indoors and play video games! ")
        if rainy_ans in ["A", "B"]:
            # whenever it is equal, break the loop
            if rainy_ans == "A": 
                print("This would be an excellent choice if we owned rainboots,")
                print("so how about we go shopping for some later? ")
                print("\U0001F327  \U000027A1  \U0001F6CD \U0001F462 ")
                print("Penguin Points:")
                global points
                points -= 10
                print(points)
            if rainy_ans == "B": 
                print("Sounds like so much fun! I wonder which games we'll play today. How about you choose!")
                print("Penguin Points:")
                points += 10
                print(points)
                video_games = input("What video game do you want to play?: ")
                print(f"{video_games} is such a good choice! Thanks for choosing!")
                print(f"\U0001F327   \U0001F6AA     \U0001F3AE 	 {CHILLY}    \U0001FA91   \U0001F327 ")
                print("Penguin Points:")
                points -= 10
                print(points)
            break


def bonus() -> None:
    """Give the player bonus points!"""
    print(f"Hello {player}!")
    while True: 
        print("Time to earn bonus Penguin Points!")
        bonus_points = input("Choose A) , B) , C), D)")
        if bonus_points in ["A", "B", "C", "D"]:
            if bonus_points == "A":
                print("You have been awared 20 bonus points!")
                print("Penguin Points:")
                global points
                points += 20
                print(points)
            if bonus_points == "B":
                print("You have been awared 1 bonus point! Better luck next time!")
                print("Penguin Points:")
                points += 1
                print(points)
            if bonus_points == "C":
                print("You have been awared 250 bonus points! Congratulations!")
                print("Penguin Points:")
                points += 250
                print(points)
            if bonus_points == "D":
                print("You have been awared 1000 bonus points! Amazing!")
                print("Penguin Points:")
                points += 1000
                print(points)
            break


def main() -> None:
    """The functions for my function."""
    greet()
    intro()
    morning()
    bonus()
    while True: 
        next_day = input("Would you like to continue to  the next day? Enter Yes or No: ")
        if next_day == "Yes":
            print("Welcome back! Here is 300 Penguin Points for your return!")
            print("Penguin Points:")
            global points
            points += 300
            print(points)
            morning()
        if next_day == "No":
            print("It is sad to see you leave. Please come again anytime! Have a wonderful rest of your day!")
        break
    

if __name__ == "__main__":
    main()