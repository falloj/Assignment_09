#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# JFallon, 2022-Mar-27, added code to handle tracks on an individual CD
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx) # This selects the CD from the list of CD objects
        # TODone add code to handle tracks on an individual CD
        # Model the sub-menu of CD options after the main menu
        while True:
            # Print menu options for that CD
            IO.ScreenIO.print_CD_menu()
            # Let the user select an option for that CD
            trackChoice = IO.ScreenIO.menu_CD_choice() 
            # Use if statements to execute the various options
            if trackChoice == 'x':
                break
            if trackChoice == 'a':
                # add track
                tplTrackInfo = IO.ScreenIO.get_track_info() # get user info about track
                PC.DataProcessor.add_track(tplTrackInfo, cd) # instantiate a new track object and it to the CD
            if trackChoice == 'd':
                # display cd
                IO.ScreenIO.show_tracks(cd)
            if trackChoice == 'r':
                # remove track
                track_idx = input('Please enter the postion for the track you would like to remove: ')
                cd.rmv_track(track_idx)
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')