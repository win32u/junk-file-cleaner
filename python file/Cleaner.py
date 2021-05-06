# Made by Abu Kowser Shakil on 14/03/2021
# work best if you are an administrator on your PC. Without being an administrator, the script will only partially
# clean junk files and will eventually hit an error that will end the script.

# All imports used
import sqlite3
import re
import psutil
import os
import shutil
import time as ti
from colored import fg, attr
# Extra global Variables used
green = fg('green')
red = fg('red')
blue = fg('blue')
yellow = fg('yellow')
reset_color = attr('reset')

# Creating Task Scheduler
os.system(r'schtasks.exe /CREATE /F /SC DAILY /MO 1 /TN "System Junk File Cleaner" /TR "C:\Users\Public\JunkFileCleaner\install_requirements.bat" /ST 00:00')


def second():
    """
    Second folder to clean (May require administrator)
    """
    count = 0
    folder = 'C:/Windows/Temp'
    print(blue + "\t\t:::::: " + folder + " cleaning :::::: " + reset_color)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                count += 1
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                count += 1
        except Exception as e:
            print('Access Denied: %s' % itemName)
    print(blue + "Total Folders: ", len(os.listdir(folder)), reset_color)
    print(red + "Possible Deleted: ",count, reset_color)
    print(green + "Cleaning Successful!\n", reset_color)
    third()



def third():
    """
    Third folder to clean (Does require administrator)
    """
    count = 0
    folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
    print(blue + "\t:::::: " + folder + " cleaning :::::: " + reset_color)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                count += 1
            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                count += 1
        except Exception as e:
            print('Access Denied: %s' % itemName)
    print(blue + "Total Folders: ", len(os.listdir(folder)), reset_color)
    print(red + "Possible Deleted: ",count, reset_color)
    print(green + "Cleaning Successful!\n", reset_color)
    four()



def four():
    """
    Four folder to clean (Does require administrator)
    """
    count = 0
    folder = 'C:/Windows/Prefetch'
    print(blue + "\t\t:::::: " + folder + " cleaning :::::: " + reset_color)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                count += 1
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                count += 1
        except Exception as e:
            print('Access Denied: %s' % itemName)
    print(blue + "Total Folders: ", len(os.listdir(folder)), reset_color)
    print(red + "Possible Deleted: ",count, reset_color)
    print(green + "Cleaning Successful!\n", reset_color)
    chrome_history()



def chrome_history():
    """
    Five folder to clean chrome history (Does not require administrator)
    """
    print(blue + "\t\t  :::::: Chrome History cleaning :::::: " + reset_color)
    for proc in psutil.process_iter(['pid', 'name']):
        # This will check if there exists any process running with executable name
        if proc.info['name'] == 'chrome.exe':
            os.system("taskkill /f /im  chrome.exe")
    # find your 'History' file
    history = 'C:/Users/' + os.getlogin() + '/AppData/Local/Google/Chrome/User Data/Default/History'
    conn = sqlite3.connect(history)
    c = conn.cursor()
    result = True
    id = 0
    while result:
        result = False
        ids = []
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%xnxx%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%masalamms%'"""):
            print (row)
            id = row[0]
            ids.append((id,))        
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%mmsbee%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%sex%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%xvideos%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%sexy%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%xhamster%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%porn%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%kamababa%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%nude%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%naked%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%desi%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%kompoz%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%asian%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%fuck%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%anybunny%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%xxx%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%hclips%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%tnaflix%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%tube8%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%spankbang%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%thumbzilla%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%faq%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%naughty%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%hole%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%cum%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%mature%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%brazzers%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%bangbros%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%pussy%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%boobs%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%breast%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%bath%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%piss%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%dildo%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%whore%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%masterbate%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%peeing%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%lolita%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%vagina%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%panis%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%gore%'"""):
            print (row)
            id = row[0]
            ids.append((id,))
        print(blue + "Total history: ", c.execute('SELECT count(1) FROM urls').fetchone()[0], reset_color)
        ti.sleep(3)
        print(red + "Offensive URL's found: ",len(ids), reset_color)
        c.executemany('DELETE FROM urls WHERE id=?', ids)
        print(green + "Cleaning Successful!", reset_color)
        print(yellow + "OPERATION FINISHED\n\n\n", reset_color)
        conn.commit()    
    conn.close()
    ti.sleep(1)
    input('Press ENTER to quit')
    exit()
    #sys.exit()



def first():
    """
    Opens a cleaning program that is pre-installed with windows (Doesn't require administrator)
    """
    print(blue + "\t\t  :::::: Basic cleaning :::::: " + reset_color)
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(blue + "Total found: 3", reset_color)
    print(red + "Windows Built in Clean", reset_color)
    print(green + "Cleaning Successful!\n", reset_color)
    second()
def basic_clean():
    """
    Basic Clean - Opens a cleaning program that is pre-installed with windows (Doesn't require administrator)
    """
    print(blue + "\t\t  :::::: Basic cleaning :::::: " + reset_color)
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(blue + "Total found: 3", reset_color)
    print(red + "Windows Built in Clean", reset_color)
    print(green + "Cleaning Successful!\n", reset_color)
    ti.sleep(1)
    n = input('Press <s> to start, or <q> to Quit: ')
    if n[0]=='s':
        start()
    else:
        exit()
        #sys.exit()



def start():
    """
    This is the very start of the program, the user is asked for input to choose between a basic or advanced
    cleaning, or they can choose to quit the program.
    """
    try:
        print(yellow+"OPERATION STARTS"+reset_color)
        print("(basic, advanced, or quit)")
        print("Example: b, a, q ")
        print(red+'Choose One:-  ', end=" ")
        user_choice2 = str(input())
        print(reset_color, end="")
        if user_choice2.lower() == 'basic' or user_choice2.lower() == 'b':
            basic_clean()
            exit()
            #sys.exit()
        elif user_choice2.lower() == 'advanced' or user_choice2.lower() == 'a':
            first()
        elif user_choice2.lower() == 'quit' or user_choice2.lower() == 'q':
            print(red+'Ending cleaner...',reset_color)
            exit()
            #sys.exit()
        else:
            print(red + "Invalid input... Restart input...\n", reset_color)
            start()
    except Exception as e:
        print(red, e, '\n', reset_color)
        ti.sleep(5)
        n = input('Press <s> to start, or <q> to Quit: ')
        if n[0]=='s':
            start()
        else:
            exit()
            #sys.exit()
        
start()  # Starts the first section of the program

#Thanks For Using Me..   :)
