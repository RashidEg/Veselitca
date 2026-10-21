import game

game.init_game()

while game.is_game_active():
    game.show_game_status()
    game.spin_wheel()

    if game.is_prize_sector():
        game.announce_prize_sector()
        choice = game.get_prize_choice()

        if game.is_take_money_choice(choice):
            game.award_money_and_exit()
        elif game.is_take_box_choice(choice):
            game.reveal_black_box()
        else:
            game.msg_invalid_prize_choice()

    elif game.is_points_sector():
        game.announce_points_sector()
        guess = game.get_player_guess()

        if not game.is_valid_input(guess):
            game.msg_invalid_input()
        elif game.is_single_letter(guess):
            if game.is_already_used(guess):
                game.msg_already_used()
            elif game.is_letter_in_word(guess):
                game.register_used_letter(guess)
                game.open_guessed_letter(guess)
                game.add_sector_score()
                game.msg_correct_guess()
            else:
                game.register_used_letter(guess)
                game.add_mistake()
                game.msg_wrong_guess()
        elif game.is_whole_word_guess(guess):
            if game.is_word_match(guess):
                game.open_all_letters()
                game.award_jackpot()
                game.msg_correct_word()
            else:
                game.trigger_instant_defeat()
                game.msg_wrong_word()

if game.is_win():
    game.show_win_screen()
elif game.is_cashout():
    game.show_cashout_screen()
else:
    game.show_lose_screen()