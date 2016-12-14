import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np

# Entry Function
def Entry():

    x = raw_input('\033[1m' + "\nDo you want to enter ? (Press y/n)" + '\033[00m')

    if x == 'y':
        print '\033[96m' + "\nWelcome to Football Client" + '\033[00m' + "\n"
        menu()
    elif x == 'n':
        exit()


# Main Menu
def menu():

    print '\033[94m' + "\nPress 1 for English Premier League"
    print "Press 2 for Spanish Primera Division"
    print "Press 3 for German Bundesliga" + '\033[00m'

    choice = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    if choice == '1':
        epl()

    elif choice == '2':
        laliga()

    elif choice == '3':
        bundesliga()

    else:
        print "Invalid choice"


# EPL function
def epl():

    print '\033[96m' + "\nWelcome to English Premier League" + '\033[00m'

    print '\033[94m' + "\nPress 1 for League Standings"
    print "Press 2 for Top Scorers"
    print "Press 3 for Top Assists"
    print "Press 4 for Discipline"
    print "Press 5 for Fairplay" + '\033[00m'

    a = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    # League Standings
    if a == '1':
        url = "http://www.espn.in/football/table/_/league/eng.1"
        leagueStandings(url)

    # Top Scorers
    elif a == '2':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '3':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '4':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/discipline"
        discipline(url)

    # Fair Play
    elif a == '5':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"

    print '\033[91m' + "\nDo you wish to continue exploring ? (Press y/n)" + '\033[00m'

    b = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    if b == 'y':
        menu()
    elif b == 'n':
        print '\033[93m' + "\nThank You" + '\033[00m'
        exit()


# Laliga function
def laliga():

    print '\033[96m' + "\nWelcome to Spanish Primera Division" + '\033[00m'

    print '\033[94m' + "\nPress 1 for League Standings"
    print "Press 2 for Top Scorers"
    print "Press 3 for Top Assists"
    print "Press 4 for Discipline"
    print "Press 5 for Fairplay" + '\033[00m'

    a = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    # League Standings
    if a == '1':
        url = "http://www.espn.in/football/table/_/league/esp.1"
        leagueStandings(url)

    # Top Scorers
    elif a == '2':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '3':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '4':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/discipline"
        discipline(url)

    # Fairplay
    elif a == '5':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"
        exit()

    print '\033[91m' + "\nDo you wish to continue exploring ? (Press y/n)" + '\033[00m'

    b = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    if b == 'y':
        menu()
    elif b == 'n':
        print '\033[93m' + "\nThank You" + '\033[00m'
        exit()


# Bundesliga function
def bundesliga():

    print '\033[96m' + "\nWelcome to German Bundesliga" + '\033[00m'

    print '\033[94m' + "\nPress 1 for League Standings"
    print "Press 2 for Top Scorers"
    print "Press 3 for Top Assists"
    print "Press 4 for Discipline"
    print "Press 5 for Fairplay" + '\033[00m'

    a = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    # League Standings
    if a == '1':
        url = "http://www.espn.in/football/table/_/league/ger.1"
        # leagueStandings_bundesliga(url)

    # Top Scorers
    elif a == '2':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '3':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '4':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/discipline"
        discipline(url)

    # Fair Play
    elif a == '5':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"

    print '\033[91m' + "\nDo you wish to continue exploring ? (Press y/n)" + '\033[00m'

    b = raw_input('\033[1m' + "\nEnter your choice : " + '\033[00m')

    if b == 'y':
        menu()
    elif b == 'n':
        print '\033[93m' + "\nThank You" + '\033[00m'
        exit()


# Function to fetch the League Standings
def leagueStandings(url):
    url = str(url)
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    row = soup.find_all("tr", attrs={'class': 'standings-row'})

    table = []

    for i in row:
        team = []
        for j in i:
            team.append(j.text)
            if len(team) == 9:
                table.append(team)

    team_name = []
    games_played = []
    wins = []
    draws = []
    losses = []
    goals_for = []
    goals_against = []
    goals_difference = []
    points = []

    for i in range(0, 20):
        x = str(i + 1)
        team_name.append(table[i][0].strip(x))
        games_played.append(table[i][1])
        wins.append(table[i][2])
        draws.append(table[i][3])
        losses.append(table[i][4])
        goals_for.append(table[i][5])
        goals_against.append(table[i][6])
        goals_difference.append(table[i][7])
        points.append(table[i][8])

    sequence = ["Position", "Team", "Games", "Wins", "Draws", "Losses", "For", "Against", "Goals Difference",
                "Points"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    pos = []
    for i in range(1, 21):
        pos.append(i)

    df["Position"] = pos
    df["Team"] = team_name
    df["Games"] = games_played
    df["Wins"] = wins
    df["Draws"] = draws
    df["Losses"] = losses
    df["For"] = goals_for
    df["Against"] = goals_against
    df["Goals Difference"] = goals_difference
    df["Points"] = points

    print "\n"
    print df.to_string()


# Function to fetch the League Standings for Bundesliga
# def leagueStandings_bundesliga(url):
#     url = str(url)
#     contest_file = urllib2.urlopen(url)
#     contest_html = contest_file.read()
#     contest_file.close()
#
#     soup = BeautifulSoup(contest_html, 'html.parser')
#
#     row = soup.find_all("tr", attrs={'class': 'standings-row'})
#
#     table = []
#
#     for i in row:
#         team = []
#         for j in i:
#             team.append(j.text)
#             if len(team) == 9:
#                 table.append(team)
#
#     team_name = []
#     games_played = []
#     wins = []
#     draws = []
#     losses = []
#     goals_for = []
#     goals_against = []
#     goals_difference = []
#     points = []
#
#     for i in range(0, 18):
#         x = str(i + 1)
#         team_name.append(table[i][0].strip(x))
#         games_played.append(table[i][1])
#         wins.append(table[i][2])
#         draws.append(table[i][3])
#         losses.append(table[i][4])
#         goals_for.append(table[i][5])
#         goals_against.append(table[i][6])
#         goals_difference.append(table[i][7])
#         points.append(table[i][8])
#
#     sequence = ["Position", "Team", "Games", "Wins", "Draws", "Losses", "For", "Against", "Goals Difference",
#                 "Points"]
#     df = pd.DataFrame()
#     df = df.reindex(columns=sequence)
#
#     pos = []
#     for i in range(1, 21):
#         pos.append(i)
#
#     df["Position"] = pos
#     df["Team"] = team_name
#     df["Games"] = games_played
#     df["Wins"] = wins
#     df["Draws"] = draws
#     df["Losses"] = losses
#     df["For"] = goals_for
#     df["Against"] = goals_against
#     df["Goals Difference"] = goals_difference
#     df["Points"] = points
#
#     print "\n"
#     print df.to_string()


# Function to fetch the Top Scorers
def topScorers(url):
    url = str(url)
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, "html.parser")
    rank = soup.find_all("td", attrs={'headers': 'rank'})
    players = soup.find_all("td", attrs={'headers': 'player'})
    team = soup.find_all("td", attrs={'headers': 'team'})
    goals = soup.find_all("td", attrs={'headers': 'goals'})

    rank_list = []
    players_list = []
    team_list = []
    goals_list = []

    for i in rank:
        rank_list.append(i.text)

    for i in players:
        players_list.append(i.text)

    for i in team:
        team_list.append(i.text)

    for i in goals:
        goals_list.append(i.text)

    sequence = ["Rank", "Player", "Team", "Goals"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    df["Rank"] = rank_list
    df["Player"] = players_list
    df["Team"] = team_list
    df["Goals"] = goals_list

    print "\n"
    print df


# Function to fetch the top assists
def topAssists(url):
    url = str(url)
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, "html.parser")
    rank = soup.find_all("td", attrs={'headers': 'rank'})
    players = soup.find_all("td", attrs={'headers': 'player'})
    team = soup.find_all("td", attrs={'headers': 'team'})
    assists = soup.find_all("td", attrs={'headers': 'goals'})

    rank_list = []
    players_list = []
    team_list = []
    assists_list = []

    for i in rank:
        rank_list.append(i.text)

    for i in players:
        players_list.append(i.text)

    for i in team:
        team_list.append(i.text)

    for i in assists:
        assists_list.append(i.text)

    sequence = ["Rank", "Player", "Team", "Assists"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    df["Rank"] = rank_list
    df["Player"] = players_list
    df["Team"] = team_list
    df["Assists"] = assists_list

    print "\n"
    print df


# Function to fetch the discipline rankings
def discipline(url):
    url = str(url)
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, "html.parser")

    rank = soup.find_all('td', attrs={'headers': 'rank'})
    player = soup.find_all('td', attrs={'headers': 'player'})
    team = soup.find_all('td', attrs={'headers': 'team'})
    points = soup.find_all('td', attrs={'headers': 'goals'})

    rank_list = []
    player_list = []
    team_list = []
    yc_list =[]
    rc_list =[]
    points_list =[]

    for i in rank:
        rank_list.append(i.text)

    for i in player:
        player_list.append(i.text)

    for i in team:
        team_list.append(i.text)

    for i in range(0, len(points), 3):
        yc_list.append(points[i].text)

    for i in range(1, len(points), 3):
        rc_list.append(points[i].text)

    for i in range(2, len(points), 3):
        points_list.append(points[i].text)

    sequence = ['Rank', 'Player', 'Team', 'Yellow Cards', 'Red Cards', 'Points']
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    df["Rank"] = rank_list
    df["Player"] = player_list
    df["Team"] = team_list
    df["Yellow Cards"] = yc_list
    df["Red Cards"] = rc_list
    df["Points"] = points_list

    print df.to_string()

def fairplay(url):
    url = str(url)
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    rank = soup.find_all('td', attrs={'headers': 'rank'})
    team = soup.find_all('td', attrs={'headers': 'team'})
    points = soup.find_all('td', attrs={'headers': 'goals'})

    rank_list = []
    team_list = []
    yc_list = []
    rc_list = []
    points_list = []

    for i in rank:
        rank_list.append(i.text)

    for i in team:
        team_list.append(i.text)

    for i in range(0, len(points), 3):
        yc_list.append(points[i].text)

    for i in range(1, len(points), 3):
        rc_list.append(points[i].text)

    for i in range(2, len(points), 3):
        points_list.append(points[i].text)

    sequence = ['Rank', 'Team', 'Yellow Cards', 'Red Cards', 'Points']
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    df["Rank"] = rank_list
    df["Team"] = team_list
    df["Yellow Cards"] = yc_list
    df["Red Cards"] = rc_list
    df["Points"] = points_list

    print df.to_string()

Entry()