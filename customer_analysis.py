# You’re given a dataframe containing sales data from a grocery store chain with columns for customer ID, gender, and date of sale.
#
# Create a new dataset with summary level information on their purchases including the columns:
#
# customer_id
# gender
# most_recent_sale
# order_count
# most_recent_sale should display the date of the customer’s most recent purchase. order_count should display the total number of purchases that the customer has made.
#
# Example:
#
# Input:
#
# import pandas as pd
#
# customers = {
# "customer_id" : [5156, 2982, 1011, 3854, 2982],
# "Gender" : ["m", "f", "m", "f", "f"],
# "Date of Sale" : ["2021-01-04", "2021-02-15", "2021-03-01", "2021-03-21", "2021-04-12"]
# }
#
# customer_df = pd.DataFrame(customers)

import pandas as pd

customers = {
    "customer_id": [5156, 2982, 1011, 3854, 2982],
    "Gender": ["m", "f", "m", "f", "f"],
    "Date of Sale": ["2021-01-04", "2021-02-15", "2021-03-01", "2021-03-21", "2021-04-12"]
}

customer_df = pd.DataFrame(customers)
customer_groups = customer_df.groupby(['customer_id', 'Gender'])
aggregated_customers = customer_groups.agg({
    'Date of Sale': 'max',
    'customer_id': 'count'
})

aggregated_customers = aggregated_customers.rename(columns={'Date_of_Sale': 'most_recent_sale', 'customer_id': 'order_count','Gender':'gender'}).reset_index()

print(aggregated_customers)




def customer_analysis(customers_df):
    customers_df['most_recent_sale'] = customers_df['customer_id'].map(
        customers_df.groupby('customer_id')['Date of Sale'].max())
    customers_df['order_count'] = customers_df['customer_id'].map(customers_df['customer_id'].value_counts())
    customers_df = customers_df[['customer_id', 'Gender', 'most_recent_sale', 'order_count']].drop_duplicates(
        ['customer_id'], ignore_index=True)
    customers_df.columns = customers_df.columns.str.lower()
    return customers_df

    return customer_groups


def test_customer_analysis_log_one_day():
    import pandas as pd
    customers = {"customer_id": [1000, 1001, 1002, 1003, 1004, 1005],
                 "Gender": ["m", "m", "f", "f", "m", "f"],
                 "Date of Sale": ["2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20"]}
    customers_df = pd.DataFrame(customers)

    true_output = pd.DataFrame({
        "customer_id": [1000, 1001, 1002, 1003, 1004,1005],
        "gender": ["m", "m", "f", "f", "m", "f"],
        "most_recent_sale": ["2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20", "2021-02-20"],
        "order_count": [1,1, 1, 1, 1, 1]

    })

    test_output = customer_analysis(customers_df)

    pd.testing.assert_frame_equal(test_output.sort_values(by=['customer_id']).reset_index(drop=True),
                                  true_output.sort_values(by=['customer_id']).reset_index(drop=True))