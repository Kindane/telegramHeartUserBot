from time import sleep
white = "🤍" # white heart emoji
red = "❤️" # red heart emoji
yellow = "💛" # yellow heart emoji

#white = "-" # white heart emoji
#red = "|" # red heart emoji
#yellow = "*" # yellow heart emoji

def arr2d2str(arr):
        result = ""
        for i in arr:
                for j in i:
                        result += j
                result += "\n"
        return result

_heart = [
        [white for i in range(11)],
        [white, white, white, red, white, white, white, red, white, white, white],
        [white, white, red, yellow, red, white, red, yellow, red, white, white],
        [white, red, yellow, yellow, red, yellow, red, yellow, yellow, red, white],
        [white, red, yellow, yellow, yellow, red, yellow, yellow, yellow, red, white],
        [white, red, yellow, yellow, yellow, yellow, yellow, yellow, yellow, red, white],
        [white, white, red, yellow, yellow, yellow, yellow, yellow, red, white, white],
        [white, white, white, red, yellow, yellow, yellow, red, white, white, white],
        [white, white, white, white, red, red, red, white, white, white, white],
        [white, white, white, white, white, red, white, white, white, white, white],
        [white for i in range(11)]
        ]

# debug
def show_heart():
    for i in _heart:
        for j in i:
            print(j, end="")
        print()

