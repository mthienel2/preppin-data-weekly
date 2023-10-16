import pandas as pd
df  = pd.read_csv(r'C:\Users\mthienel.ga\Desktop\PD 2023 Wk 1 Input.csv')

df['Bank'] = df['Transaction Code'].str.split('-').str[0]

df['Transaction Code'] = df['Transaction Code'].str.replace('^.*?-', '', n=1)

replacements = {
    1: 'Online',
    2: 'In-Person'
    }
df['Online or In-Person'] = df['Online or In-Person'].replace(replacements)

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], format = '%d/%m/%Y %H:%M:%S').dt.day_name()

result = df.groupby('Bank')['Value'].sum()

output1 = result.reset_index()
output1.columns = ['Bank', 'Value']
output1.to_csv('Output 1.csv', index=False)

result2 = df.groupby(['Bank', 'Online or In-Person', 'Transaction Date'])['Value'].sum()

output2 = result2.reset_index()
output2.columns = ['Bank','Online or In-Person','Transaction Date','Value']
output2.to_csv('Output 2.csv', index=False)

result3 = df.groupby(['Bank', 'Customer Code'])['Value'].sum()

output3 = result3.reset_index()
output3.columns = ['Bank', 'Customer Code','Value']
output3.to_csv('Output 3.csv', index=False)