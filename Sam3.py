from datetime import datetime as dt
from time import sleep

for i in range(5):
    print(dt.now())
    if i!=4: sleep(1)