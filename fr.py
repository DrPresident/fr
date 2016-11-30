#!/usr/bin/env python

import sys
import os

commands = ['-c','-s','-t']

print sys.argv

def pBadArg(arg):
    if arg:
        print >> sys.stderr, "Error: Unexpected Argument " + arg 
    else:
        print >> sys.stderr, "Invalid arguments"
    quit()

def pUsage():
    print "Usage: "
    quit()

def isInt(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

hasFile = False
verbose = False
prev = None
find = None
replace = None
tabs = None
spaces = None

def pDebug(arg):
    if arg is not None:
        print "curArg: " + sys.argv[arg]
    print "hasFile: " + str(hasFile)
    print "verbose: " + str(verbose)
    print "prev: " + str(prev)
    print "find: " + str(find)
    print "replace: " + str(replace)
    print "tabs: " + str(tabs)
    print "spaces: " + str(spaces)

for arg in range(1,len(sys.argv)):

    if os.path.isfile(sys.argv[arg]):
        if not hasFile:
            print sys.argv[arg] + " is a file: " + str(os.path.isfile(sys.argv[arg]))
            pDebug(arg)
            f = open(sys.argv[arg])
            source = f.read()
            f.close()
            hasFile = True
        else:
            pBadArg(sys.argv[arg])

    elif sys.argv[arg] == "-t":
        print "checking if " + sys.argv[arg]
        pDebug(arg)
        if replace:
            pBadArg(sys.argv[arg])
        elif find: 
            replace = '\t'
        else:
            find = '\t'

    elif prev == "-c":
        if not prev: 
            pBadArg(sys.argv[arg])

        if replace: 
            pBadArg(sys.argv[arg])
        elif find: 
            replace = sys.argv[arg]
        else:
            find = sys.argv[arg]

    elif isInt(sys.argv[arg]):
        if not prev: 
            pBadArg(sys.argv[arg])

        elif prev == "-s":
            spaces = int(sys.argv[arg])
        elif prev == "-t":
            tabs = int(sys.argv[arg])
        else:
            pBadArg(sys.argv[arg])

    elif sys.argv[arg] in commands: 
        print "command " + sys.argv[arg] + " is good"

    else:
        pBadArg(sys.argv[arg])

    prev = sys.argv[arg]

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
    if replace: 
        pBadArg(sys.argv[arg])
     
    elif find: 
        replace  = ""
        for x in range(0,spaces):
            replace += ' ' 
    else:
        find = ""
        for x in range(0,spaces):
            find += ' ' 

if find and replace: 
    if not hasFile:
        source = sys.stdin.read()        

    for line in source:
        print source.replace(find, replace)

else: pUsage()
