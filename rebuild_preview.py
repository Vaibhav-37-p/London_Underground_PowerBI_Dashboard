from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'axes.labelcolor':'#41556d','xtick.color':'#41556d','ytick.color':'#41556d','text.color':'#102f50','axes.titleweight':'bold'})
BLUE='#2467a2'; LIGHT='#89b6df'; TEAL='#169c9a'; BG='#eff5fb'
def canvas(title,subtitle):
 f=plt.figure(figsize=(16,10),facecolor=BG)
 f.text(.045,.94,title,fontsize=27,weight='bold')
 f.text(.045,.906,subtitle,fontsize=11,color='#41556d')
 return f
def cards(f,items):
 for i,(label,value,detail) in enumerate(items):
  x=.045+i*.235
  f.patches.append(FancyBboxPatch((x,.76),.218,.112,boxstyle='round,pad=0.009',transform=f.transFigure,facecolor='white',edgecolor='#d5e2f1',zorder=-1))
  f.text(x+.01,.84,label,fontsize=10,weight='bold')
  f.text(x+.01,.795,value,fontsize=25,weight='bold')
  f.text(x+.01,.772,detail,fontsize=8,color='#526b86')
def panel(f,pos,title):
 a=f.add_axes(pos,facecolor='white');a.set_title(title,loc='left',pad=16,fontsize=13);a.grid(axis='x',alpha=.12);a.set_axisbelow(True);return a
def bars(a,s,color=BLUE,million=True):
 s=s.sort_values(); vals=s.values/(1e6 if million else 1)
 a.barh(s.index.astype(str),vals,color=color,height=.6);a.set_xlim(0,max(vals)*1.22)
 for i,v in enumerate(vals):a.text(v+max(vals)*.025,i,f'{v:,.2f}M' if million else f'{v:,.0f}',va='center',fontsize=9)
 a.tick_params(axis='y',length=0);a.xaxis.set_major_formatter(FuncFormatter(lambda v,p:f'{v:g}'+('M' if million else '')))
def save(f,name):
 f.savefig(ROOT/(name+'.png'),dpi=125,facecolor=f.get_facecolor())
 f.savefig(ROOT/(name+'.pdf'),facecolor=f.get_facecolor())
 plt.close(f)

# Original workbooks control the results; the combined CSV mixes modes at interchanges.
hist=[]
for year in range(2007,2018):
 raw=pd.read_excel(ROOT/'multi-year-station-entry-and-exit-figures.xls',sheet_name=f'{year} Entry & Exit',header=None)
 ids=pd.to_numeric(raw.iloc[:,0],errors='coerce')
 values=pd.to_numeric(raw.iloc[:,-1],errors='coerce')
 valid=ids.notna() & values.notna()
 assert not ids[valid].duplicated().any()
 hist.append({'year':year,'entries_exits':float(values[valid].sum()*1e6),'station_rows':int(valid.sum())})
raw=pd.read_excel(ROOT/'AC2021_AnnualisedEntryExit.xlsx',sheet_name='Annualised',header=6)
lu=raw.loc[raw.Mode.eq('LU'),['NLC','Station','En/Ex']].copy()
lu['Station']=lu.Station.str.strip();assert len(lu)==270 and lu.NLC.is_unique
lu=lu.rename(columns={'En/Ex':'entries_exits'})
annual=pd.DataFrame(hist+[{'year':2021,'entries_exits':float(lu.entries_exits.sum()),'station_rows':len(lu)}])
annual.to_csv(ROOT/'verified_annual_totals.csv',index=False,float_format='%.6f')
rank=lu.sort_values('entries_exits',ascending=False);rank.to_csv(ROOT/'verified_2021_stations.csv',index=False,float_format='%.6f')
total=lu.entries_exits.sum();top=rank.iloc[0]
f=canvas('London Underground','Station entries & exits | Original annual-count workbooks | 2007–2017 and 2021')
cards(f,[('2021 annualised entries & exits',f'{total/1e9:.3f}B','LU mode only'),('Stations in 2021',str(len(lu)),'Distinct NLC station identifiers'),('Busiest station in 2021',f'{top.entries_exits/1e6:.2f}M',top.Station),('Historical coverage','12 years','2018–2020 omitted: source gap')])
a=panel(f,[.065,.29,.40,.39],'Annual station entries & exits')
series=annual.set_index('year').entries_exits.reindex(range(2007,2022))/1e9
a.grid(axis='y',alpha=.15);a.plot(series.index,series.values,color=BLUE,marker='o',lw=2.4)
a.set_ylim(0,3.5);a.set_xlim(2006.5,2021.7);a.set_xticks([2007,2009,2011,2013,2015,2017,2019,2021]);a.set_ylabel('Annualised entries + exits (billions)')
a.axvspan(2017.5,2020.5,color='#dfe7f0',alpha=.65);a.text(2019,1.8,'Source gap\n2018–2020',ha='center',fontsize=10,color='#526b86')
a.annotate(f'{series.loc[2021]:.3f}B',(2021,series.loc[2021]),xytext=(-10,15),textcoords='offset points',ha='center',weight='bold')
a=panel(f,[.66,.29,.285,.39],'Top 10 Underground stations | 2021')
bars(a,rank.head(10).set_index('Station').entries_exits)
f.text(.055,.205,'What the data shows',fontsize=13,weight='bold')
f.text(.055,.167,f"King’s Cross St Pancras leads with {top.entries_exits/1e6:.2f}M annualised entries and exits.\nStratford’s LU-only figure is {float(lu.loc[lu.NLC.eq(719),'entries_exits'].iloc[0])/1e6:.2f}M; counts from other rail modes are excluded.",fontsize=11,linespacing=1.6)
f.text(.055,.082,'Reading the figures: entries and exits are station movements, not unique passengers or journeys.\nAnnualisation methods and network coverage vary across years. Missing years are not treated as zero.',fontsize=10,color='#526b86',linespacing=1.5)
f.text(.055,.025,'Source: TfL annual-count workbooks in this repository. Static, reproducible preview; see README for definitions.',fontsize=8,color='#526b86')
save(f,'London_Underground_Dashboard')
print(json.dumps({'total_2021':total,'top_station':top.Station,'top_value':top.entries_exits,'years':hist},indent=2))
