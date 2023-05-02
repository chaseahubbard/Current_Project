import pandas as pd
import matplotlib.pyplot as plt
import math
df = pd.read_excel("DJ Problem Set Data.xlsx", sheet_name='Room Inventory')
df2 = pd.read_excel("DJ Problem Set Data.xlsx", sheet_name='Fall Course Schedule')

offics = df.loc[df['Description'] == 'Office']
#print(offics)
count = 0
'''
for col in offics.columns:
   
    if count == 5:
        oplot = offics[col].mean()
        plt.figure()
        offics[col].plot(kind = 'hist')
        #print((offics['ASF'].sum())/(offics[col].sum()))
        df['ratio'] = df['ASF'] / df[col]
        #print(offics.loc[offics["ASF"] > 200])
        plt.show()
    count += 1

'''
'''
classroom = df.loc[((df['Description']=='Class') | (df['Description']=='Classroo') | (df['Description']=='Classroom')) ]
#print(classroom['Stations'].sum()) 
#print(classroom.loc[(classroom['Building']=='C')])
#print(df2)
gkk = df2.groupby(['Building',"Room"])
gk2 = df2.groupby(['Days','Begin Time'])
with pd.option_context('display.max_rows',None,'display.max_columns',None):
    print(df.sort_values(by='ratio'))
'''
df2['Room'] = df2['Room'].astype('str')



empty = df2.loc[((df2['Room']=='nan'))]
dict1 ={}
print(len(empty.index) * 300 * 4000)
print(df.loc[((df['Stations']>=200))])
building_c = (df.loc[(df['Building']=='C')])
#print(df.dtypes)
for col in building_c.columns:
    if count == 5:
        oneh = building_c.loc[(building_c[col] >=100) & (building_c[col] < 200)]
        twoh = building_c.loc[(building_c[col] >=200) & (building_c[col] < 300)]
        threeh = building_c.loc[(building_c[col] >=300) & (building_c[col] < 400)]
        fourh = building_c.loc[(building_c[col] >=400) & (building_c[col] < 500)]
        fiveh = building_c.loc[(building_c[col] >=500) & (building_c[col] < 600)]
        sixh = building_c.loc[(building_c[col] >=600) & (building_c[col] < 700)]
        sevenh = building_c.loc[(building_c[col] >=700) & (building_c[col] < 800)]
        eighth = building_c.loc[(building_c[col] >=800) & (building_c[col] < 900)]
        zeroh = building_c.loc[(building_c[col] >=0) & (building_c[col] < 100)]
        nineh = building_c.loc[(building_c[col] >=900) & (building_c[col] < 1000)]                               
    count += 1



total_asf = oneh['ASF'].sum() + twoh['ASF'].sum() + threeh['ASF'].sum() + fourh['ASF'].sum() + fiveh['ASF'].sum() +  sixh['ASF'].sum() + sevenh['ASF'].sum() +eighth['ASF'].sum() + nineh['ASF'].sum()
total_asf_list = [oneh['ASF'].sum(), twoh['ASF'].sum(), threeh['ASF'].sum() , fourh['ASF'].sum(), fiveh['ASF'].sum(), sixh['ASF'].sum(), sevenh['ASF'].sum(),eighth['ASF'].sum(), nineh['ASF'].sum()]
count2 = 0
print(zeroh['ASF'].sum() / total_asf)
for x in total_asf_list:
    count2 += 100
    ratio = x / total_asf
    print('For Building C Code {} has a value of {} and a ratio of {}'.format(count2, x, ratio))
  
print(total_asf)
#dfmerge = pd.merge(df,df2,on=['Room','Building'], how='inner')

count = 0
building_b = (df.loc[(df['Building']=='B')])
#print(df.dtypes)
for col in building_b.columns:

    if count == 5:
        onehb = building_b.loc[(building_b[col] >=100) & (building_b[col] < 200)]
        twohb = building_b.loc[(building_b[col] >=200) & (building_b[col] < 300)]
        threehb = building_b.loc[(building_b[col] >=300) & (building_b[col] < 400)]
        fourhb = building_b.loc[(building_b[col] >=400) & (building_b[col] < 500)]
        fivehb = building_b.loc[(building_b[col] >=500) & (building_b[col] < 600)]
        sixhb = building_b.loc[(building_b[col] >=600) & (building_b[col] < 700)]
        sevenhb = building_b.loc[(building_b[col] >=700) & (building_b[col] < 800)]
        eighthb = building_b.loc[(building_b[col] >=800) & (building_b[col] < 900)]
        zerohb = building_b.loc[(building_b[col] >=0) & (building_b[col] < 100)]
        ninehb = building_b.loc[(building_b[col] >=900) & (building_b[col] < 1000)]                               
    count += 1



total_asfb = onehb['ASF'].sum() + twohb['ASF'].sum() + threehb['ASF'].sum() + fourhb['ASF'].sum() + fivehb['ASF'].sum() +  sixhb['ASF'].sum() + sevenhb['ASF'].sum() +eighthb['ASF'].sum() + ninehb['ASF'].sum()
total_asf_listb = [onehb['ASF'].sum(), twohb['ASF'].sum(), threehb['ASF'].sum() , fourhb['ASF'].sum(), fivehb['ASF'].sum(), sixhb['ASF'].sum(), sevenhb['ASF'].sum(),eighthb['ASF'].sum(), ninehb['ASF'].sum()]
count2 = 0
print(zerohb['ASF'].sum() / total_asfb)
for x in total_asf_listb:
    count2 += 100
    ratio = x / total_asfb
    print('For Building B Code {} has a value of {} and a ratio of {}'.format(count2, x, ratio))
  
print(total_asfb)

count = 0

building_a = (df.loc[(df['Building']=='A')])
#print(df.dtypes)
for col in building_a.columns:
    if count == 5:
        oneha = building_a.loc[(building_a[col] >=100) & (building_a[col] < 200)]
        twoha = building_a.loc[(building_a[col] >=200) & (building_a[col] < 300)]
        threeha = building_a.loc[(building_a[col] >=300) & (building_a[col] < 400)]
        fourha = building_a.loc[(building_a[col] >=400) & (building_a[col] < 500)]
        fiveha = building_a.loc[(building_a[col] >=500) & (building_a[col] < 600)]
        sixha = building_a.loc[(building_a[col] >=600) & (building_a[col] < 700)]
        sevenha = building_a.loc[(building_a[col] >=700) & (building_a[col] < 800)]
        eightha = building_a.loc[(building_a[col] >=800) & (building_a[col] < 900)]
        zeroha = building_a.loc[(building_a[col] >=0) & (building_a[col] < 100)]
        nineha = building_a.loc[(building_a[col] >=900) & (building_a[col] < 1000)]                               
    count += 1



total_asfa = oneha['ASF'].sum() + twoha['ASF'].sum() + threeha['ASF'].sum() + fourha['ASF'].sum() + fiveha['ASF'].sum() +  sixha['ASF'].sum() + sevenha['ASF'].sum() +eightha['ASF'].sum() + nineha['ASF'].sum()
total_asf_lista = [oneha['ASF'].sum(), twoha['ASF'].sum(), threeha['ASF'].sum() , fourha['ASF'].sum(), fiveha['ASF'].sum(), sixha['ASF'].sum(), sevenha['ASF'].sum(),eightha['ASF'].sum(), nineha['ASF'].sum()]
count2 = 0
print(zeroha['ASF'].sum() / total_asfa)
for x in total_asf_lista:
    count2 += 100
    ratio = x / total_asfa
    print('For Building A Code {} has a value of {} and a ratio of {}'.format(count2, x, ratio))
  
print(total_asfa)

count = 0

building_d = (df.loc[(df['Building']=='D')])
#print(df.dtypes)
for col in building_d.columns:
    if count == 5:
        onehd = building_d.loc[(building_d[col] >=100) & (building_d[col] < 200)]
        twohd = building_d.loc[(building_d[col] >=200) & (building_d[col] < 300)]
        threehd = building_d.loc[(building_d[col] >=300) & (building_d[col] < 400)]
        fourhd = building_d.loc[(building_d[col] >=400) & (building_d[col] < 500)]
        fivehd = building_d.loc[(building_d[col] >=500) & (building_d[col] < 600)]
        sixhd = building_d.loc[(building_d[col] >=600) & (building_d[col] < 700)]
        sevenhd = building_d.loc[(building_d[col] >=700) & (building_d[col] < 800)]
        eighthd = building_d.loc[(building_d[col] >=800) & (building_d[col] < 900)]
        zerohd = building_d.loc[(building_d[col] >=0) & (building_d[col] < 100)]
        ninehd = building_d.loc[(building_d[col] >=900) & (building_d[col] < 1000)]                               
    count += 1



total_asfd = onehd['ASF'].sum() + twohd['ASF'].sum() + threehd['ASF'].sum() + fourhd['ASF'].sum() + fivehd['ASF'].sum() +  sixhd['ASF'].sum() + sevenhd['ASF'].sum() +eighthd['ASF'].sum() + ninehd['ASF'].sum()
total_asf_listd = [onehd['ASF'].sum(), twohd['ASF'].sum(), threehd['ASF'].sum() , fourhd['ASF'].sum(), fivehd['ASF'].sum(), sixhd['ASF'].sum(), sevenhd['ASF'].sum(),eighthd['ASF'].sum(), ninehd['ASF'].sum()]
count2 = 0

print(zerohd['ASF'].sum() / total_asfd)
for x in total_asf_listd:
    count2 += 100
    ratio = x / total_asfd
    print('For Building D Code {} has a value of {} and a ratio of {}'.format(count2, x, ratio))
  
print(total_asfd)

count = 0


building_f = (df.loc[(df['Building']=='F')])
#print(df.dtypes)
for col in building_f.columns:
    if count == 5:
        onehf = building_f.loc[(building_f[col] >=100) & (building_f[col] < 200)]
        twohf = building_f.loc[(building_f[col] >=200) & (building_f[col] < 300)]
        threehf = building_f.loc[(building_f[col] >=300) & (building_f[col] < 400)]
        fourhf = building_f.loc[(building_f[col] >=400) & (building_f[col] < 500)]
        fivehf = building_f.loc[(building_f[col] >=500) & (building_f[col] < 600)]
        sixhf = building_f.loc[(building_f[col] >=600) & (building_f[col] < 700)]
        sevenhf = building_f.loc[(building_f[col] >=700) & (building_f[col] < 800)]
        eighthf = building_f.loc[(building_f[col] >=800) & (building_f[col] < 900)]
        zerohf = building_f.loc[(building_f[col] >=0) & (building_f[col] < 100)]
        ninehf = building_f.loc[(building_f[col] >=900) & (building_f[col] < 1000)]                               
    count += 1



total_asff = onehf['ASF'].sum() + twohf['ASF'].sum() + threehf['ASF'].sum() + fourhf['ASF'].sum() + fivehf['ASF'].sum() +  sixhf['ASF'].sum() + sevenhf['ASF'].sum() +eighthf['ASF'].sum() + ninehf['ASF'].sum()
total_asf_listf = [onehf['ASF'].sum(), twohf['ASF'].sum(), threehf['ASF'].sum() , fourhf['ASF'].sum(), fivehf['ASF'].sum(), sixhf['ASF'].sum(), sevenhf['ASF'].sum(),eighthf['ASF'].sum(), ninehf['ASF'].sum()]
count2 = 0
print(zerohf['ASF'].sum() / total_asff)
for x in total_asf_listf:
    count2 += 100
    ratio = x / total_asff
    print('For Building F Code {} has a value of {} and a ratio of {}'.format(count2, x, ratio))
  
print(total_asff)

#print(dfmerge)
number_of_classes = (40/1.5)/3
number_of_classes = math.ceil(number_of_classes)
thirty_hours = 250 / number_of_classes #28 students for 40 hours of classroom use

#14 hours and 30 minutes
print(thirty_hours)
print(number_of_classes)


unassigned_classes = df2.loc[((df2['Room'])=='nan')]
print(unassigned_classes.count())

# increase of un-credited space is 0.44471

#Need to find the average prices of the rooms by the amount of people that are in the rooms 


#Okay I already found the percentage price for each room but they are not ordered
count = 0
for col in df:
    if count == 5:
        some = df.loc[(df[col]>=100) & (df[col] < 200)] 
    count += 1 
some["Price_per_station"] = some['ASF'] / some['Stations']
some2 = some.loc[some['Price_per_station'] < 99999999]
print(some2.first)
#some2.plot.hist(x = 'Stations', y = 'ASF', rot = 0)
#plt.show()
gra = some2.groupby(['Stations'])['Price_per_station'].mean()
gra2 = some2.groupby(['Stations'])['Price_per_station'].count()
print(gra)
print(gra2)

#look at 36 seems the best value 22.730556

#this would be 22.7 * 36
best_cost = 22.730556 * 36 
#use this one for all of them
b_c_extra = best_cost * 0.44471
b_result = (best_cost + b_c_extra) * 300
print(b_result * 17) #about 6,029,251

#look to renivate the poor performing ones should focus on building c.
