import random

min = 1
max = 10


print(f"Jugador 1, elige un número entre {min} y {max}")
guess1 = input()
int1 = int(guess1)

print(f"Jugador 2, elige un número entre {min} y {max}")
guess2 = input()
int2 = int(guess2)

answer = random.randint(min, max)
score1 = abs(int1 - answer)
score2 = abs(int2 - answer)

print(f"El número era {answer}" )

if int(score1) > int(score2):
	print("El ganador es el Jugador 2")
elif int(score1) < int(score2):
	print("El ganador es el Jugador 1")
else:
    print("Empate!!")


