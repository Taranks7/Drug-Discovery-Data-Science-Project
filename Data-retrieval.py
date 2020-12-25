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
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

df = pd.DataFrame.from_dict(res)
df.head(3)
#will print table







