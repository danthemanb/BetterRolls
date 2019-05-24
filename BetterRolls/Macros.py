import shelve
import os

#Form: ,macro name stuff
#,unmacro name

def create(user, list):
    if(len(list) < 2):
        return 1
    cmdKey = user+list[0]
    cmd=[]
    for i in range(1, len(list)):
        cmd += list[i]
    db = shelve.open("BetterRolls/macro.txt")
    db[cmdKey] = cmd
    db.close()
    return 0

def delete(user, cmdName):
    cmdKey = user+cmdName
    db = shelve.open("BetterRolls/macro.txt")
    flag = cmdKey in db
    if flag:
        del db[cmdKey]
    db.close()

def get(user, cmdName):
    cmdKey = user+cmdName
    db = shelve.open("BetterRolls/macro.txt")
    cmd = db[cmdKey]
    db.close()
    return cmd
