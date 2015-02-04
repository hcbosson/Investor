#Enacts transactions

import ass
import li
import econ

def buy_stock(title,price,q,div):
    if title=='oe':
        x=ass.OE(title,price,q,div)
    if title=='ae':
        x=ass.AE(title,price,q,div)
    if title=='ys':
        x=ass.YS(title,price,q,div)
    if title=='ei':
        x=ass.EI(title,price,q,div)
    if title=='mm':
        x=ass.MM(title,price,q,div)
    if title=='pb':
        x=ass.PB(title,price,q,div)
    if title=='sy':
        x=ass.SY(title,price,q,div)
    if title=='hz':
        x=ass.HZ(title,price,q,div)
    if title=='io':
        x=ass.IO(title,price,q,div)
    if title=='bp':
        x=ass.BP(title,price,q,div)
    if title=='pp':
        x=ass.PP(title,price,q,div)
    if title=='mc':
        x=ass.MC(title,price,q,div)
    if title=='hm':
        x=ass.HM(title,price,q,div)
    if title=='gs':
        x=ass.GS(title,price,q,div)
    if title=='wp':
        x=ass.WP(title,price,q,div)
    if title=='fs':
        x=ass.FS(title,price,q,div)
    if title=='dl':
        x=ass.DL(title,price,q,div)
    if title=='dr':
        x=ass.DR(title,price,q,div)
    if title=='it':
        x=ass.IT(title,price,q,div)
    if title=='bc':
        x=ass.BC(title,price,q,div)
    return x


def infoStock(title):
    if title=='oe':
        return ass.OE.TITLE
    if title=='ae':
        return ass.AE.TITLE
    if title=='ys':
        return ass.YS.TITLE
    if title=='ei':
        return ass.EI.TITLE
    if title=='mm':
        return ass.MM.TITLE
    if title=='pb':
        return ass.PB.TITLE
    if title=='sy':
        return ass.SY.TITLE
    if title=='hz':
        return ass.HZ.TITLE
    if title=='io':
        return ass.IO.TITLE
    if title=='BP':
        return ass.HM.TITLE
    if title=='pp':
        return ass.PP.TITLE
    if title=='mc':
        return ass.MC.TITLE
    if title=='hm':
        return ass.HM.TITLE
    if title=='gs':
        return ass.GS.TITLE
    if title=='wp':
        return ass.wp.TITLE
    if title=='fs':
        return ass.FS.TITLE
    if title=='dl':
        return ass.DL.TITLE
    if title=='dr':
        return ass.DR.TITLE
    if title=='it':
        return ass.IT.TITLE
    if title=='bc':
        return ass.BC.TITLE
    return x


def _purchase_helper(economy,mymoney):
    result=''
    prompt2='Type the category of asset you wish to purchase (deposit, t bill, \
corp bond, junk bond, cdo, stock).'
    while not (result=='return'):
        print ''
        result=raw_input(prompt2)
        if result=='deposit':
            x= _all_asset_helper(ass.Deposit(0.0),'buy',economy,mymoney)
            if x!=None:
                return x
        elif result=='t bill':
            x= _all_asset_helper(ass.T_Bill(0.0,0),'buy',economy,mymoney)
            if x!=None:
                return x
        elif result=='corp bond':
            x= _all_asset_helper(ass.Corp_Bond(0.0,0),'buy',economy,mymoney)
            if x!=None:
                return x
        elif result=='junk bond':
            x= _all_asset_helper(ass.Junk_Bond(0.0,0),'buy',economy,mymoney)
            if x!=None:
                return x
        elif result=='cdo':
            x= _all_asset_helper(ass.CDO(0.0,0),'buy',economy,mymoney)
            if x!=None:
                return x
        elif result=='stock':
            x=_all_asset_helper(ass.Stock(),'buy',economy,mymoney)


def _nominal_asset_helper(ob, tran,economy,mymoney, title, price):
    result=''
    if tran=='buy':
        while not (result=='return'):
            prompt21='How may '+title+' would you like to buy at \
'+str(price)+' dollars?'
            print ''
            result=raw_input(prompt21)
            try:
                q=int(result)
                if type(ob)==ass.T_Bill:
                    x=ass.T_Bill(economy.get_tby(), q)
                elif type(ob)==ass.Corp_Bond:
                    x=ass.Corp_Bond(economy.get_corpy(),q)
                elif type(ob)==ass.Junk_Bond:
                    x=ass.Junk_Bond(economy.get_junky(),q)
                elif type(ob)==ass.CDO:
                    x=ass.CDO(economy.get_cdoy(), q)
                if title in mymoney.assets:
                    mymoney.assets[title]=mymoney.assets[title]+[x]
                    mymoney.cash=mymoney.cash-x.find_value()
                    return mymoney
                else:
                    mymoney.assets[title]=[x]
                    mymoney.cash=mymoney.cash-x.find_value()
                    return mymoney
            except:
                if result!='return':
                    print 'You did not enter a float. Please try again.'
                    return _nominal_asset_helper(ob, tran,economy,mymoney, title, price)
            
    elif tran=='sell':
        print ''
        try:
            print str(mymoney.assets[title])
        except(KeyError):
            print 'You do not currently own any '+title+'s.'
            result='return'
        while not (result=='return'):
            prompt31='This is how much money you have in this category of asset. \
Type the number for the place of the asset you would like to sell.'
            print ''
            result=raw_input(prompt31)
            try:
                if title in mymoney.assets:
                    q=int(result)
                    if len(mymoney.assets[title])>=q:
                        prompt311='How many of this category of asset would you \
like to sell?'
                        res=raw_input(prompt311)
                        num=int(res)
                        quant=mymoney.assets[title][q-1].quantity
                        if quant<=num:
                            m=mymoney.assets[title][q-1]
                            mymoney.cash=mymoney.cash+m.find_value()
                            mymoney.assets[title].remove(mymoney.assets[title][q-1])
                        elif quant>num:
                            m=mymoney.assets[title][q-1]
                            mymoney.cash=mymoney.cash+m.find_value(num)
                            mymoney.assets[title][q-1].quantity=mymoney.assets[title][q-1].quantity-num
                    else:
                        print 'The int you chose was not in the range. Try again.'
            except:
                if result!='return':
                    print 'You did not enter an int. Please try again.'
                    return _nominal_asset_helper(ob, tran,economy,mymoney, title, price)


def _stock_helper(tran,economy,mymoney):
    result=''
    if tran=='buy':
        while not (result=='return'):
            print ''
            print 'The following are available stocks:'
            economy.print_stockmarket()
            print ''
            prompt111='Which company\'s stock would you like to purchase?'
            title=raw_input(prompt111)
            if title not in economy.stockmarket.allids:
                print 'You did not enter a valid stock id.'
                return None
            prompt211='How many '+title+' would you like to buy at \
'+str(economy.stockmarket.get_price(title))+' dollars?'
            print ''
            result=raw_input(prompt211)
            try:
                q=int(result)
                x=buy_stock(title,economy.stockmarket.get_price(title),q,economy.stockmarket.get_div(title))    
                if 'Stock' in mymoney.assets:
                    mymoney.assets['Stock']=mymoney.assets['Stock']+[x]
                    mymoney.cash=mymoney.cash-x.find_value()
                    return mymoney
                else:
                    mymoney.assets['Stock']=[x]
                    mymoney.cash=mymoney.cash-x.find_value()
                    return mymoney
            except:
                if result!='return':
                    print 'You did not enter a float. Please try again.'
                    return _stock_helper(tran,economy,mymoney)
            
    elif tran=='sell':
        print ''
        try:
            z=str(mymoney.assets['Stock'])
        except(KeyError):
            print 'You do not currently own any '+Stocks+'s.'
            result='return'
        while not (result=='return'):
            z=str(mymoney.assets['Stock'])
            print z
            prompt31='These are the stocks that you own. \
Type the number for the place of the asset you would like to sell.'
            print ''
            result=raw_input(prompt31)
            try:
                if 'Stock' in mymoney.assets:
                    q=int(result)
                    if len(mymoney.assets['Stock'])>=q:
                        prompt311='How many of this category of asset would you \
like to sell?'
                        res=raw_input(prompt311)
                        print 'li'
                        num=int(res)
                        print 'hi'
                        quant=mymoney.assets['Stock'][q-1].quantity
                        print 'yo'
                        if quant<=num:
                            m=mymoney.assets['Stock'][q-1]
                            print 'uh'
                            mymoney.cash=mymoney.cash+m.find_value()
                            print 'bl'
                            mymoney.assets['Stock'].remove(mymoney.assets['Stock'][q-1])
                            print 'he'
                        elif quant>num:
                            print 'she'
                            m=mymoney.assets['Stock'][q-1]
                            print 'duh'
                            mymoney.cash=mymoney.cash+m.find_value(num)
                            print 'la'
                            mymoney.assets['Stock'][q-1].quantity=mymoney.assets['Stock'][q-1].quantity-num
                    else:
                        print 'The int you chose was not in the range. Try again.'
            except:
                if result!='return':
                    print 'You did not enter an int. Please try again.'
                    return _stock_helper(tran,economy,mymoney)



def _all_liability_helper(ob, tran,economy,mymoney):
    if isinstance(ob,li.Debt):
        if type(ob)==li.Loan:
            result1=''
            result2=''
            if tran=='borrow':
                while not ((result1=='return') or (result2=='return')):
                    prompt41='How many US dollars (float) would you like to borrow'
                    print ''
                    result1=raw_input(prompt41)
                    print ''
                    prompt42='How long would you like to take out your loan?'
                    result2=raw_input(prompt42)
                    try:
                        q=float(result1)
                        n=float(result2)
                        x=li.Loan(q,economy.get_inte(),n)
                        l=x.interestrate
                        prompt43='Are you sure you would like to borrow '+str(q)+' \
dollars for '+str(n)+' years at '+str(l)+' percent interest? (yes or no)'
                        result3=raw_input(prompt43)
                        if result3=='yes':
                            if 'Loan' in mymoney.liabilities:
                                print 'no'
                                mymoney.liabilities['Loan']=mymoney.liabilities['Loan']+[x]
                                print 'maybe'
                                mymoney.cash=mymoney.cash+q
                                print 'so'
                                return mymoney
                            else:
                                print 'ugh'
                                mymoney.liabilities['Loan']=[x]
                                print 'bob'
                                mymoney.cash=mymoney.cash+q
                                return mymoney
                    except:
                        if (result1!='return') and (result2!='return'):
                            print 'You did not enter a float. Please try again.'
                            return _all_liability_helper(ob,tran,economy,mymoney)
            
            elif tran=='repay':
                print ''
                result=''
                try:
                    print str(mymoney.liabilities['Loan'])
                except(KeyError):
                    print 'You do not have any outstanding debts.'
                    result='return'
                while not (result=='return'):
                    prompt44='These are the loans you currently have taken out in your name. \
Type the number for the place of the loan you wish to repay.'
                    print ''
                    result=raw_input(prompt44)
                    try:
                        if 'Loan' in mymoney.liabilities:
                            q=int(result)
                            if len(mymoney.liabilities['Loan'])>=q:
                                m=mymoney.liabilities['Loan'][q-1]
                                mymoney.cash=mymoney.cash-m.value
                                mymoney.liabilities['Loan'].remove(mymoney.liabilities['Loan'][q-1])
                            else:
                                print 'The int you chose was not in the range. Try again.'
                    except:
                        if result!='return':
                            print 'You did not enter an int. Please try again.'
                            return _all_liability_helper(ob,tran,economy,mymoney)

def _all_asset_helper(ob, tran,economy,mymoney):
    if isinstance(ob,ass.NonfixedAsset):
        if type(ob)==ass.Deposit:
            result=''
            if tran=='buy':
                while not (result=='return'):
                    prompt21='How may US dollars (float) would you like to put into a CD?'
                    print ''
                    result=raw_input(prompt21)
                    try:
                        q=float(result)
                        x=ass.Deposit(q,economy.get_inte())
                        if 'Deposit' in mymoney.assets:   
                            mymoney.assets['Deposit']=mymoney.assets['Deposit']+[x]
                            mymoney.cash=mymoney.cash-q
                            return mymoney
                        else:
                            mymoney.assets['Deposit']=[x]
                            mymoney.cash=mymoney.cash-q
                            return mymoney
                    except:
                        if result!='return':
                            print 'You did not enter a float. Please try again.'
                            return _all_asset_helper(ob,tran,economy,mymoney)
            
            elif tran=='sell':
                print ''
                try:
                    print str(mymoney.assets['Deposit'])
                except(KeyError):
                    print 'You do not currently own any deposits.'
                    result='return'
                while not (result=='return'):
                    prompt31='This is how much money you have in this category of asset. \
Type the number for the place of the asset you would like to sell.'
                    print ''
                    result=raw_input(prompt31)
                    try:
                        if 'Deposit' in mymoney.assets:
                            q=int(result)
                            if len(mymoney.assets['Deposit'])>=q:
                                m=mymoney.assets['Deposit'][q-1]
                                mymoney.cash=mymoney.cash+m.value
                                mymoney.assets['Deposit'].remove(mymoney.assets['Deposit'][q-1])
                            else:
                                print 'The int you chose was not in the range. Try again.'
                    except:
                        if result!='return':
                            print 'You did not enter an int. Please try again.'
                            return _all_asset_helper(ob,tran,economy,mymoney)
    if isinstance(ob,ass.NominalAsset):
        if isinstance(ob,ass.Bond):
            if type(ob)==ass.T_Bill:
                y=_nominal_asset_helper(ob, tran,economy,mymoney, 'T Bill', economy.get_tbp())
                return y
            if type(ob)==ass.Corp_Bond:
                y=_nominal_asset_helper(ob, tran,economy,mymoney, 'Corp Bond', economy.get_corpp())
                return y
            if type(ob)==ass.Junk_Bond:
                y=_nominal_asset_helper(ob, tran,economy,mymoney, 'Junk Bond', economy.get_junkp())
                return y
        if type(ob)==ass.CDO:
            y=_nominal_asset_helper(ob, tran,economy,mymoney, 'CDO', economy.get_cdop())
    if isinstance(ob,ass.RealAsset):
        if isinstance(ob,ass.Stock):
            y=_stock_helper(tran,economy,mymoney)
            


def _seller_helper(economy,mymoney):
    result=''
    prompt31='Type the category of asset you wish to sell (deposit, t bill, corp \
bond, junk bond, cdo,stock).'
    while not (result=='return'):
        print ''
        result=raw_input(prompt31)
        if result=='deposit':
            x=_all_asset_helper(ass.Deposit(0.0), 'sell',economy,mymoney)
            if x!=None:
                return x
        elif result=='t bill':
            x=_all_asset_helper(ass.T_Bill(0.0,0),'sell',economy,mymoney)
            return x
        elif result=='corp bond':
            x=_all_asset_helper(ass.Corp_Bond(0.0,0),'sell',economy,mymoney)
            return x
        elif result=='junk bond':
            x=_all_asset_helper(ass.Junk_Bond(0.0,0),'sell',economy,mymoney)
            return x
        elif result=='cdo':
            x=_all_asset_helper(ass.CDO(0.0,0),'sell',economy,mymoney)
            return x
        elif result=='stock':
            x=_all_asset_helper(ass.Stock(),'sell',economy,mymoney)


def _liabilities_helper(economy, mymoney):
    result=''
    prompt4='Type either borrow or repay to manage your debt.'
    while not (result=='return'):
        print ''
        result=raw_input(prompt4)
        if result=='borrow':
            x=_all_liability_helper(li.Loan(0.0,0.0,0.0),'borrow',economy,mymoney)
            if x!=None:
                return x
        if result=='repay':
            x=_all_liability_helper(li.Loan(0.0,0.0,0.0),'repay',economy,mymoney)
            if x!=None:
                return x

def _derivatives_helper(economy,mymoney):
    _DERIVATIVES=['option']
    result='';result1=''
    while (result!='return') and (result1!='return'):
        result='';result1=''
        while result!='buy' and result!='use' and result!='return':
            prompt89='Would you like to buy or use your derivatives?'
            print ''
            result=raw_input(prompt89)
            print
        if result=='buy':
            while (result1 not in _DERIVATIVES) and result1!='return':
                prompt90='Type the category of derivative you wish to purchase (option).'
                result1=raw_input(prompt90)
                print ''
            if result1=='option':
                x= _all_derivatives_helper('Option',result,economy,mymoney)
                if x!=None:
                    return x
        if result=='use':
            while (result1 not in _DERIVATIVES) and result1!='return':
                prompt99='Type the category of derivative you wish to use (option).'
                result1=raw_input(prompt99)
                print ''
            if result1=='option':
                x= _all_derivatives_helper('Option',result,economy,mymoney)
                if x!=None:
                    return x


def _all_derivatives_helper(der,tran,economy,mymoney):
    opt_names=['call','put','short']
    result=''
    if tran=='buy':
        if der=='Option':
            while not (result=='return'):
                print ''
                print 'The following are available stocks:'
                economy.print_stockmarket()
                print ''
                prompt111='Which company\'s stock would you like to purchase an option \
for?'
                title=raw_input(prompt111)
                if title not in economy.stockmarket.allids:
                    print 'You did not enter a valid stock id.'
                    return None
                print ''
                prompt112='Which kind of option would you like to purchase? (call,put,short)'
                opt=raw_input(prompt112)
                if (opt not in opt_names):
                    return None
                print 'These are the options available for this stock.'
                economy.stockmarket.print_option(title,opt)
                prompt131='What duration would you like your option to have? (int)'
                length=raw_input(prompt131)
                if length not in ['1','2','5']:
                    return None
                option=economy.stockmarket.get_option(title,opt,length)
                length=int(length)
                print ''
                prompt211='How many '+opt+'s would you like to buy for '+title+' stock \
with stike price of '+str(option[0])+' and premium of '+str(option[1])+'?'
                print ''
                result=raw_input(prompt211)
                try:
                    q=int(result)
                    if opt=='call':
                        x=ass.Call(title,option[0],q,length)
                    if opt=='put':
                        x=ass.Put(title,option[0],q,length)
                    if opt=='short':
                        x=ass.Short(title,option[0],q,length)
                    if opt in mymoney.assets:
                        mymoney.derivatives[der]=mymoney.derivatives[der]+[x]
                        mymoney.cash=mymoney.cash-q*option[1]
                        return mymoney
                    else:
                        print x
                        mymoney.derivatives[der]=[x]
                        mymoney.cash=mymoney.cash-q*option[1]
                        return mymoney
                except:
                    if result!='return':
                        print 'You did not enter a float. Please try again.'
                        return _all_derivatives_helper(der,tran,economy,mymoney)
            
    elif tran=='use':
        while not (result=='return'):
            print ''
            try:
                z=str(mymoney.derivatives[der])
            except(KeyError):
                print 'You do not currently own any '+der+'s.'
                return _all_derivatives_helper(der,tran,economy,mymoney)
            print z
            prompt31='These are the '+der+'s that you own. \
Type the number for the place of the asset you would like to use.'
            print ''
            result=raw_input(prompt31)
            try:
                if der in mymoney.derivatives:
                    q=int(result)
                    if len(mymoney.derivatives[der])>=q:
                        prompt311='How many '+der+'s would you \
like to use?'
                        x=mymoney.derivatives[der][q-1]
                        num1=raw_input(prompt311)
                        try:
                            num=int(num1)
                        except:
                            print 'You did not enter an int.'
                            return None
                        if num>x.quantity:
                            num=x.quantity
                        keep='yes'
                        if type(x)==ass.Call:
                            prompt313='Would you like to carry out market operations \
so that you receive cash instead of new assets? (yes or no)'
                            keep=raw_input(prompt313)
                        if keep=='yes':
                            mymoney.cash=mymoney.cash+x.find_value(economy)*num
                            if num==x.quantity:
                                mymoney.derivatives[der].remove(mymoney.derivatives[der][q-1])
                            else:
                                x.quantity=x.quantity-num
                        elif keep=='no':
                            mymoney.cash=mymoney.cash-x.price*num
                            div=economy.stockmarket.get_div(self.name)
                            y=buy_stock(x.name,x.price,num,div)
                            if 'Stock' in mymoney.assets:
                                mymoney.assets['Stock']=mymoney.assets['Stock']+[y]
                                return mymoney
                            else:
                                mymoney.assets['Stock']=[x]
                                return mymoney
                    else:
                        print 'The int you chose was not in the range. Try again.'
            except:
                if result!='return':
                    print 'You did not enter an int. Please try again.'
                    return _stock_helper(tran,economy,mymoney)
