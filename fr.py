#!/usr/bin/env python
#############################################################
# fr - find and replace                                     #
# script to open a file and replace every instance          #
#   of a given string with another, primary purpose is for  #
#   retabbing files                                         #
#                                                           # 
#   -s --space NUM                                          #
#       NUM is the number of sequential spaces              #
#   -t --tab NUM                                            #
#       NUM is the number of sequential tab characters      #
#   -c --characters CHAR                                    #
#       CHAR is the character sequence                      #
#   -i --indent-only                                        #
#       only change indents                                 #
#   -f --first NUM                                          #
#       only replace first NUM occurrences, defaults        #
#       to 1                                                #
#############################################################

import sys
import os
import pdb

commands = ['-c','--characters','-s','--space','-t','--tab','-i','--indent-only','-f','--first']

print sys.argv

def pBadArg(arg):
    if arg:
        sys.stderr.write("Error: Unexpected Argument " + arg) 
    else:
        sys.stderr.write("Invalid arguments")
    quit()

def pUsage():
    sys.stdout.write("Usage: ")
    quit()

def isInt(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

def ignore():
    return

hasFile = False
verbose = False
prev = None
find = None
replace = None
tabs = None
spaces = None

def pDebug(arg):
    if arg is not None:
        print "curArg: " + arg
    print "hasFile: " + str(hasFile)
    print "verbose: " + str(verbose)
    print "prev: " + str(prev)
    print "find: " + str(find)
    print "replace: " + str(replace)
    print "tabs: " + str(tabs)
    print "spaces: " + str(spaces)

for arg in sys.argv:

    if arg == sys.argv[0]:
        continue

    elif os.path.isfile(arg):
        if not hasFile:
            print arg + " is a file: " + str(os.path.isfile(arg))
            #pDebug(arg)
            f = open(arg)
            source = f.read()
            f.close()
            hasFile = True
        else:
            pBadArg(arg)

    elif arg == "-t" or arg == "--tab":
        print "checking if " + arg
        #pDebug(arg)
        if replace:
            pBadArg(arg)
        elif find: 
            replace = '\t'
        else:
            find = '\t'

    elif arg == "-s" or arg == "--space":
        print "checking if " + arg
        #pDebug(arg)
        if replace: 
            pBadArg(arg)
        elif find:
            replace = ' '
        else:
            find = ' '

    elif prev == "-c" or prev == "--characters":
        if not prev: 
            pBadArg(arg)

        if replace: 
            pBadArg(arg)
        elif find: 
            replace = arg
        else:
            find = arg

    elif isInt(arg):
        if not prev: 
            pBadArg(arg)

        elif prev == "-s":
            spaces = int(arg)
        elif prev == "-t":
            tabs = int(arg)
        else:
            pBadArg(arg)

    elif arg in commands: 
        print "command " + arg + " is good"

    else:
        pBadArg(arg)

    prev = arg

if tabs: 
    if replace: 
        pBadArg(sys.argv[arg])
    elif find: 
        replace  = ""
        for x in range(0,tabs):
            replace += '\t' 
    else:
        find = ""
        for x in range(0,tabs):
            find += '\t' 

if spaces: 
    if find == ' ':
        for x in range(1,spaces):
            find += ' '
    elif replace == ' ':
        for x in range(1,spaces):
            replace += ' '

if tabs:
    if find == '\t':
        for x in range(1,tabs):
            find += '\t'
    elif replace == '\t':
        for x in range(1,tabs):
            replace += '\t'

#pdb.set_trace()
if find and replace: 
    if not hasFile:
        source = sys.stdin.read()        

    sys.stdout.write(repr(source.replace(find, replace)))
    sys.stdout.write('\n')
    sys.stdout.write(source.replace(find, replace))

else: pUsage()
