import tkinter as tk

from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        self.game_link = None
        self.create_canvas()

    def create_canvas(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.title("Texas Hold'em")
        self.root.grid_columnconfigure(0, weight=4)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=2)

    def set_frame(self, frame):
        if frame == "username":
            self.create_username_frame()
            self.username_frame.pack()
        elif frame == "game":
            self.create_community_frame()
            self.create_user_frame()
            self.create_stats_frame()
            self.create_action_frame()
            self.community_frame.grid(column=0, row=0)
            self.user_frame.grid(column=0, row=1)
            self.stats_frame.grid(column=1, row=0)
            self.action_frame.grid(column=1, row=1)
        elif frame == "stats":
            self.create_end_frame()
            self.community_frame.grid_forget()
            self.user_frame.grid_forget()
            self.stats_frame.grid_forget()
            self.action_frame.grid_forget()

            self.end_frame.pack()

            # self.create_end_stats_frame()
            # self.end_stats_frame.pack()

    def check_user_input(self):
        username = self.username.get()
        n_players = self.n_players.get()
        if len(username) > 12:
            self.username_message.set("Max username length is 12. Enter Username.")
        elif len(username) == 0:
            self.username_message.set("Username can't be empty. Enter Username.")
        else:
            try:
                n_players = int(n_players)
                assert 0 < n_players < 23
                self.n_players_final = n_players
                self.username_final = username
                self.game_link.user_mode()
            except ValueError:
                self.n_players_message.set("Not a valid integer. Enter Number of Bots.")
            except AssertionError:
                self.n_players_message.set("Not in range 1-22. Enter Number of Bots.")

    def create_username_frame(self):
        self.username_frame = tk.Frame(self.root)

        self.username = tk.StringVar()
        self.n_players = tk.IntVar(value=1)
        self.username_message = tk.StringVar(value="Enter Username")
        self.n_players_message = tk.StringVar(
            value="Enter Number of Bots to Play Against."
        )

        username_label = tk.Label(
            self.username_frame, textvariable=self.username_message
        )
        username_label.pack()

        username_entry = tk.Entry(self.username_frame, textvariable=self.username)
        username_entry.pack()

        n_players_label = tk.Label(
            self.username_frame, textvariable=self.n_players_message
        )
        n_players_label.pack()

        n_players_entry = tk.Spinbox(
            self.username_frame, from_=1, to=22, textvariable=self.n_players
        )
        n_players_entry.pack()

        submit_button = tk.Button(
            self.username_frame,
            text="Continue",
            command=self.check_user_input,
        )
        submit_button.pack()

        quit_button = tk.Button(
            self.username_frame, text="Quit", command=self.root.destroy
        )
        quit_button.pack()

    def set_card_user(self, num, card):
        if num == 1:
            self.card1_label.destroy()
            self.card1_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.card1_label = tk.Label(self.user_frame, image=self.card1_img)
            self.card1_label.pack(side=tk.LEFT)
        elif num == 2:
            self.card2_label.destroy()
            self.card2_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.card2_label = tk.Label(self.user_frame, image=self.card2_img)
            self.card2_label.pack(side=tk.LEFT)
        elif num == 3:
            self.c_card1_label.destroy()
            self.c_card1_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.c_card1_label = tk.Label(self.community_frame, image=self.c_card1_img)
            self.c_card1_label.pack(side=tk.LEFT)
        elif num == 4:
            self.c_card2_label.destroy()
            self.c_card2_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.c_card2_label = tk.Label(self.community_frame, image=self.c_card2_img)
            self.c_card2_label.pack(side=tk.LEFT)
        elif num == 5:
            self.c_card3_label.destroy()
            self.c_card3_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.c_card3_label = tk.Label(self.community_frame, image=self.c_card3_img)
            self.c_card3_label.pack(side=tk.LEFT)
        elif num == 6:
            self.c_card4_label.destroy()
            self.c_card4_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.c_card4_label = tk.Label(self.community_frame, image=self.c_card4_img)
            self.c_card4_label.pack(side=tk.LEFT)
        elif num == 7:
            self.c_card5_label.destroy()
            self.c_card5_img = ImageTk.PhotoImage(
                Image.open(".//images//" + card + ".png").resize((100, 145))
            )
            self.c_card5_label = tk.Label(self.community_frame, image=self.c_card5_img)
            self.c_card5_label.pack(side=tk.LEFT)

    def create_user_frame(self):
        self.user_frame = tk.Frame(self.root)

        # self.card1 = tk.StringVar()
        # self.card2 = tk.StringVar()

        self.card1_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )

        self.card2_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )

        self.card1_label = tk.Label(self.user_frame, image=self.card1_img)
        self.card1_label.pack(side=tk.LEFT)
        self.card2_label = tk.Label(self.user_frame, image=self.card2_img)
        self.card2_label.pack(side=tk.LEFT)
        # tk.Label(self.user_frame, textvariable=self.card1).pack(side=tk.RIGHT)
        # tk.Label(self.user_frame, textvariable=self.card2).pack(side=tk.RIGHT)

    def create_community_frame(self):
        self.community_frame = tk.Frame(self.root)

        # self.c_card1 = tk.StringVar()
        # self.c_card2 = tk.StringVar()
        # self.c_card3 = tk.StringVar()
        # self.c_card4 = tk.StringVar()
        # self.c_card5 = tk.StringVar()

        self.c_card1_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )
        self.c_card2_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )
        self.c_card3_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )
        self.c_card4_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )
        self.c_card5_img = ImageTk.PhotoImage(
            Image.open(".//images//empty.png").resize((100, 145))
        )

        self.c_card1_label = tk.Label(self.community_frame, image=self.c_card1_img)
        self.c_card1_label.pack(side=tk.LEFT)
        self.c_card2_label = tk.Label(self.community_frame, image=self.c_card2_img)
        self.c_card2_label.pack(side=tk.LEFT)
        self.c_card3_label = tk.Label(self.community_frame, image=self.c_card3_img)
        self.c_card3_label.pack(side=tk.LEFT)
        self.c_card4_label = tk.Label(self.community_frame, image=self.c_card4_img)
        self.c_card4_label.pack(side=tk.LEFT)
        self.c_card5_label = tk.Label(self.community_frame, image=self.c_card5_img)
        self.c_card5_label.pack(side=tk.LEFT)

        # self.c_card1_label = tk.Label(self.community_frame, textvariable=self.c_card1)
        # self.c_card2_label = tk.Label(self.community_frame, textvariable=self.c_card2)
        # self.c_card2_label.pack()
        # self.c_card3_label = tk.Label(self.community_frame, textvariable=self.c_card3)
        # self.c_card3_label.pack()
        # self.c_card4_label = tk.Label(self.community_frame, textvariable=self.c_card4)
        # self.c_card4_label.pack()
        # self.c_card5_label = tk.Label(self.community_frame, textvariable=self.c_card5)
        # self.c_card5_label.pack()

    def create_stats_frame(self):
        self.stats_frame = tk.Frame(self.root)

        tk.Label(self.stats_frame, text="Username | Balance | Action").pack()

        self.bot_text = {}

        for i in range(1, self.n_players_final + 1):
            self.bot_text[str(i)] = [tk.StringVar(value=f"Player {i} | $10 | Check")]
            self.bot_text[str(i)].append("")
            # self.bot_text[str(i)].append(
            #     tk.Label(self.stats_frame, textvariable=self.bot_text[str(i)][0]).pack()
            # )
            # self.bot_text[str(i)][-1].pack()
            tk.Label(self.stats_frame, textvariable=self.bot_text[str(i)][0]).pack()

    def create_action_frame(self):
        self.action_frame = tk.Frame(self.root)

        self.bet_message = tk.StringVar(value="Enter Bet Amount")
        self.bet_amount = tk.IntVar()

        tk.Label(self.action_frame, text="Select Your Action:").pack()

        self.fold_button = tk.Button(
            self.action_frame,
            text="Fold",
            command=lambda: self.game_link.valid_decision("f"),
        )
        self.fold_button.pack()

        self.check_button = tk.Button(
            self.action_frame,
            text="Check",
            command=lambda: self.game_link.valid_decision("c"),
        )
        self.check_button.pack()

        self.bet_button = tk.Button(
            self.action_frame,
            text="Bet",
            command=lambda: self.game_link.valid_decision("b"),
        )
        self.bet_button.pack()

        self.bet_label = tk.Label(self.action_frame, textvariable=self.bet_message)

        self.bet_entry = tk.Spinbox(self.action_frame, textvariable=self.bet_amount)

        self.bet_confirm_button = tk.Button(
            self.action_frame,
            text="Confirm Bet",
            command=lambda: self.game_link.valid_decision(
                "e" + str(self.bet_amount.get())
            ),
        )

    def create_end_frame(self):
        self.end_frame = tk.Frame(self.root)

        self.winner_message = tk.StringVar()
        self.player_message = tk.StringVar()

        self.winner_label = tk.Label(self.end_frame, textvariable=self.winner_message)
        self.winner_label.pack()

        self.player_label = tk.Label(self.end_frame, textvariable=self.player_message)
        self.player_label.pack()

        for key in self.bot_text:
            tk.Label(self.end_frame, text=self.bot_text[key][1]).pack()

        self.new_game_button = tk.Button(
            self.end_frame, text="New Game", command=self.game_link.new_game
        )

        self.quit_button = tk.Button(
            self.end_frame, text="Quit", command=self.root.destroy
        )

    # def create_end_stats_frame(self):
    #     self.end_stats_frame = tk.Frame(self.root)

    #     for key in self.bot_text:
    #         tk.Label(self.end_stats_frame, text=self.bot_text[key][1]).pack()


if __name__ == "__main__":
    pass
