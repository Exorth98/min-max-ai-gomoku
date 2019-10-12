from random import randint
import os
from GlobalVariables import *

def ConvertToInt(letter):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    return letters.index(letter)

def Result(jeu,profondeur,user,ai):

    coupPossible=majCoupPossible(jeu);
    max = -500000;
    maxi=7;
    maxj=7;
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):           
            if jeu[i][j] == ' ' and coupPossible[i][j]==True:
                jeu[i][j] = ai
                tmp = Min(jeu,profondeur,-500000,500000,user,ai)
                if tmp>max:
                    max = tmp
                    maxi = i
                    maxj = j 
                rnd = randint(0,1)
                if tmp == max and rnd == 0:
                    maxi = i
                    maxj = j      
                jeu[i][j] = ' '
    jeu[maxi][maxj] = ai
    return jeu

def Max(jeu,profondeur,alpha,beta,user,ai):

    coupPossible=majCoupPossible(jeu);
    if profondeur == 0 :   
        return utility(jeu,user,ai)
    if TerminalTest(jeu,user,ai)!='Nobody' : 
        return utility(jeu,user,ai)
    max = -500000;
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == ' ' and coupPossible[i][j]==True:
                jeu[i][j] = ai
                tmp = Min(jeu,profondeur-1,alpha,beta,user,ai) 
                if tmp>alpha:
                    alpha=tmp
                if alpha>beta:
                    jeu[i][j] = ' '
                    #print("COUPER MAX")
                    return tmp;
                if tmp > max:
                    max = tmp
                rnd = randint(0,1)
                if tmp == max and rnd == 0:
                    max = tmp
                jeu[i][j] = ' '
    return max;

def Min(jeu,profondeur,alpha,beta,user,ai):

    coupPossible=majCoupPossible(jeu);
    if profondeur == 0 :   
        return utility(jeu,user,ai)
    if TerminalTest(jeu,user,ai)!='Nobody' :  
        return utility(jeu)
    min = 500000;
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j] == ' ' and coupPossible[i][j]==True:
                jeu[i][j] = user
                tmp = Max(jeu,profondeur-1,alpha,beta,user,ai)
                if tmp<beta:
                    beta=tmp
                if alpha>beta:
                    jeu[i][j] = ' '
                    #print("COUPER MIN")
                    return tmp;
                if tmp < min :
                    min = tmp
                rnd = randint(0,1)
                if tmp == min and rnd == 0:
                    min = tmp
                jeu[i][j] = ' '
    return min

def playAI(board, depth,user,ai):
    print("L'IA joue ...")
    Result(board,depth,user,ai)
    printBoard(board)

def majCoupPossible(jeu):
    global taillePlateau
    coupPossible = [False] * taillePlateau
    #print("AYYYA");
    for i in range(taillePlateau):
        coupPossible[i] = [False] * taillePlateau
    for i in range(len(jeu)):
        for j in range(len(jeu[0])): 
            if jeu[i][j]!=' ':
                
                for k in range(5):
                    for l in range(5):
                        if i+k-2>=0 and j+l-2>=0 and i+k-2<len(jeu) and j+l-2<len(jeu):
                            coupPossible[i+k-2][j+l-2]=True;           

                            
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            if jeu[i][j]!=' ':
                coupPossible[i][j]=False;
    #printBoard(coupPossible)

    global round
    if(round == 3):
        for i in range(7):
            for j in range(7):
                coupPossible[i+4][j+4]



    return coupPossible;

def ConvertIntToLettre(nb):
    array = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    return array[nb];

def printBoard(board):

    print("    01  02  03  04  05  06  07  08  09  10  11  12  13  14  15")
    for i in range(len(board)):
        print(" {} |".format(ConvertIntToLettre(i)), end='')
        for j in range(len(board)):
            print(" {} ".format(board[i][j]), end ='|')
        print()
    print()

def utility(jeu,user,ai): #compte le nb de n pions aligné
    #print ("yay")
    nb_de_pions = 0
    #On compte le nombre de pions présents sur le plateau
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if jeu[i][j] != ' ':
                nb_de_pions = nb_de_pions + 1
    vainqueur = TerminalTest(jeu,user,ai)
    if vainqueur != 'Nobody':
        if vainqueur == ai :     
            return 100000 - nb_de_pions
        elif vainqueur == user :
            return 0 - 100000 + nb_de_pions
        else :
            return 0;  
    
    score1 = points(jeu,ai) 
    score2 = -1.2*points(jeu,user)
    score = score1-score2
    '''print(score1)
    print(score2)
    print(score)'''
    return score ;
    
def points(jeu,t):
    retour=0;

    for i in range(len(jeu)):
        for j in range(len(jeu[0])-4): 
            compteur1 = [' ']*5;
            compteur2 = [' ']*5;
            compteur3 = [' ']*5;
            for k in range(5):
                compteur1[k]=jeu[i][j+k];
                compteur2[k]=jeu[j+k][i];
                if i<len(jeu[0])-4:
                    compteur3[k]=jeu[i+k][j+k];
            if heuristiqueUtileKa(compteur1,t):         
                retour+=heuristique5(compteur1,t);
            if heuristiqueUtileKa(compteur2,t):
                retour+=heuristique5(compteur2,t);
            if i<len(jeu[0])-4:
                if heuristiqueUtileKa(compteur3,t):
                    retour+=heuristique5(compteur3,t);
        for j in range(len(jeu[0])-5): 
            compteur1 = [' ']*6;
            compteur2 = [' ']*6;
            compteur3 = [' ']*6;
            for k in range(6):
                compteur1[k]=jeu[i][j+k];
                compteur2[k]=jeu[j+k][i];
                if i<len(jeu[0])-5:
                    compteur3[k]=jeu[i+k][j+k];
            if heuristiqueUtileKa(compteur1,t):
                retour+=heuristique5(compteur1,t);
            if heuristiqueUtileKa(compteur2,t):
                retour+=heuristique5(compteur2,t);
            if i<len(jeu[0])-5:
                if heuristiqueUtileKa(compteur3,t):
                    retour+=heuristique5(compteur3,t);
        for j in range(len(jeu[0])-6): 
            compteur1 = [' ']*7;
            compteur2 = [' ']*7;
            compteur3 = [' ']*7;
            for k in range(7):
                compteur1[k]=jeu[i][j+k];
                compteur2[k]=jeu[j+k][i];
                if i<len(jeu[0])-6:
                    compteur3[k]=jeu[i+k][j+k];
            if heuristiqueUtileKa(compteur1,t):
                retour+=heuristique5(compteur1,t);
            if heuristiqueUtileKa(compteur2,t):
                retour+=heuristique5(compteur2,t);
            if i<len(jeu[0])-6:
                if heuristiqueUtileKa(compteur3,t):
                    retour+=heuristique5(compteur3,t);
    return retour
 
def heuristiqueUtileKa(compteur,t):
    for i in range(len(compteur)):
        if compteur[i]!=t and compteur[i] !=' ':
            return False
    return True;

def heuristique5(compteur,t):
    retour = 0;
    if compteur==[' ',t,' ',t,' ']:
        retour+=2;
    elif compteur==[' ',t,t,' ',' ']:
        retour+=2;
    elif compteur==[' ',' ',t,t,' ']:
        retour+=2;
    elif compteur==[t,' ',' ',' ',t]:
        retour+=1;
    elif compteur==[t,' ',' ',t,' ']:
        retour+=1;
    elif compteur==[' ',t,' ',' ',t]:
        retour+=1;
    elif compteur==[t,' ',t,' ',' ']:
        retour+=1;
    elif compteur==[' ',' ',t,' ',t]:
        retour+=1;

    elif compteur==[' ',t,t,t,' ']:
        retour+=15;
    elif compteur==[t,t,t,' ',' ']:
        retour+=15;
    elif compteur==[' ',' ',t,t,t]:
        retour+=15;
    elif compteur==[t,' ',t,t,' ']:
        retour+=10;
    elif compteur==[' ',t,t,' ',t]:
        retour+=10;
    elif compteur==[' ',t,' ',t,t]:
        retour+=10;
    elif compteur==[t,t,' ',t,' ']:
        retour+=10;

    elif compteur==[t,t,' ',t,t]:
        retour+=70;
    elif compteur==[t,t,t,t,' ']:
        retour+=70;
    elif compteur==[' ',t,t,t,t]:
        retour+=70;
    elif compteur==[t,t,t,' ',t]:
        retour+=70;
    elif compteur==[t,' ',t,t,t]:
        retour+=70;
    elif compteur==[t,t,t,t,t]:
        retour+=20000
    return retour;

def heuristique6(compteur,t):
    retour =0;
    if compteur==[' ',' ',t,t,' ',' ']:
        retour+=3;
    elif compteur==[' ',t,' ',' ',t,' ']:
        compteur+=3
    elif compteur1==[' ',t,t,t,t,' ']:
        retour+=5000;
    elif compteur1==[' ',t,' ',t,t,' ']:
        retour+=70;
    elif compteur1==[t,t,' ',t,t,' ']:
        retour+=70;
    elif compteur1==[' ',t,t,' ',t,t]:
        retour+=70;
    elif compteur1==[' ',t,t,' ',t,' ']:
        retour+=70;
    elif compteur1==[' ',t,t,t,' ',' ']:
        retour+=72;
    elif compteur1==[' ',' ',t,t,t,' ']:
        retour+=72;
    return retour;

def heuristique7(compteur,t):
    retour =0;
    if compteur1==[' ',t,' ',t,t,' ',' ']:
        retour+=25
    elif compteur1==[' ',t,t,' ',t,t,' ']:
        retour+=70
    elif compteur1==[' ',' ',t,t,' ',t,' ']:
        retour+=25
    elif compteur1==[' ',' ',t,t,t,' ',' ']:
        retour+=110
    elif compteur==[' ',' ',t,' ',t,' ',' ']:
        retour+=10;
    return retour;

def TerminalTest(jeu,user,ai):

    #On compte le nombre de cases vides
    empty = 0
    for i in range(len(jeu)):
        for j in range(len(jeu[0])): 
            if jeu[i][j] == ' ':
                empty = empty + 1;
    #compteur1;
    #compteur2;
    #compteur3;
    for i in range(len(jeu)):
        for j in range(len(jeu[0])-4): 
            compteur1 = [' ']*5;
            compteur2 = [' ']*5;
            compteur3 = [' ']*5;
            for k in range(5):
                compteur1[k]=jeu[i][j+k];
                compteur2[k]=jeu[j+k][i];
                if i<len(jeu[0])-4:
                    compteur3[k]=jeu[i+k][j+k];
            if(compteur1==[ai,ai,ai,ai,ai]or compteur2==[ai,ai,ai,ai,ai]or compteur3==[ai,ai,ai,ai,ai]):
                return ai;
            if(compteur1==[user,user,user,user,user]or compteur2==[user,user,user,user,user]or compteur3==[user,user,user,user,user]):
                return user;
    if empty == 0:
        return 'Draw';
    else:
        return 'Nobody';


if __name__ == "__main__":

    '''plateau = [' '] * taillePlateau
    for i in range(taillePlateau):
        plateau[i] = [' '] * taillePlateau
    playAI(plateau,1)'''
    print(ConvertToInt('A'))
    # profondeur 0: prevois un coup ennemi, puis un coup allié, puis joue ce coup allié
    # profondeur 1: prevois un coup ennemi, puis un coup allié, puis  un ennemi, puis un allié et joue ce coup

    os.system("pause")



#python C:\datascience\GomokuV2.py
