star,equal = '*'*48,'='*48
product = {'Books  ': 49.95,'Computer': 579.99,'Monitor':124.89}
total = 0
print('',star,'\n'
    "\t\tCoding Temple, Inc.\n\t\t283 Franklin St.\n\t\tBoston, MA\n",equal,'\n\tProduct Name\tProduct Price')
for name,price in product.items():
    print('\t',name,'\t$',price)
    total = total + price

print('',equal,'\n\t\t\tTotal\n\t\t\t$',total,'\n',equal,'\n\n\tThanks for shopping with us today!\n\n',star)

def reverse(var):
    return var[::-1]
