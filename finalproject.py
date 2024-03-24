import random

def get_user_choice():
    user_choice = input("Швиденько вибирайте: камінь, ножиці або папір: ").strip().lower()
    if user_choice not in ["камінь", "ножиці", "папір"]:
        print("Та блін нормально впишіть: камінь, ножиці або папір.")
        user_choice = input("Виберіть: камінь, ножиці або папір: ").strip().lower()
    return user_choice


def get_computer_choice():
    choices = ["камінь", "ножиці", "папір"]
    return random.choice(choices)


def hto_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ви думаєте як комп'ютер!НІЧИЯ"
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
            (user_choice == "ножиці" and computer_choice == "папір") or \
            (user_choice == "папір" and computer_choice == "камінь"):
        return "Харош, тепер ви супер сігма 2019про"
    else:
        return "Параженіе..."


def main():
    print("Гра 'Камінь, ножиці, папір'")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Ви вибрали: {user_choice}")
        print(f"Комп'ютер вибрав: {computer_choice}")

        winner = hto_winner(user_choice, computer_choice)
        print(winner)

        play_again = input("Го ше раз?(го/гг тіма раків я ліваю): ").strip().lower()
        if play_again != "го":
            break


if __name__ == "__main__":
    main()