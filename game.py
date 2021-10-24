import random


def define_game_type():
    print('Enter a list of options in winning order (e.g.: scissors, paper, rock):', end=' ')
    user_choice = input().split(',')
    basic_options = ['scissors', 'paper', 'rock']
    print("Okay, let's start")
    if user_choice == ['']:
        return basic_options
    elif all(item in user_choice[:3] for item in basic_options):
        return basic_options + user_choice[3:]
    else:
        return list(reversed(user_choice))


def define_winning_options(user_list):
    winning_list = {}
    number_of_combinations = [*range(0, len(user_list) // 2)]
    for choice in user_list:
        winning_list[choice] = []
        for n in number_of_combinations:
            index_for_element = user_list.index(choice) + 1 + n
            if index_for_element >= (len(user_list)):
                winning_list[choice].append(user_list[index_for_element - len(user_list)])
            else:
                winning_list[choice].append(user_list[index_for_element])
    return winning_list


users_option = ''

print('Enter your name: ', end='')
user_name = input()
print(f'Hello, {user_name}')

basic_combination = define_winning_options(define_game_type())

with open('rating.txt', 'r') as scores:
    scores_dict = {}
    for line in scores:
        (key, val) = line.split()
        scores_dict[key] = int(val)
    if user_name not in list(scores_dict):
        scores_dict[user_name] = 0

    while users_option != '!exit':
        users_option = input()
        computer_option = random.choice(list(basic_combination))
        if users_option in list(basic_combination):
            if computer_option == users_option:
                scores_dict[user_name] += 50
                print(f'There is a draw ({computer_option})')
            elif computer_option in basic_combination[users_option]:
                scores_dict[user_name] += 100
                print(f'Well done. The computer chose {computer_option} and failed')
            else:
                print(f'Sorry, but the computer chose {computer_option}')
        elif users_option == '!exit':
            break
        elif users_option == '!rating':
            print(f'Your rating: {scores_dict[user_name]}')  # work on this
        else:
            print('Invalid input')

print('Bye!')


