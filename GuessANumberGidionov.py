import random

computer_number = random.randint(1, 100)
counter = 0
while True:
    player_input = input("Познай номера (1-100): ")
    counter += 1

    if not player_input.isdigit():
        print("Невалиден вход. Опитай пак...")
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        if counter == 1:
            print("НЕВЕРОЯТНО, ПОЗНА ОТ ПЪРВИЯ ПЪТ!")
        else:
            print(f"ПОЗДРАВЛЕНИЕ, позна с {counter} опита")
        break
    elif player_number > computer_number:
        print("Твърде високо!")
        print("Опитай пак!")
        continue
    else:
        print("Твърде ниско!")
        print("Опитай пак!")
        continue


