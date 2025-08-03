import time,os
a = '##### ##### #    # ##### #         # #####  ###  #   #   #   #####'
b = '    # #     ##   # #      #   #   #  #       #   #   #  # #  #   #'
c = '   #  ####  #  # # #  ##   # # # #   ####    #   ##### ##### #   #'
d = '  #   #     #   ## #   #    #   #    #       #   #   # #   # #   #'
e = '##### ##### #    # #####    #   #    #####  ###  #   # #   # #####'
i = 1
while(i<70):
    # Cross-platform screen clear command
    os.system('cls' if os.name == 'nt' else 'clear')
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    a = ' ' + a
    b = ' ' + b
    c = ' ' + c
    d = ' ' + d
    e = ' ' + e
    time.sleep(0.1)
    i = i + 1
    
