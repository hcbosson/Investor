#Manages economy


import li
import ass
import trns
import random
import math

#helper functions
def multiply(list1,list2):
    new=[]
    length1=len(list2)
    length2=len(list1)
    for z in range(length2):
        y=0
        for x in range(length1):
            y=y+list2[x]*list1[z]
        new.append(y)
    return new


def multiply_matrix(list1, list2):
    """Returns: the product of two matrices
    Precondition: list1 must be an mxn matrix, and list2 must be an nxp matrix"""
    new=[]
    length=len(list1)
    for x in range(length):
        new.append(multiply(list2[x] ,list1[x]))
    return new


def interestrate_randomization():
    """Returns a random jerk for the class Interestrate."""
    x= random.uniform(-.1,.1)
    return x

def regression(thelist):
    avey=float(sum(thelist))/len(thelist)
    avex=float(len(thelist))/2
    mn=0
    md=0
    for i in range(len(thelist)):
        if ((i+1-avex)**2)!=0:
            mn=mn+((i+1-avex)*(thelist[i]-avey))
            md=md+((i+1-avex)**2)
    m=float(mn)/md
    return m

def residual(m,b,thelist):
    pass
    

def call_finder(price,past,length):
    if len(past)<10:
        return 0
    m=(regression(past)+past[-1]-past[-2])/2
    yhat=m*math.sqrt(length)+price
    return yhat

def put_finder(price,past,length):
    return call_finder(price,past,length)


class GDP(object):
    """Gross Domestic Output, as determined by the following sectors:
    Agrigulcture, forestry, fishing, and hunting [list]
    Mining [list]
    Utilities [list]
    Construction [list]
    Manufacturing [list]
    Wholsesale trade [list]
    Retail trade [list]
    Transportation and warehousing [list]
    Information [list]
    Finace, insurance, real estate, rental, and leasing [list]
    Professional and business services [list]
    Educational services, health care, and social assistance [list]
    Arts, entertainment, etc [list]
    Other non government
    Government [list]
    All sectors [list]
    GDP [float]
    
    Calculated using output matrix*[[ag],[mi],[ut],[con],[man],[whol],[ret],[tran],
    [info],[fir],[pro],[ehc],[art],[oth],[gov]]"""
    _ag_in=[0.98954,0,0,0,0,0.00170,0.000227,0,0,0,0,0,0,0,0.00853]
    _min_in=[0,0.9976,0.000019,0,0.00122,0,0,0,0,0,0.000331,0,0,0,.000779]
    _ut_in=[0,0,0.76714,0,0,0,0,0.00148,0,0,0,0,0,0,0.231383]
    _con_in=[0.000704,0.0152,0.00194,0.94,0.0039,0.0036,0.0039,
             0.00044,0.0013,0.0095,0.0017,0.0017,0.002,0.0003,0.013]
    _man_in=[0,0.0055,0,0,.9876,0.0014,0.0032,0,0.0001,0,0.0004,0,0,0,0.0016]
    _whol_in=[0,0.0004,0,0,0.037,0.954,0,0,0.00377,0,0.0041,0,0,0.0004,0]
    _ret_in=[0,0,0,0,0,0,.968,0,0.0016,0.001,0.005,0.009,0.0065,0.0036,0.004]
    _tran_in=[0,0,0,0,0,0.0013,0.004,0.967,0,0.0005,0,0,0,0,0.026]
    _info_in=[0,0,0,0,0,0,0,0,0.9727,0,0.024,0,0.0002,0.0002,0.0026]
    _fir_in=[0,0,0,0,0,0.0021,0.0022,0.0001,0.0008,0.9798,0.0002,0.001,0.003,
             0.0001,0.011]
    _pro_in=[0,0.0003,0.0002,0,0.043,0.0056,0.001,0.0007,0.064,0.0044,0.835,
             0.011,0.002,0.0004,0.03]
    _ehc_in=[0,0,0,0,0,0,0.0003,0,0.0005,0,0.0005,0.8846,0,0,0.1134]
    _art_in=[0.001,0,0,0,0,0,0.03,0.0003,0,0,0,0.019,0.892,0.004,0.054]
    _oth_in=[0,0,0,0,0.0001,0.08,0.12,0.0003,0.003,0.0024,0.0017,0,0.003,0.783,
             0.0058]
    _gov_in=[0,0,0.0007,0,0,0,0,0,0,0,0,0,0,0,.9993]
    output=[_ag_in,_min_in,_ut_in,_con_in,_man_in,_whol_in,_ret_in,_tran_in,_info_in,
            _fir_in,_pro_in,_ehc_in,_art_in,_oth_in,_gov_in]
    _gdp_ratio=[0.0162,0.0195,0.0167,0.0406,0.1947,0.0491,0.0469,0.0345,0.0412,
                0.1727,0.1242,0.0863,0.0410,0.0249,0.0911]
    sector_ids=['Agrigulcture, forestry, fishing, and hunting','Mining','Utilities','Construction','Manufacturing','Wholsesale trade',
                'Retail trade','Transportation and warehousing','Information',
                'Finace, insurance, real estate, rental, and leasing','Professional and business services',
                'Educational services, health care, and social assistance,',
                'Arts, entertainment, etc','Other non government','Government']
    
    def __init__(self):
        self.ag=[random.uniform(-.01,.05),0.0,0.0,0.0,0.03]
        self.mi=[random.uniform(-.01,.05),0.0,0.0,0.0,0.03]
        self.ut=[random.uniform(-.01,.05),0.0,0.0,0.0,0.0]
        self.con=[random.uniform(-.01,.05),0.0,0.0,0.0,0.07]
        self.man=[random.uniform(-.01,.05),0.0,0.0,0.0,0.05]
        self.whol=[random.uniform(-.01,.05),0.0,0.0,0.0,0.04]
        self.ret=[random.uniform(-.01,.05),0.0,0.0,0.0,0.05]
        self.tran=[random.uniform(-.01,.05),0.0,0.0,0.0,0.03]
        self.info=[random.uniform(-.01,.05),0.0,0.0,0.0,0.04]
        self.fir=[random.uniform(-.01,.05),0.0,0.0,0.0,0.06]
        self.pro=[random.uniform(-.01,.05),0.0,0.0,0.0,0.05]
        self.ehc=[random.uniform(-.01,.05),0.0,0.0,0.0,0.02]
        self.art=[random.uniform(-.01,.05),0.0,0.0,0.0,0.07]
        self.oth=[random.uniform(-.01,.05),0.0,0.0,0.0,0.04]
        self.gov=[random.uniform(-.01,.05),0.0,0.0,0.0,0.0]
        self._gdp_all=[self.ag,self.mi,self.ut,self.con,self.man,self.whol,
                       self.ret,self.tran,self.info,self.fir,self.pro,self.ehc,
                       self.art,self.oth,self.gov]
        self._all_sectors=[[self.ag[0]],[self.mi[0]],[self.ut[0]],[self.con[0]],
            [self.man[0]],[self.whol[0]],[self.ret[0]],[self.tran[0]],[self.info[0]],
            [self.fir[0]],[self.pro[0]],[self.ehc[0]],[self.art[0]],[self.oth[0]],
            [self.gov[0]]]
        gdp=multiply_matrix([self._gdp_ratio],self._all_sectors)
        self.gdp=gdp[0][0]
    
    def gdp_change(self,inte,infl):
        for x in self._gdp_all:
            gj=random.uniform(-.5,.5)+(.01-inte)+(.02-infl)
            if x[1]>0.0:
                gj=gj-x[1]
            if x[1]<0.0:
                gj=gj-x[1]
            ga=x[2]
            gv=x[1]
            g=x[0]
            x[3]=gj
            x[2]=ga+.1*gj
            x[1]=.1*((.5*gj*gj)+ga)+gv
            x[0]=.1*((.33*gj*gj*gj)+(.5*ga*ga)+gv)+g
            if x[0]>=(x[4]+0.01):
                x[1]=x[1]-(x[0]-.05)
            if x[0]<=(.01-x[4]):
                x[1]=x[1]-(x[0]-.05)
            if x[0]>=.5:
                x[0]=0.25
                x[1]=-.1
                x[2]=-.1
                x[3]=-.1
            if x[0]<=-.25:
                x[1]=x[2]+.5
                x[2]=x[3]+.5
                x[3]=x[4]+.5
            if self.gdp>8:
                x[0]=x[0]-.01
            if self.gdp<-.4:
                x[0]=x[0]+.01
        self._all_sectors=[[self.ag[0]],[self.mi[0]],[self.ut[0]],[self.con[0]],
            [self.man[0]],[self.whol[0]],[self.ret[0]],[self.tran[0]],[self.info[0]],
            [self.fir[0]],[self.pro[0]],[self.ehc[0]],[self.art[0]],[self.oth[0]],
            [self.gov[0]]]
        for i in range(365):
            self._all_sectors=multiply_matrix(self.output,self._all_sectors)
        for x in range(len(self._gdp_all)):
            self._gdp_all[x][0]=self._all_sectors[x][0]
        gdp=multiply_matrix([self._gdp_ratio],self._all_sectors)
        self.gdp=gdp[0][0]
        #print self.gdp


class Interestrate(object):
    """Attributes:
    interestrate: 1/3a^3+1/2b^2+c+d
    interestrate velocity: 1/2a^2+b+c
    interestrate acceleration: a+b
    interestrate jerk: a [random number]
    
    a is the only random number, b is the acceleration from the last turn, \
    c is the velocity from the last turn, and d is the interestrate from \
    the last turn."""
    
    def __init__(self,interestrate,iv,ia,ij):
        self.interestrate=interestrate
        self.iv=iv
        self.ia=ia
        self.ij=ij
    
    def interestrate_change(self):
        ij=interestrate_randomization()
        if self.iv>0.0:
            ij=ij-self.iv
        if self.iv<0.0:
            ij=ij-self.iv
        ia=self.ia
        iv=self.iv
        i=self.interestrate
        self.ij=ij
        self.ia=ia+.1*ij
        self.iv=.1*((.5*ij*ij)+ia)+iv
        x=.1*((.33*ij*ij*ij)+(.5*ia*ia)+iv)+i
        if x>=0:
            self.interestrate=x
        else:
            self.interestrate=0.0
        if x>=0.05:
            self.iv=self.iv-(x-.05)
    

class Inflation(object):
    """Attributes:
    inflation: 1/3a^3+1/2b^2+c+d
    inflation velocity: 1/2a^2+b+c
    inflation acceleration: a+b
    inflation jerk: a [random number]
    
    a is the only random number, b is the acceleration from the last turn, \
    c is the velocity from the last turn, and d is the inflation from \
    the last turn."""
    
    def __init__(self,inflation,iv,ia,ij):
        self.inflation=inflation
        self.iv=iv
        self.ia=ia
        self.ij=ij
    
    def inflation_change(self):
        ij=interestrate_randomization()
        if self.iv>0.0:
            ij=ij-self.iv
        if self.iv<0.0:
            ij=ij-self.iv
        ia=self.ia
        iv=self.iv
        i=self.inflation
        self.ij=ij
        self.ia=ia+.1*ij
        self.iv=.1*((.5*ij*ij)+ia)+iv
        x=.1*((.33*ij*ij*ij)+(.5*ia*ia)+iv)+i
        if x>=0:
            self.inflation=x
        else:
            self.inflation=0.0
        if x>=0.05:
            self.iv=self.iv-(x-.07)

class Bond_Yields(object):
    """Representation of the yield for bonds
    
    instance attributes:
        t_bill: yield data for t bills [list]
        corp: yield data for corporate bonds [list]
        junk: yield data for junk bonds [list]
        all: the list of instance attributes [list]
    
    instance attribute characteristics:
        yields: 1/3a^3+1/2b^2+c+d
        yields velocity: 1/2a^2+b+c
        yields acceleration: a+b
        yields jerk: a [random number]
    
    all values are stored in lists, where the first value is _real_yields,
    the second is yields, the third is velocity, the fourth is acceleration,
    and the fifth is jerk.
    
    jerk is the same as for interest rates, but the yield has the added influence
    of a random number."""
    allids=['T Bill', 'Corporate', 'Junk']
    
    def __init__(self,t_bill, corp,junk):
        t_bill_price=1000*(1.0/(1.0+t_bill))**10
        self.t_bill=[t_bill,t_bill,0.0,0.0,0.0,0.05,t_bill_price]
        corp_price=1000*(1.0/(1.0+corp))**5
        self.corp=[corp,corp,0.0,0.0,0.0,0.1,corp_price]
        junk_price=1000*(1.0/(1.0+junk))**10
        self.junk=[junk,junk,0.0,0.0,0.0,0.15,junk_price]
        self.all=[self.t_bill,self.corp,self.junk]
    
    def yield_change(self,j,inte,infl,gdp):
        for x in self.all:
            yj=j
            if x[2]>0.0:
                yj=yj-x[2]
            if x[2]<0.0:
                yj=yj-x[2]
            ya=x[3]
            yv=x[2]
            y=x[0]
            x[4]=yj
            x[3]=ya+.1*yj
            x[2]=.1*((.5*yj*yj)+ya)+yv
            z=.1*((.33*yj*yj*yj)+(.5*ya*ya)+yv)+y
            if z>=0:
                x[0]=z
            else:
                x[0]=0.0
            if z>=x[5]:
                x[2]=x[2]-(z-.05)
            x[1]=x[0]+random.uniform(-.004,.004)+infl
        self.t_bill[6]=1000*(1.0/(1.0+self.t_bill[1]))**10
        self.corp[6]=1000*(1.0/(1.0+self.corp[1]))**5
        self.junk[6]=1000*(1.0/(1.0+self.junk[1]))**10
        corprisk=math.fabs(1-math.pow((1+inte)/(1+self.corp[1]),1.0/5))
        self.corprisk=math.fabs(corprisk-(.02-gdp))
        junkrisk=math.fabs(1-math.pow((1+inte)/(1+self.junk[1]),1.0/10))
        self.junkrisk=math.fabs(junkrisk-(.02-gdp))
    
    def get_t_bill(self):
        return self.t_bill[1]
    
    def get_t_bill_price(self):
        return self.t_bill[6]
    
    def get_corp(self):
        return self.corp[1]
    
    def get_corp_price(self):
        return self.corp[6]
    
    def get_junk(self):
        return self.junk[1]
    
    def get_junk_price(self):
        return self.junk[6]


class CDO_Yield(object):
    """Representation of the yield for treasury bonds
    
    instance attributes:
        yields: 1/3a^3+1/2b^2+c+d
        yields velocity: 1/2a^2+b+c
        yields acceleration: a+b
        yields jerk: a [random number]
    
    jerk is the same as for interest rates, but the yield has the added influence
    of a random number."""
    
    def __init__(self,yields,yv,ya,yj,realyields,inte):
        self.yields=yields
        self.yv=yv
        self.ya=ya
        self.yj=yj
        self._real_yields=realyields
        self._cdo_price=10000*(1.0/(1.0+self.yields))**30
        self.cdorisk=math.fabs(1-math.pow((1+inte)/(1+yields),1.0/30))
    
    def yield_change(self,ij,inte,infl,gdp):
        yj=ij
        if self.yv>0.0:
            yj=yj-self.yv
        if self.yv<0.0:
            yj=yj-self.yv
        ya=self.ya
        yv=self.yv
        y=self._real_yields
        self.yj=yj
        self.ya=ya+.1*yj
        self.yv=.1*((.5*yj*yj)+ya)+yv
        x=.1*((.33*yj*yj*yj)+(.5*ya*ya)+yv)+y
        if x>=0:
            self._real_yields=x
        else:
            self._real_yields=0.0
        if x>=0.05:
            self.yv=self.yv-(x-.1)
        self.yields=self._real_yields+random.uniform(-.005,.005)+infl
        self._cdo_price=10000*(1.0/(1.0+self.yields))**30
        cdorisk=math.fabs(1-math.pow((1+inte)/(1+self.yields),1.0/30))
        self.cdorisk=math.fabs(cdorisk-(.02-gdp))


class Stock_Market(object):
    """Represents the current state of the stock market, including the value
    of all stocks, their current trajectories, dividends, past data, and a stock
    market index. It includes the stocks with the following ids:
    Instance invariants:
        [oe,ae,ys,ei,mm,pb,sy,hz,io,bp,pp,ml,hm] [each one is a list]
        
        each stock is represented as a list in the following format:
        [value, real_value, velocity, acceleration, jerk,industry_data, dividend,
        past_data,calls,puts,shorts]
        
        calls=[[strike price,premium](for one year maturity),[strike price,
        premium](for two year maturity),[strike price,premium](for five year
        maturity)]"""
    _oe_industry_data=[0,0,0,0,.1,0,.2,0,.4,.1,.1,0,.1,0,0] #orange inc (apple)
    _ae_industry_data=[0,0,1.0,0,0,0,0,0,0,0,0,0,0,0,0] #american electric
    _ys_industry_data=[0,0,0,0,0,0,0,0,0.4,0.1,0.1,0,.4,0,0] #yourspace (facebook)
    _ei_industry_data=[.1,.3,.3,.1,0,0,0,.1,0,.1,0,0,0,0,0] #enron immobile
    _mm_industry_data=[0,0,0,0,.6,0,.1,.1,0,.2,0,0,0,0,0] #major motors (GM)
    _pb_industry_data=[0,0,0,0,0,0,0,0,.1,.8,.1,0,0,0,0] #people's bank (BAC)
    _sy_industry_data=[0,0,0,0,0,0,.9,0,0,.1,0,0,0,0,0] #stacy's (macy's)
    _hz_industry_data=[0,0,.9,0,0,0,0,0,.1,0,0,0,0,0,0] #Horizon (verizon)
    _io_industry_data=[1.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #insanto (monsanto)
    _bp_industry_data=[.2,0,0,0,0,0,.8,0,0,0,0,0,0,0,0] #burger prince (McDonald's)
    _pp_industry_data=[0,0,0,0,0,0,0,0,0,0,0,0,1.0,0,0] #pelican publishing (penguin)
    _mc_industry_data=[0,0,.5,0,0,0,0,0,0,0,0,0,.5,0,0] #monocast (comcast)
    _hm_industry_data=[0,0,0,0,0,.3,.7,0,0,0,0,0,0,0,0] #hugemart (walmart)
    _gs_industry_data=[0,0,0,0,0,0,0,0,0,1.0,0,0,0,0,0] #goldfinger stacks (Goldman Sachs)
    _wp_industry_data=[0,0,0,0,0,0,0,0,.3,0,0,0,.7,0,0] #wepick (Netflix)
    _fs_industry_data=[0,0,0,0,.8,0,0,.1,0,0,0,0,0,0,.1] #formerly known as american steel (US Steel)
    _dl_industry_data=[0,0,0,0,0,0,0,0,.5,.1,.1,.1,.1,.1,0]
    _dr_industry_data=[0,1.0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    _it_industry_data=[0,0,0,0,0,0,0,.1,0,0,0,0,0,.1,.8]
    _bc_industry_data=[0,0,0,0,0,0,0,0,0,.1,.7,0.1,0,0,.1]
    allids=['oe','ae','ys','ei','mm','pb','sy','hz','io','bp','pp','mc','hm','gs',
            'wp','fs','dl','dr','it','bc']
    
    def __init__(self):
        x=random.uniform(1.0,100.0)
        self.oe=[x,x,0,0,0,self._oe_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.ae=[x,x,0,0,0,self._ae_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.ys=[x,x,0,0,0,self._ys_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.ei=[x,x,0,0,0,self._ei_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.mm=[x,x,0,0,0,self._mm_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.pb=[x,x,0,0,0,self._pb_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.sy=[x,x,0,0,0,self._sy_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.hz=[x,x,0,0,0,self._hz_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.io=[x,x,0,0,0,self._io_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.bp=[x,x,0,0,0,self._bp_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.pp=[x,x,0,0,0,self._pp_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.mc=[x,x,0,0,0,self._mc_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.hm=[x,x,0,0,0,self._hm_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.gs=[x,x,0,0,0,self._gs_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.wp=[x,x,0,0,0,self._wp_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.fs=[x,x,0,0,0,self._fs_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.dl=[x,x,0,0,0,self._dl_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.dr=[x,x,0,0,0,self._dr_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.it=[x,x,0,0,0,self._it_industry_data,0,[],[[]],[[]],[[]]]
        x=random.uniform(1.0,100.0)
        self.bc=[x,x,0,0,0,self._bc_industry_data,0,[],[[]],[[]],[[]]]
        self.all_stocks=[self.oe,self.ae,self.ys,self.ei,self.mm,self.pb,self.sy,
                         self.hz,self.io,self.bp,self.pp,self.mc,self.hm,self.gs,
                         self.wp,self.fs,self.dl,self.dr,self.it,self.bc]
        total=[]
        for x in self.all_stocks:
            total=total+[x[0]]
        self.index=[100.0]+total
        self.split=[]
    def stock_market_change(self, gdp,inte):
        split=[]
        for x in self.all_stocks:
            if len(x[7])<10:
                x[7]=x[7]+[x[0]]
            else:
                x[7]=x[7][1:]+[x[0]]
                ave=sum(x[7])/10
                new=0
                for y in x[7]:
                    new=new+math.fabs(y-ave)/ave
                if new<.5:
                    x[6]=x[0]*(.05-(new/10))
            j=random.uniform(-0.2,0.2)
            if x[2]>0.0:
                j=j-x[2]
            if x[2]<0.0:
                j=j-x[2]
            a=x[3]
            v=x[2]
            x[4]=j
            x[3]=a+.1*j
            x[2]=.1*((.5*j*j)+a)+v
            z1=.1*((.33*j*j*j)+(.5*a*a)+v)
            z2=multiply_matrix([x[5]],gdp._all_sectors)
            z=z1+z2[0][0]
            x[1]=x[1]*(1.0+z)
            if x[1]<=0.0:
                x[1]=0.0
            x[0]=x[1]*(1.0+random.uniform(-.03,.03))
            if x[0]>600:
                x[0]=x[0]*.05
                x[1]=x[1]*.05
                split=split+[self.allids[self.all_stocks.index(x)]]
            call1=call_finder(x[0],x[7],1)
            if call1>x[0]:
                call2=call_finder(x[0],x[7],2)
                call5=call_finder(x[0],x[7],5)
            else:
                call1=x[0]*(1+inte)
                call2=x[0]*((1+inte)**2)
                call5=x[0]*((1+inte)**5)
            put1=put_finder(x[0],x[7],1)
            if put1<x[0]:
                put2=put_finder(x[0],x[7],2)
                put5=put_finder(x[0],x[7],5)
            else:
                put1=x[0]*(1.0/(1+inte/2))
                put2=x[0]*(1.0/((1+inte/2)**2))
                put5=x[0]*(1.0/((1+inte/2)**5))
            pre1=(.005+inte/2)*x[0]
            pre2=(((1.005+inte/2)**2)-1)*x[0]
            pre5=(((1.005+inte/2)**5)-1)*x[0]
            x[8]=[[call1,pre1],[call2,pre2],[call5,pre5]]
            x[9]=[[put1,pre1],[put2,pre2],[put5,pre5]]
            x[10]=[[x[0],0.0],[x[0],0.0],[x[0],0.0]]
        self.all_stocks=[self.oe,self.ae,self.ys,self.ei,self.mm,self.pb,self.sy,
                         self.hz,self.io,self.bp,self.pp,self.mc,self.hm,self.gs,
                         self.wp,self.fs,self.dl,self.dr,self.it,self.bc]
        net=0
        for i in range(len(self.all_stocks)):
            net=net+self.all_stocks[i][0]/self.index[i+1]
        self.index[0]=net*100.0
        self.split=split
    
    def get_price(self, title):
        pos=self.allids.index(title)
        return self.all_stocks[pos][0]
    
    def get_div(self, title):
        pos=self.allids.index(title)
        return self.all_stocks[pos][6]
    
    def get_option(self, title, opt,length):
        pos=self.allids.index(title)
        if opt=='call':
            if length=='1':
                return self.all_stocks[pos][8][0][:]
            if length=='2':
                return self.all_stocks[pos][8][1][:]
            if length=='5':
                return self.all_stocks[pos][8][2][:]
        if opt=='put':
            if length=='1':
                return self.all_stocks[pos][9][0][:]
            if length=='2':
                return self.all_stocks[pos][9][1][:]
            if length=='5':
                return self.all_stocks[pos][9][2][:]
        if opt=='short':
            if length=='1':
                return self.all_stocks[pos][10][0][:]
            if length=='2':
                return self.all_stocks[pos][10][1][:]
            if length=='5':
                return self.all_stocks[pos][10][2][:]
    def print_option(self,title,opt):
        pos=self.allids.index(title)
        if opt=='call':
            x=self.all_stocks[pos][8]
        if opt=='put':
            x=self.all_stocks[pos][9]
        if opt=='short':
            x=self.all_stocks[pos][10]
        print opt+'s for '+title+':'
        print '1 year   strike price:'+str(x[0][0])+' premium: '+str(x[0][1])
        print '2 years   strike price:'+str(x[1][0])+' premium: '+str(x[1][1])
        print '5 years   strike price:'+str(x[2][0])+' premium: '+str(x[2][1])
    

class Economy(object):
    """Represents the state of the world economy.
    
    Instance Attributes:
        interestrate: The annual nominal interest rate [float >=0.0]
        inflation: The annual rate of inflation [float >=0.0]"""
        
    
    def __init__(self, gdp, inte, infl,bonds,cdo,stocks):
        self.gdpgrowth=gdp
        self.interestrate=inte
        self.inflation=infl
        self.bonds=bonds
        self.cdo=cdo
        self.stockmarket=stocks
    
    def __str__(self):
        """Readable string representation of the world economy."""
        print 'Annualized real GDP growth: '+`self.get_gdp()`
        x=self.gdpgrowth
        for i in range(len(x._all_sectors)):
            print x.sector_ids[i]+': '+str(x._all_sectors[i])
        print
        print 'The nominal interestrate: '+`self.get_inte()`
        return 'The inflation rate: '+`self.get_infl()`

    
    def __repr__(self):
        print 'Annualized real GDP growth: '+`self.get_gdp()`
        for i in range(len(x._all_sectors)):
            print x.sector_ids[i]+': '+str(x._all_sectors[i]) 
        print
        print 'The nominal interestrate: '+`self.get_inte()`
        return 'The inflation rate: '+`self.get_infl()`
    
    def print_stockmarket(self):
        for i in range(len(self.stockmarket.all_stocks)):
            x=round(self.stockmarket.all_stocks[i][0],2)
            y=self.stockmarket.allids[i]
            z=[]
            for a in self.stockmarket.all_stocks[i][7]:
                z=z+[round(a,2)]
            w=round(self.stockmarket.all_stocks[i][6],2)
            print str(y)+' price: '+str(x)+' dividend: '+str(w)
            print 'past prices: '+str(z)
            print
    
    def print_bonds(self):
        for i in range(len(self.bonds.all)):
            x=self.bonds.all[i][1]
            y=self.bonds.allids[i]
            z=self.bonds.all[i][6]
            print str(y)+' yield: '+str(x)+' price: '+str(z)
    
    def print_securities(self):
        x=self.get_cdoy()
        y=self.get_cdop()
        print 'CDO yield: '+str(x)+' price: '+str(y)
        
    def update(self):
        self.interestrate.interestrate_change()
        self.inflation.inflation_change()
        self.gdpgrowth.gdp_change(self.interestrate.interestrate,self.inflation.inflation)
        self.bonds.yield_change(self.interestrate.ij,self.get_inte(),
                                self.get_infl(),self.get_gdp())
        self.cdo.yield_change(self.interestrate.ij,self.get_inte(),self.get_infl(),
                              self.get_gdp())
        self.stockmarket.stock_market_change(self.gdpgrowth,self.interestrate.interestrate)
    
    def get_gdp(self):
        return self.gdpgrowth.gdp
    
    def get_inte(self):
        return self.interestrate.interestrate+self.inflation.inflation
    
    def get_infl(self):
        return self.inflation.inflation
    
    def get_tby(self):
        return self.bonds.get_t_bill()
    
    def get_tbp(self):
        return self.bonds.get_t_bill_price()
    
    def get_corpy(self):
        return self.bonds.get_corp()
    
    def get_corpp(self):
        return self.bonds.get_corp_price()
    
    def get_corpr(self):
        return self.bonds.corprisk
    
    def get_junky(self):
        return self.bonds.get_junk()
    
    def get_junkp(self):
        return self.bonds.get_junk_price()
    
    def get_junkr(self):
        return self.bonds.junkrisk
    
    def get_cdoy(self):
        return self.cdo.yields
    
    def get_cdop(self):
        return self.cdo._cdo_price
    
    def get_cdor(self):
        return self.cdo.cdorisk
    
    
    