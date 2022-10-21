import argparse
import random

from GUI import GUI


class CardDeck:
    """Class for a card deck and has methods to simulate pulling cards from the deck."""

    def __init__(self) -> None:
        self.create_deck()

    def create_deck(self):
        """Creates a deck of cards by looping through the different variables of a card."""
        values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        suits = ("H", "D", "S", "C")
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(suit + str(value))

    def pull_card(self) -> str:
        """Returns a random card from the deck and removes that card from the deck.

        Returns:
            str: A string representing a card in the deck.
        """
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card


class Player:
    """Class to represent each player and their stats in a game of poker."""

    community_cards = []

    def __init__(self, name: str) -> None:
        self.balance = 10
        self.bet_amount = 0
        self.name = name
        self.personal_cards = ()
        self.hand = []
        self.score = int()
        self.tie_data = []

    @classmethod
    def set_community_cards(cls, cards: tuple) -> None:
        """Updates the class variable of community_card with data from tuple.

        Args:
            cards (tuple): Cards to add to the class variable community_cards.
        """
        for card in cards:
            cls.community_cards.append(card)

    @classmethod
    def get_community_cards(cls) -> list:
        """Returns the class variable community_cards.

        Returns:
            list: Class variable community_cards.
        """
        return cls.community_cards

    def start_game(self, card1: str, card2: str):
        """_summary_

        Args:
            card1 (str): First personal card that was pulled.
            card2 (str): Second personal card that was pulled.
        """
        self.personal_cards = (card1, card2)
        self.hand = [card1, card2]

    def set_hand(self, cards: tuple):
        """Loops through tuple of cards and adds cards to the instance variable hand.

        Args:
            cards (tuple): Tuple of cards to add to instance variable hand.
        """
        for card in cards:
            self.hand.append(card)

    def get_name(self) -> str:
        """Returns name instance variable.

        Returns:
            str: Instance variable of name.
        """
        return self.name

    def set_bet_amount(self, bet_amount: int):
        """Sets the instance variable of bet_amount to a new int.

        Args:
            bet_amount (int): Int value that replace the instance variable of bet_amount.
        """
        self.bet_amount = bet_amount

    def get_bet_amount(self) -> int:
        """Returns instance variable of bet_amount.

        Returns:
            int: Instance variable of bet_amount.
        """
        return self.bet_amount

    def set_balance(self, balance: int):
        """Adds int input to the instance variable of balance to update player balance.

        Args:
            balance (int): Int to add to the balance instance variable.
        """
        self.balance += balance

    def get_balance(self) -> int:
        """Return balance instance variable.

        Returns:
            int: Balance instance variable.
        """
        return self.balance

    def get_personal_cards(self) -> tuple:
        """Return personal_cards instance variable.

        Returns:
            tuple: personal_cards instance variable.
        """
        return self.personal_cards

    def get_score(self) -> int:
        """Return score instance variable.

        Returns:
            int: score instance variable.
        """
        return self.score

    def get_tie_data(self) -> list[int]:
        """Return tie_data instance variable.

        Returns:
            list[int]: tie_data instance variable.
        """
        return self.tie_data

    def calculate_score(self):
        """Calculates and sets the score and tie_data instance variables.
        Calls class methods parse_data(), straight(), repeated_suit(), royal_flush(), repeated_values(),
        straight_flush(), and score_data() to determine score and tie_data instance variables."""
        same_suit, same_value, clean_data = self.parse_data()
        royal_flush, straight_flush, flush = self.flush(same_suit)
        straight = self.straight(clean_data)
        pair, three, four = self.repeated_values(same_value)
        self.score_data(
            royal_flush,
            straight_flush,
            flush,
            straight,
            pair,
            three,
            four,
            clean_data,
        )

    def flush(self, same_suit: dict) -> tuple[bool, tuple, tuple]:
        """Determines whether the hand qualifies as flush, straight flush, or a royal flush.

        Args:
            same_suit (dict): Dictionary with card suit as key and a list of card values with the given suit as the value.

        Returns:
            tuple[bool, tuple, tuple]: Bool showing if the hand is a royal flush. Tuple of highest value in the cards that is
            used for a straight flush. Tuple of the highest five card values that make a flush.
        """
        royal_flush = False
        straight_flush = []
        flush = ()

        for suit in same_suit:
            if len(same_suit[suit]) >= 5:
                flush = tuple(sorted(same_suit[suit], reverse=True)[:5])

                flush_copy = same_suit[suit][:]
                flush_copy = sorted(list(set(flush_copy)))
                for index in range(len(flush_copy) - 4):
                    if flush_copy[index] + 4 == flush_copy[index + 4]:
                        straight_flush.append(flush_copy[index + 4])
                    if flush_copy[index] == 10:
                        royal_flush = True

        straight_flush = tuple(sorted(straight_flush, reverse=True)[:1])

        return royal_flush, straight_flush, flush

    def parse_data(self) -> tuple[dict, dict, list]:
        """Loops through player card data and returns the information in useful data types to later be used to determine the winner.

        Returns:
            tuple[dict, dict, list]: A dict with the suit as the key and the number of occurrences as value. A dict with the card value as
            the key and the number of occurrences as the value. A list of all the card values.
        """
        same_suit = {}
        same_value = {}
        clean_data = []

        for card in self.hand:
            # Sets variables for card value and suit. Replacing 1 with 14 for easier calculations.
            card_suit = card[:1]
            card_value = card[1:]
            card_value = int(card_value)

            if card_value == 1:
                card_value = 14

            # Adds card value to clean_data list.
            clean_data.append(card_value)

            # Adds card suit to same_suit as key with a list of the values that have that suit.
            if card_suit not in same_suit:
                same_suit[card_suit] = [card_value]
            elif card_suit in same_suit:
                same_suit[card_suit].append(card_value)

            # Adds card value to same_value as key with value 1 if doesn't exist and iterates value if already present.
            if card_value not in same_value:
                same_value[card_value] = 1
            elif card_value in same_value:
                same_value[card_value] += 1

        # Sorts clean_data for easier calculations later.
        clean_data.sort(reverse=True)

        # Sorts same_suit for easier calculations later.
        for suit in same_suit:
            same_suit[suit] = sorted(same_suit[suit])

        return same_suit, same_value, clean_data

    def straight(self, clean_data: list) -> tuple:
        """Determines if the hand qualifies as a straight.

        Args:
            clean_data (list): List of all the card values in the hand.

        Returns:
            tuple: If hand qualifies as a straight the highest value in the straight is added to this tuple.
        """
        straight = []

        value_list = sorted(list(set(clean_data)))

        for index in range(len(value_list) - 4):
            if value_list[index] + 4 == value_list[index + 4]:
                straight.append(value_list[index + 4])

        straight = tuple(sorted(straight, reverse=True)[:1])

        return straight

    def repeated_values(self, same_value: dict) -> tuple[list, list, list]:
        """Determines if there are 2, 3 or 4 occurrences of a value.

        Args:
            same_value (dict): A dict with the card value as the key and the number of occurrences as the value.

        Returns:
            tuple[list, list, list]: First list has bool of if there are pairs in the hand and what those values are.
            Second list includes bool of if there are three of the same value and what those values are.
            Third list includes bool of if there are four occurrences and what that value is.
        """
        pair = [False, []]
        three = [False, []]
        four = [False]

        for key in same_value:
            # If there are two occurrences modify pair.
            if same_value[key] == 2:
                pair[0] = True
                pair[1].append(key)
            # If there are three occurrences modify three.
            elif same_value[key] == 3:
                three[0] = True
                three[1].append(key)
            # If there are four occurrences modify four.
            elif same_value[key] == 4:
                four[0] = True
                four.append(key)

        return pair, three, four

    def score_data(
        self,
        royal_flush: bool,
        straight_flush: tuple[int],
        flush: tuple[int],
        straight: tuple[int],
        pair: list,
        three: list,
        four: list,
        clean_data: list,
    ):
        """Calculates the score of the hand and collects tie data for tie-breaking scenarios.

        Args:
            royal_flush (bool): Bool showing if the hand is a royal flush.
            straight_flush (tuple[int]): Tuple of highest value in the cards that is used for a straight flush.
            flush (tuple[int]): Tuple of the highest five card values that make a flush.
            straight (tuple[int]): If hand qualifies as a straight the highest value in the straight is added to this tuple.
            pair (list): List has bool of if there are pairs in the hand and what those values are.
            three (list): List includes bool of if there are three of the same value and what those values are.
            four (list): List includes bool of if there are four occurrences and what that value is.
            clean_data (list): List of all the card values in the hand.
        """
        self.tie_data = []

        # Checks to see the score of the particular hand and adds information respectively to tie_data in the event of a tie.
        if royal_flush:
            self.score = 0
            self.tie_data.append(1)
        elif len(straight_flush) > 0:
            self.score = 1
            self.tie_data.append(straight_flush[0])
        elif four[0]:
            self.score = 2
            self.tie_data.append(four[1])
            iterator = 0
            clean_data.sort(reverse=True)
            for value in clean_data:
                if iterator == 1:
                    break
                if value != four[1]:
                    self.tie_data.append(value)
                    iterator += 1
            assert iterator == 1
            assert len(self.tie_data) == 2
        elif three[0] and pair[0]:
            self.score = 3
            pair[-1].sort(reverse=True)
            three[1].sort(reverse=True)
            self.tie_data.append(three[1][0])
            self.tie_data.append(pair[-1][0])
            assert len(self.tie_data) == 2
        elif len(three[1]) == 2:
            self.score = 3
            three[1].sort(reverse=True)
            self.tie_data.append(three[1][0])
            self.tie_data.append(three[1][1])
            assert len(self.tie_data) == 2
        elif len(flush) > 0:
            self.score = 4
            self.tie_data = sorted(flush[:5], reverse=True)
            assert len(self.tie_data) == 5
        elif len(straight) > 0:
            self.score = 5
            self.tie_data.append(straight[0])
            assert len(self.tie_data) == 1
        elif three[0]:
            self.score = 6
            three[1].sort(reverse=True)
            self.tie_data.append(three[1][0])
            iterator = 0
            clean_data.sort(reverse=True)
            for value in clean_data:
                if iterator == 2:
                    break
                if value != three[1][0]:
                    self.tie_data.append(value)
                    iterator += 1
            assert iterator == 2
            assert len(self.tie_data) == 3
        elif len(pair[-1]) >= 2:
            self.score = 7
            pair_lst = sorted(pair[-1], reverse=True)[:2]
            self.tie_data = pair_lst
            assert len(self.tie_data) == 2
            iterator = 0
            for value in sorted(clean_data, reverse=True):
                if iterator == 1:
                    break
                if value not in pair_lst:
                    self.tie_data.append(value)
                    iterator += 1
            assert iterator == 1
            assert len(self.tie_data) == 3
        elif pair[0]:
            self.score = 8
            self.tie_data.append(pair[-1][0])
            iterator = 0
            clean_data.sort(reverse=True)
            for value in clean_data:
                if iterator == 3:
                    break
                if value != pair[-1][0]:
                    self.tie_data.append(value)
                    iterator += 1
            assert iterator == 3
            assert len(self.tie_data) == 4
        else:
            self.score = 9
            clean_data.sort(reverse=True)
            self.tie_data = clean_data[:5]

    def prob(self, n_players):
        wins = 0
        losses = 0
        tie = 0

        community = Player.community_cards
        hand = self.hand

        deck = CardDeck().deck
        for card in hand:
            deck.remove(card)

        self.calculate_score()

        for i in range(len(deck)):
            for z in range(1 + i, len(deck)):
                temp_player = Player("233")
                temp_player.hand = [deck[i], deck[z]] + community
                temp_player.calculate_score()
                winner = Game().get_winner([self, temp_player])
                if len(winner) == 1:
                    if winner[0] == self:
                        wins += 1
                    else:
                        losses += 1
                else:
                    tie += 1

        return (wins / (wins + losses + tie)) ** n_players


class Game:
    """Class that handles the processes of a game of poker."""

    def __init__(self) -> None:
        # self.probability = Probability()
        # self.run_gui()
        pass

    def run_gui(self, d=False):
        self.gui_link = GUI()
        self.gui_link.game_link = self  # type: ignore
        self.debug = d
        self.gui_link.set_frame("username")
        self.gui_link.root.mainloop()

    def user_mode(self):
        username = self.gui_link.username_final
        n_player = self.gui_link.n_players_final
        self.n_player = n_player
        self.players = []
        self.main_player = Player(username)
        self.players.append(self.main_player)

        for num in range(1, n_player + 1):
            player = Player(str(num))
            self.players.append(player)

        self.game_num = 1
        self.gui_link.username_frame.destroy()
        self.gui_link.set_frame("game")

        self.round1()

    def valid_decision(self, decision):
        self.gui_link.fold_button.pack_forget()
        self.gui_link.check_button.pack_forget()
        self.gui_link.bet_button.pack_forget()
        if decision == "b":
            self.gui_link.bet_label.pack()
            self.gui_link.bet_entry.pack()
            self.gui_link.bet_confirm_button.pack()
        elif decision[0] == "e":
            self.bet_amount = int(decision[1:])
            if self.bet_amount <= (
                self.main_player.get_balance() - self.main_player.get_bet_amount()
            ):
                self.decision = "b"
                self.gui_link.bet_message.set("Enter Bet Amount.")
                self.gui_link.bet_label.pack_forget()
                self.gui_link.bet_entry.pack_forget()
                self.gui_link.bet_confirm_button.pack_forget()
                if self.round == 2:
                    self.round_2()
                elif self.round == 3:
                    self.round_3()
                elif self.round == 4:
                    self.round_4()
            else:
                self.gui_link.bet_message.set(
                    "Bet Amount is Invalid. Enter Bet Amount."
                )
        elif decision == "c":
            self.decision = "c"
            if self.round == 2:
                self.round_2()
            elif self.round == 3:
                self.round_3()
            elif self.round == 4:
                self.round_4()
        elif decision == "f":
            self.decision = "f"
            if self.round == 2:
                self.round_2()
            elif self.round == 3:
                self.round_3()
            elif self.round == 4:
                self.round_4()

    def round1(self):
        self.deck = CardDeck()
        for player in self.players:
            player.start_game(self.deck.pull_card(), self.deck.pull_card())

        self.gui_link.set_card_user(1, self.main_player.get_personal_cards()[0])
        self.gui_link.set_card_user(2, self.main_player.get_personal_cards()[1])

        # self.gui_link.card1.set(self.main_player.get_personal_cards()[0])
        # self.gui_link.card2.set(self.main_player.get_personal_cards()[1])

        self.round = 2

    def round_2(self):
        self.cont_players = self.players[:]
        if self.decision == "f":
            self.cont_players.remove(self.main_player)
        elif self.decision == "b":
            self.main_player.set_bet_amount(self.bet_amount)

        Player.set_community_cards(
            (self.deck.pull_card(), self.deck.pull_card(), self.deck.pull_card())
        )

        self.gui_link.set_card_user(3, Player.get_community_cards()[0])
        self.gui_link.set_card_user(4, Player.get_community_cards()[1])
        self.gui_link.set_card_user(5, Player.get_community_cards()[2])
        # self.gui_link.c_card1.set(Player.get_community_cards()[0])
        # self.gui_link.c_card2.set(Player.get_community_cards()[1])
        # self.gui_link.c_card3.set(Player.get_community_cards()[2])

        for player in self.cont_players[:]:
            player.set_hand(tuple(Player.get_community_cards()))
            player.calculate_score()
            prob = player.prob(len(self.players))
            if (prob > 0.025) and (player != self.main_player):
                bet_amount = round(prob * 0.5 * player.get_balance())
                if ((player.get_balance() - player.get_bet_amount()) - bet_amount) < 0:
                    bet_amount = player.get_balance() - player.get_bet_amount()

                player.set_bet_amount(bet_amount)
                if self.debug:
                    self.gui_link.bot_text[player.get_name()][0].set(
                        f"Player {player.get_name()}| ${player.get_balance() - player.get_bet_amount()} | Bet ${bet_amount} | Win% {prob * 100:.2f}%"
                    )
                else:
                    self.gui_link.bot_text[player.get_name()][0].set(
                        f"Player {player.get_name()}| ${player.get_balance() - player.get_bet_amount()} | Bet ${bet_amount}"
                    )
            elif player != self.main_player:
                self.cont_players.remove(player)
                self.gui_link.bot_text[player.get_name()][0].set(
                    f"Player {player.get_name()}| Folds"
                )
        self.round = 3

        if self.main_player in self.cont_players:
            self.gui_link.fold_button.pack()
            self.gui_link.check_button.pack()
            self.gui_link.bet_button.pack()
        else:
            self.round_3()

    def round_3(self):
        if self.main_player in self.cont_players:
            if self.decision == "f":
                self.cont_players.remove(self.main_player)
            elif self.decision == "b":
                self.main_player.set_bet_amount(self.bet_amount)

        Player.set_community_cards((self.deck.pull_card(), self.deck.pull_card()))
        self.gui_link.set_card_user(6, Player.get_community_cards()[3])
        self.gui_link.set_card_user(7, Player.get_community_cards()[4])
        # self.gui_link.c_card4.set(Player.get_community_cards()[3])
        # self.gui_link.c_card5.set(Player.get_community_cards()[4])

        for player in self.cont_players:
            player.set_hand(
                (Player.get_community_cards()[3], Player.get_community_cards()[4])
            )
            player.calculate_score()
            if player != self.main_player:
                prob = player.prob(len(self.cont_players))

                bet_amount = round(prob * 0.25 * player.get_balance())
                if ((player.get_balance() - player.get_bet_amount()) - bet_amount) < 0:
                    bet_amount = player.get_balance() - player.get_bet_amount()

                player.set_bet_amount(player.get_bet_amount() + bet_amount)

                if self.debug:
                    self.gui_link.bot_text[player.get_name()][0].set(
                        f"Player {player.get_name()}| ${player.get_balance() - player.get_bet_amount()} | Bet ${bet_amount} | Win% {prob * 100:.2f}%"
                    )
                else:
                    self.gui_link.bot_text[player.get_name()][0].set(
                        f"Player {player.get_name()}| ${player.get_balance() - player.get_bet_amount()} | Bet ${bet_amount}"
                    )

        self.round = 4

        if self.main_player in self.cont_players:
            self.gui_link.fold_button.pack()
            self.gui_link.check_button.pack()
            self.gui_link.bet_button.pack()
        else:
            self.round_4()

    def round_4(self):
        if self.main_player in self.cont_players:
            if self.decision == "f":
                self.cont_players.remove(self.main_player)
            elif self.decision == "b":
                self.cont_players.append(self.main_player)
                self.main_player.set_bet_amount(self.bet_amount)

        self.gui_link.fold_button.pack()
        self.gui_link.check_button.pack()
        self.gui_link.bet_button.pack()

        winner = self.get_winner(self.cont_players)

        total_bet = 0
        for player in self.players:
            total_bet += player.get_bet_amount()
            player.set_balance(-(player.get_bet_amount()))
            player.set_bet_amount(0)

        for player in self.players:
            if player != self.main_player:
                self.gui_link.bot_text[player.get_name()][
                    1
                ] = f"Player {player.get_name()} | ${player.get_balance()} | Cards {player.personal_cards[0]}, {player.personal_cards[1]}"

        self.gui_link.set_frame("stats")

        winning_names = ""
        for winning_player in winner:
            winning_player.set_balance(total_bet / len(winner))
            winning_names = winning_names + winning_player.get_name() + " "

        self.gui_link.winner_message.set(f"Winner: {winning_names}")

        self.gui_link.player_message.set(
            f"{self.main_player.get_name()} | ${self.main_player.get_balance()}"
        )

        for player in self.players:
            if player.get_balance() == 0:
                if player != self.main_player:
                    self.gui_link.bot_text[str(player.get_name())][0].set(
                        f"Player {player.get_name()} | $0 | Left Game"
                    )
                self.players.remove(player)
            elif player != self.main_player:
                self.gui_link.bot_text[str(player.get_name())][0].set(
                    f"Player {player.get_name()}| ${player.get_balance()} | Check"
                )

        if (self.main_player in self.players) and (len(self.players) > 1):
            self.gui_link.new_game_button.pack()
        self.gui_link.quit_button.pack()

    def new_game(self):
        self.game_num += 1
        self.gui_link.end_frame.destroy()
        # self.gui_link.end_stats_frame.destroy()
        self.gui_link.community_frame.grid(column=0, row=0)
        self.gui_link.user_frame.grid(column=0, row=1)
        self.gui_link.stats_frame.grid(column=1, row=0)
        self.gui_link.action_frame.grid(column=1, row=1)

        Player.community_cards = []

        # self.gui_link.c_card1.set("")
        # self.gui_link.c_card2.set("")
        # self.gui_link.c_card3.set("")
        # self.gui_link.c_card4.set("")
        # self.gui_link.c_card5.set("")
        self.gui_link.set_card_user(3, "empty")
        self.gui_link.set_card_user(4, "empty")
        self.gui_link.set_card_user(5, "empty")
        self.gui_link.set_card_user(6, "empty")
        self.gui_link.set_card_user(7, "empty")

        self.gui_link.set_card_user(1, "empty")
        self.gui_link.set_card_user(2, "empty")

        # self.gui_link.card1.set("")
        # self.gui_link.card2.set("")

        self.round1()

    def get_winner(self, player_data: list) -> list:
        """Determines the winner of a game based on player scores and tie data.

        Args:
            player_data (list): List of Player instances for a game of poker.

        Returns:
            list: List of Player instances that represent the winner(s) of a game of poker.
        """
        # Loops through players and checks to see which player has the lowest score.
        min_score = 11
        winner = []
        for player in player_data:
            if player.get_score() < min_score:
                winner = [player]
                min_score = player.get_score()
            elif player.get_score() == min_score:
                winner.append(player)

        # If there are multiple players with the lowest score, the tie_breaker method is called.
        if len(winner) > 1:
            return self.tie_breaker(winner)
        else:
            return winner

    def tie_breaker(self, tied_players: list) -> list:
        """Determines the winner of a game of poker given tie_data for each player.

        Args:
            tied_players (list): List of Player instances with the same score.

        Returns:
            list: List of Player instance(s) that won the tie.
        """
        # Loops through tie_data for the given players and determines who has a higher value.
        winner = []
        for index in range(len(tied_players[0].get_tie_data())):
            max_value = 0
            winner = []
            for player in tied_players:
                if player.get_tie_data()[index] > max_value:
                    max_value = player.get_tie_data()[index]
                    winner = [player]
                elif player.get_tie_data()[index] == max_value:
                    winner.append(player)
            # If after checking an index of tie_data a winner is determined it is then returned. Else the next index is checked.
            if len(winner) == 1:
                return winner
            else:
                tied_players = winner[:]

        return winner


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", required=False)
    args = parser.parse_args()
    if args.debug:
        Game().run_gui(True)
    else:
        Game().run_gui()
