import requests
import datetime
import time
from selenium.common.exceptions import TimeoutException

r = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/eur/')
now = datetime.datetime.now()
timer = time.time()

with open("file.csv", "w", newline='') as file:


    for i in range(3):

        print(i)
        time.sleep(15)

        try:
            now = datetime.datetime.now()
            print(r.text)
            print('Data i godzina: ', now.strftime(" %d.%m.%Y %H:%M:%S"))
            print('Czas wykonania zapytania: ', (str(now.second)) + ' sec')


        except TimeoutException:
            print('There is timeout')

        i += 1

        file.write(r.text)
        file.write('\n')