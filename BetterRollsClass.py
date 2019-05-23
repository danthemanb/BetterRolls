import random
import re
from collections import namedtuple

class SingleGRoll(object):
    def __init__(self):
        self.num=1
        self.type='d'
        self.size=10

GResult = namedtuple('GResult', ['width','height'])

class BetterRoll(object):
    # Keeps track of an entire command given to the bot
    def __init__(self):
        self.diceList=[]
        self.formattedDice=""
        self.sum=0


    def getDiceList(self):
        list=""
        for die in self.diceList:
            list = list + f'[{die}] '
        return list

    def addTerm(self, term):
        self.diceList.append(term.dicelist)

#    def format(self):
        #Format the object

    def Roll(self, n, type):
            ''' Rolls n dice of size type.  For instance, 4d10.  Returns a list of results  '''
            res = [0] * n
            for i in range(n):
                res[i] = random.randint(1, type)
            return res

    def getFormattedDice(self):
        return self.formattedDice


class BetterGRoll(BetterRoll):
    def __init__(self):
        self.matches=[]
        self.formattedMatches=""
        self.wiggle=0
        super().__init__()

    def Calc(self, rollList):
        self.rollDice(rollList)
        matches = self.findMatches()
        print(f'matches is {matches}')
        output = self.format(matches)
        print(f'output is {output}')
        return output

    def rollDice(self, rollList):
        if(not rollList):
            return None
        for roll in rollList:
            print(f'Num-{roll.num}, Type-{roll.type}, Size-{roll.size}')
            if (roll.type=='d'):
                res = super().Roll(roll.num, roll.size)
                self.diceList.extend(res)
            if (roll.type=='h'):
                for i in range(roll.num):
                    self.diceList.append(roll.size)
            if (roll.type=='w'):
                self.wiggle = self.wiggle + roll.num

    def parse(self, rawList):
        expression = r'^((?P<num>\d+)?(?P<type>[dw])(10)?|(?P<hnum>\d+)?(?P<htype>h)(?P<hsize>\d+)?)$'
        rollList = []
        for raw in rawList:
            roll = SingleGRoll()
            res = re.match(expression, raw, re.I)
            if res:
                if res.group("type"):
                    roll.type=res.group("type")
                    if res.group("num"):
                        roll.num=int(res.group("num"))
                    #Roll(num, size, res.group("type"))  # put type tolower() first
                else:
                    roll.type=res.group("htype")
                    if res.group("hnum"):
                        roll.num=int(res.group("hnum"))
                    if res.group("hsize"):
                        roll.size=int(res.group("hsize"))
                    #Roll(num, size, res.group("type")  # put type tolower() first
            else:
                print("Invalid Format")
                return None

            rollList.append(roll)
        return rollList

    def format(self, matchList):
        self.sum = sum(self.diceList)
        if matchList:
            self.formattedMatches += "And have Matches: "
            for match in matchList:
                self.formattedMatches += f'{match.width}x{match.height}, '
        else:
            self.formattedMatches += "And have no Matches"
        for die in self.diceList:
            self.formattedDice += f'[ {die} ] '
        output=f'You rolled: {self.formattedDice} \n{self.formattedMatches}'
        if(self.wiggle > 0):
            output += f'\nAnd {self.wiggle} wiggle dice!'
        return output


    def findMatches(self):
        # Format the godlike object
        tempList = self.diceList.copy()
        tempList.sort()
        resList=[]
        width=0
        old = -1
        print(f'tempList is {tempList}')
        for find in tempList:
            if(width > 0):
                if (find==old):
                    width += 1
                else:
                    cur = GResult(width+1, height)
                    resList.append(cur)
                    width=0
                    old=find
            else:
                if (find==old):
                    height = find
                    width += 1
                else:
                    old=find
        if(width > 0):
            cur = GResult(width+1, height)
            resList.append(cur)
        self.matches=resList
        print(f'resList is {resList}')
        return resList
