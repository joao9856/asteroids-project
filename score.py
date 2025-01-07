import json

try:
    highscore = int(json.load(open("highscore.txt")))
except:
    json.dump(0,open("highscore.txt","w")) 
    highscore = 0


class Score():
    def __init__(self):
        self.score = 0
        self.highscore = highscore
    
    def set_highscore(self):
        if self.highscore > highscore:
            json.dump(self.highscore,open("highscore.txt","w"))

    def score_add(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score