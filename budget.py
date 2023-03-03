from os import truncate


class Category:

 def __init__(self,name):
     self.name=name
     self.ledger=list()


 def __str__(self):
     title=f"{self.name:*^30}\n"
     items=""
     total=0

     for item in self.ledger:
         items+=f"{item['description'][0:23]:23}" +f"{item['amount']:>7.2f}"+'\n'
         total+=item['amount']


     output=title+items+"Total: "+str(total)
     return output


 def deposit(self,amount,description=""):
     self.ledger.append({"amount":amount,"description":description})


 def withdraw(self,amount,description=""):

     if(self.check_funds(amount)):
         self.ledger.append({"amount":-amount,"description":description})
         return True
     return False

 def get_balance(self):
     total_cash=0
     for item in self.ledger:
         total_cash+=item["amount"]

     return total_cash


 def transfer(self,amount,category):
     if(self.check_funds(amount)):
         self.withdraw(amount,"Transfer to "+category.name)
         category.deposit(amount,"Transfer from "+self.name)
         return True
     return False

 def check_funds(self,amount):
     if(self.get_balance()>=amount):
         return True
     return False
 def get_withdrawl(self):
     total=0
     for item in self.ledger:
         if item["amount"]<0:
             total+=item["amount"]
             return total


 def getTotals(categories):
     total=0
     breakdown=[]
     for category in categories:
         total+=category.get_withdrawl()
         breakdown.append(category.get_withdrawl())
     rounded=list(map(lambda x: truncate(x/total),breakdown))
     return  rounded

 def create_spend_chart(categories):
    res="Percentage Spent by Category"
    i=100
    totals= categories.getTotals(categories)
    while i>=0:
      cat_spaces= ""
      for total in totals:
          if total*100>=i:
              cat_spaces+="o  "
          else:
              cat_spaces+="  "
      res+=str(i).rjust(3)+"|"+ cat_spaces + ("\n")
      i-=10
    dashes="-"+"---"*len(categories)
    names=[]
    xaxis=""
    for category in categories:
        names.append(category.name)

    maxi=max(names,key=len)


    for x in range(len(maxi)):
        namestr='  '
        for name in names:
            if x>=len(name):
                namestr+="  "
            else:
                namestr+=name[x]+"  "

        if(x!=len(maxi)-1):
            namestr+='\n'





