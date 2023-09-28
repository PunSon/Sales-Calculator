class SalesItem:
    def __init__(self,num='',category='',quantity=0,UnitPrice=0.0,ExtendedPrice=0.0):
        self.AccountNumber=num
        self.category=category
        self.quantity=int(quantity)
        self.UnitPrice=float(UnitPrice)
        self.ExtendedPrice=float(ExtendedPrice)
    def setAccountNumber(self,setnum):
        self.AccountNumber=setnum
    def setCategory(self,setcategory):
        self.category=setcategory
    def setQuantity(self,setquantity):
        self.quantity=setquantity
    def setUnitPrice(self,setunitprice):
        self.UnitPrice=setunitprice
    def setExtendedPrice(self,setextendedprice):
        self.ExtendedPrice=setextendedprice
    def getAccountNumber(self):
        return self.AccountNumber
    def getCategory(self):
        return self.category
    def getQuantity(self):
        return self.quantity
    def getUnitPrice(self):
        return self.UnitPrice
    def getExtendedPrice(self):
        return self.ExtendedPrice
    def __str__(self):
        return "Account Number "+ self.AccountNumber +'\n'+'Category '+ self.category+'\n'+'Quantity '+str(self.quantity)+'\n'+ 'Unit Price '+str(self.UnitPrice)+'\n'+'Extended Price '+str(self.ExtendedPrice)