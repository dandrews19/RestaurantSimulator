# Restaurant Simulator

#### This project is meant to run a simulation of a restaurant with patrons being seated, taking orders, and ringing them up,


# How it works
#### This algorithm uses information from different places in order to execute the simulation. It ensures that the restaurant runs through a timed simulation (so that the restaurant can close at a specified time), and has its own preset menu and a list of names for potential customers. Every "15" minutes (not actually 15 minutes for the sake of running through the whole simulation) the status of the restaurant updates, stating who has entered, who is seated, who is ordering, who is eating, who is paying, and who is leaving. The algorithm then "moves" each person to the next step, and when someone is in the ordering status, the user is prompted to select menu items, which are then stored for that person to be rung uo when they are in the "paying" status. Once the restaurant is empty and the simulation runs past its set end time, the program stops.

# GIF

#### Here is a gif running through all the options on the three-day interval:
![Gif of Restaurant Demo](https://github.com/dandrews19/RestaurantSimulator/blob/main/RestaurantDemo.gif)

# Modules Used

- Datetime, for having the ability to run the program based on time

# How to use
#### To use this program, all you have to do is press run in Run.py; make sure you have all the modules installed, and all the additional files are in your directory.
