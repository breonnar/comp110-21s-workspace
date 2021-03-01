"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730327440"


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculates the days remaining target % vaccinated is reached."""
    percent_vaccination_goal_population = population * (target / 100)
    remaining_population = percent_vaccination_goal_population - (doses / 2)
    people_vax_per_day = doses_per_day / 2
    days_remaining = remaining_population / people_vax_per_day
    return round(days_remaining)


# TODO 3: Define future_date function
def future_date(days_out: int) -> str:
    """Calculates the days remaining until the future date is reached."""
    today = datetime.today()
    deadline = today + timedelta(days_out)
    return deadline.strftime("%B %d, %Y")


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_remaining: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    fut_date: str = future_date(days_remaining)
    # TODO 5: Print the expected output using the variables above.

    print("We will reach " + str(round(target)) + "% vaccination in " + str(
        days_remaining) + " days, which falls on " + fut_date + ".")


if __name__ == "__main__":
    main()
