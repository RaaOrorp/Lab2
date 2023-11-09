import random


num_stones = random.randint(4, 30)
print(f"В кучке {num_stones} камней.")

while num_stones > 0:
    player_choice = int(input("Сколько камней вы хотите взять (1-3)?: "))
    while player_choice < 1 or player_choice > 3:
        player_choice = int(input("Вы можете взять от 1 до 3 камней. Сколько камней вы хотите взять (1-3)? "))

    num_stones -= player_choice
    print(f"В кучке осталось {num_stones} камней.")

    if num_stones == 0:
        print("Вы выиграли!")
        exit()

    computer_choice = random.randint(1, 3)
    num_stones -= computer_choice
    print(f"Компьютер взял {computer_choice} камней.")
    print(f"В кучке осталось {num_stones} камней.")

    if num_stones == 0:
        print("Компьютер выиграл!")
        exit()