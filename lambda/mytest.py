"""Checking Lamba inbuilt function"""
MYDISC = {
    'cruise': lambda price: price - 5,
    'flight': lambda price: price - 10,
    'train': lambda price: price - 1
    }

print(__doc__,"\n")
print(MYDISC['cruise'](100))
print(MYDISC['flight'](100))

print("\nInserting key:value in Applydict...\n")
MYDISC['rocket'] = lambda price: price ** 2
print(MYDISC['rocket'](100))
