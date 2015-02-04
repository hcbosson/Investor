#Manage assets

import econ
import li
import random


class Finance(econ.Economy):
    pass

class Derivative(Finance):
    pass


class Asset(Finance):
    def find_value(self, quantity=None):
        if quantity==None:
            return self.value*self.quantity
        else:
            return self.value*quantity


class RealAsset(Asset):
    def _inflating(self,inflation):
        pass


class Stock(RealAsset):
    def __init__(self,name=None,value=0,quantity=0,dividend=0):
        self.name=name
        self.value=value
        self.quantity=quantity
        self.div=dividend
    
    def __str__(self):
        return ('Stock '+self.name+': (price: '+str(self.value)+' quantity: '
                +str(self.quantity)+' dividend: '+str(self.div)+')')
    
    def __repr__(self):
        return ('Stock '+self.name+': (price: '+str(self.value)+' quantity: '
                +str(self.quantity)+' dividend: '+str(self.div)+')')
    
    def _interest(self,economy):
        self.value=economy.stockmarket.get_price(self.name)
        self.div=economy.stockmarket.get_div(self.name)
        if self.name in economy.stockmarket.split:
            self.quantity=self.quantity*20
    
    def give_div(self):
        return self.quantity*self.div
    
    

class NominalAsset(Asset):
    def _inflating(self, inflation):
        self.value=(self.value*(1.0/(1.0+inflation)))
        

class NonfixedAsset(NominalAsset):
    def _interest(self,economy):
        self.value=(self.value*(1.0+self.interestrate))

class Deposit(NonfixedAsset):
    """Represents a deposit which has a certain value and increases in value for
    each year that is it owned by the player by the value of the interest rate.
    It is not independent of inflation.
    
    Instance Attributes:
        value: The value of the deposit owned by the player. [float >=0.0]"""
    
    def __init__(self,value,interestrate=0.0):
        assert type(value)==float, str(value)+' is not a float.'
        assert value>=0.0, str(value)+' is not greater than or equal to 0.0'
        
        self.inte=interestrate
        self.value=value
    
    def __str__(self):
        return 'Deposit: (deposit: '+str(self.value)+', yield: '+str(self.inte)+')'
    
    def __repr__(self):
        return 'Deposit: (deposit: '+str(self.value)+', yield: '+str(self.inte)+')'
    
    def find_value(self):
        return self.value


class Bond(NominalAsset):
    """Represents a Treasury bond with maturity of 10 years.
    Shows projected value (nominal), current value,
    and annual yield. Str representation also shows projected
    real value."""
    
    def __init__(self, yields, quantity, face_value, length):
        self.face_value=face_value
        self.length=length
        self.yields=yields
        self.quantity=quantity
        self.value=self.face_value*(1.0/(1.0+self.yields))**self.length
        
    def __str__(self):
        return ('(current value: '+str(self.value)+', yield: \
'+str(self.yields)+', time to maturity: '+str(self.length)+', quantity: \
'+str(self.quantity)+')')
    
    def __repr__(self):
        return ('(current value: '+str(self.value)+', yield: \
'+str(self.yields)+', time to maturity: '+str(self.length)+', quantity: \
'+str(self.quantity)+')')
    
    def maturing(self,mymoney):
        self.length=self.length-1
        if self.length==0:
            mymoney.cash=mymoney.cash+self.value*self.quantity
            return 'paid off'
    

class T_Bill(Bond):
    def __init__(self, yields, quantity):
        Bond.__init__(self, yields, quantity, 1000, 10)
    
    def __str__(self):
        return 'T Bill: '+Bond.__str__(self)
    
    def __repr__(self):
        return 'T Bill: '+Bond.__repr__(self)
    
    def _interest(self,economy):
        self.value=(self.face_value*(1.0/(1.0+economy.get_tby()))**self.length)
    
class Corp_Bond(Bond):
    def __init__(self, yields, quantity):
        Bond.__init__(self, yields, quantity, 1000, 5)
    
    def __str__(self):
        return 'Corporate Bond: '+Bond.__str__(self)
    
    def __repr__(self):
        return 'Corporate Bond: '+Bond.__repr__(self)
    
    def _interest(self, economy):
        self.value=(self.face_value*(1.0/(1.0+economy.get_corpy()))**self.length)
        num=0
        for i in range(self.quantity):
            x=random.uniform(0.0,1.0)
            if x<=economy.get_corpr():
                self.quantity=self.quantity-1
                num=num+1
                if self.quantity==0:
                    self.length=1
        if num>0:
            print str(num)+' corporate bonds defaulted.'
    

class Junk_Bond(Bond):
    def __init__(self, yields, quantity):
        Bond.__init__(self, yields, quantity, 1000, 10)
    
    def __str__(self):
        return 'Junk Bond: '+Bond.__str__(self)
    
    def __repr__(self):
        return 'Junk Bond: '+Bond.__repr__(self)
    
    def _interest(self, economy):
        self.value=(self.face_value*(1.0/(1.0+economy.get_junky()))**self.length)
        num=0
        for i in range(self.quantity):
            x=random.uniform(0.0,1.0)
            if x<=economy.get_junkr():
                self.quantity=self.quantity-1
                num=num+1
                if self.quantity==0:
                    self.length=1
        if num>0:
            print str(num)+' junk bonds defaulted.'



class CDO(NominalAsset):
    """Represents a collateralized debt obligation with duration 30 years.
    Shows projected value (nominal), current value,
    and annual yield. Str representation also shows projected
    real value."""
    
    def __init__(self, yields, quantity, face_value=10000, length=30):
        self.face_value=face_value
        self.length=length
        self.yields=yields
        self.quantity=quantity
        self.value=self.face_value*(1.0/(1.0+self.yields))**self.length
        
    def __str__(self):
        return ('CDO: (current value: '+str(self.value)+', return: \
'+str(self.yields)+', time to completion: '+str(self.length)+', quantity: \
'+str(self.quantity)+')')
    
    def __repr__(self):
        return ('CDO: (current value: '+str(self.value)+', return: \
'+str(self.yields)+', time to completion: '+str(self.length)+', quantity: \
'+str(self.quantity)+')')
    
    def maturing(self,mymoney):
        self.length=self.length-1
        if self.length==0:
            mymoney.cash=mymoney.cash+self.value*self.quantity
            return 'paid off'
    
    def _interest(self,economy):
        self.value=(self.face_value*(1.0/(1.0+economy.get_cdor()))**self.length)
        num=0
        for i in range(self.quantity):
            x=random.uniform(0.0,1.0)
            if x<=economy.get_cdor():
                self.quantity=self.quantity-1
                num=num+1
                if self.quantity==0:
                    self.length=1
        if num>0:
            print str(num)+' cdos defaulted.'


class OE(Stock):
    """Representation of the innovative tech firm Orange Inc."""
    TITLE='The innovative tech firm Orange Inc'
    
class AE(Stock):
    """Representation of the utility American Electric."""
    TITLE='The utility American Electric.'


class YS(Stock):
    """Representation of the social networking startup Your Space."""
    TITLE='The social networking startup Your Space.'


class EI(Stock):
    """Representation of the oil giant Enron Immobile."""
    TITLE='The oil giant Enron Immobile.'


class MM(Stock):
    """Representation of American car manufacturer Major Motors."""
    TITLE='The American car manufacturer Major Motors.'


class PB(Stock):
    """Representation of the consumer bank The People's Bank."""
    TITLE='The consumer bank The People\'s Bank.'


class SY(Stock):
    """Representation of the department store Stacy's."""
    TITLE='The department store Stacy\'s.'


class HZ(Stock):
    """Representation of the telecommuications firm Horizon."""
    TITLE='The telecommuications firm Horizon.'


class IO(Stock):
    """Representation for the agricultural chemical firm Insanto."""
    TITLE='The agricultural chemical firm Insanto.'


class BP(Stock):
    """Representation for the fast-food chain Burger Prince."""
    TITLE='The fast-food chain Burger Prince.'


class PP(Stock):
    """Representation for the publishing giant Pelican Publishing."""
    TITLE='The publishing giant Pelican Publishing.'


class MC(Stock):
    """Representation for the universally hated cable provider Monocast."""
    TITLE='The universally hated cable provider Monocast.'


class HM(Stock):
    """Representation for the superstore chain Hugemart."""
    TITLE='The superstore chain Hugemart.'


class GS(Stock):
    """Representation for the soulless investment bank Goldfinger Stacks."""
    TITLE='The soulless investment bank Goldfinger Stacks.'
        
        
class WP(Stock):
    """Representation of the video streaming provider WePick."""
    TITLE='The video streaming provider WePick.'


class FS(Stock):
    """Representation of the steel manufacturer Formerly Known as American Steel."""
    TITLE='The steel manufacturer Formerly Known as American Steel.'


class DL(Stock):
    """Representation of the search monopoly Doodle."""
    TITLE='The search monopoly Doodle.'


class DR(Stock):
    """Representation of the mining firm Diamonds are Forever."""
    TITLE='The mining firm Diamonds are Forever.'


class IT(Stock):
    """Representation of the heavily subsidized railway IsTrack."""
    TITLE='The heavily subsidized railway IsTrack.'


class BC(Stock):
    """ Representation of the large consulting firm Bridgehammer Consulting."""
    TITLE='The large consulting firm Bridgehammer Consulting.'

class Stock_Option(Derivative):
    def __init__(self, name=None,price=0,quantity=0,length=0):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.length=length
    
    def maturing(self,mymoney,economy):
        self.length=self.length-1
        if self.length<0:
            return 'paid off'
    
    def _inflating(self, interestrate):
        pass    
    
    def _interest(self,economy):
        if self.name in economy.stockmarket.split:
            self.quantity=self.quantity*20
            self.price=self.price/20
    

class Call(Stock_Option):
    def find_value(self, economy):
        inc=economy.stockmarket.get_price(self.name)-self.price
        if inc<=0:
            return 0.0
        return inc
    
    def __str__(self):
        return ('Call: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
    
    def __repr__(self):
        return ('Call: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
    

class Put(Stock_Option):
    def find_value(self, economy):
        inc=self.price-economy.stockmarket.get_price(self.name)
        if inc<=0:
            return 0.0
        return inc
    
    def __str__(self):
        return ('Put: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
    
    def __repr__(self):
        return ('Put: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
    

class Short(Stock_Option):
    def maturing(self,mymoney,economy):
        self.length=self.length-1
        print 'working'
        if self.length<0:
            print 'paid off'
            mymoney.cash=mymoney.cash+self.quantity*self.find_value(economy)
            return 'paid off'
    
    def find_value(self, economy):
        print 'getting value'
        val=self.price-economy.stockmarket.get_price(self.name)
        print val
        print
        return val
    
    def __str__(self):
        return ('Short: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
    
    def __repr__(self):
        return ('Short: (stock: '+self.name+', strike price: '+str(self.price)+', \
quantity: '+str(self.quantity)+', time to completion: '+str(self.length)+')')
