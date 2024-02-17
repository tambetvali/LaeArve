#
# This is simple test class.
#   It won't check the variables, but returns some data to check.
#   You can also turn on the more verbose mode to validate the code.
#   TODO: somebody might want to implement log files.

# ====================== Configuration ======================

do_the_tests = True
always_verbose = False

# ======================== Internals ======================== 

import colorama

testing = False
header = 0

#def testclass(cls):

def dothetests():
    global do_the_tests
    return do_the_tests

def beverbose():
    global testing, always_verbose
    return testing or always_verbose

def loghead(string, sender = "", level = 1):
    if beverbose():
        log()
        if sender: sender += ": "
        print(colorama.Fore.LIGHTBLUE_EX + "==" + sender + string + "==" + colorama.Fore.RESET)
        header = level

def logsubhead(string, sender = ""):
    if beverbose():
        if sender: sender += ": "
        print(colorama.Fore.RED + " ! " + colorama.Fore.RESET + sender + string)

def log(string = "", sender = ""):
    if beverbose():
        if sender: sender += ": "
        print("   " + sender + string)

def testhead(string):
    global testing
    if testing:
        log()
        print(colorama.Fore.LIGHTBLUE_EX + "=" + string + "=" + colorama.Fore.RESET)

def testsubhead(string):
    global testing
    if testing:
        print("     " + string)

def testfoot(string = "", sender = "", level = 0):
    global testing
    if testing:
        if sender: sender += ": "
        print(colorama.Fore.RED + " @ " + colorama.Fore.RESET + sender + string)
        header = level

def test(cls):
    global testing
    if testing:
        testable = cls(test = True)
        testable.test()
        del(testable)

def start_tests():
    global testing
    print("do tests: " + str(testing))
    testing = dothetests()

def stop_tests():
    global testing
    testing = False