import numpy as np
import random
from random import choice

# Clé 5X5
K = np.array([['A','Z','I','X','D'],
              ['E','U','T','G','Y'],
              ['O','N','K','Q','M'],
              ['H','F','J','L','S'],
              ['V','R','P','B','C']])

# Caractère spécial
speciale = "X"

# Fonction pour séparer les lettres semblables
def separer_lettres_semblables(message):
  index = 0
  while (index < len(message)):
    m1 = message[index]
    if index == len(message) - 1:
      message = message + speciale  # Ajouté
      index += 2  # Ajouté
      continue
    m2 = message[index+1]
    if m1 == m2:
      message = message[:index] + speciale + message[index+1:]
    index += 2
  return message

# Fonction pour chiffrer le message
def Chiffrement_playfair(message, Key):

  message_chiffrer = ""

  message = message.upper()
  message = message.replace(' ', '')
  message = separer_lettres_semblables(message)

  for i in range(0, len(message)-1, 2):
    x1, y1 = np.where(Key == message[i])[0][0], np.where(Key == message[i])[1][0]
    x2, y2 = np.where(Key == message[i+1])[0][0], np.where(Key == message[i+1])[1][0]

    if Key[x1, y1] == '':  # Ajouté
      carac_dispo = list(Key.flatten())
      carac_dispo.remove(speciale)
      carac_aleatoire = random.choice(carac_dispo)
      Key[x1, y1] = carac_aleatoire

    if Key[x2, y2] == '':  # Ajouté
      carac_dispo = list(Key.flatten())
      carac_dispo.remove(speciale)
      carac_aleatoire = random.choice(carac_dispo)
      Key[x2, y2] = carac_aleatoire

    if x1 == x2:
      message_chiffrer += Key[x1, (y1+1)%5] + Key[x2, (y2+1)%5]
    elif y1 == y2:
      message_chiffrer += Key[(x1+1)%5, y1] + Key[(x2+1)%5, y2]
    else:
      message_chiffrer += Key[x1, y2] + Key[x2, y1]

  return message_chiffrer

# Fonction pour déchiffrer le message
def dechiffrement_playfair(message, Key):

  message_dechiffrer = ""

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

# Test avec un message
message = "attaque surprise a l'aube"
print('Le message original est :', message)

message_chiffre = Chiffrement_playfair(message, K)
