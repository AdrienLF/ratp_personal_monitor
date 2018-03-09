# ratp_personal_monitor
A very small, 100% python project to check when the buses and subways will arrive.

# Requirements
This project was written 100% with python. All your need is the last version of remi to be able to use the local web interface. The script prints to the terminal anyway. 

Download remi here: https://github.com/dddomodossola/remi

# Setup
The program gets the info from Pierre Grimaud's ratp API. It is very easy to use. In the RATP_Watch.py file, look for requests.get and you will find urls starting with "https://api-ratp.pierre-grimaud.fr/v3/schedules"
If you're looking for info about a bus, add /bus, if metro, add /metros. Then add the number, the name of the station, and which way (A, R, or both). 

Find the doc for the API here: https://api-ratp.pierre-grimaud.fr/v3/documentation
Find the github for the API here: https://github.com/pgrimaud/horaires-ratp-api

As for velib, the API wasn't updated on opendata.paris.fr yet, so it kind of uses a "hack", using the API for the interactive map on valib-metropole.fr. Since the results are kind of a mess, I just iterated through the items. 
In get_velib(), change "xxxxx" in the if "xxxx" in str(item): by the name of the station you want the info on. Simple. 

To use the program, run RATP-interfaceV2.py. It should open your browser and display the info. The interface is only 480x320, optimized for a small rapsberry pi screen.
To change the logo for the buses and metro, look for "https://www.ratp.fr/sites/default/files/network" and change for the correct url. 

# TO DO
This was written for my own consumption, therefore requires you to get your hands dirty to get it to work. If enough people are interested, I might write an interactive setup that will modify the code to get the info and logo easily. 



