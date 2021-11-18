# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:57:40 2021

@author: u0983512
"""


import pandas as pd
import os
import glob
import csv
import pickle

personal_drive = input('Enter root drive: ')
os.chdir('%s' %personal_drive)

question = input('Do yu want to erase the old med groups? (y/n) ')

if question == 'y':
    med_grps = [val for val in [os.path.basename(x)[:-4] for x in glob.glob('./saved_medgrps/*.pkl')]]
    for m in med_grps:
        os.remove('./saved_medgrps/%s.pkl' %(personal_drive,m))
elif question == 'n':
    print('Caution! You will be adding to the saved med groups if there are different entries than before!')
        
# <codecell> Create a function for documentation as the dataset is built
def doc(text1, text2, text3, file_t, file_c):
    print('%s,' %text1, '%s:' %text2, '%s' %text3)
    t = open(file_t, 'a', newline='')    
    print('%s,' %text1, '%s:' %text2, '%s' %text3, file = t)
    
    words =[]
    words.append(text1)
    words.append(text2)
    words.append(text3)
    with open(file_c, mode='a', newline='') as c:
        doc_writer = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        doc_writer.writerow(words)

# <codecell> Functions to organize medications depending of level of hierarchy
def group_by_hier1(common_name, df, inc_1, excl_2, excl_3, excl_4, excl_cat, table_name):    
    limited_meds = df.loc[df['catalog_hier1'].notna()]
    limited_meds = limited_meds.loc[(limited_meds['catalog_hier1'].str.contains(inc_1))]
    if excl_2 != 'none_2':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier2'].str.contains(excl_2, na=False))]
    if excl_3 != 'none_3':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier3'].str.contains(excl_3, na=False))]
    if excl_4 != 'none_4':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier4'].str.contains(excl_4, na=False))]
    if excl_cat != 'none_cat':
        limited_meds = limited_meds.loc[~(limited_meds['catalog'].str.contains(excl_cat, na=False))]
    limited_meds.drop_duplicates(inplace=True)

    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', limited_meds['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', limited_meds['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', limited_meds['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', limited_meds['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', limited_meds['catalog'].nunique(), file_t, file_c)
    print(limited_meds[['catalog']])
    
    pickle.dump(limited_meds, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))


def group_by_hier2(common_name, df, inc_2, excl_3, excl_4, excl_cat, table_name):    
    limited_meds = df.loc[df['catalog_hier2'].notna()]
    limited_meds = limited_meds.loc[(limited_meds['catalog_hier2'].str.contains(inc_2))]
    if excl_3 != 'none_3':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier3'].str.contains(excl_3, na=False))]
    if excl_4 != 'none_4':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier4'].str.contains(excl_4, na=False))]
    if excl_cat != 'none_cat':
        limited_meds = limited_meds.loc[~(limited_meds['catalog'].str.contains(excl_cat, na=False))]
    limited_meds.drop_duplicates(inplace=True)

    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', limited_meds['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', limited_meds['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', limited_meds['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', limited_meds['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', limited_meds['catalog'].nunique(), file_t, file_c)
    print(limited_meds[['catalog']])
    
    pickle.dump(limited_meds, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))    
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))


def group_by_hier3(common_name, df, inc_3, excl_4, excl_cat, table_name):    
    
    #common_name='ccb_nonrate'
    #inc_3 = 'calcium channel blockers|ca channel'
    #excl_4 = 'diltiazem|verapamil'
    #excl_cat = 'none_cat'
    
    limited_meds = df.loc[df['catalog_hier3'].notna()]
    limited_meds = limited_meds.loc[(limited_meds['catalog_hier3'].str.contains(inc_3))]
    if excl_4 != 'none_4':
        limited_meds = limited_meds.loc[~(limited_meds['catalog_hier4'].str.contains(excl_4, na=False))]
    if excl_cat != 'none_cat':
        limited_meds = limited_meds.loc[~(limited_meds['catalog'].str.contains(excl_cat, na=False))]
    limited_meds.drop_duplicates(inplace=True)

    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', limited_meds['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', limited_meds['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', limited_meds['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', limited_meds['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', limited_meds['catalog'].nunique(), file_t, file_c)
    print(limited_meds[['catalog']])
    
    pickle.dump(limited_meds, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))    
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))


def group_by_hier4(common_name, df, inc_4, excl_cat, table_name):    
    limited_meds = df.loc[df['catalog_hier4'].notna()]
    limited_meds = limited_meds.loc[(limited_meds['catalog_hier4'].str.contains(inc_4))]
    if excl_cat != 'none_cat':
        limited_meds = limited_meds.loc[~(limited_meds['catalog'].str.contains(excl_cat, na=False))]
    limited_meds.drop_duplicates(inplace=True)

    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', limited_meds['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', limited_meds['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', limited_meds['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', limited_meds['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', limited_meds['catalog'].nunique(), file_t, file_c)
    print(limited_meds[['catalog']])
    
    pickle.dump(limited_meds, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))    
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))


def group_by_cat(common_name, df, inc_cat, table_name):    
    limited_meds = df.loc[df['catalog'].notna()]
    limited_meds = limited_meds.loc[(limited_meds['catalog'].str.contains(inc_cat))]
    limited_meds.drop_duplicates(inplace=True)

    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', limited_meds['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', limited_meds['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', limited_meds['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', limited_meds['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', limited_meds['catalog'].nunique(), file_t, file_c)
    print(limited_meds[['catalog']])
    
    pickle.dump(limited_meds, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))    
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))


def group_by_list(df, hier3, group_name, extras, table_name):
    hier3 = 'thiazides and thiazide-like diuretics'
    group = df.loc[df['catalog_hier3'] == hier3]
    group = group[['catalog']]
    group.drop_duplicates(inplace=True)
    group.reset_index(inplace=True, drop=True)
    g_list = group.at[0,'catalog']
    group.drop(index=0, inplace=True)
    for g in group.itertuples(index=False):
        g_list = g_list + '|' + g[0]
    if extras != 'none_extras':
        g_list = g_list + '|' + extras
    group_by_cat(group_name, df, g_list, table_name)


def combine(group1, group2, common_name, table_name):    
    grp1 = pickle.load( open( './saved_medgrps/%s_table.pkl' %group1, 'rb' ) )
    grp2 = pickle.load( open( './saved_medgrps/%s_table.pkl' %group2, 'rb' ) )
    grp = grp1.merge(grp2, how = 'outer')
    
    doc(common_name, 'Number of unique level 1 rows in the hieracrchy', grp['catalog_hier1'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 2 rows in the hieracrchy', grp['catalog_hier2'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 3 rows in the hieracrchy', grp['catalog_hier3'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique level 4 rows in the hieracrchy', grp['catalog_hier4'].nunique(), file_t, file_c)
    doc(common_name, 'Number of unique catalog rows in the hieracrchy', grp['catalog'].nunique(), file_t, file_c)
    print('Combine, then remove original, for %s and %s' %(group1, group2))
    print(grp[['catalog']])

    pickle.dump(grp, open('./saved_medgrps/%s_table.pkl' %common_name, 'wb'))    
    os.remove('./saved_medgrps/%s_table.pkl' %group1)
    os.remove('./saved_medgrps/%s_table.pkl' %group2)
    os.remove('./saved_medgrps/%s_names.pkl' %group1)
    os.remove('./saved_medgrps/%s_names.pkl' %group2)
    rx_names = {common_name: table_name}
    pickle.dump(rx_names, open('./saved_medgrps/%s_names.pkl' %common_name, 'wb'))
        
# <codecell> Start off the documentation, pull in the reference data set
file_t = './documentation/medications_summary.txt'
t = open(file_t, 'w', newline='')
print('This doc provides a summary of the medication data', file = t)
t.close()

file_c = './documentation/medications_summary.csv'
with open(file_c, mode='w', newline='') as c:
    doc_writer = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    doc_writer.writerow(['Drug Group', 'Item', 'Value'])

df = pd.read_excel('./other_docs/CATALOG_HIER_e2.xlsx')
df = df.applymap(lambda s:s.lower() if type(s) == str else s)
df.columns = map(str.lower, df.columns)
df = df[['catalog', 'catalog_hier1', 'catalog_hier2', 'catalog_hier3', 'catalog_hier4']]
df.sort_values(by=['catalog_hier1', 'catalog_hier2', 'catalog_hier3', 'catalog_hier4', 'catalog'], inplace=True)
df.drop_duplicates(inplace=True)
# <codecell> Description of the raw data set
doc('All drugs', 'Number of unique rows in the hieracrchy', len(df), file_t, file_c)
doc('All drugs', 'Number of unique level 1 rows in the hieracrchy', df['catalog_hier1'].nunique(), file_t, file_c)
doc('All drugs', 'Number of unique level 2 rows in the hieracrchy', df['catalog_hier2'].nunique(), file_t, file_c)
doc('All drugs', 'Number of unique level 3 rows in the hieracrchy', df['catalog_hier3'].nunique(), file_t, file_c)
doc('All drugs', 'Number of unique level 4 rows in the hieracrchy', df['catalog_hier4'].nunique(), file_t, file_c)
doc('All drugs', 'Number of unique catalogs in the hieracrchy', df['catalog'].nunique(), file_t, file_c)

# <codecell>
group_by_hier2('rx_anticmv', df, 'cmv agents', 'none_3', 'none_4', 'none_cat', 'Cytomegalovirus')  
group_by_hier3('rx_antihepatitisb', df, 'hepatitis b agents', 'none_4', 'none_cat', 'Hepatitis B agents')  
group_by_hier3('rx_antihepatitisc', df, 'hepatitis c agents', 'none_4', 'none_cat', 'Hepatitis C agents')  
group_by_hier2('rx_herpes', df, 'herpes agents', 'none_3', 'none_4', 'none_cat', 'Herpes agents')  
group_by_hier2('rx_flu', df, 'influenza agents', 'none_3', 'none_4', 'none_cat', 'Influenza agents')
group_by_hier1('rx_antifungals', df, 'antifungals', 'none_2', 'none_3', 'none_4', 'none_cat', 'Antifungals')  
group_by_hier1('rx_antihistamines', df, 'antihistamines', 'none_2', 'none_3', 'none_4', 'nitroglycerin', 'Antihistamines')  
group_by_hier2('rx_carbapenems', df, 'carbapenems', 'none_3', 'none_4', 'none_cat', 'Carbapenems')  
group_by_hier1('rx_cephalosporins', df, 'cephalosporins', 'none_2', 'none_3', 'none_4', 'none_cat', 'Cephalosporins')
group_by_hier1('rx_macrolides', df, 'macrolides', 'none_2', 'none_3', 'none_4', 'none_cat', 'Macrolides')
group_by_hier1('rx_fluoroquinolones', df, 'fluoroquinolones', 'none_2', 'none_3', 'none_4', 'none_cat', 'Fluoroquinolones')
group_by_hier1('rx_penicillins', df, 'penicillins', 'none_2', 'none_3', 'none_4', 'none_cat', 'Penicillins')
group_by_hier1('rx_tetracyclines', df, 'tetracyclines', 'none_2', 'none_3', 'none_4', 'none_cat', 'Tetracyclines')

group_by_hier2('rx_stimulantsamphetamines', df, 'stimulants|amphetamines', 'none_3', 'none_4', 'simvastatin|metoprolol|docusate|pravastatin|glimepiride', 'Stimulants and amphetamines')
group_by_hier2('rx_obesity', df, 'anorexiants|anti-obesity', 'none_3', 'none_4', 'none_cat', 'Anorexiants and anti-obesity')  #naltrexone-bupropion hcl in catalog
group_by_hier1('rx_anticonvulsants', df, 'anticonvulsants', 'anticonvulsants - benzodiazepines', 'none_3', 'none_4', 'lisinopril', 'Anticonvulsants') #Need to separate seizure and other?
group_by_hier2('rx_ssri', df, 'ssris', 'none_3', 'none_4', 'none_cat', 'SSRI')  
group_by_hier2('rx_snri', df, 'snris', 'none_3', 'none_4', 'metoprolol', 'SNRI') #metop looks like a weird error  

group_by_hier2('rx_antirheumatic', df, 'antirheumatic', 'none_3', 'none_4', 'none_cat', 'Rheumatic agents')
group_by_hier2('rx_nsaid', df, 'nsaids|migraine products - nsaids', 'none_3', 'none_4', 'none_cat', 'NSAIDs') #naproxen-sumatriptan, sumatriptan-naproxen sodium

group_by_hier3('rx_migraine', df, 'migraine products|migraine combinations', 'none_4', 'lisinopril', 'Migraine agents')
group_by_hier1('rx_opioids', df, 'analgesics - opioid', 'none_2', 'none_3', 'none_4', 'none_cat', 'Opioids')
group_by_hier1('rx_androgens', df, 'androgens-anabolic', 'none_2', 'none_3', 'none_4', 'none_cat', 'Androgens')
group_by_hier1('rx_antacids', df, 'antacids', 'none_2', 'none_3', 'none_4', 'none_cat', 'Antacids, not PPI or H2 blockers')  
group_by_hier2('rx_benzo', df, 'benzodiazepines', 'none_3', 'none_4', 'albuterol|midazolam', 'Benzodiazepines')
group_by_hier1('rx_bronchodil', df, 'antiasthmatic and bronchodilator agents', 'monoclonal|xanthines', 'mixed adrenergics', 'none_4', 'isoproterenol', 'Antiasthmatic and bronchodilator agents')  

group_by_cat('rx_aspirin', df, '^aspirin$', 'Aspirin')
group_by_hier2('rx_nitrates', df, 'nitrates', 'none_3', 'none_4', 'amyl', 'Nitrates') #Includes IV
group_by_hier2('rx_warfarin', df, 'coumarin anticoagulants', 'none_3', 'none_4', 'none_cat', 'Warfarin')  
group_by_cat('rx_dabigatran', df, 'dabigatran', 'Dabigatran')
group_by_cat('rx_p2y12', df, 'prasugrel|clopidogrel|ticagrelor', 'P2Y12 inhibitors')
group_by_hier3('rx_thrombini', df, 'thrombin inhibitors - hirudin type', 'none_4', 'none_cat', 'Thrombin inhibitors, not dabigatran')
group_by_cat('rx_argatroban', df, 'argatroban', 'Argatroban')

group_by_hier2('rx_factorXa1', df, 'direct factor xa inhibitors', 'none_3', 'none_4', 'none_cat', 'Factor Xa inhibitors')  
group_by_cat('rx_edoxaban', df, 'edoxaban', 'Factor Xa inhibitors')
combine('rx_factorXa1', 'rx_edoxaban', 'rx_factorXa', 'Factor Xa inhibitors')

#Diabetes- one catalog item can be present in mutiple groups
group_by_cat('rx_metformin', df, 'metformin', 'Metformin')
group_by_hier3('rx_dp4', df, 'dipeptidyl peptidase-4', 'none_4', 'none_cat', 'DPP-4 inhibitors')

group_by_hier2('rx_glp11', df, 'glp-1', 'none_3', 'none_4', 'none_cat', 'GLP-1 antagonists1')  
group_by_list(df, 'incretin mimetic agents (glp-1 receptor agonists)', 'rx_glp12', 'none_extras', 'GLP-1 antagonists2')
combine('rx_glp11', 'rx_glp12', 'rx_glp1', 'GLP-1 antagonists')

group_by_hier3('rx_sulfonylurea', df, 'sulfonylurea', 'none_4', 'none_cat', 'Sulfonylurea')  
group_by_hier3('rx_thiazolidinedione', df, 'thiazolidinedione', 'none_4', 'none_cat', 'Thiazolidinedione')  
group_by_cat('rx_sglt2', df, 'gliflozin', 'SGLT2 inhibitors')  

group_by_hier2('rx_insulin1', df, 'insulin', 'none_3', 'none_4', 'pioglitazone|rosiglitazone|mecasermin', 'Insulin')
group_by_cat('rx_insulin2', df, 'insulin degludec-liraglutide|insulin glargine-lixisenatide', 'Insulin')
combine('rx_insulin1', 'rx_insulin2', 'rx_insulin', 'Insulin')

group_by_hier2('rx_h2blocker', df, 'h-2 antagonists', 'none_3', 'none_4', 'estropipate', 'H2 blockers')
group_by_hier2('rx_ppi', df, 'proton pump inhibitors', 'none_3', 'none_4', 'montelukast', 'Proton pump inhibitors')
group_by_hier1('rx_antiemetics', df, 'antiemetics', 'none_2', 'none_3', 'none_4', 'none_cat', 'Antiemetics')  # dextrose-fructose-sod citrate, fructose-dextrose-phosphor acd

#Lipids- one catalog item can be present in mutiple groups
group_by_hier2('rx_statin', df, 'hmg coa reductase inhibitors', 'none_3', 'none_4', 'none_cat', 'Statins')  
group_by_hier2('rx_fibrates', df, 'fibric acid derivatives', 'none_3', 'none_4', 'none_cat', 'Fibrates')  
group_by_hier2('rx_bileacid', df, 'bile acid sequestrants', 'none_3', 'none_4', 'none_cat', 'Bile acid sequestrants')  
group_by_hier2('rx_omega3', df, 'antihyperlipidemics - misc', 'none_3', 'none_4', 'none_cat', 'Omega-3 fatty acids')  
group_by_hier4('rx_ezetimibe', df, 'ezetimibe', 'none_cat', 'Ezetimibe')

group_by_hier2('rx_niacin1', df, 'nicotinic acid derivatives', 'none_3', 'none_4', 'none_cat', 'Niacin') #There are niacin entries combined with simva and lova
group_by_cat('rx_niacin2', df, 'lovastatin-niacin|niacin-simvastatin', 'Niacin')
combine('rx_niacin1', 'rx_niacin2', 'rx_niacin', 'Niacin')

#HTN- one catalog item can be present in mutiple groups
group_by_hier3('rx_acei', df, 'ace inhibitors', 'none_4', 'none_cat', 'ACE inhibitors')  
group_by_hier3('rx_arb', df, 'angiotensin ii receptor antagonists', 'none_4', 'none_cat', 'Angiotensin receptor blockers')
group_by_cat('rx_clonidine', df, 'clonidine', 'Clonidine') #get rid of ophthalmic?
group_by_cat('rx_mra', df, 'eplerenone|spironolactone', 'Mineralocorticoid receptor antagonists')
group_by_hier2('rx_Ksparingdiuretics', df, 'potassium sparing diuretics', 'none_3', 'none_4', 'eplerenone|spironolactone', 'Potassium sparing diuretics')  

group_by_hier2('rx_vasodilators', df, 'vasodilators', 'none_3', 'none_4', 'none_cat', 'Vasodilators, including PH')  #seperate out PH drugs?
group_by_hier2('rx_directrenin', df, 'direct renin inhibitors', 'none_3', 'none_4', 'none_cat', 'Direct renin inhibitors')  

group_by_hier2('rx_loopdiuretics1', df, 'loop diuretics', 'none_3', 'none_4', 'none_cat', 'Loop diuretics')  
group_by_list(df, 'loop diuretics', 'rx_loopdiuretics2', 'none_extras', 'Loop diuretics')
combine('rx_loopdiuretics1', 'rx_loopdiuretics2', 'rx_loopdiuretics', 'Loop diuretics')

group_by_hier3('rx_thiazide1', df, 'thiazide', 'none_4', 'none_cat', 'Thiazides')
group_by_list(df, 'thiazides and thiazide-like diuretics', 'rx_thiazide2', 'hctz', 'Thiazides')
combine('rx_thiazide1', 'rx_thiazide2', 'rx_thiazide', 'Thiazides')

group_by_hier2('rx_carbonic_anhydrase_i', df, 'carbonic anhydrase inhibitors', 'none_3', 'none_4', 'none_cat', 'Carbonic anhydrase inhibitors')
group_by_hier4('rx_digoxin', df, 'digoxin', 'digoxin immune fab', 'Digoxin')

group_by_hier3('rx_bbselective', df, 'beta blockers cardio-selective', 'none_4', 'betaxolol|trimethoprim', 'Selective beta blockers')
group_by_cat('rx_bbhf', df, 'metoprolol|carvedilol|bisoprolol', 'Heart failure beta blockers')
group_by_hier3('rx_bbnonselective', df, 'beta blockers non-selective', 'timolol|sotalol', 'none_cat', 'Non-selective beta blockers')
group_by_cat('rx_ccbrate', df, 'diltiazem|verapamil', 'Calcium channel blockers, rate control')
group_by_hier3('rx_ccbnonrate', df, 'calcium channel blockers|ca channel', 'none_4', 'diltiazem|verapamil', 'Calcium channel blockers, non-rate control')
group_by_hier4('rx_inotropes', df, 'milrinone|dobutamine', 'none_cat', 'Introopes')
group_by_cat('rx_arni', df, 'sacubitril-valsartan', 'Angiotensin receptor-neprilysin inhibitor')
group_by_cat('rx_riociguat', df, 'riociguat', 'Riociguat')
group_by_cat('rx_ivabradine', df, 'ivabradine', 'Ivabradine')
group_by_cat('rx_tafamidis', df, 'tafamidis', 'Tafamidis')


group_by_hier2('rx_antiarrhythmics1a', df, 'antiarrhythmics type i-a', 'none_3', 'none_4', 'none', 'Class 1A antiarrhythmics')
group_by_hier2('rx_antiarrhythmics1b', df, 'antiarrhythmics type i-b', 'none_3', 'none_4', 'none', 'Class 1B antiarrhythmics')
group_by_hier2('rx_antiarrhythmics1c', df, 'antiarrhythmics type i-c', 'none_3', 'none_4', 'none', 'Class 1C antiarrhythmics')
group_by_hier2('rx_antiarrhythmics3', df, 'antiarrhythmics type iii', 'none_3', 'none_4', 'none', 'Class 3 antiarrhythmics')
group_by_hier4('rx_sotalol', df, 'sotalol', 'none_cat', 'Sotalol')  
group_by_hier3('rx_2b3ai', df, 'glycoprotein iib/iiia receptor inhibitors', 'none_4', 'none_cat', 'GP2b3a inhibitors')  
group_by_hier2('rx_prostaglandin_vaso', df, 'prostaglandin vasodilators', 'none_3', 'none_4', 'none', 'Prostaglandin vasodilators')

#Cancer-ish
group_by_hier3('rx_monoab', df, 'monoclonoal antibodies|monoclonal antibodies', 'none_4', 'none_cat', 'Monoclonal antibodies')
group_by_hier3('rx_antiandrogens', df, 'antiandrogens', 'none_4', 'none_cat', 'Antiandrogens')
group_by_hier3('rx_aromatase_i', df, 'aromatase inhibitors', 'none_4', 'none_cat', 'Aromatase inhibitors')
group_by_hier3('rx_lhrh', df, 'lhrh analogs', 'none_4', 'none_cat', 'LHRH analogs')
group_by_hier3('rx_tyrosinekinasei', df, 'tyrosine kinase inhibitors', 'none_4', 'none_cat', 'Tyrosine kinase inhbitors')
group_by_hier3('rx_macrolideimmunosuppressants', df, 'macrolide immunosuppressants', 'none_4', 'none_cat', 'Macrolide immunosuppressants')
group_by_hier4('rx_mycophenolate', df, 'mycophenolate', 'none_cat', 'Mycophenylate')  

group_by_cat('rx_anthracyclines', df, 'doxorubicin|daunorubicin|mitoxantrone', 'Anthracyclines')

group_by_hier3('rx_iron', df, 'iron', 'none_4', 'none_cat', 'Iron')
group_by_hier2('rx_magnesium', df, 'magnesium', 'none_3', 'none_4', 'none_cat', 'Magnesium')
group_by_hier1('rx_parkinsons', df, 'antiparkinson agents', 'none_2', 'none_3', 'none_4', 'none_cat', 'Parkinsons agents')  
group_by_hier1('rx_antipsychmanic', df, 'antipsychotics/antimanic agents', 'none_2', 'none_3', 'none_4', 'none_cat', 'Antipsychotics/antimanic agents')  
group_by_hier2('rx_tricyclic', df, 'tricyclic agents', 'none_3', 'none_4', 'diltiazem', 'Tricyclics')
group_by_hier2('rx_hydantoins', df, 'hydantoins', 'none_3', 'none_4', 'none_cat', 'Hydantoins') #paroxetine?
group_by_hier1('rx_antidiarrhea', df, 'antidiarrheals', 'none_2', 'none_3', 'none_4', 'none_cat', 'Anti-diarrheals')  
group_by_hier2('rx_calciumrx', df, '^calcium$', 'none_3', 'none_4', 'none_cat', 'Calcium supplements')

group_by_hier2('rx_glucocorticosteroids', df, 'glucocorticosteroids', 'none_3', 'none_4', 'none_cat', 'Glucocorticosteroids')
group_by_hier2('rx_steroidstopical', df, 'corticosteroids - topical', 'none_3', 'none_4', 'none_cat', 'Topical steroids')
group_by_hier2('rx_steroidsnasal', df, 'nasal steroids', 'none_3', 'none_4', 'none_cat', 'Nasal steroids')
group_by_hier1('rx_contraceptives', df, 'contraceptives', 'none_2', 'none_3', 'none_4', 'none_cat', 'Contraceptives')
group_by_hier1('rx_laxatives', df, 'laxatives', 'none_2', 'none_3', 'none_4', 'none_cat', 'Laxatives')
group_by_hier3('rx_diaphragms', df, 'diaphragms', 'none_4', 'none_cat', 'Diaphragms')
group_by_hier1('rx_coughcold', df, 'cough/cold/allergy', 'none_2', 'none_3', 'none_4', 'none_cat', 'Cough and cold')
group_by_hier2('rx_diagnuc', df, 'diagnostic radiopharmaceuticals', 'none_3', 'none_4', 'none_cat', 'Nuclear diagnostic')
group_by_hier1('rx_gout', df, 'gout agents', 'none_2', 'none_3', 'none_4', 'levonorgestrel', 'Gout agents')
group_by_hier1('rx_ophtho', df, 'ophthalmic agents', 'none_2', 'none_3', 'none_4', 'none_cat', 'Ophthalmic agents')
group_by_hier2('rx_phosbinder', df, 'phosphate binder agents', 'none_3', 'none_4', 'none_cat', 'Phos binders')
group_by_hier2('rx_thyroid', df, 'thyroid hormones', 'none_3', 'none_4', 'none_cat', 'Thyroid replacement')
group_by_cat('rx_methimazole', df, 'methimazole', 'Methimazole')

# <codecell>
rx_names = {}
med_names = [val for val in [os.path.basename(x)[:-4] for x in glob.glob('./saved_medgrps/*_names.pkl')]]
for m in med_names:
    rx = pickle.load(open( './saved_medgrps/%s.pkl' %m, 'rb'))
    rx_names.update(rx)
    os.remove('./saved_medgrps/%s.pkl' %m)

pickle.dump(rx_names, open('./saved_medgrps/rx_names_all.pkl', 'wb'))    

# <codecell> Create csv for groupings

med_grps = [val for val in [os.path.basename(x)[:-4] for x in glob.glob('./saved_medgrps/*_table.pkl')]]
df = pd.read_pickle('./saved_medgrps/%s.pkl' %med_grps[0])
df_cols = df.columns
new_df = pd.DataFrame(columns = df_cols)
new_df['med_grp'] = ''
for m in med_grps:
    df = pd.read_pickle('./saved_medgrps/%s.pkl' %m)
    df['med_grp'] = m
    new_df = new_df.append(df)

new_df.to_csv('./saved_medgrps/rx_names_mapped.csv', index=False)
