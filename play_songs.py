import csv
import sys
import main
import city_weather
import datetime
import random
import os
import time
import glob
from pygame import mixer

mood=main.mood_label()
city = city_weather.get_city()
city2 = city+" weather"
temp = int(city_weather.weather(city2))
now = datetime.datetime.now()
time = str(now.time())
v = time.find(":")
time=int(time[0:v])

if(time<16):
    time_s="Morning"
elif(time<20):
    time_s="Evening"
else:
    time_s="Night"


if(temp<15):
    temp_s="Rain"
elif(temp<25):
    temp_s="Normal"
else:
    temp_s="Hot"
                           

#read csv, and split on "," the line
csv_file = csv.reader(open('Songs_mood.csv', "r"), delimiter=",")



#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if mood == row[0] and temp_s == row[2] and city == row[1] and time_s == row[3]:
         val = row[4]
         
        
mixer.init()

lists_of_songs = os.listdir("/Users/rs_en/Desktop/Mood Recognititon/songs/"+val)

for song in lists_of_songs:
    if song.endswith(".mp3"):
        file_path = "/Users/rs_en/Desktop/Mood Recognititon/songs/"+val +"/"+ song
        mixer.music.load(str(file_path))
        mixer.music.play()
        while True:
            print("Playing::::: " + song)
            print("Press 'p' to pause")
            print("Press 'r' to resume")
            print("Press 'v' set volume")
            print("Press 'n' for next song")
            ch = input("['p','r','v','n']>>>")
            if ch == "p":
                mixer.music.pause()
            elif ch == "r":
                mixer.music.unpause()
            elif ch == "v":
                v = float(input("Enter volume(0 to 1): "))
                mixer.music.set_volume(v)
            elif ch == "n":
                mixer.music.stop()
                break
        
