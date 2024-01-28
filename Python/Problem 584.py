import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filtered_customers = customer[(pd.isna(customer['referee_id'])) | (customer['referee_id'] != 2)]
    return filtered_customers[['name']]


# def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
#     names = []
#     for index, row in customer.iterrows():
#         if pd.isna(row['referee_id']):
#             names.append(row['name'])
        
#         elif row['referee_id'] != 2:
#             names.append(row['name'])
        
#     return pd.DataFrame({'name': names})