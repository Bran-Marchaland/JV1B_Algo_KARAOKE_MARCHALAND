import random


class Player:

    def __init__(self,pseudo,numJoueur,score0,score1,score2,score3,score4):
        self.pseudo = pseudo
        self.numJoueur = numJoueur
        self.score0 = score0    
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4

    def moyenne(self,score0,score1,score2,score3,score4):
        scores = [0,0,0,0,0]
        for i in range(0,len(scores)):
            valeurs=score0
            scores[i] = valeurs
            valeurs=valeurs+1
            resultat = resultat + scores[i]
        SH = scores[0]
        print ("plus grand score : ",SH)

        



    def NScore(self):
        choix = input("choix musique  0 à 4")
        self.newS=random.randint(50,100)
        if (choix == 0):
            if (self.score0 < self.newS):
                self.score0 = self.newS 
                print("scores mis à jour")
            else:
                print("les scores non pas bouger")

        elif (choix == 1):
            if (self.score1 < self.newS):
                self.score1 = self.newS 
                print("scores mis à jour")
            else:
                print("les scores non pas bouger")

        elif (choix == 2):
            if (self.score2 < self.newS):
                self.score2 = self.newS 
                print("scores mis à jour")
            else:
                print("les scores non pas bouger")

        elif (choix == 3):
            if (self.score3 < self.newS):
                self.score3 = self.newS 
                print("scores mis à jour")
            else:
                print("les scores non pas bouger")

        elif (choix == 4):
            if (self.score4 < self.newS):
                self.score4 = self.newS 
                print("scores mis à jour")
            else:
                print("les scores non pas bouger")





NJ = int(input("Combien de joueur ? "))

while (NJ!=0):
    NJ=NJ-1
    Player()



