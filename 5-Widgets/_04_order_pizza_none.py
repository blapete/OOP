def orderPizza(size, style='regular', topping=None):
    PRICE_OF_TOPPING = 1.50 

    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.00
    else:
        price = 18.00 # large

    if style == 'deepdish':
        price = price + 2.00

    line = 'You have ordered a ' + size + ' ' + style + ' pizza with '
    if topping is None: 
        print(line +'no topping')
    else:
        print(line + topping)
        price = price + PRICE_OF_TOPPING

    print('The price is $', price)
    print()
    
  
orderPizza('large')                                             # large regular no topping

orderPizza('large', style='regular')                            # large regular no topping

orderPizza('medium', style='deepdish', topping='mushrooms')     # medium deepdish mushrooms

orderPizza('small', topping='mushrooms')                        # small regular mushrooms