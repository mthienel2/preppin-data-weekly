import pandas as pd

# Import CSV files
swift_codes_df = pd.read_csv(r'C:\Users\mthienel.ga\Desktop\Cleaning\Week 2\Swift Codes.csv')
transactions_df = pd.read_csv(r'C:\Users\mthienel.ga\Desktop\Cleaning\Week 2\Transactions.csv')

# Merge the transactions_df with swift_codes_df on the "Bank" column to get the SWIFT code and Check Digits for each transaction
merged_df = transactions_df.merge(swift_codes_df, on="Bank", how="left")

# Construct the IBAN using the provided pattern
merged_df['IBAN'] = 'GB' + merged_df['Check Digits'] + merged_df['SWIFT code'] + merged_df['Sort Code'].str.replace('-', '') + merged_df['Account Number'].astype(str)

# Select the necessary columns for the final output
iban_output_generated_df = merged_df[['Transaction ID', 'IBAN']]

iban_output_generated_df.head()
iban_output_generated_df.to_csv('Output.csv', index=False)