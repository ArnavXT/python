import random
import enchant  # type: ignore
from termcolor import colored  # type: ignore

d = enchant.Dict("en_US")

words = ['apple', 'about', 'above', 'abide', 'adore', 'alarm', 'alien', 'alive', 'alone', 'amaze', 'angel', 'anger', 
         'angle', 'ankle', 'apply', 'arena', 'argue', 'arise', 'armor', 'aroma', 'arrow', 'aside', 'audio', 'avoid', 
         'award', 'aware', 'awake', 'basic', 'beach', 'beard', 'beast', 'begin', 'being', 'belly', 'bench', 'berry', 
         'birth', 'black', 'blade', 'blame', 'blank', 'blast', 'blend', 'bless', 'blind', 'block', 'blood', 'board', 
         'boast', 'boost', 'booty', 'brain', 'brave', 'bread', 'break', 'brick', 'bride', 'brief', 'bring', 'broad', 
         'brown', 'brush', 'buddy', 'build', 'burst', 'buyer', 'cabin', 'cable', 'camel', 'candy', 'carry', 'carve', 
         'catch', 'cause', 'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'charm', 'chart', 'chase', 'cheap', 
         'cheat', 'check', 'cheer', 'chest', 'chief', 'child', 'chill', 'china', 'chirp', 'choir', 'choke', 'chunk', 
         'civic', 'claim', 'class', 'clean', 'clear', 'clerk', 'click', 'climb', 'clock', 'close', 'cloud', 'coach', 
         'coast', 'count', 'court', 'cover', 'crack', 'craft', 'crash', 'crawl', 'crazy', 'cream', 'creek', 'creep', 
         'crime', 'cross', 'crowd', 'crown', 'curve', 'daily', 'dance', 'death', 'debut', 'delay', 'devil', 'diary', 
         'dirty', 'ditch', 'diver', 'dizzy', 'dozen', 'draft', 'drain', 'drama', 'drawn', 'dream', 'dress', 'drift', 
         'drill', 'drink', 'drive', 'drunk', 'dwarf', 'eager', 'earth', 'elbow', 'elite', 'empty', 'enjoy', 'enter', 
         'entry', 'equal', 'error', 'exact', 'extra', 'faith', 'false', 'fault', 'favor', 'feast', 'fiber', 'fifth', 
         'fifty', 'fight', 'final', 'finds', 'flame', 'flask', 'flesh', 'float', 'flood', 'floor', 'flour', 'focus', 
         'force', 'forth', 'found', 'frame', 'fresh', 'front', 'frost', 'fruit', 'giant', 'glass', 'glide', 'glory', 
         'grace', 'grand', 'grant', 'grape', 'grass', 'great', 'greed', 'grief', 'grind', 'group', 'guard', 'guess', 
         'guest', 'guide', 'habit', 'happy', 'harsh', 'heart', 'heavy', 'hello', 'honey', 'honor', 'horse', 'house', 
         'human', 'humor', 'ideal', 'image', 'index', 'inner', 'input', 'irony', 'issue', 'jelly', 'joint', 'judge', 
         'juice', 'kneel', 'knife', 'knock', 'known', 'label', 'labor', 'laugh', 'layer', 'lemon', 'level', 'light', 
         'limit', 'liver', 'local', 'loose', 'lucky', 'lunch', 'magic', 'major', 'maker', 'march', 'marry', 'match', 
         'maybe', 'meant', 'media', 'medal', 'merge', 'metal', 'minor', 'model', 'money', 'month', 'moral', 'motor', 
         'mount', 'mouse', 'mouth', 'movie', 'music', 'naked', 'nasty', 'never', 'newer', 'night', 'noise', 'north', 
         'novel', 'nurse', 'occur', 'ocean', 'offer', 'often', 'order', 'other', 'ought', 'outer', 'paint', 'panel', 
         'panic', 'paper', 'party', 'pause', 'peace', 'peach', 'pearl', 'pedal', 'petty', 'phone', 'photo', 'piece', 
         'pilot', 'place', 'plain', 'plant', 'plate', 'plaza', 'plead', 'point', 'pride', 'prime', 'print', 'prior', 
         'prize', 'proof', 'proud', 'pupil', 'queen', 'quest', 'quick', 'quiet', 'quite', 'radio', 'raise', 'rally', 
         'range', 'rapid', 'reach', 'react', 'ready', 'relax', 'reply', 'reset', 'right', 'risky', 'rival', 'robot', 
         'rocky', 'rough', 'round', 'route', 'royal', 'ruler', 'sandy', 'scale', 'scare', 'scene', 'scope', 'score', 
         'scout', 'serve', 'shady', 'shake', 'shape', 'share', 'sharp', 'sheer', 'shift', 'shine', 'shock', 'shore', 
         'short', 'sight', 'silly', 'skill', 'skull', 'sleep', 'slice', 'slide', 'smart', 'smile', 'snake', 'solid', 
         'solve', 'sound', 'space', 'spark', 'speak', 'spend', 'spice', 'spike', 'spine', 'spite', 'split', 'spoil', 
         'sport', 'staff', 'stage', 'stain', 'stand', 'stark', 'start', 'state', 'steal', 'steam', 'steel', 'steep', 
         'stiff', 'still', 'stock', 'stone', 'store', 'storm', 'story', 'strap', 'straw', 'strip', 'stuck', 'style', 
         'sugar', 'sunny', 'super', 'sweet', 'table', 'taste', 'teach', 'tease', 'teeth', 'thank', 'theft', 'their', 
         'theme', 'there', 'thick', 'thief', 'thing', 'think', 'third', 'those', 'throw', 'tight', 'title', 'toast', 
         'today', 'token', 'topic', 'total', 'touch', 'tough', 'tower', 'toxic', 'trace', 'track', 'trade', 'trail', 
         'train', 'treat', 'trend', 'trial', 'tribe', 'trick', 'troop', 'truck', 'truly', 'trust', 'truth', 'twice', 
         'uncle', 'under', 'union', 'upper', 'upset', 'urban', 'usual', 'vague', 'valid', 'value', 'video', 'virus', 
         'vivid', 'voice', 'voter', 'waste', 'watch', 'water', 'weary', 'weigh', 'weird', 'whale', 'wheat', 'wheel', 
         'where', 'which', 'while', 'white', 'whole', 'whose', 'woman', 'worry', 'worse', 'worst', 'worth', 'would', 
         'wound', 'write', 'wrong', 'young', 'youth', 'zebra', 'zero']

answer = random.choice(words)
key = list(answer)

print("Each guess must be a valid five-letter word. You get 6 chances.")
print("The color of a tile will change to show how close your guess was.")
print("If the tile turns " + colored("green", "green") + " the letter is in the word and in the correct spot.")
print("If the tile turns " + colored("yellow", "yellow") + " the letter is in the word but in the wrong spot.")
print("If the tile is blank, the letter is not in the word.\n")

for attempt in range(6):
    guess = input(f"Attempt {attempt + 1}/6 - Enter your guess (5-letter word): ").lower()

    while len(guess) != 5 or not d.check(guess):
        guess = input("Invalid input! Please enter a valid 5-letter word: ").lower()

    output = ""

    for j in range(5):
        if guess[j] == key[j]:
            output += colored(guess[j], 'green')
        elif guess[j] in key:
            output += colored(guess[j], 'yellow')
        else:
            output += "_"

    print(output)

    if guess == answer:
        print(colored(f"Congratulations! You've guessed the word: {answer}", 'green'))
        break
else:
    print(colored(f"Game over! The correct word was: {answer}", 'red'))

w = input("Thanks for playing!")

