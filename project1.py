class product_info:
    mrp=0
    pur_rate=0
    sale_rate=0
    exp_date=" "
    discount=0.0
    final_price=0.0
    


class purchase(product_info):
    def _init_(self):
        print("Inside Purchse")
        com_name=" "
        product_name=" "
    def input_company(self):
        print('''+++MENU+++
        MENU:-PLEASE SELECT THE COMPANY 
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name=input()

    def input_product(self):
        if(self.com_name=="AGAPPE"):
            print('''PRODUCTS:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')
        elif(self.com_name=="BIOMEURIX"):
            print('''PRODUCTS:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name=="ARKRAY"):
            print('''PRODUCTS:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name=="NIHON KOHDEN"):
            print('''PRODUCTS:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')      
        elif(self.com_name=="BIOLAB"):
            print('''PRODUCTS:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        self.product_name=input()  
    def products(self):
        print("PLEASE ENTER THE PRODUCT INFORMATION")
        print("MRP")
        self.mrp=int(input())
        print("SALE_RATE")
        self.sale_rate=int(input())
        print("PURCHASE_RATE")
        self.pur_rate=int(input())
        print("EXPIRY DATE")
        self.exp_date=input()
        print("DISCOUNT")
        self.discount=float(input())
        print("FINAL PRICE")
        self.final_price=float(input())
           
        
    def update_database(self):
        pass        

class sales(product_info):
    
    def _init_(self):
        print("Inside sales")
        self.com_name=" "
        self.product_name=" "
        self.customer_name=" "

    def input_company(self):
        print('''+++MENU+++
        MENU:-PLEASE SELECT THE COMPANY 
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name=input()
        #print(self.com_name)

    def input_product(self):
        if(self.com_name=="AGAPPE"):
            print('''PRODUCTS:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')
        elif(self.com_name=="BIOMEURIEX"):
            print('''PRODUCTS:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name=="ARKRAY"):
            print('''PRODUCTS:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name=="NIHON KOHDEN"):
            print('''PRODUCTS:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')      
        elif(self.com_name=="BIOLAB"):
            print('''PRODUCTS:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        self.product_name=input()      

        
      
        

    def input_customer(self):
        print("PLEASE ENTER THE CUSTOMER NAME")
        self.customer_name=input()

    def products(self):
        print("PLEASE ENTER THE PRODUCT INFORMATION")
        print("MRP")
        self.mrp=int(input())
        print("SALE_RATE")
        self.sale_rate=int(input())
        print("PURCHASE_RATE")
        self.pur_rate=int(input())
        print("EXPIRY DATE")
        self.exp_date=input()
        print("DISCOUNT")
        self.discount=float(input())
        print("FINAL PRICE")
        self.final_price=float(input())


        
#if"name"=="main":
print('''PLEASE SELECT FROM THE GIVEN OPTIONS
1)BUY
2)SALE''')
choice=int(input())
buy = purchase()
sell = sales()
if choice==1:
    buy.input_company()
    buy.input_product()

elif choice==2:
    sell.input_customer()
    sell.input_company()
    sell.input_product()
