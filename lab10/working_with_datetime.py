import time
import datetime
import pytz
from zoneinfo import ZoneInfo



# now_seconds = time.time()
# print('number of seconds since the Unix epoch: ', now_seconds)

# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)

# user_birth_datetime = datetime.datetime(year=1990, month=12, day=20)
# user_birth_date = datetime.date(year=1990, month=12, day=20)

# print(user_birth_datetime)
# print(user_birth_date)
# print(user_birth_date.year)


# # ---------------------------- datetime.strftime() --------------------------- #
# now = datetime.datetime.now()
# now_str = now.strftime("%d.%m.%Y")
# print(now_str)

# # ---------------------------- datetime.strptime() --------------------------- #
# user_birth_date_str = "20.12.1990" # "DD.MM.YYYY"
# user_birth_date = datetime.datetime.strptime(user_birth_date_str, "%d.%m.%Y")
# print(user_birth_date.year)


# --------------------------- Datetime Arithmetics --------------------------- #
# user_birth_date_str = "20.12.1990" # "DD.MM.YYYY"
# user_birth_date = datetime.datetime.strptime(user_birth_date_str, "%d.%m.%Y")
# print(user_birth_date.year)

# now = datetime.datetime.now()
# delta = now - user_birth_date
# print( delta.days )
# print( now.year - user_birth_date.year)


# now = datetime.datetime.now()
# after_two_weeks = datetime.timedelta(weeks=3)

# print( now + after_two_weeks )



# --------------------------------- Timezones -------------------------------- #

# sofia_tz = pytz.timezone('Europe/Sofia')
# funafuti_tz = pytz.timezone('Pacific/Funafuti')

# sofia_now = datetime.datetime.now(sofia_tz)
# funafuti_now = datetime.datetime.now(funafuti_tz)

# print(sofia_now)
# print(funafuti_now)



# sofia_tz = ZoneInfo('Europe/Sofia')
# funafuti_tz = ZoneInfo('Pacific/Funafuti')

# sofia_now = datetime.datetime.now(sofia_tz)
# funafuti_now = datetime.datetime.now(funafuti_tz)

# print(sofia_now)
# print(funafuti_now)


# --------------------------------- Examples --------------------------------- #
# # Task1: print the weekday of today date
# weekday_na.mes_mapping = {
#     'bg': ["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
#     'en': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# }
# today_date = datetimedatetime.now()
# weekday = today_date.weekday()
# print(weekday_names_mapping['bg'][weekday])




    # def find_years_with_weekday(birth_date:str, target_weekday:str, search_period:tuple):
    #     """Finds years within a specified period when a given date falls on a specified weekday.

    #     Parameters:
    #         birth_date (datetime.datetime): The date of interest.
    #         target_weekday (str): The name of the weekday to match.
    #         search_period (tuple): A tuple specifying the start (inclusive) and end (exclusive) years to search.

    #     Returns:
    #         list: A list of years within the search_period when birth_date falls on target_weekday.
    #     """

    #     date = datetime.datetime.strptime(birth_date, "%d.%m.%Y")
    #     print(date.day)

    #     for year in range(*search_period):
    #         future_date = datetime.date(year=year,month=date.month, day=date.day)
    #             ...


    # find_years_with_weekday('31.12.2000', 'sunday', (2023, 2100))




# --------------------------- datetime.time vs time -------------------------- #
import time

# print('Hello')
# time.sleep(2)
# print('world')

# print(time.time())
# time.sleep(1)
# print(time.time())



# -------------------------------- Timing code ------------------------------- #
from functools import reduce

#start timer
# start = time.time()


# # do some time intensive stuff:
# num_range = (1, 10_000_000)
# sum = reduce(lambda x,y:x+y, range(num_range[0],num_range[1]+1))
# print(f"The sum of numbers from {num_range[0]} to {num_range[1]} is: ", sum)

# #end timer
# end = time.time()

# print("[Finished in {:.3f}s]".format(end - start))

#The sum of numbers from 1 to 10000000 is:  50000005000000
