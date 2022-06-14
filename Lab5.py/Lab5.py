from moduleLab5 import input_name, game_dice, winner

namePlayer1 = input_name(1)
namePlayer2 = input_name(2)
summPointsPlayers = game_dice(namePlayer1, namePlayer2)
winner (namePlayer1, namePlayer2, summPointsPlayers[0],summPointsPlayers[1])
