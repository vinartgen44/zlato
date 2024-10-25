def total_price(price: list):
    total = sum(price)
    return "{:.2f}".format(total)

def tax_price(price):
    return "{:.2f}".format((price * 20) / 120)

def price_free_tax(price):
    t = float(price) - float(tax_price(price))
    return "{:.2f}".format(t)


if __name__ == '__main__':
    print(total_price([100, 200, 300.5]))