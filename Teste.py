import os
import random

classe = []

class classes:
    nome = ""
    maxhp = 0
    maxmana = 0
    atk = 0
    matk = 0
    def __init__ (self, nome, maxhp, maxmana, atk, matk):
        self.nome = nome
        self.maxhp = maxhp
        self.maxmana = maxmana
        self.atk = atk
        self.matk = matk
    def atacar(self):
        print("Rolando um dado... ")
        os.system('pause')
        r = random.randrange(1, 21)
        if r == 1:
            dmg = 0
        elif r == 20:
            print("DANO CRITICO!")
            dmg = self.atk * 2
        else:
            if self.atk == 1:
                dmg = 1
            else:
                dmg = random.randrange(1, int(self.atk))
        print("Rolou: " + str(r) + " você causou " + str(dmg) + " pontos de dano")
        os.system('pause')
        return dmg
    
    def fireball(self):
        self.maxmana = self.maxmana-4
        print("Rolando um dado... ")
        os.system('pause')
        r = random.randrange(1, 21)
        if r == 1:
            dmg = 0
        elif r == 20:
            print("DANO CRITICO!")
            dmg = self.matk * 2
        else:
            if self.atk == 1:
                dmg = 1
            else:
                dmg = random.randrange(1, int(self.atk))
        print("Rolou: " + str(r) + " você causou " + str(dmg) + " pontos de dano")
        os.system('pause')
        return dmg

mago = classes("Mago", 30, 20, 1, 6)
classe.append(mago)
barbaro = classes("Barbaro", 60, 5, 5, 1)
classe.append(barbaro)
inimigo = barbaro

opc = 0

while opc != 3:
    os.system('cls')
    print("0 - Mago")
    print("1 - Barbaro")
    opc = int(input("Escolha: "))
    os.system('cls')
    print("Classe escolhida: " + classe[opc].nome)
    print("1 - Ataque Normal")
    print("2 - Magia")
    opa = int(input("Escolha: "))
    if opa == 1:
        classe[opc].atacar()
    elif opa == 2:
        classe[opc].fireball()