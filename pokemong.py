
from PyQt5 import QtCore, QtGui, QtWidgets
import random

#Below are the variables needed for the game
pname=""; gender=""
turns=3; wins=0
pokemon=""
enemy=""; enpokemon=""
p1moves=""; p2moves=""
p1val=0; p2val=0
p1energy = 100; p2energy = 100
p1attack=""
attack2=0
donebattle=[]; endonebattle=[]

class Ui_MainWindow(object):
    #this is the function for the play button at the welcome screen
    def playbutton(self):
        self.playerwidget.show()

    #this is the proceed button
    def proceedbutton(self):
        global pname, turns, wins
        global gender
        gender=self.CBPGENDER.currentText()
        name=self.LEPNAME.text()
        pname=name
        #the player needs to enter name and gender first in order to proceed
        if pname == "" or gender == "":
            if pname == "":
                self.lblpwarning1.show()
            elif gender == "":
                self.lblpwarning1.hide()
                self.lblpwarning2.show()
            pass
        #if the player entered name and gender, game proceeds
        elif pname != "" and gender != "":
            self.battlewidget.hide(); self.playerwidget.hide()
            self.selectionwidget.show()
            self.LCDWINS.display(wins); self.LCDTURNS.display(turns); self.PICCHOSEN.setPixmap(QtGui.QPixmap("pokeball.png"))
            self.PBSTART.setEnabled(True); self.frplayerpokemons.setEnabled(True)
            self.lblwinorlose.hide(); self.lblpwarning1.hide(); self.lblpwarning2.hide()
        return pname, gender

    #this is the radio button for "bulbasaur" in the pokemon selection
    def p1click(self):
        global pokemon
        pokemon="bulbasaur"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("bulbasaur.png"))
        return pokemon

    # this is the radio button for "charmander" in the pokemon selection
    def p2click(self):
        global pokemon
        pokemon = "charmander"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("charmander.png"))
        return pokemon

    # this is the radio button for "squirtle" in the pokemon selection
    def p3click(self):
        global pokemon
        pokemon = "squirtle"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("squirtle.png"))
        return pokemon

    # this is the radio button for "pikachu" in the pokemon selection
    def p4click(self):
        global pokemon
        pokemon = "pikachu"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("pikachu.png"))
        return pokemon

    # this is the radio button for "pidgey" in the pokemon selection
    def p5click(self):
        global pokemon
        pokemon = "pidgey"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("pidgey.png"))
        return pokemon

    # this is the radio button for "snorlax" in the pokemon selection
    def p6click(self):
        global pokemon
        pokemon = "snorlax"
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("snorlax.png"))
        return pokemon

    #this is the back button, will return to the player info screen
    def backbutton(self):
        global pname, gender
        pname=""; self.gender=""
        self.LEPNAME.setText("")
        self.CBPGENDER.setCurrentIndex(0)
        self.battlewidget.hide(); self.selectionwidget.hide(); self.playerwidget.hide()
        self.lblpwarning1.hide(); self.lblpwarning2.hide()
        return pname, gender

    #this is the start button.
    def startbutton(self):
        global pname,gender, turns, wins, enemy, enpokemon, p1moves, p1energy, p2energy, attack2, endonebattle
        #player can't proceed if he/she didn't pick a pokemon
        if pokemon == "":
            self.lblpickpokemon.show()
            pass
        #if player select a pokemon the game proceeds
        elif pokemon != "":
            self.lblpickpokemon.hide()
            #will generate a random enemy for the player
            enilist=["Garry", "Red", "Dark"]
            #and generate a random pokemon for the enemy
            enipklist = ["treecko", "torchic", "mudkip", "shinx", "tailow", "riolu"]
            enpokemon=random.choice(enipklist)
            enemy=random.choice(enilist)
            while enemy in endonebattle:
                enemy = random.choice(enilist)
                if enemy not in endonebattle:
                    break
            endonebattle.append(enemy)
            self.enemyname.setText(enemy)
            if enemy == "Garry":
                self.P2PIC.setPixmap(QtGui.QPixmap("en2.png"))
            elif enemy == "Red":
                self.P2PIC.setPixmap(QtGui.QPixmap("en1.png"))
            elif enemy == "Dark":
                self.P2PIC.setPixmap(QtGui.QPixmap("en3.png"))
            self.player1name.setText(pname)
            if gender == "BOY":
                self.P1PIC.setPixmap(QtGui.QPixmap("playerb.png"))
            elif gender == "GIRL":
                self.P1PIC.setPixmap(QtGui.QPixmap("playergirl.png"))
            self.battlewidget.show()
            self.selectionwidget.hide(); self.playerwidget.hide()

            #Will just display the picture of the pokemon of the player
            if pokemon == "bulbasaur":
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("bulbasaur.png"))
                p1moves=["Vine Whip", "Razor Leaf", "Heal", "Defense"]
            elif pokemon == "charmander":
                p1moves = ["Ember", "Flame thrower", "Heal", "Defense"]
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("charmander.png"))
            elif pokemon == "squirtle":
                p1moves = ["Bubble", "Water gun", "Heal", "Defense"]
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("squirtle.png"))
            elif pokemon == "pikachu":
                p1moves = ["Iron tail", "Thunder schock", "Heal", "Defense"]
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("pikachu.png"))
            elif pokemon == "pidgey":
                p1moves = ["Wing attack", "Aerial Ace", "Heal", "Defense"]
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("pidgey.png"))
            elif pokemon == "snorlax":
                p1moves = ["Lick", "Body Slam", "Heal", "Defense"]
                self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("snorlax.png"))

            self.P1ATT1.setText(p1moves[0]); self.P1ATT2.setText(p1moves[1]); self.P1ATT3.setText(p1moves[2]); self.P1ATT4.setText(p1moves[3])

            if enpokemon == "treecko":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2treecko.png"))
            elif enpokemon == "torchic":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2torchic.png"))
            elif enpokemon == "mudkip":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2mudkip.png"))
            elif enpokemon == "shinx":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2shinx.png"))
            elif enpokemon == "tailow":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2tailow.png"))
            elif enpokemon == "riolu":
                self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2riolu.png"))
            self.LBLP2ATTACK.setText(enemy+" choose "+enpokemon)

            #at the start of game, all pokemons have 100 energy
            p1energy=100; p2energy=100
            self.LCDENERGY1.display(p1energy); self.LCDENERGY2.display(p2energy)
            self.PBBEXIT.setEnabled(False)
            self.LBLWINLOSE.hide(); self.PBFIGHT.setEnabled(True)
            #this will just uncheck all the radio buttons
            self.P1ATT1.setAutoExclusive(False); self.P1ATT1.setChecked(False); self.P1ATT1.setAutoExclusive(True)
            self.P1ATT2.setAutoExclusive(False); self.P1ATT2.setChecked(False); self.P1ATT2.setAutoExclusive(True)
            self.P1ATT3.setAutoExclusive(False); self.P1ATT3.setChecked(False); self.P1ATT3.setAutoExclusive(True)
            self.P1ATT4.setAutoExclusive(False); self.P1ATT4.setChecked(False); self.P1ATT4.setAutoExclusive(True)
            self.P1ATT2.setEnabled(True); attack2=0
            self.P1ATT2.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(167, 128, 0);")
            font = self.P1ATT2.font()
            font.setStrikeOut(False)
            self.P1ATT2.setFont(font)
        return p1moves, enemy, enpokemon, p1energy, p2energy, attack2, endonebattle

    #this will determine if the type of pokemon of enemy is stronger than the player's pokemon type
    def enpokemonattack(self):
        global enpokemon, p2val, pokemon
        if enpokemon == "treecko" and pokemon == "squirtle":
            p2val = 50
        elif enpokemon == "torchic" and pokemon == "bulbasaur":
            p2val = 50
        elif enpokemon == "mudkip" and enpokemon == "charmander":
            p2val = 50
        elif enpokemon == "shinx" and enpokemon == "squirtle":
            p2val = 50

        elif enpokemon == "treecko" and enpokemon == "charmander":
            p2val = 20
        elif pokemon == "torchic" and enpokemon == "squirtle":
            p2val = 20
        elif pokemon == "mudkip" and enpokemon == "bulbasaur":
            p2val = 20

        else:
            p2val = 30
        return p2val

    #This is the fight button
    def fightbutton(self):
        global p1val, p2val, p1energy, p2energy, enpokemon, turns, wins, p1attack, pokemon, attack2
        p2moves=[]
        #if the player didn't pick a move, the game will not proceed
        if p1val==0:
            self.selectattack.show()
        #if the player pick a move game proceeds
        elif p1val!= 0:
            self.selectattack.hide()
            #if pokemons have 0 energy, exit button is enabled
            if p1energy <= 0 or p2energy <= 0:
                self.PBFIGHT.setEnabled(False); self.PBBEXIT.setEnabled(True)
            #if pokemons don't have 0 energy yet, game continues and player can't exit
            elif p1energy > 0 and p2energy > 0:
                #generating random moves for the enemy's pokemon
                if enpokemon == "treecko":
                    p2moves=["Pound", "Grass knot", "Heal", "Defense"]
                elif enpokemon == "torchic":
                    p2moves=["Scratch", "Flamethrower", "Heal", "Defense"]
                elif enpokemon == "mudkip":
                    p2moves=["Mudshot", "Hydropump", "Heal", "Defense"]
                elif enpokemon == "shinx":
                    p2moves=["Spark", "Thunder bolt", "Heal", "Defense"]
                elif enpokemon == "tailow":
                    p2moves=["Peck", "Endeavor", "Heal", "Defense"]
                elif enpokemon == "riolu":
                    p2moves=["Quick attack", "Cross chop", "Heal", "Defense"]

                p2attack=random.choice(p2moves)
                if p2attack == p2moves[0]:
                    p2val=20
                elif p2attack == p2moves[1]:
                    self.enpokemonattack()
                elif p2attack == p2moves[2]:
                    p2val=10
                elif p2attack == p2moves[3]:
                    p2val=-10

                self.LBLWINLOSE.show(); self.LBLWINLOSE.setText(pokemon + " use "+ p1attack+ "!")
                self.LBLP2ATTACK.setText(enpokemon + " use "+ p2attack+ "!")

                #this is the value of the moves
                if p2val == -10:
                    if p1val == 30:
                        attack2+=1
                    else:
                        pass
                elif p2val != -10:
                    if p1val == 20:
                        p2energy-=20
                        if p2energy >= 0:
                            self.LCDENERGY2.display(p2energy)
                        elif p2energy < 0:
                            self.LCDENERGY2.display(0)
                    elif p1val == 30:
                        attack2+=1
                        p2energy-=30
                        if p2energy >= 0:
                            self.LCDENERGY2.display(p2energy)
                        elif p2energy < 0:
                            self.LCDENERGY2.display(0)
                    elif p1val == 50:
                        attack2 += 1
                        p2energy -= 50
                        if p2energy >= 0:
                            self.LCDENERGY2.display(p2energy)
                        elif p2energy < 0:
                            self.LCDENERGY2.display(0)
                    elif p1val == 10:
                        if p1energy == 100:
                            pass
                        elif p1energy < 100:
                            p1energy+=10
                            if p1energy > 0:
                                self.LCDENERGY1.display(p1energy)
                            elif p1energy <=0:
                                self.LCDENERGY1.display(0)

                if p1val == -10:
                    pass
                elif p1val != -10:
                    if p2val == 20:
                        p1energy-=20
                        if p1energy >= 0:
                            self.LCDENERGY1.display(p1energy)
                        elif p1energy < 0:
                            self.LCDENERGY1.display(0)
                    elif p2val == 30:
                        p1energy-=30
                        if p1energy >= 0:
                            self.LCDENERGY1.display(p1energy)
                        elif p1energy < 0:
                            self.LCDENERGY1.display(0)
                    elif p2val == 50:
                        p1energy-=50
                        if p1energy >= 0:
                            self.LCDENERGY1.display(p1energy)
                        elif p1energy < 0:
                            self.LCDENERGY1.display(0)
                    elif p2val == 10:
                        if p2energy == 100:
                            pass
                        elif p2energy < 100:
                            p2energy+=10
                            if p2energy > 0:
                                self.LCDENERGY2.display(p2energy)
                            elif p2energy <= 0:
                                self.LCDENERGY2.display(0)
        #will uncheck all the radio buttons of moves
        self.P1ATT1.setAutoExclusive(False); self.P1ATT1.setChecked(False); self.P1ATT1.setAutoExclusive(True)
        self.P1ATT2.setAutoExclusive(False); self.P1ATT2.setChecked(False); self.P1ATT2.setAutoExclusive(True)
        self.P1ATT3.setAutoExclusive(False); self.P1ATT3.setChecked(False); self.P1ATT3.setAutoExclusive(True)
        self.P1ATT4.setAutoExclusive(False); self.P1ATT4.setChecked(False); self.P1ATT4.setAutoExclusive(True)
        #if the special attack is used twice, it will be disabled
        if attack2 == 2:
            self.P1ATT2.setEnabled(False)
            p1val=0
            self.P1ATT2.setStyleSheet("border-color: rgb(66, 66, 66);\n"
                                      "color: rgb(80, 80, 0);")
            font = self.P1ATT2.font()
            font.setStrikeOut(True)
            self.P1ATT2.setFont(font)
        #this will determine who won the game
        if p1energy <=0 or p2energy <= 0:
            if p1energy > p2energy:
                self.LBLWINLOSE.show();
                self.LBLWINLOSE.setText("YOU WON THE MATCH")
                wins += 1
                self.LCDWINS.display(wins)
            elif p1energy < p2energy:
                self.LBLWINLOSE.show()
                self.LBLWINLOSE.setText("YOU LOSE THE MATCH")
            else:
                self.LBLWINLOSE.show()
                self.LBLWINLOSE.setText("It's a TIE")
            turns -= 1
            self.LCDTURNS.display(turns)
            self.PBFIGHT.setEnabled(False); self.PBBEXIT.setEnabled(True)
        p1val=0
        return p1val, p2val, p1energy, p2energy, enpokemon, turns, wins, p1attack, attack2

    #this is the radio button for attack 1 of player1
    def att1click(self):
        global p1val, p1attack
        p1val=20
        p1attack=self.P1ATT1.text()
        return p1val, p1attack

    # this is the radio button for attack 2 of player1
    def att2click(self):
        global p1val, p1attack
        self.types()
        p1attack = self.P1ATT2.text()
        return p1val, p1attack

    # this will determine if the player's pokemon type is stronger than the enemy's pokemon
    def types(self):
        global pokemon, enpokemon, p1val
        if pokemon == "bulbasaur" and enpokemon == "mudkip":
            p1val=50
        elif pokemon == "charmander" and enpokemon == "treecko":
            p1val=50
        elif pokemon == "squirtle" and enpokemon == "torchic":
            p1val=50
        elif pokemon == "pikachu" and enpokemon == "mudkip":
            p1val=50

        elif pokemon == "bulbasaur" and enpokemon == "torchic":
            p1val=20
        elif pokemon == "charmander" and enpokemon == "mudkip":
            p1val=20
        elif pokemon == "squirtle" and enpokemon == "treecko":
            p1val=20
            
        else:
            p1val=30
        return p1val

    # this is the radio button for move 3 of player1
    def att3click(self):
        global p1val, p1attack
        p1val=10
        p1attack = self.P1ATT3.text()
        return p1val, p1attack

    # this is the radio button for move 4 of player1
    def att4click(self):
        global p1val, p1attack
        p1val=-10
        p1attack = self.P1ATT4.text()
        return p1val, p1attack

    #this is the exit button at the battle
    def exitbattle(self):
        global turns, wins, pokemon, donebattle
        #will append the pokemon to a list if it's done battling
        donebattle.append(pokemon)
        self.battlewidget.hide(); self.selectionwidget.show(); self.playerwidget.hide()
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("pokeball.png"))
        #will uncheck all the radio buttons of the pokemon seleciton
        self.RB1.setAutoExclusive(False); self.RB1.setChecked(False); self.RB1.setAutoExclusive(True)
        self.RB2.setAutoExclusive(False); self.RB2.setChecked(False); self.RB2.setAutoExclusive(True)
        self.RB3.setAutoExclusive(False); self.RB3.setChecked(False); self.RB3.setAutoExclusive(True)
        self.RB4.setAutoExclusive(False); self.RB4.setChecked(False); self.RB4.setAutoExclusive(True)
        self.RB5.setAutoExclusive(False); self.RB5.setChecked(False); self.RB5.setAutoExclusive(True)
        self.RB6.setAutoExclusive(False); self.RB6.setChecked(False); self.RB6.setAutoExclusive(True)
        #to check if the pokemon is already used in a battle. if it is, it will be striked out.
        self.strike()
        pokemon=""
        #if player don't have turns, player can't play the game
        if turns == 0:
            self.PBSTART.setEnabled(False)
            self.frplayerpokemons.setEnabled(False)
            self.lblwinorlose.show()
            if wins == 3:
                self.lblwinorlose.setText("YEY! YOU WON 🎉")
            elif wins < 3:
                self.lblwinorlose.setText("Better luck next try 😓")
        return donebattle, pokemon

    #this is a function to unstrike all the pokemons if game is restarted
    def unstrike(self):
        global donebattle
        donebattle.clear()
        self.RB1.setEnabled(True); self.RB2.setEnabled(True); self.RB3.setEnabled(True); self.RB4.setEnabled(True); self.RB5.setEnabled(True); self.RB6.setEnabled(True)

        font = self.RB1.font(); font.setStrikeOut(False); self.RB1.setFont(font)
        self.RB1.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        font = self.RB2.font(); font.setStrikeOut(False); self.RB2.setFont(font)
        self.RB2.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        font = self.RB3.font(); font.setStrikeOut(False); self.RB3.setFont(font)
        self.RB3.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        font = self.RB4.font(); font.setStrikeOut(False); self.RB4.setFont(font)
        self.RB4.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        font = self.RB5.font(); font.setStrikeOut(False);  self.RB5.setFont(font)
        self.RB5.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        font = self.RB6.font(); font.setStrikeOut(False); self.RB6.setFont(font)
        self.RB6.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                               "color: rgb(167, 128, 0);")
        return donebattle

    #this is a function to strike out all pokemons that already battled
    def strike(self):
        global donebattle
        if "bulbasaur" in donebattle:
            self.RB1.setEnabled(False)
            font = self.RB1.font()
            font.setStrikeOut(True)
            self.RB1.setFont(font)
            self.RB1.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")
        if "charmander" in donebattle:
            self.RB2.setEnabled(False)
            font = self.RB2.font()
            font.setStrikeOut(True)
            self.RB2.setFont(font)
            self.RB2.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")
        if "squirtle" in donebattle:
            self.RB3.setEnabled(False)
            font = self.RB3.font()
            font.setStrikeOut(True)
            self.RB3.setFont(font)
            self.RB3.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")
        if "pikachu" in donebattle:
            self.RB4.setEnabled(False)
            font = self.RB4.font()
            font.setStrikeOut(True)
            self.RB4.setFont(font)
            self.RB4.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")
        if "pidgey" in donebattle:
            self.RB5.setEnabled(False)
            font = self.RB5.font()
            font.setStrikeOut(True)
            self.RB5.setFont(font)
            self.RB5.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")
        if "snorlax" in donebattle:
            self.RB6.setEnabled(False)
            font = self.RB6.font()
            font.setStrikeOut(True)
            self.RB6.setFont(font)
            self.RB6.setStyleSheet("border-color: rgb(48, 48, 48);\n"
                                   "color: rgb(80, 80, 0);")

    #this is the home button at the selection widget
    def homebutton(self):
        global turns, wins, pokemon
        #if home is clicked, game will restart
        turns=3
        wins=0
        pokemon=""
        self.battlewidget.hide()
        self.selectionwidget.hide()
        self.playerwidget.hide()
        self.LEPNAME.setText(""); self.CBPGENDER.setCurrentIndex(0)
        #uncheck all the radio buttons
        self.RB1.setAutoExclusive(False); self.RB1.setChecked(False); self.RB1.setAutoExclusive(True)
        self.RB2.setAutoExclusive(False); self.RB2.setChecked(False); self.RB2.setAutoExclusive(True)
        self.RB3.setAutoExclusive(False); self.RB3.setChecked(False); self.RB3.setAutoExclusive(True)
        self.RB4.setAutoExclusive(False); self.RB4.setChecked(False); self.RB4.setAutoExclusive(True)
        self.RB5.setAutoExclusive(False); self.RB5.setChecked(False); self.RB5.setAutoExclusive(True)
        self.RB6.setAutoExclusive(False); self.RB6.setChecked(False); self.RB6.setAutoExclusive(True)
        #unstrike all the radio buttons as well
        self.unstrike()
        return turns, wins, pokemon

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainscreen = QtWidgets.QWidget(self.centralwidget)
        self.mainscreen.setGeometry(QtCore.QRect(0, 0, 791, 601))
        self.mainscreen.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.mainscreen.setObjectName("mainscreen")
        self.logo = QtWidgets.QLabel(self.mainscreen)
        self.logo.setGeometry(QtCore.QRect(40, -40, 671, 491))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pokemon-logo-black-transparent.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.PBPLAY = QtWidgets.QPushButton(self.mainscreen)
        self.PBPLAY.setGeometry(QtCore.QRect(230, 460, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBPLAY.setFont(font)
        self.PBPLAY.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBPLAY.setObjectName("PBPLAY")
        self.PBEXIT = QtWidgets.QPushButton(self.mainscreen)
        self.PBEXIT.setGeometry(QtCore.QRect(420, 460, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBEXIT.setFont(font)
        self.PBEXIT.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBEXIT.setObjectName("PBEXIT")
        self.lblbattle = QtWidgets.QLabel(self.mainscreen)
        self.lblbattle.setGeometry(QtCore.QRect(270, 320, 241, 61))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(26)
        self.lblbattle.setFont(font)
        self.lblbattle.setStyleSheet("color: rgb(130, 130, 130);")
        self.lblbattle.setObjectName("lblbattle")
        self.playerwidget = QtWidgets.QWidget(self.centralwidget)
        self.playerwidget.setGeometry(QtCore.QRect(0, 0, 791, 601))
        self.playerwidget.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.playerwidget.setObjectName("playerwidget")
        self.PBPROCEED = QtWidgets.QPushButton(self.playerwidget)
        self.PBPROCEED.setGeometry(QtCore.QRect(290, 440, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBPROCEED.setFont(font)
        self.PBPROCEED.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBPROCEED.setObjectName("PBPROCEED")
        self.PBBACK = QtWidgets.QPushButton(self.playerwidget)
        self.PBBACK.setGeometry(QtCore.QRect(440, 440, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBBACK.setFont(font)
        self.PBBACK.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBBACK.setObjectName("PBBACK")
        self.lblpinfo = QtWidgets.QLabel(self.playerwidget)
        self.lblpinfo.setGeometry(QtCore.QRect(180, 160, 451, 61))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(24)
        self.lblpinfo.setFont(font)
        self.lblpinfo.setStyleSheet("color: rgb(130, 130, 130);")
        self.lblpinfo.setObjectName("lblpinfo")
        self.lblpname = QtWidgets.QLabel(self.playerwidget)
        self.lblpname.setGeometry(QtCore.QRect(180, 250, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblpname.setFont(font)
        self.lblpname.setStyleSheet("color: rgb(117, 117, 117);")
        self.lblpname.setObjectName("lblpname")

        self.lblpwarning1 = QtWidgets.QLabel(self.playerwidget)
        self.lblpwarning1.setGeometry(QtCore.QRect(290, 220, 125, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblpwarning1.setFont(font)
        self.lblpwarning1.setStyleSheet("color: rgb(200, 0, 0);")
        self.lblpwarning1.setObjectName("lblpwarning1")

        self.lblpwarning2 = QtWidgets.QLabel(self.playerwidget)
        self.lblpwarning2.setGeometry(QtCore.QRect(290, 293, 125, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblpwarning2.setFont(font)
        self.lblpwarning2.setStyleSheet("color: rgb(200, 0, 0);")
        self.lblpwarning2.setObjectName("lblpwarning2")

        self.LEPNAME = QtWidgets.QLineEdit(self.playerwidget)
        self.LEPNAME.setGeometry(QtCore.QRect(290, 260, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LEPNAME.setFont(font)
        self.LEPNAME.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(93, 93, 93);")
        self.LEPNAME.setText("")
        self.LEPNAME.setObjectName("LEPNAME")
        self.lblgnder = QtWidgets.QLabel(self.playerwidget)
        self.lblgnder.setGeometry(QtCore.QRect(180, 320, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblgnder.setFont(font)
        self.lblgnder.setStyleSheet("color: rgb(117, 117, 117);")
        self.lblgnder.setObjectName("lblgnder")
        self.CBPGENDER = QtWidgets.QComboBox(self.playerwidget)
        self.CBPGENDER.setGeometry(QtCore.QRect(290, 330, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CBPGENDER.setFont(font)
        self.CBPGENDER.setStyleSheet("background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);")
        self.CBPGENDER.setObjectName("CBPGENDER")
        self.CBPGENDER.addItem("")
        self.CBPGENDER.setItemText(0, "")
        self.CBPGENDER.addItem("")
        self.CBPGENDER.addItem("")
        self.selectionwidget = QtWidgets.QWidget(self.centralwidget)
        self.selectionwidget.setGeometry(QtCore.QRect(0, 0, 791, 601))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(26)
        self.selectionwidget.setFont(font)
        self.selectionwidget.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.selectionwidget.setObjectName("selectionwidget")
        self.PBHOME = QtWidgets.QPushButton(self.selectionwidget)
        self.PBHOME.setGeometry(QtCore.QRect(580, 480, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBHOME.setFont(font)
        self.PBHOME.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBHOME.setObjectName("PBHOME")
        self.PBSTART = QtWidgets.QPushButton(self.selectionwidget)
        self.PBSTART.setGeometry(QtCore.QRect(580, 410, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBSTART.setFont(font)
        self.PBSTART.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBSTART.setObjectName("PBSTART")
        self.lblpick = QtWidgets.QLabel(self.selectionwidget)
        self.lblpick.setGeometry(QtCore.QRect(70, 90, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblpick.setFont(font)
        self.lblpick.setStyleSheet("color: rgb(207, 159, 0);")
        self.lblpick.setObjectName("lblpick")

        self.lblpickpokemon = QtWidgets.QLabel(self.selectionwidget)
        self.lblpickpokemon.setGeometry(QtCore.QRect(520, 350, 210, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(70)
        self.lblpickpokemon.setFont(font)
        self.lblpickpokemon.setStyleSheet("color: rgb(200, 0, 0);")
        self.lblpickpokemon.setObjectName("lblpickpokemon")

        self.lblwinorlose = QtWidgets.QLabel(self.selectionwidget)
        self.lblwinorlose.setGeometry(QtCore.QRect(50, 480, 275, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblwinorlose.setFont(font)
        self.lblwinorlose.setStyleSheet("color: rgb(207, 159, 0);")
        self.lblwinorlose.setObjectName("lblwinorlose")

        self.frplayerpokemons = QtWidgets.QFrame(self.selectionwidget)
        self.frplayerpokemons.setGeometry(QtCore.QRect(50, 120, 671, 221))
        self.frplayerpokemons.setStyleSheet("border: 1px solid gray;")
        self.frplayerpokemons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frplayerpokemons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frplayerpokemons.setObjectName("frplayerpokemons")
        self.PICCHOSEN = QtWidgets.QLabel(self.frplayerpokemons)
        self.PICCHOSEN.setGeometry(QtCore.QRect(40, 20, 201, 181))
        self.PICCHOSEN.setStyleSheet("border-color:none;")
        self.PICCHOSEN.setText("")
        self.PICCHOSEN.setPixmap(QtGui.QPixmap("pokeball.png"))
        self.PICCHOSEN.setScaledContents(True)
        self.PICCHOSEN.setObjectName("PICCHOSEN")
        self.RB1 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB1.setGeometry(QtCore.QRect(290, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB1.setFont(font)
        self.RB1.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB1.setObjectName("RB1")
        self.RB2 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB2.setGeometry(QtCore.QRect(290, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB2.setFont(font)
        self.RB2.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB2.setObjectName("RB2")
        self.RB3 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB3.setGeometry(QtCore.QRect(290, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB3.setFont(font)
        self.RB3.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB3.setObjectName("RB3")
        self.RB4 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB4.setGeometry(QtCore.QRect(480, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB4.setFont(font)
        self.RB4.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB4.setObjectName("RB4")
        self.RB5 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB5.setGeometry(QtCore.QRect(480, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB5.setFont(font)
        self.RB5.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB5.setObjectName("RB5")
        self.RB6 = QtWidgets.QRadioButton(self.frplayerpokemons)
        self.RB6.setGeometry(QtCore.QRect(480, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RB6.setFont(font)
        self.RB6.setStyleSheet("border-color: rgb(48, 48, 48);\n"
"color: rgb(167, 128, 0);")
        self.RB6.setObjectName("RB6")
        self.LCDTURNS = QtWidgets.QLCDNumber(self.selectionwidget)
        self.LCDTURNS.setGeometry(QtCore.QRect(50, 420, 111, 51))
        self.LCDTURNS.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.LCDTURNS.setObjectName("LCDTURNS")
        self.lblturns = QtWidgets.QLabel(self.selectionwidget)
        self.lblturns.setGeometry(QtCore.QRect(50, 370, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblturns.setFont(font)
        self.lblturns.setStyleSheet("color: rgb(207, 159, 0);")
        self.lblturns.setObjectName("lblturns")
        self.lblwins = QtWidgets.QLabel(self.selectionwidget)
        self.lblwins.setGeometry(QtCore.QRect(210, 370, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblwins.setFont(font)
        self.lblwins.setStyleSheet("color: rgb(207, 159, 0);")
        self.lblwins.setObjectName("lblwins")
        self.LCDWINS = QtWidgets.QLCDNumber(self.selectionwidget)
        self.LCDWINS.setGeometry(QtCore.QRect(210, 420, 111, 51))
        self.LCDWINS.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.LCDWINS.setObjectName("LCDWINS")
        self.PBHOME.raise_()
        self.PBSTART.raise_()
        self.frplayerpokemons.raise_()
        self.lblpick.raise_()
        self.lblpickpokemon.raise_()
        self.lblwinorlose.raise_()
        self.LCDTURNS.raise_()
        self.lblturns.raise_()
        self.lblwins.raise_()
        self.LCDWINS.raise_()
        self.battlewidget = QtWidgets.QWidget(self.centralwidget)
        self.battlewidget.setGeometry(QtCore.QRect(0, 0, 791, 601))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(26)
        self.battlewidget.setFont(font)
        self.battlewidget.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.battlewidget.setObjectName("battlewidget")
        self.p1frame = QtWidgets.QFrame(self.battlewidget)
        self.p1frame.setGeometry(QtCore.QRect(20, 410, 731, 161))
        self.p1frame.setStyleSheet("border: 1px solid gray;\n"
"background-color: rgb(66, 66, 66);")
        self.p1frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.p1frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.p1frame.setObjectName("p1frame")
        self.PBBEXIT = QtWidgets.QPushButton(self.p1frame)
        self.PBBEXIT.setGeometry(QtCore.QRect(580, 90, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBBEXIT.setFont(font)
        self.PBBEXIT.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBBEXIT.setObjectName("PBBEXIT")
        self.PBFIGHT = QtWidgets.QPushButton(self.p1frame)
        self.PBFIGHT.setGeometry(QtCore.QRect(580, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PBFIGHT.setFont(font)
        self.PBFIGHT.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(255, 199, 0);\n"
"}")
        self.PBFIGHT.setObjectName("PBFIGHT")
        self.P1PIC = QtWidgets.QLabel(self.p1frame)
        self.P1PIC.setGeometry(QtCore.QRect(10, 10, 161, 141))
        self.P1PIC.setStyleSheet("border-color: rgb(66, 66, 66);")
        self.P1PIC.setText("")
        self.P1PIC.setPixmap(QtGui.QPixmap("playerb.png"))
        self.P1PIC.setScaledContents(True)
        self.P1PIC.setObjectName("P1PIC")
        self.P1ATT1 = QtWidgets.QRadioButton(self.p1frame)
        self.P1ATT1.setGeometry(QtCore.QRect(200, 48, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.P1ATT1.setFont(font)
        self.P1ATT1.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(167, 128, 0);")
        self.P1ATT1.setObjectName("P1ATT1")
        self.P1ATT2 = QtWidgets.QRadioButton(self.p1frame)
        self.P1ATT2.setGeometry(QtCore.QRect(200, 89, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.P1ATT2.setFont(font)
        self.P1ATT2.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(167, 128, 0);")
        self.P1ATT2.setObjectName("P1ATT2")
        self.P1ATT3 = QtWidgets.QRadioButton(self.p1frame)
        self.P1ATT3.setGeometry(QtCore.QRect(380, 48, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.P1ATT3.setFont(font)
        self.P1ATT3.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(167, 128, 0);")
        self.P1ATT3.setObjectName("P1ATT3")
        self.P1ATT4 = QtWidgets.QRadioButton(self.p1frame)
        self.P1ATT4.setGeometry(QtCore.QRect(380, 89, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.P1ATT4.setFont(font)
        self.P1ATT4.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(167, 128, 0);")
        self.P1ATT4.setObjectName("P1ATT4")

        self.player1name = QtWidgets.QLabel(self.p1frame)
        self.player1name.setGeometry(QtCore.QRect(217, 10, 175, 38))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.player1name.setFont(font)
        self.player1name.setStyleSheet("border-color: rgb(66, 66, 66);\n"
"color: rgb(207, 159, 0);")
        self.player1name.setObjectName("player1name")

        self.selectattack = QtWidgets.QLabel(self.p1frame)
        self.selectattack.setGeometry(QtCore.QRect(287, 128, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        self.selectattack.setFont(font)
        self.selectattack.setStyleSheet("border-color: rgb(66, 66, 66);\n"
                                       "color: rgb(200, 0, 0);")
        self.selectattack.setObjectName("selectattack")

        self.LBLP2ATTACK = QtWidgets.QLabel(self.battlewidget)
        self.LBLP2ATTACK.setGeometry(QtCore.QRect(100, 60, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LBLP2ATTACK.setFont(font)
        self.LBLP2ATTACK.setStyleSheet("color: rgb(200, 11, 4);\n"
"background-color: rgb(65, 65, 65);")
        self.LBLP2ATTACK.setObjectName("LBLP2ATTACK")
        self.lblvs = QtWidgets.QLabel(self.battlewidget)
        self.lblvs.setGeometry(QtCore.QRect(340, 220, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblvs.setFont(font)
        self.lblvs.setStyleSheet("color: rgb(182, 182, 182);")
        self.lblvs.setObjectName("lblvs")
        self.P2PIC = QtWidgets.QLabel(self.battlewidget)
        self.P2PIC.setGeometry(QtCore.QRect(630, 20, 131, 121))
        self.P2PIC.setStyleSheet("border-color: rgb(66, 66, 66);")
        self.P2PIC.setText("")
        self.P2PIC.setPixmap(QtGui.QPixmap("playerb.png"))
        self.P2PIC.setScaledContents(True)
        self.P2PIC.setObjectName("P2PIC")
        self.P1POKEMONPIC = QtWidgets.QLabel(self.battlewidget)
        self.P1POKEMONPIC.setGeometry(QtCore.QRect(30, 230, 171, 161))
        self.P1POKEMONPIC.setStyleSheet("border-color: rgb(66, 66, 66);")
        self.P1POKEMONPIC.setText("")
        self.P1POKEMONPIC.setPixmap(QtGui.QPixmap("charmander.png"))
        self.P1POKEMONPIC.setScaledContents(True)
        self.P1POKEMONPIC.setObjectName("P1POKEMONPIC")
        self.lblenergy1 = QtWidgets.QLabel(self.battlewidget)
        self.lblenergy1.setGeometry(QtCore.QRect(240, 360, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblenergy1.setFont(font)
        self.lblenergy1.setStyleSheet("color: rgb(207, 159, 0);")
        self.lblenergy1.setObjectName("lblenergy1")
        self.LCDENERGY1 = QtWidgets.QLCDNumber(self.battlewidget)
        self.LCDENERGY1.setGeometry(QtCore.QRect(340, 370, 81, 31))
        self.LCDENERGY1.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.LCDENERGY1.setObjectName("LCDENERGY1")
        self.P2POKEMONPIC = QtWidgets.QLabel(self.battlewidget)
        self.P2POKEMONPIC.setGeometry(QtCore.QRect(560, 140, 171, 161))
        self.P2POKEMONPIC.setStyleSheet("border-color: rgb(66, 66, 66);")
        self.P2POKEMONPIC.setText("")
        self.P2POKEMONPIC.setPixmap(QtGui.QPixmap("2shinx.png"))
        self.P2POKEMONPIC.setScaledContents(True)
        self.P2POKEMONPIC.setObjectName("P2POKEMONPIC")
        self.lblenergy2 = QtWidgets.QLabel(self.battlewidget)
        self.lblenergy2.setGeometry(QtCore.QRect(340, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblenergy2.setFont(font)
        self.lblenergy2.setStyleSheet("color: rgb(200, 11, 4);")
        self.lblenergy2.setObjectName("lblenergy2")

        self.enemyname = QtWidgets.QLabel(self.battlewidget)
        self.enemyname.setGeometry(QtCore.QRect(565, 24, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.enemyname.setFont(font)
        self.enemyname.setStyleSheet("color: rgb(200, 11, 4);")
        self.enemyname.setObjectName("enemyname")

        self.LCDENERGY2 = QtWidgets.QLCDNumber(self.battlewidget)
        self.LCDENERGY2.setGeometry(QtCore.QRect(440, 130, 81, 31))
        self.LCDENERGY2.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.LCDENERGY2.setObjectName("LCDENERGY2")
        self.LBLWINLOSE = QtWidgets.QLabel(self.battlewidget)
        self.LBLWINLOSE.setGeometry(QtCore.QRect(470, 370, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LBLWINLOSE.setFont(font)
        self.LBLWINLOSE.setStyleSheet("color: rgb(182, 182, 182);\n"
"background-color: rgb(65, 65, 65);\n"
"")
        self.LBLWINLOSE.setText("")
        self.LBLWINLOSE.setObjectName("LBLWINLOSE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.PBEXIT.clicked.connect(QtWidgets.qApp.quit)
        self.PBPLAY.clicked.connect(self.playbutton)
        self.PBBACK.clicked.connect(self.backbutton)
        self.PBSTART.clicked.connect(self.startbutton)
        self.PBBEXIT.clicked.connect(self.exitbattle)
        self.PBFIGHT.clicked.connect(self.fightbutton)
        self.PBPROCEED.clicked.connect(self.proceedbutton); self.PBHOME.clicked.connect(self.homebutton)
        self.RB1.clicked.connect(self.p1click); self.RB2.clicked.connect(self.p2click); self.RB3.clicked.connect(self.p3click); self.RB4.clicked.connect(self.p4click); self.RB5.clicked.connect(self.p5click); self.RB6.clicked.connect(self.p6click)
        self.P1ATT1.clicked.connect(self.att1click); self.P1ATT2.clicked.connect(self.att2click); self.P1ATT3.clicked.connect(self.att3click); self.P1ATT4.clicked.connect(self.att4click)

        self.LBLWINLOSE.hide(); self.lblpickpokemon.hide(); self.selectattack.hide()
        self.battlewidget.hide(); self.selectionwidget.hide(); self.playerwidget.hide()
        self.lblpwarning1.hide(); self.lblpwarning2.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PBPLAY.setText(_translate("MainWindow", "Play"))
        self.PBEXIT.setText(_translate("MainWindow", "Exit"))
        self.lblbattle.setText(_translate("MainWindow", "B A T T L E"))
        self.PBPROCEED.setText(_translate("MainWindow", "Proceed"))
        self.PBBACK.setText(_translate("MainWindow", "Back"))
        self.lblpinfo.setText(_translate("MainWindow", "P L A Y E R  I N F O"))
        self.lblpname.setText(_translate("MainWindow", "Name :"))
        self.lblpwarning1.setText(_translate("MainWindow", "Please fill this field"))
        self.lblpwarning2.setText(_translate("MainWindow", "Please fill this field"))
        self.lblgnder.setText(_translate("MainWindow", "Gender :"))
        self.CBPGENDER.setItemText(1, _translate("MainWindow", "BOY"))
        self.CBPGENDER.setItemText(2, _translate("MainWindow", "GIRL"))
        self.PBHOME.setText(_translate("MainWindow", "Home"))
        self.PBSTART.setText(_translate("MainWindow", "Start"))
        self.lblpick.setText(_translate("MainWindow", " Pick your pokemon!"))
        self.lblpickpokemon.setText(_translate("MainWindow", " Choose a pokemon first!"))
        self.lblwinorlose.setText(_translate("MainWindow", "jejejje"))
        self.RB1.setText(_translate("MainWindow", "Bulbasaur"))
        self.RB2.setText(_translate("MainWindow", "Charmander"))
        self.RB3.setText(_translate("MainWindow", "Squirtle"))
        self.RB4.setText(_translate("MainWindow", "Pikachu"))
        self.RB5.setText(_translate("MainWindow", "Pidgey"))
        self.RB6.setText(_translate("MainWindow", "Snorlax"))
        self.lblturns.setText(_translate("MainWindow", "Turns"))
        self.lblwins.setText(_translate("MainWindow", "Wins"))
        self.PBBEXIT.setText(_translate("MainWindow", "Exit"))
        self.PBFIGHT.setText(_translate("MainWindow", "FIGHT"))
        self.P1ATT1.setText(_translate("MainWindow", "Bulbasaur"))
        self.P1ATT2.setText(_translate("MainWindow", "Bulbasaur"))
        self.P1ATT3.setText(_translate("MainWindow", "Bulbasaur"))
        self.P1ATT4.setText(_translate("MainWindow", "Bulbasaur"))
        self.LBLP2ATTACK.setText(_translate("MainWindow", "DDF"))
        self.lblvs.setText(_translate("MainWindow", "VS"))
        self.lblenergy1.setText(_translate("MainWindow", "ENERGY"))
        self.player1name.setText(_translate("MainWindow", "hehehe"))
        self.selectattack.setText(_translate("MainWindow", "Choose your move!"))
        self.lblenergy2.setText(_translate("MainWindow", "ENERGY"))
        self.enemyname.setText(_translate("MainWindow", "hohoho"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
