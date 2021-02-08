"""A vaccination calculator."""

__author__ = "730327440"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population = float(input("Population:"))
doses_given = float(input("Doses given:"))
doses_given_per_day = float(input("Doses given per day:"))
target_percent_vaccinated = float(input("Target percent vaccinated:"))

percent_vaccination_goal_population = population * (target_percent_vaccinated / 100)
remaining_population = percent_vaccination_goal_population - (doses_given / 2)
people_vax_per_day = doses_given_per_day / 2
days_remaining = remaining_population / people_vax_per_day

today = datetime.today()
deadline = today + timedelta(days_remaining)

print( "We will reach " + str(round(target_percent_vaccinated)) + "% vaccination in " + str(
    round(days_remaining)) + " days, which falls on " + deadline.strftime("%B %d, %Y") + ".")