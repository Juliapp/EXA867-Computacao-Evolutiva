from random import random

def binaryToInt(binaryList):
    str1 = ""
    str1 = str1.join(binaryList)
    return int(str1, 2)

class Individuo :
    def __init__(self, tamanhoCromossomo):
        self.tamanhoCromossomo = tamanhoCromossomo
        self.cromossomo = []
        self.valor = 0
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = []
        
        self.randomCromossomo()
        self.atualizaValor()
        
        
    #preencher o cromossomo de forma aleatória
    def randomCromossomo(self):
        for i in range(self.tamanhoCromossomo):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
    def atualizaValor(self):
        self.valor = binaryToInt(self.cromossomo)
        
    def getFitnessPercent(self):
        return self.fitnessPercent
    
    #Função pra mutar o bit
    def mutatBit(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'     
                    
    
    def isInRange(self, num):
        if num >= self.faixaRoleta[0] and num <= self.faixaRoleta[1]:
            return True
        else:
            return False
            
    def printCromossomo(self):
        print('Cromossomo: ' + str(self.cromossomo) + ' | Valor: ' + str(self.valor) + ' | Fitness: ' + str(self.fitnessPercent))
        print('Faixa da roleta: entre ' + str(self.faixaRoleta[0]) + ' e ' + str(self.faixaRoleta[1]))
        
    