#print("I'm imported right now")

class PlayerScore:
    def __init__(self):
        #print("new constructor")
        self.__rolls = []
    
    def roll(self, pins):
        if isinstance(pins, int):
            self.__rolls.append(pins)
        else:
            raise TypeError

    def score(self):
        score = 0
        index = 0
        for frame in range(10):
            if self.__rolls[index] == 10:
                #STRIKE
                score += 10 + self.__rolls[index+1] + self.__rolls[index+2]
                index += 1
            elif self.__rolls[index] + self.__rolls[index+1] == 10:
                #Spare
                score += 10 + self.__rolls[index+2]
                index += 2
            else:
                score += self.__rolls[index] + self.__rolls[index+1]
                index += 2
            
        return score
