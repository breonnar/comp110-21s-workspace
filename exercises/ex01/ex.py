import random
todays_forecast = random.choice("weather")
player: str
adventure_points: int = 0
CHILLY = "\U0001F427"


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
            global adventure_points 
            adventure_points += 5
            print(adventure_points)
            sunny_plans()
        if todays_forecast == "rainy" :
            print(f"{CHILLY} wants to know waddle do today.")
            print(f"Penguin Points:")
            global adventure_points
            adventure_points += 5
            print(adventure_points)
            rainy_plans()
        if todays_forecast == "windy":
            print(f"{CHILLY} wants to know waddle do today.")
            print(f"Penguin Points:")
            global adventure_points
            adventure_points += 5
            print(adventure_points)
            windy_plans()





def main() -> None:
    morning()
    

if __name__ == "__main__":
    main()