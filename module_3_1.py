calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [string.upper() for string in list_to_search]

print(string_info("Pycharm"))
print(string_info("milk"))
print(string_info("yellow"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'kyclic'])) # No matches
print(is_contains('mouse', ['cat', 'dog', 'moUse']))
print(calls)


