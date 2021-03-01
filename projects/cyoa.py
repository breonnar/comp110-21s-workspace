"""Python Penguin"""
__author__: str = "730327440"


import random
todays_forecast = random.choice("weather")
player: str = input( "What is your name? " )
adventure_points: int = 0
CHILLY = "\U0001F427"


def greet():
    """Kindly greet the player."""
    print(f"Greetings! {player}, welcome to Python's Pet Penguins! {CHILLY}")
    print("Penguin Points:")
    global adventure_points
    adventure_points += 5
    print(adventure_points)


def intro():
    """Beginning of the game."""
    print( "To begin...")
    pet_name = input ( "What is the name of your pet? " )
    print(f" {pet_name} , what a lovely name!" )
    print( "Let's Start!" )
    print("Penguin Points:")
    global adventure_points
    adventure_points += 10
    print(adventure_points)


def morning():
    """Good Morning Penguins!"""
    print ( "Good morning, let's see how the weather is today!" )
#Choose weather to begin day 
    weather : str = ["snowy", "sunny", "rainy", "windy"]
    todays_forecast = random.choice(weather)
    print(f"The weather today is {todays_forecast}!")
    if todays_forecast == "snowy" :
        print(f"{CHILLY} wants to know waddle do today.")
        print(f"Penguin Points:")
        global adventure_points
        adventure_points += 5
        print(adventure_points)
        snow_plans()   
    else:
        if todays_forecast == "sunny" : 
            print(f"{CHILLY} wants to know waddle do today.")
            print(f"Penguin Points:")
            adventure_points += 5
            print(adventure_points)
            sunny_plans()
        if todays_forecast == "rainy" :
            print(f"{CHILLY} wants to know waddle do today.")
            print(f"Penguin Points:")
            adventure_points += 5
            print(adventure_points)
            rainy_plans()
        if todays_forecast == "windy":
            print(f"{CHILLY} wants to know waddle do today.")
            print(f"Penguin Points:")
            adventure_points += 5
            print(adventure_points)
            windy_plans()


def snow_plans():
    """What will you do while it is snowing?"""
    todays_forecast == "snowy"
    while True:
        snow_ans = input( "Do you want to: A) Build a snowman and drink hot chocolate. B) Pick strawberries and drink iced tea. [A/B] ? :")
        if snow_ans in ["A","B"]:
            #whenever it is equal to A or B, break the loop
            if snow_ans == "A": 
                print("Yay! Great choice!Let's go have fun in the snow!")
                print(f" \u2744 \u2744 \u2744 \u2603 {CHILLY} \u2744 \u2744 \u2744")
                print(f" \u2615 {CHILLY}")
                print(f"Penguin Points:") 
                global adventure_points
                adventure_points += 10
                print(adventure_points)
            elif snow_ans == "B":
                print("Oh no! It is way too cold for picking strawberries! Not the best choice!                                               \
                    You tried to go strawberry picking, but ended up with a cold instead (because it is not strawberry season...).")
                print("Since you now have a cold, you must go see the doctor!")
                print(f"\U0001F328 \U0001F6AB \U0001F353")
                print(f"Penguin Points:")
                adventure_points -= 10
                print(adventure_points)
            break
    

def sunny_plans():
    """What will you do while it is sunny?"""
    todays_forecast == "sunny"
    while True: 
        sun_ans = input( "Do you want to: A) Sleep in and tell your friend Paula Bear that you'll hang out later. B) Swim at the beach with your friend, Paula Bear.  [A/B] ? :")
        if sun_ans in ["A","B"]:
        #whenever it is equal, break the loop
            if sun_ans == "A": 
                print("Although sleeping in is great, it has now messed up your sleeping schedule. Also, Paul Bear missed you today!")
                print(f"\U0001F6CC \U0001F6AB ")
                print(f"Penguin Points:") 
                global adventure_points
                adventure_points -= 10
                print(adventure_points)
            elif sun_ans == "B":
                print("What a wonderful idea! The weather was so perfect for riding the waves! We also found many cool shells and enjoyed some delicious ice cream too!")
                print(f" \U0001F30A \U0001F30A \U0001F30A \U0001F3D6 \U0001F43B {CHILLY} ")
                print(f"Penguin Points:")
                adventure_points += 10
                print(adventure_points)
        break


def windy_plans():
    """What will you do when it is windy?"""
    todays_forecast == "windy"
    while True:
        windy_ans = input("Do you want to: A) Go fly kites with friends. B) Play badminton with friends. [A/B] ? :")
        if windy_ans in ["A","B"]:
        #whenever it is equal, break the loop
            if windy_ans == "A": 
                print("Execellent Choice! You are now ready to show your friends your new red kite!")
                print(f"\U0001F332 \U0001F32C \U0001FA81 {CHILLY} \U0001F43B \U0001F994 \U0001F415 \U0001F43C \U0001F332 ")
                print(f"Penguin Points:") 
                global adventure_points
                adventure_points += 10
                print(adventure_points)
            if windy_ans == "B": 
                print("While badminton with friends is a lot of fun, it is not the best choice because the wind unfortnatlety causes the birdie to fly in the wrong direction. It looks as if you guys have lost 2 birdies so far.")
                print(f" \U0001F32C \U0001F3F8 \U0001F6AB ")
                print(f"Penguin Points:")
                adventure_points -= 10
                print(adventure_points)
            break


def rainy_plans():
        """What will you do when it is rainy?"""
        todays_forecast == "rainy"
        while True:
            rainy_ans = input("Do you want to: A) Go outside for a long walk while listening to your favorite music. B) Stay indoors, play video games, and chat with friends! ")
            if rainy_ans in ["A","B"]:
        #whenever it is equal, break the loop
                if rainy_ans == "A" : 
                    print("This would be an excellent choice if we owned rainboots, so how about we go shopping for some later? ")
                    print(f" \U0001F327  \U000027A1  \U0001F6CD \U0001F462 	")
                    print(f"Penguin Points:")
                    global adventure_points
                    adventure_points -= 10
                    print(adventure_points)
                if rainy_ans == "B" : 
                    print("Sounds like so much fun! I wonder which games we'll play today. How about you choose!")
                    print(f"Penguin Points:")
                    adventure_points += 10
                    print(adventure_points)
                    video_games = input("What video game do you want to play?: ")
                    print("That game is such a good choice! Thanks for choosing!")
                    print(f"\U0001F327   \U0001F6AA     \U0001F3AE 	 {CHILLY}    \U0001FA91   \U0001F327 ")
                    print(f"Penguin Points:")
                    adventure_points -= 10
                    print(adventure_points)
                break


def bonus():
    """Give the player bonus points"""
    print(f"Hello {player}!")
    while True: 
        print("Time to earn bonus Penguin Points!")
        bonus_points = input("Choose A) , B) , C), D)")
        if bonus_points in ["A","B", "C", "D"]:
            if bonus_points == "A":
                print("You have been awared 20 bonus points!")
                print(f"Penguin Points:")
                global adventure_points
                adventure_points += 10
                print(adventure_points)
            if bonus_points == "B":
                print("You have been awared 1 bonus point! Better luck next time!")
                print(f"Penguin Points:")
                adventure_points += 1
                print(adventure_points)
            if bonus_points == "C":
                print("You have been awared 250 bonus points! Congratulations!")
                print(f"Penguin Points:")
                adventure_points += 250
                print(adventure_points)
            if bonus_points == "D":
                print("You have been awared 1000 bonus points! Amazing!")
                print(f"Penguin Points:")
                adventure_points += 1000
                print(adventure_points)
            break


def main() -> None:
    greet()
    intro()
    morning()
    bonus()
    while True: 
        next_day = input ("Would you like to continue to  the next day? Enter Yes or No:" )
        if next_day == "Yes":
            print("Welcome back! Here is 300 Penguin Points for your return!")
            print(f"Penguin Points:")
            global adventure_points
            adventure_points += 300
            print(adventure_points)
            morning()
        if next_day == "No":
            print("It is sad to see you leave. Please come again anytime! Have a wonderful rest of your day!")
        break
    

if __name__ == "__main__":
    main()