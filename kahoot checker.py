import requests
import random

amount = input("How many random codes do you want to check?:")
working_codes = []

for x in range(int(amount)):
 code = random.randint(1000000,9999999)
 urls = requests.get(f"https://kahoot.it/reserve/session/{code}/?164833284718").text
 print(F"{code}.{urls}")
 amount_active = len(working_codes)
 if urls != str("Not found"):
     working_codes.append(code)

if amount_active != 0:
 print(f"{amount_active} codes are active!")
elif amount_active == 0:
    print(f"{amount_active} codes are active!")
if amount_active != 0:
 print(working_codes)
