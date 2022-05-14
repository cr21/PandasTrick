# You’re given two dataframes: transactions and products.
#
# The transactions dataframe contains transaction ids, product ids, and the total amount of each product sold.
#
# The products dataframe contains product ids and prices.
#
# Write a function to return a dataframe containing every transaction
# with a total value of over \$100$100. Include the total value of the transaction as a new column in the dataframe.


import pandas as pd

transactions = {"transaction_id" : [1, 2, 3, 4, 5], "product_id" : [101, 102, 103, 104, 105], "amount" : [3, 5, 8, 3, 2]}

products = {"product_id" : [101, 102, 103, 104, 105], "price" : [20.00, 21.00, 15.00, 16.00, 52.00]}

df_transactions = pd.DataFrame(transactions)

df_products = pd.DataFrame(products)

df = df_transactions.merge(df_products,on='product_id')
df['total_value'] = df['amount'] * df['price']
df = df[df['total_value'] > 100.0][['transaction_id','product_id','amount','total_value']]
df.reset_index(drop=True)
print(df)


###

#  transaction_id  product_id  amount  total_value
# 1               2         102       5        105.0
# 2               3         103       8        120.0
# 4               5         105       2        104.0
