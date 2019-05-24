import shelve

#Form: ,macro name stuff
#,unmacro name

def create(user, list):
    if not user:
        return -1
    if(len(list) < 2):
        return -1
    
