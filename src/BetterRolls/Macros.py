import shelve
import os

#Form: ,macro name stuff
#,unmacro name
MACROPATH = "BetterRolls/macros/macro"

def create(user, list):
    if not user:
        return 1
    if not list:
        return 1
    cmdKey = user+list[0]
    '''
    cmd=""
    for i in range(1, len(list)):
        cmd += list[i]
        cmd += " "
    '''
    cmd = list[1:]
    print(f'Creating Macro {cmdKey} with data {cmd}')
    db = shelve.open(MACROPATH)
    db[cmdKey] = cmd
    db.close()
    return 0

def delete(user, cmdName):
    if not user:
        return 1
    if not cmdName:
        return 1
    cmdKey = user+cmdName
    print(f'Deleting Macro {cmdKey}')
    db = shelve.open(MACROPATH)
    flag = cmdKey in db
    if flag:
        del db[cmdKey]
    db.close()
    return 0

def get(user, cmdName):
    if not user:
        return None
    if not cmdName:
        return None
    cmdKey = user+cmdName
    db = shelve.open(MACROPATH)
    flag = cmdKey in db
    if not flag:
        return None
    cmd = db[cmdKey]
    print(f'Getting Macro {cmdKey} that had data {cmd}')
    db.close()
    return cmd
