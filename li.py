#Manage liabilities


import ass
import econ


class Liability(ass.NonfixedAsset):
    pass


class Debt(Liability):
    """Representation of a set quantity of debt owed by the player."""
    
    def __init__(self,value, interestrate):
        self.value=value
        self.interestrate=interestrate

class Loan(Debt):
    def __init__(self,value,interestrate,length):
        Debt.__init__(self,value,interestrate*(1.0+(.2*interestrate))**(length))
        self.length=length
    
    def __str__(self):
        x='(Quantity borrowed: '+str(self.value)+', interest: \
'+str(self.interestrate)+', remaining time: '+str(self.length)+')'
        return x
    
    def __repr__(self):
        x= '(Quantity borrowed: '+str(self.value)+', interest: \
'+str(self.interestrate)+', remaining time: '+str(self.length)+')'
        return x
    
    def paying_off_loan(self,mymoney):
        self.length=self.length-1
        if self.length==0:
            mymoney.cash=mymoney.cash-self.value
            return 'paid off'