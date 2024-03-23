import os
import random

classe = []
vida = []

class classes:
    nome = ""
    maxhp = 0
    hpatual = 0
    maxmana = 0
    atk = 0
    matk = 0
    def __init__ (self, nome, maxhp, hpatual, maxmana, atk, matk):
        self.nome = nome
        self.maxhp = maxhp
        self.hpatual = hpatual
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
            dmg = random.randrange(1, int(self.atk)+1)
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
            dmg = random.randrange(1, int(self.atk)+1)
        print("Rolou: " + str(r) + " você causou " + str(dmg) + " pontos de dano")
        os.system('pause')
        return dmg

mago = classes("Mago", 30, 15, 20, 1, 6)
classe.append(mago)
barbaro = classes("Barbaro", 60, 40, 5, 5, 1)
classe.append(barbaro)
inimigo = random.randrange(0, 2)

opc = 0

"""while opc != 3:
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
        classe[opc].fireball()"""

vida.clear()
print("Barra de vida do Jogador: ")
for x in range(0, mago.maxhp):
    if x < mago.hpatual:
        vida.append("-")
    elif x >= mago.hpatual:
        vida.append(" ")

    if x == 0:
        print("[" + vida[x], end="")
    elif x < mago.maxhp-1:
        print(vida[x], end="")
    else:
        print(vida[x]+ "]" + str(mago.hpatual) + "/" + str(mago.maxhp))
print("         ,    _")
print("        /|   | |")
print("      _/_\\_  >_<")
print("     .-\\-/.   |")
print("    /  | | \\_ |")
print("    \\ \\| |\\__(/")
print("    /(`---')  |")
print("   / /     \\  |")
print("_.'  \\'-'  /  |")
print("`----'`=-='   '")
os.system('pause')