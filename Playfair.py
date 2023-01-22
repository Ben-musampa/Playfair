import numpy as np
import random

#clé 5X5
K = np.array([['A','Z','I','X','D'],
                ['E','U','T','G','Y'],
                ['O','N','K','Q','M'],
                ['H','F','J','L','S'],
                ['V','R','P','B','C']])
#choisir aleatoirement un caractère ssi l'indice dans le tableau a plus d'un carractère


#print(np.char.str_len(K))


speciale = "X" #le carractère speciale

#La première fonction est celle qui s'occupe de remplacer les doublons par le caractère spéciale 
def separer_lettres_semblables(message):
    index = 0
    while (index<len(message)):
        m1 = message[index]
        if index == len(message)-1:
            message = message + speciale
            index += 2
            continue
        m2 = message[index+1]
        if m1==m2:
            message = message[:index+1] + speciale + message[index+1:]
        index +=2   
    return message

#print(separer_lettres_semblables("FEMME"))

#la deuxième fonction s'occupe de chiffrer le message
def Chiffrement_playfair(message, Key):

    message_chiffrer=""

    message = message.upper()
    message = message.replace(' ', '')
    message = separer_lettres_semblables(message)


    for i in range(0, len(message)-1, 2): 
        """pour chaque i (occurence) dans l'intervalle allant de O à la longeur du message -1
        en sotant deux caratère et les régroupés deux-à-deux puis faire:
        """
        x1, y1 = np.where(Key == message[i])[0][0], np.where(Key == message[i])[1][0]
        x2, y2 = np.where(Key == message[i+1])[0][0], np.where(Key == message[i+1])[1][0]

        """étant dans numpy nous pouvons nous permetre d'utiliser la fonction where pour facilement trouver 
        l'emplacelent de nos données, ici de nos occurences
        
        puis:"""
        
        if x1 == x2:
            message_chiffrer += Key[x1, (y1+1)%5] + Key[x2, (y2+1)%5]
        elif y1 == y2:
            message_chiffrer += Key[(x1+1)%5, y1] + Key[(x2+1)%5, y2]
        else:
            message_chiffrer += Key[x1, y2] + Key[x2, y1]

    return message_chiffrer

#la troisième fonction s'occupe à déchiffrer le message 
def dechiffrement_playfair(message, Key):

    message_dechiffrer=""

    message = message.upper()
    message = message.replace(' ', '')
    message = separer_lettres_semblables(message)

    for i in range(0, len(message)-1, 2):
        x1, y1 = np.where(Key == message[i])[0][0], np.where(Key == message[i])[1][0]
        x2, y2 = np.where(Key == message[i+1])[0][0], np.where(Key == message[i+1])[1][0]

        if x1 == x2:
            message_dechiffrer += Key[x1, (y1-1)%5] + Key[x2, (y2-1)%5]
        elif y1 == y2:
            message_dechiffrer += Key[(x1-1)%5, y1] + Key[(x2-1)%5, y2]
        else:
            message_dechiffrer += Key[x1, y2] + Key[x2, y1]

    return message_dechiffrer


print('le message chiffré est : ')
print(Chiffrement_playfair("ejdjdjejgavoiejynkyvtivozu", K))
print('le message déchiffré est : ')
print(dechiffrement_playfair("ejdjdjejgavoiejynkyvtivozu", K))
