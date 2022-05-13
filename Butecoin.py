from hashlib import sha256
import time


class block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp=timeStamp
        self.data=data
        self.previousHash=previousHash
        self.kuvvet=0
        self.hash=self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet=self.kuvvet+1
            ozet=sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:4]=="0000":
                break
        return ozet

class blockChain:
    def __init__(self):
        self.chain=[self.genesisOlustur()]

    def genesisOlustur(self):
        return block(time.ctime,"bute","")

    def blockEkle(self,data):
        node= block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk=self.chain[i-1].hash
                suan=self.chain[i].previousHash
                if ilk!=suan:
                    return "zincir kırıldı"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash :
                    return "zincir kırıldı"
        return "zincir saglam"

    def listeleme(self):

        print("BlockChain= ")

        for i in range(len(self.chain)):
            print("-------------------------------------")
            print("Block=> ",i,"\nHash = " ,str(self.chain[i].hash),"\nZaman =",str(self.chain[i].timeStamp),"Data =",str(self.chain[i].data),"\nKuvvet =",str(self.chain[i].kuvvet),"\nPreviousHash =",str(self.chain[i].previousHash))
            print("-------------------------------------")
            
ButeChain = blockChain()

while True:
        print("Lütfen seciminizi yapiniz \nBlock eklemek için 1 \nBlockChain'i görmek için 2\nZinciri kontrol etmel için 3\nÇıkmak için 4 ü secin")
        data =input()
        if data=="1":
            print("Gönderilen miktarı giriniz:")
            miktar=input()
            ButeChain.blockEkle(miktar)
        elif data=="2":
            ButeChain.listeleme()
        elif data=="3":
            print(str(ButeChain.kontrol()))
        elif data=="4":
            break
        


         
             

