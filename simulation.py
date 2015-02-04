#Runs the game


import random
import li
import ass
import trns
import econ


def find_networth(assets, liabilities, cash):
    networth=0.0
    for x in assets:
        for y in range(len(assets[x])):
            networth=networth+assets[x][y].find_value()
    for i in liabilities:
        for l in range(len(liabilities[i])):
            networth=networth-liabilities[i][l].value
    return networth+cash

def concluding_liabilities_helper(y,mymoney):
    if y=='Loan':
        for x in range(len(mymoney.liabilities['Loan'])):
                result=mymoney.liabilities['Loan'][x].paying_off_loan(mymoney)
                if result=='paid off':
                    mymoney.liabilities['Loan'].remove(mymoney.liabilities['Loan'][x])

def concluding_assets_helper(y,mymoney):
    for x in range(len(mymoney.assets[y])):
        result=mymoney.assets[y][x].maturing(mymoney)
        if result=='paid off':
            mymoney.assets[y].remove(mymoney.assets[y][x])


def concluding_derivatives_helper(y,mymoney,economy):
    for x in range(len(mymoney.derivatives[y])):
        result=mymoney.derivatives[y][x].maturing(mymoney,economy)
        if result=='paid off':
            mymoney.derivatives[y].remove(mymoney.derivatives[y][x])
    

class Wealth(object):
    """Represents all holdings of the player in this game.
    
    Instance Attributes:
        assets: The list of all noncash holdings owned by the player [list of objects]
        liabilities: The list of all debts owed by the player [list of objects]
        cash: The number of US dollars the player has not invested [float >=0.0]
        networth: The total value of all assets and cash minus the value of all
        liabilities, measures in US dollars [float]"""
    
    def __init__(self, assets={},derivatives={}, liabilities={}, cash=0.0):
        self.assets=assets
        self.derivatives=derivatives
        self.liabilities=liabilities
        self.cash=cash
        self.networth= find_networth(assets, liabilities, cash)
    
    def __str__(self):
        """Readable string representation of the player's current wealth."""
        print 'Your assets:'
        for x in self.assets:
            for y in range(len(self.assets[x])):
                print `self.assets[x][y]`
        print ''
        print 'Your derivatives:'
        for x in self.derivatives:
            for y in range(len(self.derivatives[x])):
                print `self.derivatives[x][y]`
        print ''
        print 'Your liabilities:'
        for i in self.liabilities:
            for j in range(len(self.liabilities[i])):
                print `self.liabilities[i][j]`
        print ''
        print 'Your available cash: '+`self.cash`
        print ''
        return 'Your networth: '+`self.networth`
        """print 'Your assets: '+`self.assets`
        print 'Your liabilities: '+`self.liabilities`
        print 'Your available cash: '+`self.cash`
        return 'Your networth: '+`self.networth`"""
    
    def __repr__(self):
        print 'Your assets:'
        for x in self.assets:
            print `x`
        print ''
        print 'Your derivatives:'
        for x in self.derivatives:
            for y in range(len(self.derivatives[x])):
                print `self.derivatives[x][y]`
        print ''
        print 'Your liabilities:'
        for i in self.liabilities:
            print `i`
        print ''
        print 'Your available cash: '+`self.cash`
        print ''
        return 'Your networth: '+`self.networth`
        """print 'Your assets: '+`self.assets`
        print 'Your liabilities: '+`self.liabilities`
        print 'Your available cash: '+`self.cash`
        return 'Your networth: '+`self.networth`"""
    
    def inflate(self,inflation):
        for x in self.assets:
            for i in range(len(self.assets[x])):
                self.assets[x][i]._inflating(inflation)
        for x in self.derivatives:
            for i in range(len(self.derivatives[x])):
                self.derivatives[x][i]._inflating(inflation)
        for y in self.liabilities:
            for j in range(len(self.liabilities[y])):
                self.liabilities[y][j]._inflating(inflation)
        self.cash=self.cash*(1.0/(1.0+inflation))
    
    def interest(self,economy):
        for x in self.assets:
            for i in range(len(self.assets[x])):
                self.assets[x][i]._interest(economy)
                if hasattr(self.assets[x][i],'div'):
                    self.cash=self.cash+self.assets[x][i].give_div()
        for y in self.liabilities:
            for j in range(len(self.liabilities[y])):
                self.liabilities[y][j]._interest(economy)
        for w in self.derivatives:
            for p in range(len(self.derivatives[w])):
                self.derivatives[w][p]._interest(economy)
            
        
    
    def get_networth(self):
        self.networth= find_networth(self.assets,self.liabilities,self.cash)
    
    def concluding(self,economy):
        if 'Loan' in self.liabilities:
            y='Loan'
            concluding_liabilities_helper(y,self)
        if 'T Bill' in self.assets:
            y='T Bill'
            concluding_assets_helper(y,self)
        if 'Corp Bond' in self.assets:
            y='Corp Bond'
            concluding_assets_helper(y,self)
        if 'Junk Bond' in self.assets:
            y='Junk Bond'
            concluding_assets_helper(y,self)
        if 'CDO' in self.assets:
            y='CDO'
            concluding_assets_helper(y,self)
        if 'Option' in self.derivatives:
            y='Option'
            concluding_derivatives_helper(y,self,economy)
    

def play_a_game():
    """Create and play a game."""
    turns=40
    gdp=econ.GDP()
    interestrate=econ.Interestrate(.01,0.0,0.0,0.0)
    inflation=econ.Inflation(.02,0.0,0.0,0.0)
    bond_yields=econ.Bond_Yields(.01,.03,.07)
    cdo_yields=econ.CDO_Yield(.02,0.0,0.0,0.0,.02,interestrate.interestrate)
    stocks=econ.Stock_Market()
    economy=econ.Economy(gdp, interestrate, inflation,bond_yields,cdo_yields,stocks)
    mymoney=Wealth({},{},{},10000.0)
    for i in range(9):
        economy.update()
    for x in range(turns):
        economy.update()
        mymoney.inflate(economy.get_infl())
        mymoney.interest(economy)
        mymoney.get_networth()
        mymoney.concluding(economy)
        play_a_turn(mymoney,economy)
    
    print 'Thank you for playing!'
    print 'You are now officially a capitalist whore.'
    print 'This is how you ended up.'
    print str(mymoney)


def play_a_turn(mymoney,economy):
    """Create and play a turn."""
    
    prompt1='Type buy to make a purchase, sell to divest, derivative to trade in derivatives\
, debt to take out or repay loans, info to see market information, or end to end \
your turn.'

    result=''
    while not (result=='end'):
        print ''
        result=raw_input(prompt1)
        if result=='buy':
            trns._purchase_helper(economy,mymoney)
        elif result=='sell':
            trns._seller_helper(economy,mymoney)
        elif result=='derivative':
            trns._derivatives_helper(economy,mymoney)
        elif result=='debt':
            trns._liabilities_helper(economy,mymoney)
        elif result=='info':
            _info_helper(economy,mymoney)
        elif result=='return':
            print 'You are at the first page. You can return no farther.'
        elif result=='quit':
            raise AssertionError
        elif result!='end':
            print 'Invalid response. Please enter a new command.'
        elif result=='end':
            if mymoney.cash<0:
                print
                print 'Fat charlie is coming for his money. Either sell assets \
or take out a loan to remain solvent.'
                print
                result==''
        mymoney.get_networth()
    
    


def _info_helper(economy,mymoney):
    result=''
    prompt5='Type economy to see general economic data, or see prices of specific \
categories of assets by typing the category (stockmarket, bonds, securities). Type wealth to \
see your current financial standing.'
    while not (result=='return'):
        print ''
        result=raw_input(prompt5)
        if result=='wealth':
            print
            print mymoney
        elif result=='economy':
            print
            print economy
        elif result=='securities':
            print
            economy.print_securities()
        elif result=='stockmarket':
            print
            economy.print_stockmarket()
            result2=''
            while not result2=='return':
                prompt34='To look up more on a specific stock type its id. Otherwise \
enter return to return.'
                print
                result2=raw_input(prompt34)
                if result2 in economy.stockmarket.allids:
                    info=trns.infoStock(result2)
                    print
                    print
                    print result2
                    print info
                    pos=economy.stockmarket.allids.index(result2)
                    x=round(economy.stockmarket.all_stocks[pos][0],2)
                    y=economy.stockmarket.allids[pos]
                    z=[]
                    for a in economy.stockmarket.all_stocks[pos][7]:
                        z=z+[round(a,2)]
                    w=round(economy.stockmarket.all_stocks[pos][6],2)
                    print
                    print str(y)+' price: '+str(x)+' dividend: '+str(w)
                    print 'past prices: '+str(z)
                    print
                    economy.stockmarket.print_option(result2,'call')
                    print
                    economy.stockmarket.print_option(result2,'put')
        elif result=='bonds':
            print
            economy.print_bonds()
    
    

#if __name__ == '__main__':
   # play_a_game()