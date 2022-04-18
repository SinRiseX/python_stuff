import requests
import random
import threading

codes = input("How many randoms kahoot codes do you want to check?: ")
speed = input("How many many rows per code generating?: ")
active_codes = []
total_codes = (int(codes)//int(speed))

def do_requests():
 for _ in range(int(total_codes)):
  code = random.randint(1000000,9999999)
  response = requests.get(f"https://kahoot.it/reserve/session/7096037/?164833284718").text
  print(F"{code}.{response}")
  if response != str("Not found"):
      active_codes.append(code)

threads = []

for i in range(int(speed)):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)
for i in range(int(speed)):
    threads[i].start()
for i in range(int(speed)):
    threads[i].join()

active_list = len(active_codes)
if active_list != 0:
 print(f"{active_list} codes are active!")
 print(active_codes)
elif active_list == 0:
    print(f"{active_list} codes are active!")