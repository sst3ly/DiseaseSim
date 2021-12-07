import random
import time

#susceptible = state 0
#infected = state 1
#deceased = state 2
#immune = state 3

 
class Person():
    def __init__(self, state=0, weakness=random.randint(1,500)):#weakness is basically a value used to calculate whether someone dies, becomes immune, gets infected, etc.
        import random
        import time
        
        self.weakness = weakness
        self.state = state
        self.infectionLength = random.randint(3,(5+round(self.weakness/100)))
        self.immunityLength = random.randint(10,(15+round(self.weakness/100)))
        self.ran = False
        self.doneWithI = False
        self.doneWithIm = False
        self.daysInfected = 0
        self.daysImmune = 0
       
    def becomeState(self, state2):
        if(self.state != 2 and self.state != 3):
            self.state = state2
            self.daysInfected = 0
        if(state2 == "reS"):
            self.state = 0
            self.daysImmune = 0
            
       
    def day(self):
        if(self.state == 1):
            self.daysInfected += 1
        if(self.state == 3):
            self.daysImmune += 1
        if(self.daysInfected == self.infectionLength):
            self.doneWithI = True
        if(self.daysImmune == self.immunityLength):
            self.doneWithIm = True
       
        
      
class simulation():
    def __init__(self):
        import random
        import time
        
        self.population = 30
        self.peopleGroups = [self.population - 1, 1, 0, 0]
        self.people = []
        
        self.livePop = self.population
        self.day = 1
        
        b = Person(state=1)
        self.people.append(b)
       
        for i in range(0,self.population-1):
            a = Person()
            self.people.append(a)
        a,b = None,None
        
        print(f"S: {self.peopleGroups[0]}, If: {self.peopleGroups[1]}, D: {self.peopleGroups[2]}, Im: {self.peopleGroups[3]}, LP: {self.livePop}")
        print("Day: ", self.day)
       
    def stepDay(self):
        self.day += 1#increase day
        
        #running daily individual updates
        for person in self.people:
            person.day()
        
        
        #infecting
        for person1 in self.people:
            selection = random.randint(0,self.population-1)
            person2 = self.people[selection]
            if(person1 != person2 and person1.ran == False and person2.ran == False):
                if(person1.state == 1):
                    wkns2 = person2.weakness
                    chanceOfInfection = random.randint(1, 500+wkns2)
                    if(chanceOfInfection <= 325):
                        person2.becomeState(1)

                if(person2.state == 1):
                    wkns1 = person1.weakness
                    chanceOfInfection = random.randint(1, 500+wkns1)
                    if(chanceOfInfection <= 325):
                        person1.becomeState(1)
            person1.ran = True
            person2.ran = True
        
        #stepping infection + immunity
        for person in self.people:
            if(person.doneWithI == True):
                wkns = person.weakness
                chance = random.randint(1, 500+wkns)
                if(chance <= 50):
                    person.becomeState(2)#die
                elif(chance <= 150 and chance >= 51):
                    person.becomeState(0)#susceptible
                elif(chance >= 151):
                    person.becomeState(3)#immune
            if(person.doneWithIm == True):
                person.becomeState("reS")
        
        #counting
                
        s = 0#0
        i1 = 0#1
        d = 0#2
        i2 = 0#3
        
        for i in self.people:
            i.ran = False
            if(i.state == 0):
                s+=1
            if(i.state == 1):
                i1+=1
            if(i.state == 2):
                d+=1
            if(i.state == 3):
                i2+=1
        self.peopleGroups[0] = s
        self.peopleGroups[1] = i1
        self.peopleGroups[2] = d
        self.peopleGroups[3] = i2
        self.livePop = s+i1+i2
        
        #resetting infection
        for person in self.people:
            person.ran = False
        
        
        print(f"S: {self.peopleGroups[0]}, If: {self.peopleGroups[1]}, D: {self.peopleGroups[2]}, Im: {self.peopleGroups[3]}, LP: {self.livePop}")
        print("Day: ", self.day)
