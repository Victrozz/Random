import time
from datetime import datetime, date

song_duration = 223
song_name = "Let It Go"

#now function stores current time in a variable (hours, minutes, seconds and 6 decimals of seconds)
now = datetime.now()

#sets a custom date, in this case, the time of the skii trip
then = datetime(year = 2023, month = 5, day = 31, hour = 14)

#sorry this is a mess
#l1 is the representation of the time left, stored in a time.deltatime variable (year all the way to miliseconds)
l1 = then - now

#l1tostring turns it into a string variable so we can show it in the console later on
l1tostring = str(l1)

#l2 converts it into seconds (float) to be divided
l2 = l1.total_seconds()

#divides the amount of seconds left by the seconds in the song
amount_of_times = l2 / song_duration

#transforms it into an int variable to get rid of the extra decimals
aot_toint = int(amount_of_times)

#transforms the new int into a string to be shown in the console later
aot_tostring = str(aot_toint)

#prints the end variables, those being the time left in a deltatime variable and the amount of times to sing the song in a string variable
print("Time left: " + l1tostring)
print("You have to sing " + song_name + " " + aot_tostring + " times!")

#4 Dec, 10:19:10 :)