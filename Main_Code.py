import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np
from prettytable import PrettyTable

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Entry Function
def Entry():

    x = raw_input(color.BOLD + "\nDo you want to enter ? (Press y/n)" + color.END)

    if x == 'y':
        print color.CYAN + color.BOLD + "\nWelcome to Football Client" + color.END + "\n"
        menu()
    elif x == 'n':
        exit()


# Main Menu
def menu():

    print color.BLUE + color.BOLD + "\nPress 1 for English Premier League"
    print "Press 2 for Spanish Primera Division"
    print "Press 3 for German Bundesliga" + color.END

    choice = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

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

    print color.CYAN + color.BOLD + "\nWelcome to English Premier League" + color.END

    print color.YELLOW + color.BOLD + "\nPress 1 for Latest League Results"
    print "Press 2 for League Fixtures"
    print "Press 3 for League Standings"
    print "Press 4 for Top Scorers"
    print "Press 5 for Top Assists"
    print "Press 6 for Discipline"
    print "Press 7 for Fairplay" + color.END

    a = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    # League Results
    if a == '1':
        url = "http://www.bbc.com/sport/football/premier-league/results"
        showResults(url)

    # League Fixtures
    elif a == '2':
        url = "http://www.bbc.com/sport/football/premier-league/fixtures"
        getFixtures(url)

    # League Standings
    elif a == '3':
        url = "http://www.espn.in/football/table/_/league/eng.1"
        leagueStandings(url)

    # Top Scorers
    elif a == '4':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '5':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '6':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/discipline"
        discipline(url)

    # Fair Play
    elif a == '7':
        url = "http://www.espnfc.com/english-premier-league/23/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"

    print color.GREEN + color.BOLD + "\nDo you wish to continue exploring ? (Press y/n)" + color.END

    b = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    if b == 'y':
        menu()
    elif b == 'n':
        print color.YELLOW + color.BOLD + "\nThank You" + color.END
        exit()


# Laliga function
def laliga():
    print color.CYAN + color.BOLD + "\nWelcome to La Liga" + color.END

    print color.YELLOW + color.BOLD + "\nPress 1 for Latest League Results"
    print "Press 2 for League Fixtures"
    print "Press 3 for League Standings"
    print "Press 4 for Top Scorers"
    print "Press 5 for Top Assists"
    print "Press 6 for Discipline"
    print "Press 7 for Fairplay" + color.END

    a = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    # League Results
    if a == '1':
        url = "http://www.bbc.com/sport/football/spanish-la-liga/results"
        showResults(url)

    # League Fixtures
    elif a == '2':
        url = "http://www.bbc.com/sport/football/spanish-la-liga/fixtures"
        getFixtures(url)

    # League Standings
    elif a == '3':
        url = "http://www.espn.in/football/table/_/league/esp.1"
        leagueStandings(url)

    # Top Scorers
    elif a == '4':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '5':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '6':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/discipline"
        discipline(url)

    # Fairplay
    elif a == '7':
        url = "http://www.espnfc.com/spanish-primera-division/15/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"
        exit()

    print color.GREEN + color.BOLD + "\nDo you wish to continue exploring ? (Press y/n)" + color.END

    b = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    if b == 'y':
        menu()
    elif b == 'n':
        print color.YELLOW + color.BOLD + "\nThank You" + color.END
        exit()


# Bundesliga function
def bundesliga():
    print color.CYAN + color.BOLD + "\nWelcome to Bundesliga" + color.END

    print color.YELLOW + color.BOLD + "\nPress 1 for Latest League Results"
    print "Press 2 for League Fixtures"
    print "Press 3 for League Standings"
    print "Press 4 for Top Scorers"
    print "Press 5 for Top Assists"
    print "Press 6 for Discipline"
    print "Press 7 for Fairplay" + color.END

    a = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    # League Results
    if a == '1':
        url = "http://www.bbc.com/sport/football/german-bundesliga/results"
        showResults(url)

    # League Fixtures
    elif a == '2':
        url = "http://www.bbc.com/sport/football/german-bundesliga/fixtures"
        getFixtures(url)

    # League Standings
    elif a == '3':
        url = "http://www.espn.in/football/table/_/league/ger.1"
        leagueStandings_bundesliga(url)

    # Top Scorers
    elif a == '4':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/scorers"
        topScorers(url)

    # Top Assists
    elif a == '5':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/assists"
        topAssists(url)

    # Discipline
    elif a == '6':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/discipline"
        discipline(url)

    # Fair Play
    elif a == '7':
        url = "http://www.espnfc.us/german-bundesliga/10/statistics/fairplay"
        fairplay(url)

    else:
        print "Invalid choice"

    print color.GREEN + color.BOLD + "\nDo you wish to continue exploring ? (Press y/n)" + color.END

    b = raw_input(color.BOLD + color.RED + "\nEnter your choice : " + color.END)

    if b == 'y':
        menu()
    elif b == 'n':
        print color.YELLOW + color.BOLD + "\nThank You" + color.END
        exit()


# Function to get the Latest Results
def showResults(url):
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    table = soup.find("table", attrs={'class': 'table-stats'})

    print "\n"

    for i in table.find_all("caption"):
        print '\033[1m' + i.text + '\033[00m'

    print "\n"

    home_team = []
    away_team = []
    score = []

    for i in table.find_all("span", attrs={'class': 'team-home teams'}):
        home_team.append(i.text)

    for i in table.find_all("span", attrs={'class': 'team-away teams'}):
        away_team.append(i.text)

    for i in table.find_all("span", attrs={'class':'score'}):
        score.append(i.text)

    home_team = map(lambda s: s.strip(), home_team)
    away_team = map(lambda s: s.strip(), away_team)
    score = map(lambda s: s.strip(), score)

    sequence = ["Home Team", "Score", "Away Team"]
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    # df["Home Team"] = home_team
    # df["Score"] = score
    # df["Away Team"] = away_team

    t = PrettyTable(sequence)

    for i in range(0,len(home_team)):
        t.add_row([home_team[i], score[i], away_team[i]])

    print t


# Function to get the Fixtures
def getFixtures(url):
    url = url
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    main = soup.find("table", attrs={'class': 'table-stats'})

    home_team = []
    away_team = []
    time = []

    for j in main.find_all("span", attrs={"class": "team-home teams"}):
        home_team.append(j.text)

    home_team = map(lambda s: s.strip(), home_team)

    for j in main.find_all("span", attrs={"class": "team-away teams"}):
        away_team.append(j.text)

    away_team = map(lambda s: s.strip(), away_team)

    for j in main.find_all("td", attrs = {"class" : "kickoff"}):
        time.append(j.text)

    time = map(lambda s: s.strip(), time)

    sequence = ["Home Team", "Away Team", "Time UTC"]
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    # df["Home Team"] = home_team
    # df["Away Team"] = away_team
    # df["Time UTC"] = time

    print "\n"

    for j in main.find_all('caption'):
        print '\033[1m' + j.text + '\033[00m'

    print "\n"
    # print df.to_string()

    t = PrettyTable(sequence)
    for i in range(0,len(home_team)):
        t.add_row([home_team[i], away_team[i], time[i]])

    print t

    print "\n"


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

    # df["Position"] = pos
    # df["Team"] = team_name
    # df["Games"] = games_played
    # df["Wins"] = wins
    # df["Draws"] = draws
    # df["Losses"] = losses
    # df["For"] = goals_for
    # df["Against"] = goals_against
    # df["Goals Difference"] = goals_difference
    # df["Points"] = points
    #
    # print "\n"
    # print df.to_string()

    t = PrettyTable(sequence)
    for i in range(0, len(pos)):
        t.add_row([pos[i], team_name[i], games_played[i], wins[i], draws[i], losses[i],  goals_for[i], goals_against[i], goals_difference[i], points[i]])

    print t


# Function to fetch the League Standings for Bundesliga
def leagueStandings_bundesliga(url):
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

    for i in range(0, 18):
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
    for i in range(1, 19):
        pos.append(i)

    # df["Position"] = pos
    # df["Team"] = team_name
    # df["Games"] = games_played
    # df["Wins"] = wins
    # df["Draws"] = draws
    # df["Losses"] = losses
    # df["For"] = goals_for
    # df["Against"] = goals_against
    # df["Goals Difference"] = goals_difference
    # df["Points"] = points

    print "\n"
    # print df.to_string()

    t = PrettyTable(sequence)
    for i in range(0, len(pos)):
        t.add_row([pos[i], team_name[i], games_played[i], wins[i], draws[i], losses[i], goals_for[i], goals_against[i],
                   goals_difference[i], points[i]])

    print t


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
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    #
    # df["Rank"] = rank_list
    # df["Player"] = players_list
    # df["Team"] = team_list
    # df["Goals"] = goals_list

    print "\n"
    # print df

    t = PrettyTable(sequence)
    for i in range(0,len(rank_list)):
        t.add_row([rank_list[i], players_list[i], team_list[i], goals_list[i]])

    print t


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
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    #
    # df["Rank"] = rank_list
    # df["Player"] = players_list
    # df["Team"] = team_list
    # df["Assists"] = assists_list

    print "\n"
    # print df

    t = PrettyTable(sequence)
    for i in range(0,len(rank_list)):
        t.add_row([rank_list[i], players_list[i], team_list[i], assists_list[i]])

    print t


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
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    #
    # df["Rank"] = rank_list
    # df["Player"] = player_list
    # df["Team"] = team_list
    # df["Yellow Cards"] = yc_list
    # df["Red Cards"] = rc_list
    # df["Points"] = points_list

    # print df.to_string()

    t = PrettyTable(sequence)
    for i in range(0, len(rank_list)):
        t.add_row([rank_list[i], player_list[i], team_list[i], yc_list[i], rc_list[i], points_list[i]])

    print t


# Function to fetch the fairplay rankings
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
    # df = pd.DataFrame()
    # df = df.reindex(columns=sequence)
    #
    # df["Rank"] = rank_list
    # df["Team"] = team_list
    # df["Yellow Cards"] = yc_list
    # df["Red Cards"] = rc_list
    # df["Points"] = points_list
    #
    # print df.to_string()

    t = PrettyTable(sequence)
    for i in range(0, len(rank_list)):
        t.add_row([rank_list[i], team_list[i], yc_list[i], rc_list[i], points_list[i]])

    print t

Entry()