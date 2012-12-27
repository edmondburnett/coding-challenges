#/usr/bin/env python2

# Challenge #104 [easy] Powerplant Simulation
# http://redd.it/11paok

def days_operational(num_days):
    """ Accept an int # of days and return # of days plant actually operated """
    n = 1;
    i = 0;
    while i < num_days:
        if i % 3 != 0 and i % 10 != 0 and i % 100 != 0: 
            n += 1
        i += 1
    return n

if __name__ == '__main__':
    days = input("Enter # of days to simulate power plant uptime: ")

    print "The plant was operational for " + str(days_operational(days)) \
            + " out of " + str(days) + " total days."
