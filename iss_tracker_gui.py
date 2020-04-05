import sys
import easygui
from easygui import *
import random
import os
import urllib.request
import json
from termcolor import colored
import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import datetime
#from colorama import init
#from colorama import Fore, Back, Style
#init()

loop = 2
while (loop==2):
    
    def exit_program():
        image = "warning.png"
        msg = "Do you want to Quit the Program?"
        title = "Quit Program?"
        choices = ["Yes", "No"]
        choice = buttonbox(msg, title, choices, image=image)
        if choice == "Yes":
            sys.exit(0)
        else:
            pass


    def main_menu():
        
        image = "iss.png"
        #msg ="SELECT AN OPTION FROM THE MENU"
        msg = " "
        title = "ISS TRACKER PROGRAM"
        choices = ["ISS Tracker", "EXIT PROGRAM"]
        choice = buttonbox(msg ,title, image=image, choices=choices)

        if choice == "ISS Tracker":
            def ISS_Tracker():
                title = "ISS Tracker Program"
                image = 'notes.png'
                iss = "ISS.png"
                image2= 'warning2.png'
                gnome_msg = ("You accessed the ISS Tracker program!")
                gnome_buttons = ["Run ISS Tracker", "<- Back to Main screen", "View ISS current coordinates", "Show ISS location in Google Maps", "Spot the ISS at spotthestation.nasa.gov/tracking_map.cfm", "Exit Program"] 
                choice = buttonbox(gnome_msg, title, gnome_buttons, image=iss)
                if choice == "Run ISS Tracker":
                    def ISS_Settings():

                        satellite = "iss_small.png"
                        msg = "Enter amount of pictures to take, and amount of seconds interval."
                        title = "ISS Tracker Screenshots program"
                        global pictures
                        pictures = integerbox("The program will access 'http://api.open-notify.org/iss-now.json' API\n\nto get the real time Latitude and Longitud coordinates of the ISS.\n\nBased on them, it will to take pictures from Google Maps.\n\nEnter amount of Pictures you want to take from Google Maps: ", title, upperbound=10000000, image=satellite)
                        if pictures == 0:
                            image = "warning.png"
                            msgbox("Please enter a value greater than 0", title, image=image)
                            ISS_Settings()
                        if pictures == None:
                            image = "warning.png"
                            msg = "Cancel and go Back to Options Menu?"
                            title = "Cancel operation?"
                            choices = ["Yes", "No", "EXIT PROGRAM"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                ISS_Tracker()
                            if choice == "No":
                                ISS_Settings()
                            if choice == "EXIT PROGRAM":
                                image = "warning.png"
                                msg = "Do you want to Quit the Program?"
                                title = "Quit Program?"
                                choices = ["Yes", "No"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "Yes":
                                    sys.exit(0)
                                if choice == "No":
                                    ISS_Settings()
                                
                            
                        else:
                            photos = "photos.png"
                            def Interval_time():    
                                title = "Seconds Interval"
                                seconds_image = "seconds.png"
                                global seconds
                                seconds = integerbox("--> Amount of pictures to take: "+str(pictures)+"\n\n--> Enter seconds interval until next picture is taken: ", title, upperbound=10000000, image=seconds_image)
                                if seconds == None or seconds == 0:
                                    image = "warning.png"
                                    msg = "No valid input was provided. A number greater than 0 must be entered.\n\nCancel and go Back to Options Menu?"
                                    title = "Cancel operation?"
                                    choices = ["Yes", "No", "<-- Back to Amount of Pictures screen", "EXIT PROGRAM"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        ISS_Tracker()
                                    if choice == "No":
                                        Interval_time()
                                    if choice == "<-- Back to Amount of Pictures screen":
                                        ISS_Settings()
                                    if choice == "EXIT PROGRAM":
                                        msg = "Do you want to Quit the Program?"
                                        title = "Quit Program?"
                                        choices = ["Yes", "No"]
                                        choice = buttonbox(msg, title, choices, image=image)
                                        if choice == "Yes":
                                            sys.exit(0)
                                        if choice == "No":
                                            Interval_time()
                                            
                                        
                                if seconds > 0:
                                    correct = "good.png"
                                    timer = "timer.png"
                                    def data_provided():
                                        title = "ISS defined settings screen"
                                        message = "Data provided: \n\n"+"--> "+str(pictures)+" Pictures\n\n"+"--> "+str(seconds)+" seconds interval\n\n * To confirm and run program now, press: RUN PROGRAM NOW.\n\n * To re-set amount of pictures, press: <-- Back to amount of pictures screen\n\n * To re-set amount of seconds, press: <-- Back to seconds interval screen"
                                        Yes = "Yes, run program now"
                                        yes_no_buttons = ['RUN PROGRAM NOW', '<-- Back to amount of pictures screen', '<-- Back to seconds interval screen', "EXIT PROGRAM"]
                                        choice = buttonbox(message, title, yes_no_buttons, image=timer)
                                        if choice == "RUN PROGRAM NOW":
                                            
                                            def api_request_and_vars():
                                                ## Trace the ISS - earth.orbital space station
                                                eoss = 'http://api.open-notify.org/iss-now.json'
                                                #Call the webserver
                                                trackiss = urllib.request.urlopen(eoss)
                                                #put into file object
                                                ztrack = trackiss.read()
                                                #json 2 python data structure
                                                result = json.loads(ztrack.decode('utf-8'))
                                                #display our pythonic data
                                                location = result['iss_position']#from 'result variable, obtain the tag 'iss_possition' into a list
                                                timesStamp = result['timestamp']
                                                message = result['message']
                                                global lat, lon, comma, space, lines #these functions can be called from another function
                                                lat = location['latitude']
                                                lon = location['longitude']
                                                lat = str(lat)
                                                lon = str(lon)
                                                now = datetime.now()
                                                yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                                                hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                                                todayis = (str(yymmday)+"-"+str(hhmmss))
                                                minutes = round(timesStamp/60)
                                                hours = round(minutes/60)
                                                day = round(hours/24)
                                                weeks = round(day/7)
                                                months = round(day/30)
                                                years = round(months/12)
                                                comma = ","
                                                space = " "
                                                global hashtags
                                                lines = ("-------------------------------------------------")
                                                hashtags = ("#################################################")
                                                log = open('iss_tracker.log', 'a')
                                                print(result)
                                                log.write('\n'+hashtags)
                                                log.write('\n'+"Actual date and time: "+todayis)
                                                print(lines)
                                                log.write('\n'+hashtags)
                                                print('Hours: '+str(hours)+' Minutes: '+str(minutes))
                                                log.write('\n'+'Hours: '+str(hours)+' Minutes: '+str(minutes))
                                                print('Actual Timestamp: '+str(timesStamp)+" in seconds")
                                                log.write('\n'+(lines))
                                                log.write('\n'+'Actual Timestamp: '+str(timesStamp)+' in seconds')
                                                log.write('\n'+(lines))
                                                print("-------------------------------------------------")
                                                log.write('\n'+'Latitude: '+str(lat))
                                                print('Latitude: '+str(lat))
                                                log.write('\n'+(lines))
                                                print("-------------------------------------------------")
                                                print('Longitude: '+str(lon))
                                                log.write('\n'+'Longitude: '+str(lon))
                                                print("-------------------------------------------------")
                                                log.write('\n'+(lines))
                                                print('Message: '+ message)
                                                log.write('\n'+'Message: '+ message)
                                                pass

                                            def timenow():
                                                global timenow
                                                global todayis, todaysdate, yymmday, hhmmss #these functions can be called from another function
                                                now = datetime.now()
                                                yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                                                hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                                                todayis = (str(yymmday)+"-"+str(hhmmss))
                                                print("Today is: "+str(yymmday)+" "+str(hhmmss))
                                                pass



                                            def main_satellite():
                                                
                                                
                                                    print("-------------------------------------------------")
                                                    print("Google Maps Module accessed.")
                                                    print("Triggering selenium webdriver to open browser...")

                                                    global driver
                                                    driver = webdriver.Firefox()
                                                    #driver = webdriver.Chrome()
                                                    driver.get("https://maps.google.com")
                                                    print("-------------------------------------------------")
                                                    print("Working directory is:")
                                                    pwd = os.system("pwd")
                                                    print("-------------------------------------------------")
                                                    global amount_of_repetitions
                                                    amount_of_repetitions = pictures
                                                    amount_of_repetitions = int(amount_of_repetitions)
                                                    global number
                                                    for number in range(amount_of_repetitions,0,-1):
                                                        if number == 1:
                                                            print("-------------------------------------------------")
                                                            print("Program terminated, returning to main menu again.")
                                                            print("-------------------------------------------------")
                                                            main_menu()
                                                        
                                                        elif number >1 :
                                                            loop = 1
                                                            while (loop==1):
                                                                
                                                                for number in range(amount_of_repetitions,0,-1):
                                                                    print("-------------------------------------------------")
                                                                    print("Amount of remaining iterations: "+str(number))
                                                                    print("-------------------------------------------------")
                                                                    print("Refresh interval in seconds set to: "+str(seconds))
                                                                    print("-------------------------------------------------")
                                                                    print("\n\nShowing ISS coordinates")
                                                                    timenow()
                                                                    print("-------------------------------------------------")
                                                                    api_request_and_vars()
                                                                    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(lat+comma+space+lon)
                                                                    driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
                                                                    print("-------------------------------------------------")
                                                                    cwd = os.getcwd()
                                                                    path = cwd
                                                                    for remaining_seconds in range(int(seconds),0,-1):
                                                                        print("Refreshing in: " +str(remaining_seconds))
                                                                        time.sleep(1)
                                                                        if remaining_seconds == 1:
                                                                            print("-------------------------------------------------")
                                                                            now = datetime.now()
                                                                            yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                                                                            hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second)
                                                                            todayis = (str(yymmday)+"-"+str(hhmmss))
                                                                            name_and_path_to_screenshots = (datepath+"/"+str(number)+"-ISS"+"-"+str(todayis)+".png")
                                                                            driver.save_screenshot(name_and_path_to_screenshots)
                                                                            print("The screenshot was saved to: " + name_and_path_to_screenshots)
                                                                            print("-------------------------------------------------")
                                                                            if number == 1:
                                                                                print("-------------------------------------------------")
                                                                                print("Program finished, returning to main menu...")
                                                                                main_menu()
                                                                            else:
                                                                                print("Waiting other 5 seconds to process picture in path...")
                                                                                for remaining_seconds in range(5,0,-1):
                                                                                    print("-------------------------------------------------")
                                                                                    print("Refreshing in: " +str(remaining_seconds))
                                                                                    time.sleep(1)
                                                                                    if remaining_seconds == 1:
                                                                                        driver.find_element_by_xpath('//*[@id="searchboxinput"]').clear()

                                                                                    elif number == 1:
                                                                                        print("-------------------------------------------------")
                                                                                        print("Program finished, returning to main menu...")
                                                                                        main_menu()

                                                                                    elif remaining_seconds < 1:
                                                                                        print("-------------------------------------------------")
                                                                                        print("Program finished, returning to main menu...")
                                                                                        main_menu()
                                                                                        pass
                                                                

                                            def directory_check():
                                                global cwd, path, create_folder, datepath
                                                cwd = os.getcwd()
                                                path = cwd
                                                now = datetime.now()
                                                yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                                                create_folder = str(yymmday)
                                                datepath = (path+"/"+create_folder)
                                                print("Current working directory is: "+cwd)
                                                cwd = os.getcwd()
                                                path = cwd
                                                try:
                                                    os.mkdir(datepath)
                                                    if datepath == (cwd+"/"+create_folder):
                                                        
                                                        print("#################################################")
                                                        print("Cannot create the directory as it already exists")
                                                        print("The screenshots of the ISS location will be")
                                                        print("in the existing path: "+path+"/"+create_folder)
                                                        main_satellite()
                                                except:
                                                    
                                                    print("#################################################")
                                                    print ("Successfully created the directory "+datepath)
                                                    print("The screenshots of the ISS location will be")
                                                    print("stored in the path created above")
                                                    main_satellite()

                                            directory_check()

                                            

                                            
                                        if choice == "<-- Back to amount of pictures screen":
                                            ISS_Settings()

                                        if choice == "<-- Back to seconds interval screen":
                                            Interval_time()

                                        if choice == "EXIT PROGRAM":
                                            image2= 'warning2.png'
                                            msg = "Do you want to Quit the Program?"
                                            title = "Quit Program?"
                                            choices = ["Yes", "No"]
                                            choice = buttonbox(msg, title, choices, image=image2)
                                            if choice == "Yes":
                                                sys.exit(0)
                                            if choice == "No":
                                                data_provided()

                                    data_provided()
                           

                        Interval_time()

                    ISS_Settings()

                if choice == "View ISS current coordinates":
                        ## Trace the ISS - earth.orbital space station
                        eoss = 'http://api.open-notify.org/iss-now.json'
                        #Call the webserver
                        trackiss = urllib.request.urlopen(eoss)
                        #put into file object
                        ztrack = trackiss.read()
                        #json 2 python data structure
                        result = json.loads(ztrack.decode('utf-8'))
                        #display our pythonic data
                        location = result['iss_position']#from 'result variable, obtain the tag 'iss_possition' into a list
                        timesStamp = result['timestamp']
                        message = result['message']
                        global lat, lon, comma, space, lines #these functions can be called from another function
                        lat = location['latitude']
                        lon = location['longitude']
                        lat = str(lat)
                        lon = str(lon)
                        now = datetime.now()
                        yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                        hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                        todayis = (str(yymmday)+"-"+str(hhmmss))
                        minutes = round(timesStamp/60)
                        hours = round(minutes/60)
                        day = round(hours/24)
                        weeks = round(day/7)
                        months = round(day/30)
                        years = round(months/12)
                        comma = ","
                        space = " "
                        global hashtags
                        lines = ("-------------------------------------------------")
                        hashtags = ("#################################################")
                        log = open('iss_tracker.log', 'a')
                        title = "ISS ACTUAL COORDINATES AND TIME"
                        ISS_MSG = "SHOWING ISS CURRENT LOCATION COORDINATES AND TIME:\n\nDATA PROVIDED BY http://api.open-notify.org/iss-now.json API.\n\nCLICK IMAGE OR ICON TO GO BACK TO PREVIOUS SCREEN."
                        print("ISS CURRENT LOCATION COORDINATES AND TIME: ")
                        print("-------------------------------------------------")
                        print(result)
                        log.write('\n'+hashtags)
                        log.write('\n'+"Actual date and time: "+todayis)
                        print(lines)
                        log.write('\n'+hashtags)
                        hours_minutes_seconds = 'Hours: '+str(hours)+' Minutes: '+str(minutes)+'\n\n'
                        print('Hours: '+str(hours)+' Minutes: '+str(minutes))
                        log.write('\n'+'Hours: '+str(hours)+' Minutes: '+str(minutes))
                        timestamp = 'Actual Timestamp: '+str(timesStamp)+" in seconds\n\n"
                        print('Actual Timestamp: '+str(timesStamp)+" in seconds")
                        log.write('\n'+(lines))
                        log.write('\n'+'Actual Timestamp: '+str(timesStamp)+' in seconds')
                        log.write('\n'+(lines))
                        print("-------------------------------------------------")
                        Latitude = 'Latitude: '+str(lat)+'\n\n'
                        Longitud = 'Longitude: '+str(lon)+'\n\n'
                        log.write('\n'+'Latitude: '+str(lat))
                        print('Latitude: '+str(lat))
                        log.write('\n'+(lines))
                        print("-------------------------------------------------")
                        print('Longitude: '+str(lon))
                        log.write('\n'+'Longitude: '+str(lon))
                        print("-------------------------------------------------")
                        log.write('\n'+(lines))
                        Message_from_API = 'Message from API: '+ message+'\n\n'
                        print('Message: '+ message)
                        log.write('\n'+'Message: '+ message)

                        now = datetime.now()
                        yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                        hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
                        todayis = (str(yymmday)+"-"+str(hhmmss))
                        digital_planet = "digital_planet.png"
                        print("Today is: "+str(yymmday)+" "+str(hhmmss))
                        msgbox(ISS_MSG, title, "TODAY IS: "+str(yymmday)+' AND THE TIME IS: '+str(hhmmss)+'\n\n''Hours: '+str(hours)+' Minutes: '+str(minutes)+'\n\n''Actual Timestamp: '+str(timesStamp)+" in seconds\n\n"'Latitude: '+str(lat)+'\n\n''Longitude: '+str(lon)+'\n\n''Message from API: '+ message+'\n\n', image=digital_planet)

                        ISS_Tracker()

                if choice == "Show ISS location in Google Maps":
                    print("Google Maps Module accessed.")
                    print("Triggering selenium webdriver to open browser...")
                    driver = webdriver.Firefox()
                    #driver = webdriver.Chrome()
                    driver.get("https://maps.google.com")
                    print("-------------------------------------------------")
                    print("Showing current location of ISS in Google Maps.")
                    ## Trace the ISS - earth.orbital space station
                    eoss = 'http://api.open-notify.org/iss-now.json'
                    #Call the webserver
                    trackiss = urllib.request.urlopen(eoss)
                    #put into file object
                    ztrack = trackiss.read()
                    #json 2 python data structure
                    result = json.loads(ztrack.decode('utf-8'))
                    #display our pythonic data
                    location = result['iss_position']#from 'result variable, obtain the tag 'iss_possition' into a list
                    lat = location['latitude']
                    lon = location['longitude']
                    lat = str(lat)
                    lon = str(lon)
                    comma = ","
                    space = " "
                    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(lat+comma+space+lon)
                    driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
                    ISS_Tracker()

                if choice == "Spot the ISS at spotthestation.nasa.gov/tracking_map.cfm":
                    print("Opening isstracker.com....")
                    print("Triggering selenium webdriver to open browser...")
                    driver = webdriver.Firefox()
                    #driver = webdriver.Chrome()
                    driver.get("https://spotthestation.nasa.gov/tracking_map.cfm")
                    print("-------------------------------------------------")
                    print("Showing current location of ISS in isstracker.com.")
                    ISS_Tracker()
                    
                if choice == "<- Back to Main screen":
                    main_menu()

                if choice == "Exit Program":
                    exit_program()
                        
            ISS_Tracker()


        if choice == "EXIT PROGRAM":
            exit_program()

    main_menu()

    
