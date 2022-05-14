import pandas as pd

# Given a dataframe with three columns:
#
# client_id
# ranking
# value
# Write a function to fill the NaN values in the value column with the previous non-NaN value from the same client_id ranked in ascending order.
#
# If there doesn’t exist a previous client_id then return the previous value.
#
# Input:
#
# print(clients_df)
# client_id	ranking	value
# 1001	1	1000
# 1001	2	NaN
# 1001	3	1200
# 1002	1	1500
# 1002	2	1250
# 1002	3	NaN
# 1003	1	1100
# 1003	2	NaN


clients = {
    "client_id": [1001, 1001, 1001, 1002, 1002, 1002, 1003, 1003],
    "ranking": [1, 2, 3, 1, 2, 3, 1, 2],
    "value": [1000, pd.NA, 1200, 1500, 1250, pd.NA, 1100, pd.NA]
}

clients_df = pd.DataFrame(clients)
# forward fill na ( fill last valid previous values
clients_df = clients_df.sort_values(by='client_id').ffill().sort_values(by='ranking')
print(clients_df)

### Another Method

X = clients_df.sort_values(['client_id', 'ranking']).fillna(method='ffill')
X.sort_values('ranking')
print(X)

##### OUTPUT

#   client_id  ranking  value
# 0       1001        1   1000
# 1       1001        2   1000
# 2       1001        3   1200
# 3       1002        1   1500
# 4       1002        2   1250
# 5       1002        3   1250
# 6       1003        1   1100
# 7       1003        2   1100
