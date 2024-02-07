"""
================================|  Временный говнокод, который нужен для тестов, пока нету самого бота  |===================================
"""


from sympy import use
from components import Game


# Тут создаётся игра
game = Game('пупа', 'лупа', 1, 2)
game.round = 1
game.StartNewRound()

user_id = game.turn.GetID()  # в боте эта переменная зависит от ID человека, чьё сообщение было обработано


# Действия, выполняемые с каждой новой обоймой
if game.shotgun.IsEmpty():
    print('текущий раунд', game.round)
    pellets = game.shotgun.Charge()
    print("Дробовик заряжен:", pellets)
    print(f"Игрок '{game.player_1.name}' получил предметы:", game.player_1.AddItems((game.round - 1) * 2))
    print(f"Игрок '{game.player_2.name}' получил предметы:", game.player_2.AddItems((game.round - 1) * 2))
print('\n' * 3)

print('Сейчас ходит игрок', game.turn.name)
    
print(f'|{game.player_1.name:{"-"}^40}|')
print('Здоровье:', game.player_1.hp)
print('Предметы:', game.player_1.GetItems())
print()
print(f'|{game.player_2.name:{"-"}^40}|')
print('Здоровье:', game.player_2.hp)
print('Предметы:', game.player_2.GetItems())
    
while (command := input("Введите команду: ")):
    print('\n' * 10)

    # Ход игрока
    if game.IsMyTurn(user_id):
        game.LoadPellet()

        # тут надо прикрутить обработчик инлайн кнопок, то есть этот match будет в функции с декоратором callback_query_handler
        match command:
            case 'to_opponent':
                game.Shot('to_opponent')

            case 'to_myself':
                game.Shot('to_myself')

            case 'use_item':  # не создавать эту кнопку, если предметов нету
                item = input("Введите желаемый предмет: ")  # В боте будут прикрепляться кнопки с текущими предметами, т.о. можно избежать лишних проверок
                
                game.GetPlayerByID(user_id).UseItem(item)
                # тут надо прикрутить обработчик инлайн кнопок, то есть этот match будет в функции с декоратором callback_query_handler
                match item:
                    # пила (значение сбрасывается само)
                    case 'saw':
                        game.shotgun.SetDamage(2)

                    # пиво
                    case 'beer':
                        print("Высранная пуля:", game.current_pellet)
                        game.LoadPellet(True)

                    # лупа
                    case 'magnifying_glass':
                        print("Сейчас в дробовике заряжена пуля:", game.current_pellet)

                    # наручники (значение сбрасывается само)
                    case 'handcuffs':
                        game.is_handcuffs_used = True

                    # сигареты
                    case 'cigarettes':
                        game.GetPlayerByID(user_id).Heal()
    
    # Если кто-то умер, нужно запустить новый раунд
    if not (winner := game.WhoWin()) is None:
        print(f"Игрок {winner.name} красава жи есть!!1!!!")
        game.StartNewRound()
        game.shotgun.pellets.clear()
    
     # Действия, выполняемые с каждой новой обоймой
    if game.shotgun.IsEmpty() and game.current_pellet == -1:
        pellets = game.shotgun.Charge()
        print("Дробовик заряжен:", pellets)
        print(f"Игрок '{game.player_1.name}' получил предметы:", game.player_1.AddItems((game.round - 1) * 2))
        print(f"Игрок '{game.player_2.name}' получил предметы:", game.player_2.AddItems((game.round - 1) * 2))

    user_id = game.turn.GetID()  # в боте эта переменная зависит от ID человека, чьё сообщение было обработано
    
    # КОСМЕТИКА
    print('Сейчас ходит игрок', game.turn.name, user_id)
    
    print(f'|{game.player_1.name:{"-"}^20}|')
    print('Здоровье:', game.player_1.hp)
    print('Предметы:', game.player_1.GetItems())
    
    print(f'|{game.player_2.name:{"-"}^20}|')
    print('Здоровье:', game.player_2.hp)
    print('Предметы:', game.player_2.GetItems())