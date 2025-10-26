

import sys, os, random
import datetime


def init():
    print ("Select a file to play with:")
    available_files = [f for f in os.listdir("data") if not f.startswith(".")]
    for n, f in enumerate(available_files):
        print(" * [{}] {}".format(n, f))
    data_file = None
    while data_file is None:
        try:
            data_file = int(input(">> "))
            if data_file >= len(available_files):

                raise Exception("OutOfRange")
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print("Error selecting file ({})".format(e))
            print("Please introduce a number from 0-{}".format(len(available_files)-1))
            data_file = None
    
    file_path = "data/"+ available_files[data_file]

    op_list = {}
    with open(file_path, "r") as f:
        for n, l in enumerate([line for line in f.readlines() if line not in ["","\n"]]):
            l = l.replace("\n", "")
            if ";" in l:
                v, h = l.split(";")
            else:
                v, h = l, "no hint"

            op_list[n] = {"value":v, "hint":h}

    n_players = None
    while n_players is None:
        try:
            n_players = int(input("Number of players;\n>> "))
            if n_players <= 2:
                raise Exception("NotEnoughPlayers")
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print("Error with number of players ({})".format(e))
            n_players = None


    print("\n\nGame ready!")
    print("Number of words:", len(op_list.keys()))
    print("Number of players:", n_players)
    start = False
    while not start:
        i = input("\nPress Enter to start")
        print(i)
        start = i == ""


    play(op_list, n_players)

def clear():
    os.system('clear||cls||echo -e "\033c"')


def play(words, n_p):
    if len(words) == 0:
        print("No words left on this list")
        print("Restart the game or chhose anothwr list")
        exit()
    random.seed(repr(datetime.datetime.now()))
    i_p = random.randrange(n_p)
    word_n = random.randrange(len(words))
    word_dict = words[word_n]
    word = word_dict["value"]
    hint = word_dict["hint"]
    words.pop(word_n)

    for p in range(n_p):
        clear()
        print("\n\n\nplayer:", p+1)
        while True:
            if input("\n\n\nPress Enter to reveal role and word") == "":
                break
            

        if p==i_p:
            print("\n * You ARE the IMPOSTOR!!!\n")
            print(" * The hint is:", hint)
        else:
            print("\n * You are NOT the impostor!\n")
            print(" * The word is:", word)
    
        while True:
            if input("\nPress Enter to before passing on to the next player") == "":
                break
        clear()
    print("\n\n\n * Type 'reveal' to show reveal the whi was the impostor")
    print(" * Type 'play' to play again")
    print(" * Remaining words:", len(words.keys()))
    while True:
        i = input(">>> ")
        if i == "reveal":
            print("The IMPOSTOR was player {}!".format(i_p+1))
        elif i == "play":
                  play(words, n_p)
    
        

    

    

    
    







if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        print("\n * Closing game")
        exit()
