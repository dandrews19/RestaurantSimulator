# Restaurant Simulator

#### This project is meant to run a simulation of a restaurant with patrons being seated, taking orders, and ringing them up,


# How it works
#### This algorithm uses information from different places in order to execute the simulation. It ensures that the restaurant runs through a timed simulation (so that the restaurant can close at a specified time), and has its own preset menu and a list of names for potential customers. Every "15" minutes (not actually 15 minutes for the sake of running through the whole simulation) the status of the restaurant updates, stating who has entered, who is seated, who is ordering, who is eating, who is paying, and who is leaving. The algorithm then "moves" each person to the next step, and when someone is in the ordering status, the user is prompted to select menu items, which are then stored for that person to be rung uo when they are in the "paying" status. Once the restaurant is empty and the simulation runs past its set end time, the program stops.

# Screenshots
![Image of Blank Tool](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Blank-Tool.png)
#### This is a screenshot of the GUI with no graphs on it. At the top, there are tabs for a single-day and three day intervals. On the left, there are two lists of buttons, labeled Current Day Options and Next Day Options. The buttons under the current day options allow the user to dispay the most recent performance of the S&P 500, and then rest of the buttons are used to display the days that the algorithm found to be similar to the most recent day. Under Next Day options, the user has the option to display how the similsr performances in the past did the day after. This can be used to try and estimate how the market will perform in the future, if there is a pattern. Below is a screenshot of what it looks like when all the plots are displayed. The user can make the graphs blank whenever they wish using the respective Reset Graph buttons. The legend on the right automatically updates when the user selects an option to be displayed, and clears when the graph is reset.
![Image of Full Tool](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Full-Tool.png)
#### The user also has all of the same options for the three day interval, and when displaying the graphs, it displays graphs of three days rather than one, as shown below.
![Image Three Day Full](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Three-Day-Full.png)
#### Here is a gif running through all the options on the three-day interval:
![Gif of Demo](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/StockDemo.gif)

# Modules Used

- Numpy, for fitting data into a polynomial and storing data in arrays
- Datetime, for having the ability to parse through data based on time
- SciPy, to integrate polynomials
- Statistics, to calculate the average value between lists
- Matplotlib, to graph all the data and display it
- Tkinter, to create a user-friendly interface with buttons that enable the plots to be shown


# How to use
#### To use this program, all you have to do is press run in mainTEST.py; make sure you have all the modules installed, StockClass.py is in your directory, and put the the provided CSV files in your directory. Additionally, the csv probably won't be updated, so you might have to somehow get data for the most current dates, or buy data from FirstRateData.com
