import requests
import ast
import datetime
import time
import csv

my_currency = 'PLN'
my_url = f'https://api.exchangeratesapi.io/latest?symbols={my_currency}'
timeout = 0.99


def my_decorator(fn):
    def wrapper():
        list_of_results = [['Kurs/Błąd pozyskania', 'Data i godzina', 'Czas wykonania']]
        while True:
            now = datetime.datetime.now()
            date_time_now = now.strftime("%d/%m/%Y, %H:%M:%S")
            try:
                start_of_execution = datetime.datetime.now()
                get_currency = fn()
                end_of_execution = datetime.datetime.now()
                execution_time = start_of_execution - end_of_execution

                get_currency_txt = get_currency.text
                currency_as_dictionary = ast.literal_eval(get_currency_txt)

                print("Kurs Euro: ",
                      currency_as_dictionary['rates']['PLN'])
                print("Data i godzina: ", date_time_now)
                print(f"Czas wykonania zapytania: {execution_time.microseconds} μs")
                row_a = [currency_as_dictionary['rates']['PLN'], date_time_now, execution_time.microseconds]
                list_of_results.append(row_a)
            except requests.Timeout:
                print('Błąd pozyskania danych')
                print("Data i godzina: ", date_time_now)
                print(f"Czas wykonania zapytania: {int(timeout * 1000000)} μs")
                row_b = ['Błąd pozyskania danych', date_time_now, timeout]
                list_of_results.append(row_b)
            print('\n=====================================\n')

            time.sleep(1)

            with open('list_of_results.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(list_of_results)

    return wrapper()


@my_decorator
def get_currency_function():
    return requests.get(my_url, timeout=timeout)