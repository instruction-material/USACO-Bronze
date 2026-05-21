# read input
with open("friday.in", "r") as file:
  input_years = int(file.readline().strip())

# 1/1/1900 was a Monday
day = 0

# dayOfWeek stores the number of 13ths that fell on each day of the week
day_of_week = [0] * 7

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# loop through years
for year in range(1900, 1900 + input_years):
  # loop through months
  for month in range(12):
    # change numDaysInMonth if it is a leap year
    num_days_in_month = days_in_month[month]

    if month == 1:  # if it is February
      if year % 100 == 0:  # if the year is a century
        if year % 400 == 0:  # if the year is divisible by 400
          num_days_in_month += 1  # leap year
      elif year % 4 == 0:  # if the year is not a century and divisible by 4
        num_days_in_month += 1  # leap year

    # loop through dates
    for date in range(1, num_days_in_month + 1):
      # update dayOfWeek when date is the 13th
      if date == 13:
        day_of_week[day] += 1

      day += 1
      # loop back around from Sun to Mon
      if day > 6:
        day = 0

# write output
with open("friday.out", "w") as file:
  file.write(
      f"{day_of_week[5]} {day_of_week[6]} {day_of_week[0]} {day_of_week[1]} {day_of_week[2]} {day_of_week[3]} {day_of_week[4]}\n"
  )
