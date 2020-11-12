# import modules for application
import tkinter as tk
from tkinter import font
from sportsreference.nba.roster import Player

# set dimensions variables
HEIGHT = 700
WIDTH = 600

# get user input
def getEntry():
    input = entry.get()
    findPlayerId(input)

# reset text areas when button pressed
def resetCommand():
    entry.delete(0, 'end')
    label['text'] = ''

# get player selected API ID
def findPlayerId(input):
    try:
        firstAndLastName = input.split()
        firstName = firstAndLastName[0]
        lastName = firstAndLastName[1]
        playerId = str(lastName[:5].lower() + firstName[:2].lower() + '01')
        getStats(playerId)
    except:
        label['text'] = 'Could not fetch any info.'

# get selected player stats from API
def getStats(id):
    try:
        player = Player(id)
        age = str(player.birth_date)
        age = age[:10]
        height = str(player.height)
        weight = str(player.weight)
        position = str(player.position)
        salary = str(player.salary)
        totalPoints = str(player.points)
        freeThrowPercentage = str(player.free_throw_percentage * 100) + '%'
        threePointPercentage = str(player.three_point_percentage * 100) + '%'
        twoPointPercentage = str(player.two_point_percentage * 100) + '%'
        assistsCurrentSeason = str(player.assists)
        name = player.name
        fouls = str(player.personal_fouls)
        minutesPlayed = str(player.minutes_played)
        playerStats = [age, height, position, salary, totalPoints, freeThrowPercentage, threePointPercentage, twoPointPercentage, 
        assistsCurrentSeason, name, minutesPlayed, fouls, weight]

        formatResponse(playerStats)
    except:
        label['text'] = 'Could not fetch any info.'

# format the string to display the stats
def formatResponse(playerStats):
    try:
        finalString = "Bio And Info:" + '\n' + '\n'\
                      + 'Birth Date: ' + playerStats[0] +'\n'  \
                      + 'Height: ' + playerStats[1] + '\n' \
                      + 'Weight: ' + playerStats[12] + '\n' \
                      + 'Position: ' + playerStats[2] + '\n' \
                      + 'Minutes Played: ' + playerStats[10] + '\n' + '\n' \
                      + playerStats[9] + ' Stats:' '\n' + '\n' \
                      + 'Total Points: ' + str(playerStats[4]) + '\n' \
                      + "Free Throw Percentage: " + str(playerStats[5]) + '\n' \
                      + "Three Point Range Percentage: " + str(playerStats[6]) + '\n' \
                      + "Two Point Range Percentage:  " + str(playerStats[7]) + '\n' \
                      + "Assists: " + playerStats[8] + '\n' \
                      + "Personal Fouls: " + playerStats[11]

        label['text'] = finalString
    except:
        label['text'] = 'Could not fetch any info.'

# set up and initialize tkinter module
root = tk.Tk()
root.title('StatIt - NBA')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background_image = tk.PhotoImage(file='basketCourt.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

# create top frame
frame = tk.Frame(root, bg='#FFA500', bd=5)
frame.place(relx=0.5, rely=0.025, relwidth=0.85, relheight=0.1, anchor='n')

# create user entry
entry = tk.Entry(frame, font=('Courier', 18), justify='center')
entry.place(relwidth=0.55, relheight=1)

# create button to display stats
button = tk.Button(frame, text="Get Statistics", font=('Courier', 15, 'bold'), command=getEntry)
button.place(relx=0.575, relheight=1, relwidth=0.43)

# create reset buttons which clear text fields
resetButton = tk.Button(text="Reset", font=('Courier', 13, 'bold'), command=resetCommand)
resetButton.place(relx=0.325, rely=0.85, relheight=0.075, relwidth=0.35)

# create the lower frame
lower_frame = tk.Frame(root, bg='#FFA500', bd=10)
lower_frame.place(relx=0.5, rely=0.22, relwidth=0.85, relheight=0.6, anchor='n')

# create the label to store the stats and final string
label = tk.Label(lower_frame, font=('Courier', 15), anchor='nw', justify='left', border=6)
label.place(relwidth=1, relheight=1)

# create the window
root.mainloop()




