from judge import judgec

seikai=[[1,2,3],[3,2,2],[1,2,2]]
relord=[[1,2,2],[1,2,2],[1,3,2]]




class simu(judgec):
    def kari(self):
        print("kyogi")


seigo=simu()
seigo.kari()
#print(seigo.judges(relord,seikai))








