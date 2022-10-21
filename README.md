# ICS33 Project - Texas Hold'em
#### An extended version of Programming Assignment 3 that adds a GUI for the user to interact with, along with smarter bots that bet based on their current probability of winning.

<br>

## Description
---
#### This project adds two main features to PA3, a GUI for easier user interactions, and smarter bots that bet based on their probability of winning. The GUI was built with tkinter and pillow to display pictures of the cards for easier gameplay. 

### Smart Bots

#### The smarter bots were implemented by creating a new method that determines the probability of the current bots hands winning against all the other possible hands. The algorithm is more of a brute force approach to the solution by simulating every other possible hand given the community cards and determines the number of those hands the current bots hand would beat and lose to. These numbers then give us the probability of the bot winning. We take this probability raise it to the factor of the number of players in the current game. This gives us a accurate probability of the current bot winning given the number of players and the hand of the bot.

### Smart Bot Behavior

#### The behavior is extremely customizable as all of the decisions are based on the probability of the bot winning. Currently the bot will fold if it has not bet any money into the game and if it has a less than 2.5% chance of winning the game. In the first round all bots check. In the second round the bot will bet (0.5 * player_balance * probability_of_winning). This number will be rounded. In the third round the bot will bet (0.25 * player_balance * probability_of_winning).


<br>

## Dependencies
---
1. #### Python 3 (Tested on 3.10.5)
2. #### Python Standard Library (argparse, random, tkinter)
3. #### Python pillow library

<br>

## Installation
---
1. #### Download and unzip the file.
2. #### Install python and python standard library.
3. #### Install python pillow library (`pip3 install pillow`)

<br>

## Usage
---
#### Simply run the main Project_Eric_Minassian.py file after you have unzipped the folder.
`python Project_Eric_Minassian.py`

#### **If you would like to see the probability of winning for each bot and how they bet accordingly, run the program with the --debug flag.**
`python Project_Eric_Minassian.py --debug`



