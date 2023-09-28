#CompanySales
from SalesItem import SalesItem
import sys

class CompanySales:
    def __init__(self,companyname="",companyaddress="",filename=""):        
        self.CompanyName=companyname
        self.CompanyAddress=companyaddress
        self.SalesList=[]
        if filename!="":
         try:
             file=open(filename,'r')
         except IOError:
             print ("File name is invalid")
             sys.exit()
              
         line = file.readline() #skip heading line
         for line in file:
            alist=line.split(',')
            salesObject = SalesItem(alist[0],alist[1],int(alist[2]),float(alist[3]),float(alist[4]))
            self.SalesList.append(salesObject)
        
    def setCompanyName(self,nname):
        self.CompanyName=nname
    def setCompanyAddress(self,naddy):
        self.CompanyAddress=naddy
    def getCompanyName(self):
        return self.CompanyName
    def getCompanyAddress(self):
        return self.CompanyAddress
    
    def __str__(self):
        return 'Company Name: '+ str(self.CompanyName)+'\nCompany Address: '+str(self.CompanyAddress)

    def filterData(self,cat): 
                     
        filterdatalist=[]
        for object in self.SalesList:
            if object.getCategory()==cat:
                filterdatalist.append(object)
        return filterdatalist
    def Stats(self,thelist):            
        maximum=0.0
        minimum=100000.0
        total=0.0

        for x in range(len(thelist)):
            price = thelist[x].getExtendedPrice()    
            if price >maximum:
                maximum = price               
            if price < minimum:
                minimum = price
            total+= price
        print('Max: ',maximum,'\nMin: ',minimum,'\nSum: ',round(total,2))
        
    def deepCopy(self,anotherObject):
        self.CompanyAddress = anotherObject.getCompanyAddress()
        self.CompanyName = anotherObject.getCompanyName()
        for i in range (len(anotherObject.SalesList)):
            acctnum = anotherObject.SalesList[i].getAccountNumber()
            cat = anotherObject.SalesList[i].getCategory()
            quantity = anotherObject.SalesList[i].getQuantity()
            unitp = anotherObject.SalesList[i].getUnitPrice()
            extp = anotherObject.SalesList[i].getExtendedPrice()
            newObject = SalesItem(acctnum,cat,quantity,unitp,extp)
            self.SalesList.append(newObject)           
    

if __name__=='__main__':
    object1=CompanySales('Buyers Inc.', '1000 KingsHighway', 'CompanySalesData.csv')
    newlist = object1.filterData("Shirt")
    for item in newlist:
        print (item)
    object1.Stats(newlist)
    # start test of shallow copy and deep copy
    print("Object1:",object1)
    object2 = CompanySales()
    print ("Object2:",object2)
    object2 = object1 #shallow copy
    print ("Object2 extended price",object2.SalesList[0].getExtendedPrice())
    object1.SalesList[0].setExtendedPrice(2.00)
    print ("Object1 SalesList[0] extended price",object1.SalesList[0].getExtendedPrice())
    print ("Object2 SalesList[0] extended price",object2.SalesList[0].getExtendedPrice())
    object3 = CompanySales()
    object3.deepCopy(object1)
    print ("Object 1",object1)
    print ("Object 2",object3)
    object3.setCompanyName("Wallmart")
    print (object1)
    print (object3)
    print (object1.SalesList[1].getUnitPrice())
    object1.SalesList[1].setUnitPrice(111.00)
    #shows a deepcopy
    print (object1.SalesList[1].getUnitPrice())
    print (object3.SalesList[1].getUnitPrice())