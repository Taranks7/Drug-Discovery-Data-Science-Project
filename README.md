# Drug Discovery Data-Science: Project Overview # 
- Retrieve biological activity data of target proteins and compounds from the ChEMBL database.
- Identify compound or molecule which can inhibit the function of the coronavirus 3C-like proteinase.
- Biological activity data used to train a regression model to predict pIC50 values.


![final image](https://user-images.githubusercontent.com/74196907/103291535-e72fb780-49e3-11eb-8d6b-e56d3c05ed9a.png)

Scatter plot showing the experimental and predicted pIC50 values based on the Regression model 

## Code and resources used: ## 
[Bioinformatics Project from scratch](https://www.youtube.com/watch?v=plVLRashaA8&list=PLtqF5YXg7GLlQJUv9XJ3RWdd5VYGwBHrP)

## How to use ## 
- 1_data-retrieval.py is used to retrieve the data, which is then stored in the bioactivity_preprocessed_data.csv file.
- Analysis of this data is is conducted in the jupyter notebook 2_data_analysis.ipynb.
- 3_Regression_Random_Forest.ipynb is used to train and test a regression model, which predicts the pIC50 values of potential therapeutics.
