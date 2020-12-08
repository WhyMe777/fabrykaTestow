import requests
#
# r = requests.get('https://fabrykatestow.pl')
#
# print(r)

# przykład 2

# post = requests.get('http://httpbin.org/post')
# put = requests.get('http://httpbin.org/put')
# delete = requests.get('http://httpbin.org/delete')
#
# print(delete)


# przykład 3 - zwraca w konsoli url strony z parametrami
# text - zwraca zawartość tekstu na danej stronie

parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)
print(r.url)
print(r.text)
print(r.encoding)