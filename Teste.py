import os
import sys
import random
from time import sleep
import colorama

classe = []
vida = []

class classes:
    nome = ""
    maxhp = 0
    hpatual = 0
    maxmana = 0
    manaatual = 0
    atk = 0
    matk = 0
    quemataca = 1
    def __init__ (self, nome, maxhp, maxmana, atk, matk):
        self.nome = nome
        self.maxhp = maxhp
        self.maxmana = maxmana
        self.atk = atk
        self.matk = matk
        self.hpatual = maxhp
        self.manaatual = maxmana

    def atacar(self):
        print("Rolando um dado... (Arma)")
        os.system('pause')
        r = random.randrange(1, 21)
        if r == 1:
            print(colorama.Fore.RED + "ERRO CRITICO!" + colorama.Fore.RESET)
            dmg = 0
        elif r == 20:
            print(colorama.Fore.RED + "DANO CRITICO!" + colorama.Fore.RESET)
            dmg = self.atk * 2
        else:
            dmg = random.randrange(1, int(self.atk)+1)
        print("Rolou: " + str(r) + "\nDano causado " + colorama.Fore.RED + str(dmg) + colorama.Fore.RESET)
        os.system('pause')
        if classes.quemataca == 1:
            inimigo.hpatual = inimigo.hpatual - dmg
        elif classes.quemataca == 0:
            jogador.hpatual = jogador.hpatual - dmg

        if classes.quemataca == 1:
            classes.quemataca = 0
        elif classes.quemataca == 0:
            classes.quemataca = 1
    
    def fireball(self):
        self.manaatual = self.manaatual-4
        print("Rolando um dado... (Cast)")
        os.system('pause')
        r = random.randrange(1, 21)
        if r == 1:
            print(colorama.Fore.RED + "ERRO CRITICO!" + colorama.Fore.RESET)
            dmg = 0
        elif r == 20:
            print(colorama.Fore.RED + "DANO CRITICO!" + colorama.Fore.RESET)
            dmg = self.matk * 2
        else:
            dmg = random.randrange(1, int(self.matk)+1)
        print("Rolou: " + str(r) + "\nDano causado " + colorama.Fore.RED + str(dmg) + colorama.Fore.RESET)
        os.system('pause')
        if classes.quemataca == 1:
            inimigo.hpatual = inimigo.hpatual - dmg
        elif classes.quemataca == 0:
            jogador.hpatual = jogador.hpatual - dmg
        
        if classes.quemataca == 1:
            classes.quemataca = 0
        elif classes.quemataca == 0:
            classes.quemataca = 1

    def decide(self):
        ri = random.randrange(1, 3)
        if ri == 1:
            inimigo.atacar()
        elif ri == 2:
            inimigo.fireball()

    def artemago():
        print(" ______________________________")        
        print("|               ,              |")
        print("|              /|   | |        |")
        print("|            _/_\\_  >_<        |")
        print("|           .-\\-/.   |         |")
        print("|          /  | | \\_ |         |")
        print("|          \\ \\| |\\__(/         |")
        print("|          /(`---')  |         |")
        print("|         / /     \\  |         |")
        print("|      _.'  \\'-'  /  |         |")
        print("|      `----'`=-='   '         |")
        print("\\______________________________/")
        
    def artebarb():
        print(" _______________________________")
        print("|                      __)\\     |")
        print("|      .----.       __)    \\    |")
        print("|     |  = = |     <  ___   |   |")
        print("|  ___|  : : |___   \\\\   `)/    |")
        print("|  \\   `----´   /\\  (\\\\)  (     |")
        print("|   \\   `.     /( \\/ /\\\\        |")
        print("|    |    :   |  \\  /  \\\\       |")
        print("|    \\        /   `\"            |")
        print("|    |xx(o)xx|                  |")
        print("\\_______________________________/")

    def att(self):
        vida.clear()
        print("Barra de vida do oponente:")
        for x in range(0, inimigo.maxhp):
            if x < inimigo.hpatual:
                vida.append("-")
            elif x >= inimigo.hpatual:
                vida.append(" ")
            if x == 0:
                print("[" + colorama.Fore.RED + vida[x], end="")
            elif x < inimigo.maxhp-1:
                print(vida[x], end="")
            else:
                print(vida[x] + colorama.Fore.RESET + "] " + str(inimigo.hpatual) + "/" + str(inimigo.maxhp))
        if inimigo.nome == "Mago":
               classes.artemago()
        elif inimigo.nome == "Barbaro":
               classes.artebarb()

        #def infos(self):
            #if jogador.nome == "Mago":


            #elif jogador.nome == "Barbaro":

    def infos(self):
        os.system('cls')
        vida.clear()
        print("Barra de vida do Jogador: ")
        for x in range(0, jogador.maxhp):
            if x < jogador.hpatual:
                vida.append("-")
            elif x >= jogador.hpatual:
                vida.append(" ")
            if x == 0:
                print("[" + colorama.Fore.LIGHTGREEN_EX + vida[x], end="")
            elif x < jogador.maxhp-1:
                print(vida[x], end="")
            else:
                print(vida[x] + colorama.Fore.RESET + "]" + str(jogador.hpatual) + "/" + str(jogador.maxhp))
        if jogador.nome == "Mago":
               classes.artemago()
        elif jogador.nome == "Barbaro":
               classes.artebarb()
        print("Ataque do jogador: " + str(jogador.atk))
        print("Ataque magico do jogador: " + str(jogador.matk))
        os.system('pause')

    def checagem(self):
        if inimigo.hpatual <= 0:    
            return 1
        elif jogador.hpatual <= 0:
            return 2
        else:
            return 0

mago = classes("Mago", 30, 20, 1, 6)
classe.append(mago)
barbaro = classes("Barbaro", 45, 5, 5, 1)
classe.append(barbaro)

try:
    os.system('cls')
    print("Escolha a classe de seu personagem: ")
    print("0 - Mago")
    opc = int(input("Escolha: "))
    jogador = classe[opc]
except:
    print("Seleção Inválida")
print("O CPU está selecionando uma classe", end="") ; sleep(1)

for x in range(1, 4):
    if x == 3:
        print(".") ; sleep(1)
    else:
        sys.stdout.flush()
        print(".", end="")  ; sleep(1)
        sys.stdout.flush()

#inimigo = classe[random.randrange(0, int(len(classe)))]
inimigo = classe[1]
print("Classe escolhida.........: " + classe[opc].nome)
print("Classe escolhida pela CPU: " + inimigo.nome)
os.system('pause')

while jogador.hpatual > 0 and inimigo.hpatual > 0:
    os.system('cls')
    inimigo.att()
    print("1 - Ataque com Arma")
    print("2 - Usar magia")
    print("3 - Mostrar status")
    try:
        r = int(input("Escolha sua ação: "))
        if r == 1:
            jogador.atacar()
            os.system('cls')
            inimigo.att()
            if jogador.checagem() == 1:
                print(colorama.Fore.LIGHTGREEN_EX + "Você venceu!" colorama.Fore.RESET)
                break
            elif jogador.checagem() == 2:
                print(colorama.Fore.RED + "Você morreu!" + colorama.Fore.RESET)
                break
            else:
                print("Ação do oponente: ")
                inimigo.decide()
                if jogador.checagem() == 1:
                    print(colorama.Fore.LIGHTGREEN_EX + "Você venceu!" colorama.Fore.RESET)
                    break
                elif jogador.checagem() == 2:
                    print(colorama.Fore.RED + "Você morreu!" + colorama.Fore.RESET)
                    break
        elif r == 2:
            jogador.fireball()
            os.system('cls')
            inimigo.att()
            if jogador.checagem() == 1:
                print(colorama.Fore.LIGHTGREEN_EX + "Você venceu!" colorama.Fore.RESET)
                break
            elif jogador.checagem() == 2:
                print(colorama.Fore.RED + "Você morreu!" + colorama.Fore.RESET)
                break
            else:
                print("Ação do oponente: ")
                inimigo.decide()
                if jogador.checagem() == 1:
                    print(colorama.Fore.LIGHTGREEN_EX + "Você venceu!" colorama.Fore.RESET)
                    break
                elif jogador.checagem() == 2:
                    print(colorama.Fore.RED + "Você morreu!" + colorama.Fore.RESET)
                    break
        elif r == 3:
            jogador.infos()
        elif r == 4:
            print("DESISTIU PQ IRMÃO??")
            break
    except Exception as error:
        print(error)
        os.system('pause')