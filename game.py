import random

secret_word = ""
word_description = ""
guessed_letters = []
used_letters = []
mistakes = 0
max_mistakes = 6
score = 0
current_sector = 0
took_cashout = False

SECTOR_PRIZE = "ПРИЗ"
WHEEL_SECTORS = [100, 500, 3000, 7000, 8000, 10000,50000, SECTOR_PRIZE]

# Содержимое черного ящика
BOX_GIFTS = [
    "Автомобиль Лада!",
    "Банка соленых огурцов!",
    "Путевка в санаторий!",
    "Автомобиль Kia !",
    "Мультиварка!"
    "Деньги: 500000 рублей"
]

KEY_WORD = "word"
KEY_DESC = "desc"

def load_random_word():
    """Читает файл words.txt и выбирает случайное слово."""
    with open("words.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    random_line = random.choice(lines)
    parts = random_line.split("|")
    return {KEY_WORD: parts[0].strip().upper(), KEY_DESC: parts[1].strip()}

def init_game():
    """Инициализирует партию и сбрасывает все переменные."""
    global secret_word, word_description, guessed_letters, used_letters
    global mistakes, score, current_sector, took_cashout
    word_data = load_random_word()
    secret_word = word_data[KEY_WORD]
    word_description = word_data[KEY_DESC]
    guessed_letters = ["_"] * len(secret_word)
    used_letters = []
    mistakes = 0
    score = 0
    current_sector = 0
    took_cashout = False

def spin_wheel():
    """Вращает барабан."""
    global current_sector
    current_sector = random.choice(WHEEL_SECTORS)

def is_prize_sector():
    """Проверяет, выпал ли сектор ПРИЗ."""
    return current_sector == SECTOR_PRIZE

def is_points_sector():
    """Проверяет, выпал ли числовой сектор с очками."""
    return current_sector != SECTOR_PRIZE

def announce_prize_sector():
    print("\n ВНИМАНИЕ! На барабане сектор ПРИЗ!")
    print("Вы можете забрать 50 000 рублей деньгами или открыть ЧЕРНЫЙ ЯЩИК!")

def announce_points_sector():
    print(f"\n На барабане: {current_sector} очков за букву!")

def get_prize_choice():
    return input("Выберите: 1 - Деньги (50 000 руб.), 2 - Черный ящик: ").strip()

def is_take_money_choice(choice):
    return choice == "1"

def is_take_box_choice(choice):
    return choice == "2"

def award_money_and_exit():
    global score, took_cashout
    score += 50000
    took_cashout = True
    print("\n Вы решили забрать деньги и закончить игру!")

def reveal_black_box():
    global took_cashout
    gift = random.choice(BOX_GIFTS)
    took_cashout = True
    print(f"\n Открываем черную коробку... А внутри: {gift}")

def is_cashout():
    return took_cashout

def add_sector_score():
    global score
    last_letter = used_letters[-1]
    count = secret_word.count(last_letter)
    score += current_sector * count

def award_jackpot():
    global score
    score += 5000

def draw_gallows():
    """Считывает файл этапа виселицы и выводит в консоль."""
    filename = f"viselitsa_{mistakes}.txt"
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

def show_game_status():
    print("\n" + "=" * 50)
    draw_gallows()
    print(f"Очки: {score}")
    print(f"Задание: {word_description}")
    print("Слово:   " + " ".join(guessed_letters))
    print("Названные буквы: " + ", ".join(used_letters))
    print("=" * 50)

def get_player_guess():
    return input("Назовите букву или слово целиком: ").strip().upper()

def is_game_active():
    return ("_" in guessed_letters) and (mistakes < max_mistakes) and (not took_cashout)

def is_valid_input(text):
    return len(text) > 0 and text.isalpha()

def is_single_letter(text):
    return len(text) == 1

def is_whole_word_guess(text):
    return len(text) > 1

def is_already_used(letter):
    return letter in used_letters

def is_letter_in_word(letter):
    return letter in secret_word

def is_word_match(word):
    return word == secret_word

def register_used_letter(letter):
    used_letters.append(letter)

def open_guessed_letter(letter):
    for index, char in enumerate(secret_word):
        if char == letter:
            guessed_letters[index] = letter

def open_all_letters():
    global guessed_letters
    guessed_letters = list(secret_word)

def add_mistake():
    global mistakes
    mistakes += 1

def trigger_instant_defeat():
    global mistakes
    mistakes = max_mistakes

def is_win():
    return ("_" not in guessed_letters) and (not took_cashout)

def msg_invalid_prize_choice():
    print("\n[!] Некорректный выбор! Сектор сгорает, игра продолжается.")


def msg_invalid_input():
    print("\n[!] Ошибка: ввод должен состоять только из букв!")

def msg_already_used():
    print("\n[!] Вы уже называли эту букву! Попробуйте другую.")

def msg_correct_guess():
    print("\n[+] Есть такая буква! Очки начислены.")

def msg_wrong_guess():
    print("\n[-] Такой буквы нет! Фигура на виселице дорисована.")

def msg_correct_word():
    print("\n[*] НЕВЕРОЯТНО! Вы угадали слово целиком!")

def msg_wrong_word():
    print("\n[x] Это не то слово! Вы отправляетесь на виселицу.")

def show_win_screen():
    show_game_status()
    print(f"\n ПОБЕДА! Вы разгадали слово: {secret_word}")
    print(f"Ваш финальный счет: {score} очков!")

def show_cashout_screen():
    print("\n ИГРА ЗАВЕРШЕНА! Вы ушли с призом.")
    print(f"Секретное слово было: {secret_word}")

def show_lose_screen():
    show_game_status()
    print(f"\n ВЫ ПРОИГРАЛИ! Слово было: {secret_word}")
    print(f"Счет: {score} очков.")