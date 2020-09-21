#!usr/bin/env python3

import sqlite3
import os

def getDownloads(downloadDB):
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
        print('\n[*] --- Files Downloaded --- ')
        for row in cursor:
            print('[+] File: ' + str(row[0]) + ' from source: ' + str(row[1]) + ' at: ' + str(row[2]))
    except Exception as exception:
        print('\n[*] Error reading moz_downloads database ',exception)

def getCookies(cookiesDB):
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')

        print('\n[*] -- Found Cookies --')
        for row in cursor:
            print('[+] Host: ' + str(row[0]) + ', Cookie: ' + str(row[1]) + ', Value: ' + str(row[2]))
    except Exception as exception:
        print('\n[*] Error reading moz_cookies database ',exception)


def getHistory(placesDB):
    try:
        connection = sqlite3.connect(placesDB)
        cursor = connection.cursor()
        cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id== moz_historyvisits.place_id;")
        print('\n[*] -- Found History --')
        for row in cursor:
            print('[+] ' + str(row[1]) + ' - Visited: ' + str(row[0]))
    except Exception as exception:
            print('\n[*] Error reading moz_places,moz_historyvisits databases ',exception)


def main():
        if os.path.isfile('downloads.sqlite'):
            getDownloads('downloads.sqlite')
        else:
            print('[!] downloads.sqlite not found ')
        
        if os.path.isfile('cookies.sqlite'):
            getCookies('cookies.sqlite')
        else:
            print('[!] cookies.sqlite not found ')
        
        if os.path.isfile('places.sqlite'):
            getHistory('places.sqlite')
        else:
            print('[!] places.sqlite not found: ')

if __name__ == '__main__':
    main()

