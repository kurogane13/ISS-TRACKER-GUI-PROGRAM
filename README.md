# ISS-TRACKER-GUI-PROGRAM

*NOTE: You can View the GUI screenshots in the Screenshots folder. To view a video of the program running, access the Videos_tutorials folder.
----------------------------------------------------------------------------------------------------------------

GUI version of the ISS tracker program - Author: Gustavo Wydler Azuaga - 04/06/2020
----------------------------------------------------------------------------------------------------------------

This program is a python api-client that tracks the ISS (International space spation) coordinates.

* It tracks the ISS from a public API(http://api.open-notify.org/iss-now.json), parses the json format to text, and displays   its actual coordinates in the console.

* You can pre-select the iterations(How many times to show snapshots and coordinates), and refresh intervals(Amount of        seconds to show coordinates). 

* It will open Google Maps with firerox(using selenium, and show the ISS coordinates as they change, 
  taking snapshots of every location to store them in a folder by date. It also has a log file, 
  where it appends the raw data in txt format.

* You can also view the coordinates in a single GUI window, spot the ISS´s location in the      spotthestation.nasa.gov/tracking_map.cfm portal through selenium as well.

---------------------------------------------------------------------------------------------------------------------------

ATTACHMENTS: I am attaching the program(iss_tracker_gui.py), and the selenium web driver (geckodriver-v0.22.0-linux64.tar.gz) which i used to trigger selenium.

---------------------------------------------------------------------------------------------------------------------------

Setup instructions:

1. Make sure to install all the python libraries before running the program.
2. Decompress geckodriver-v0.22.0-linux64.tar.gz in /usr/bin/ (sudo tar -xvzf geckodriver-v0.22.0-linux64.tar.gz -C /usr/bin)
or executable path.
3. Run the program with python 3 (python3.6 iss_tracker_gui.py) . Tested with python3.6
 
IMPORTANT NOTE: ALL THE .png IMAGES MUST BE IN THE PATH WHERE THE PROGRAM IS LAUNCHED FROM.

IF THE PROGRAM IS LAUNCHED FROM THE /home/$USER path, THEY SHOULD BE THERE WHEN OPENING WITH THE TERMINAL.

ALSO, THE .png FILES SHOULD BE IN THE FOLDER WITH THE iss_tracker_gui.py

---------------------------------------------------------------------------------------------------------------------------

Hope you like it!.
 
