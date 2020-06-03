import os
import time
def Win() :
    os.system('cls')
def other() :
    os.system('clear')
def main() :
    result = os.name
    # length = [1,2,3]
    # x = 2
    # print(result)
    print(result)
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