import random

bot_options = ["Piedra!", "Papel!", "Tijeras!"]
player_options = ["piedra", "papel", "tijera", "tijeras"]
incorrect_option = []

print("Juguemos al piedra, papel o tijera!")
print ("Empieza tú!")

while True:
	
	random_option = random.randint(0, 2)
	bot_choice = bot_options[random_option]

	choice = input()

	for i in player_options:  
		if i.lower() != choice.lower():
			incorrect_option.append(True)
	
	if incorrect_option.count(True) == 4:
		incorrect_option *= 0
		print("No hagas trampas! Elige piedra, papel o tijera!")
	else:
		print(bot_choice)
		if choice.lower() == "piedra": 
			if random_option == 0:
				print("Empate piedra")
    	    
			elif random_option == 1:
				print("Ganas tú!")
    	    
			elif random_option == 2:
				print("Gano yo!")
    	
		if choice.lower() == "papel":
			if random_option == 0:
				print("Ganas tú")
    	    	
			elif random_option == 1:
				print("Empate papel")
    	    
			elif random_option == 2:
				print("Gano yo")
    	
		if choice.lower() == "tijera" or choice.lower() == "tijeras":
			if random_option == 0:
				print("Gano yo!")
    			
			elif random_option == 1:
				print("Ganas tú!")
    		
			elif random_option == 2:
				print ("Empate tijera")

		print("Juguemos otra!")
    	
	


