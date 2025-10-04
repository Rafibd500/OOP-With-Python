# static attribute(class attribute)
# static method @staticmethod
# class method @classmethod
# difference between static method and class method

class Shopping:
    cart = []   # static attribute/ class attribute
    def __init__(self, customer_name, id, age):
        self.customer_name = customer_name  # instance attribute
        self.id = id
        self.age = age 
        self.origin = 'BD'
    def parchase(self, item, quantity):
        print(f'{item} {quantity}')
    #static method
    @staticmethod
    def calling2(item):
        print(f'I am calling2 item: {item}')
    #class method
    @classmethod
    def calling(self, item):
        print(f'I am calling item: {item}.')   
        # print(self.origin)        #!!!!!!!!!!! ConFusion !!!!!!!!!!!!!   

Shopping.parchase(-1, 'kodu', 2)
user1 = Shopping('customer', 101, 29)
user1.parchase('potol', 5)

Shopping.calling('alu')
user1.calling('vat\n')

Shopping.calling2('alu')
user1.calling2('vat\n')