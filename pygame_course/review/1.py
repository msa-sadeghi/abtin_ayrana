# s = "These words are separated by spaces"
# print(s.split(" "))
# s = "These,words,are,separated,by,spaces"
# print(s.split(","))
# products = ["laptop", "pc", "tablet"]
# prices = [3000, 2600, 1000]
# print("*" * 50)
# print("\t\tMy company")
# print("\t\tAddress:Tehran")
# print( "=" * 50 )
# print("\tProduct Name\tProduct Price")
# print(f"\t{products[0]}\t\t{prices[0]}")
# print(f"\t{products[1]}\t\t{prices[1]}")
# print(f"\t{products[2]}\t\t{prices[2]}")
# print('=' * 50)
# print('\t\t\tTotal')
# print(f'\t\t\t{sum(prices)}')
# print( "=" * 50)
# print('\t\tThanks for shopping!!')
# print( "*" * 50)

# name = input("What is your name? ")
# print(f'Hello {name}')
# print('Hello', name)
# print('Hello {}'.format(name))

# x = int('5')
# print(type(x))

# x = False
# print(int(x))

try:
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
except:
    print("you must enter number")
    x = 0
    y = 0

print(x + y)