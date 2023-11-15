# Meghnad Bose
# 6 November 2023
# Homework 2

user_birthyear = int(input ("Which year were you born in? "))
import datetime
today = datetime.date.today()
year = today.year


if (user_birthyear > year):
  user_birthyear = int(input ("Please enter a year of birth that isn't in the future! "))

user_age = year - user_birthyear

print ("You are around", user_age, "years old.")

# To estimate how many times the user's heart has beaten, we need a value for the average heartbeats per minute in human beings.
# The following value, of an average heart rate of 80, is based on information provided by the National Heart, Lung, and Blood Institute of the United States on their website.
# Source: https://www.nhlbi.nih.gov/health/heart/heart-beats

avg_human_heartrate_per_min = 80
tot_human_heartbeats = user_age * 365 * 24 * 60 * avg_human_heartrate_per_min
print (f'Your heart has beaten around {tot_human_heartbeats:,} times.')
# To estimate how many times a blue whale's heart has beaten, we need a value for the average heart rate of blue whales. 
# In November 2019, a team of researchers led by J. A. Goldbogen published a study that stated that a single beat of the blue whale’s heart takes about 1.8 seconds.
# Source: https://www.pnas.org/doi/10.1073/pnas.1914273116

bluewhale_heartbeat_in_seconds = 1.8
avg_bluewhale_heartrate_per_min = 60 / bluewhale_heartbeat_in_seconds
tot_bluewhale_heartbeats = int(user_age * 365 * 24 * 60 * avg_bluewhale_heartrate_per_min)
print (f"In this time, a blue whale's heart has beaten around {tot_bluewhale_heartbeats:,} times.")

# The normal heart rate of a rabbit is 200 to 300 beats per minute, according to the following study titled 'Ferrets, Rabbits, and Rodents', viewed at the National Library of Medicine's online archive.
# We will therefore be using the average of 250 heartbeats per minutes for the purpose of estimating how many times a rabbit's heart has beaten in a given period.  
# Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7258697/

avg_rabbit_heartrate_per_min = 250
tot_rabbit_heartbeats = user_age * 365 * 24 * 60 * avg_rabbit_heartrate_per_min
if (tot_rabbit_heartbeats >= 1000000000):
  tot_rabbit_heartbeats_in_billions = tot_rabbit_heartbeats / 1000000000
  print (f"And a rabbit's heart has beaten around, {tot_rabbit_heartbeats_in_billions} billion times.")
else:
  print (f"And a rabbit's heart has beaten around, {tot_rabbit_heartbeats} times.")


# I had initially written the print statements without the f-strings, and the heartbeat numbers were displayed without commas, making them very difficult to read.
# That problem was solved by using f-strings and adding commas in the number.

my_birthyear = 1993
my_age = year - my_birthyear

if my_age > user_age: 
  print (f'My age is {my_age}. I am older than you.')
elif my_age < user_age:
  print (f'My age is {my_age}. I an younger than you.')
elif my_age == user_age:
  print (f'My age is {my_age}. I am around the same age as you.')

presidents_since_1980 = ["Jimmy Carter", "Ronald Reagan", "George H. W. Bush", "Bill Clinton", "George W. Bush", "Barack Obama", "Donald Trump", "Joe Biden"]
party = ["Democratic", "Republican", "Republican", "Democratic", "Republican", "Democratic", "Republican", "Democratic"]
year_left_office = [1981, 1989, 1993, 2001, 2009, 2017, 2021, today.year]

president_count = 0
dem_president_count = 0

for president in presidents_since_1980:
  if (year_left_office[president_count] > user_birthyear and party[president_count] == 'Democratic'):
    dem_president_count = dem_president_count + 1
  president_count = president_count + 1

print (f'There have been {dem_president_count} Democratic presidents of the United States who have taken office in your lifetime.')

president_count = 0

for president in presidents_since_1980:
  if (year_left_office[president_count] > user_birthyear):
    print (f'{presidents_since_1980[president_count]} was the President of the United States at the time you were born.')
    break
  else: 
    president_count = president_count + 1

# We could have probably solved questions 7 and 8 using dictionaries instead of lists as well. I chose to use lists because I felt it did the job simply enough.