class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team


class Board:
    def __init__(self, turns = 0, spot = [], player_list=[]):
        self.turns = turns
        self.spot = spot
        self.player_list = player_list

    def init(self):
        count = 1
        for _ in range(9):
            self.spot.append(count)
            count += 1

        key1 = input("Enter Player 1 name: ")
        key2 = input("Enter Player 2 name: ")
        key3 = input(f'{key1} please choose between X/O: ')
        if key3.lower() == "x":
            key4 = 'X'
            key5 = 'O'
        else:
            key4 = 'O'
            key5 = 'X'

        player1 = Player(key1, key4)
        player2 = Player(key2, key5)
        self.player_list.append(player1)
        self.player_list.append(player2)

    def show_board(self):
        print('\n')
        print(f'{self.spot[0]} | {self.spot[1]} | {self.spot[2]}')
        print("--|---|--")
        print(f'{self.spot[3]} | {self.spot[4]} | {self.spot[5]}')
        print("--|---|--")
        print(f'{self.spot[6]} | {self.spot[7]} | {self.spot[8]}')
        print('\n')

    def print_win(self, player):
        print(f'{player.name} has won')
        self.show_board() 

    def winner(self, player):
        if self.spot[0] == self.spot[1] == self.spot[2]:
            self.print_win(player)
            return True
        elif self.spot[3] == self.spot[4] == self.spot[5]:
            self.print_win(player)
            return True
        elif self.spot[6] == self.spot[7] == self.spot[8]:
            self.print_win(player)
            return True
        elif self.spot[0] == self.spot[3] == self.spot[6]:
            self.print_win(player)
            return True
        elif self.spot[1] == self.spot[4] == self.spot[7]:
            self.print_win(player)
            return True
        elif self.spot[2] == self.spot[5] == self.spot[8]:
            self.print_win(player)
            return True
        elif self.spot[0] == self.spot[4] == self.spot[8]:
            self.print_win(player)
            return True
        elif self.spot[2] == self.spot[4] == self.spot[6]:
            self.print_win(player)
            return True
        
        if self.turns == 9:
            print("Tie Game")
            self.show_board()
            self.end()
        
    def end(self):
        key = input("Play again? (Y/N): ")
        if key.lower() == 'y':
            self.player_list.clear()
            self.spot.clear()
            self.turns = 0
            self.run_game()
        else:
            exit()

    def ask_player(self, player):
            self.show_board()  
            if player == self.player_list[0]:          
                key = int(input(f'{self.player_list[0].name} please enter a # to place your {self.player_list[0].team}: '))
                if self.spot[key-1] == 'X' or self.spot[key-1] == 'O':
                    print("That spot was already taken")
                    self.ask_player(self.player_list[0])
                self.spot[key-1] = self.player_list[0].team
                self.turns += 1
                win1 = self.winner(self.player_list[0])
                if win1 == True:
                    self.end()
                self.ask_player(self.player_list[1])
            else:
                self.show_board()
                key = int(input(f'{self.player_list[1].name} please enter a # to place your {self.player_list[1].team}: '))
                if self.spot[key-1] == 'X' or self.spot[key-1] == 'O':
                    print("That spot was already taken")
                    self.ask_player(self.player_list[1])
                self.spot[key-1] = self.player_list[1].team
                self.turns += 1
                win2 = self.winner(self.player_list[1])
                if win2 == True:
                    self.end()
                self.ask_player(self.player_list[0])

    def run_game(self):
        self.init()
        self.ask_player(self.player_list[0])

me = Board()
me.run_game()