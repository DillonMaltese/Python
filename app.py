#import subprocess
#subprocess.Popen('C:\\Windows\\System32\\calc.exe')

import time, psutil
def checkIfProcessRunning(processName):
        '''Check if there are any running process that contains the given name processName.
        Iterate over the all the running process'''
        print('Checking if application is running...')
        for proc in psutil.process_iter():
                try:
                        # Check if process name contains the given name string.
                        if processName.lower() in proc.name().lower():
                                return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        return False;

chromeRunning = True
while chromeRunning:
    if checkIfProcessRunning('Music'):
        #Only happens if the program is running
        print('Instance of Chrome is Running...waiting.')
        time.sleep(10) # Wait 30 seconds and try again
        print('Checking again...')
    else:
        #Only happens if the program is not running
        print('Chrome is not running, good to go.')
        chromeRunning = False # Sets chromeRunning False to exit loop