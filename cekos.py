import os
import time
import platform
def Win() :
    os.system('cls')
def other() :
    os.system('clear')
def main() :
    result = os.name
    platfrm = platform.system()
    # length = [1,2,3]
    # x = 2
    # print(result)
    print('Your Operating System is ' + str(platfrm) + '\n')
    time.sleep(1)
    if result == 'nt' :
        for deva in reversed(range(0,4)) :
            print('Clear in',deva)
            time.sleep(1)
        Win()
    else :
        for deva in reversed(range(0,4)) :
            print('Clear in',deva)
            time.sleep(1)
        other()
        
main()
