applydisc = {
    'cruise': lambda price: price - 5,
    'flight': lambda price: price - 10,
    'train': lambda price: price - 1
    }

print(applydisc['cruise'](100))
print(applydisc['flight'](100))

applydisc['rocket'] = lambda price: price ** 2
print(applydisc)
print(applydisc['rocket'](100))
