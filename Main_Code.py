import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd

def epl():
    print '\033[1m' + "\nWelcome to English Premier League"

    print "Press 1 for League Standings"
    print "Press 2 for Top Scorers"
    print "Pr"


def menu():
    print "\nPress 1 for English Premier League"
    print "Press 2 for La liga"
    print "Press 3 for Bundesliga"

    choice = raw_input("Enter your choice : ")

    if choice == '1':
        epl()

    elif choice == '2':
        laliga()

    elif choice == '3':
        bundesliga()

    else:
        print "Invalid Choice"

def Entry():
    x = raw_input("\nDo you want to enter ? (Press y/n)")
    if x == 'y':
        print "\nWelcome to Football Client" + "\n"
        menu()
    elif x == 'n':
        exit()

Entry()