#environment and python
source venv/bin/activate
ipython 

# install ChEMBL web service package
pip install chembl_webresource_client

#import libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client

#target search for coronavirus 
#assign new_client.taget to target variable
target = new_client.target
target_query = target.search('coronavirus')
#assign query in argument 
targets = pd.DataFrame.from_dict(target_query)
targets
# will output targets of proteins and organisms
#targets are target proteins/organisms that drugs will act on 

#we will use one of these single protein's to investigate further: SARS coronavirus 3c-like proteinase
#bioactivity data for coronavirus 3C-like proteinase, this is the fifth(0 is the first, 4th is fifth) entry in the output we printed above
#this has a tax_id 227859
#and x_ref_id P0C6U8

selected_target = targets.target_chembl_id[4]

selected_target
#will output 'CHEMBL3927', this is it's unique target id

#bioactivity data, reported as IC50 values
activity = new_client.activity
#selected target is the target_chembl_id and filter select the IC50 containing values 
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

df = pd.DataFrame.from_dict(res)
#will print table
#only view first 5 rows 
df.head(5)

#bioactivity unit type IC50 was selected, check this 
df.standard_type.unique()
# will print array(['IC50'], dtype=object)

#standard value is also seen in the printed table, this is the drug potency. The lower the number, the more potent("better") the drug 
#we want the standard value number to be as low as possilbe
# meaning tha the inhibitory concentration at 50% will have a lower concentration 
#in order to elicit 50% of the inhibition of a target protein, a lower concentration of the drug is required
# save bioactivity dta to csv file 
df.to_csv('bioactivity_data.csv', index=False)


#missing datain the standard_value column 
df2 = df[df.standard_value.notna()]
df2

#in this dataset there are no missing values in the standard_value column 

#labeling compounds as active, inactive or intermediate
#The bioactivity data is in the IC50 unit. 
# values of less than 1000 nM = active 
# greater than 10,000 nM = inactive. 
# 1,000 and 10,000 nM = intermediate.
bioactivity_class = []
for i in df2.standard_value:
  if float(i) >= 10000:
    bioactivity_class.append("inactive")
  elif float(i) <= 1000:
    bioactivity_class.append("active")
  else:
    bioactivity_class.append("intermediate")
    
    
#iterate molecule_chembl_id into list
mol_cid = []
for i in df2.molecule_chembl_id:
  mol_cid.append(i)
  
  
  # iterate canonical_smiles into list
  canonical_smiles = []
for i in df2.canonical_smiles:
  canonical_smiles.append(i)
  
  # iterate standard_value into list
  standard_value = []
for i in df2.standard_value:
  standard_value.append(i)
  
  #combine into dataframe 
  data_tuples = list(zip(mol_cid, canonical_smiles, bioactivity_class, standard_value))
df3 = pd.DataFrame( data_tuples,  columns=['molecule_chembl_id', 'canonical_smiles', 'bioactivity_class', 'standard_value'])
  
  
  #save 
  df3.to_csv('bioactivity_preprocessed_data.csv', index=False)

  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
    
    
    
    
    








