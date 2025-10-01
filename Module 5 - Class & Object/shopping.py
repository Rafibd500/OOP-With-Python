class Shopping:
    def __init__(self, name):
        self.cart = []
    def add_to_cart(self, item_name, quatitiy, price):
        item = {'name':item_name, 'quatitiy':quatitiy, 'price' : price}
        self.cart.append(item)
    def remove_items(self, item_name):
        total_item = len(self.cart)
        for i in range(0, total_item):
            if self.cart[i]['name'] == item_name:
                self.cart.pop(i)
                return
        print("Item not exist.")            
    def checkout(self, ammount):
        total = 0
        for item in self.cart:
            total += item['price']
        print(total)
        extra = abs(total - ammount)
        if(ammount<total):
            print(f'Your total cost is {total} Tk. But you entered {ammount} TK. Please pay more {extra} Tk.')
            old_total = ammount
            while(1):
                extra_inp = int(input())
                if(extra_inp<extra):
                    old_total += extra_inp
                    extra = total - old_total
                    print(f'Your total cost is {total} Tk. But you entered total {old_total} TK. Please pay more {extra} Tk.')
                elif (extra_inp > extra):
                    old_total += extra_inp
                    extra = abs(total - old_total)
                    print(f'Here is your Product.\nYour total cost is {total} Tk. But you entered total {old_total} TK. Please take your extra money: {extra} Tk. Thanks for bringing with us.')
                    break
                else : 
                    print('Here is your Product. Thanks for bringing with us.')
                    break
        elif (ammount>total):
            print(f'Here is your Product.\nYour total cost is {total} Tk. But you entered total {ammount} TK. Please take your extra money: {extra} Tk. Thanks for bringing with us.')
        else:
            print('Here is your Product. Thanks for bringing with us.')




kuddus = Shopping('Kuddus Ali')
kuddus.add_to_cart('pen', 2, 200)
kuddus.add_to_cart('pencil', 2, 200)
kuddus.add_to_cart('pen', 2, 200)
kuddus.remove_items('penk')
print(kuddus.cart)
# kuddus.checkout(200)