# You’re given two dataframes. One contains information about addresses and the other contains relationships between various cities and states:
#
# Example:
#
# df_addresses
#
# address
# 4860 Sunset Boulevard, San Francisco, 94105
# 3055 Paradise Lane, Salt Lake City, 84103
# 682 Main Street, Detroit, 48204
# 9001 Cascade Road, Kansas City, 64102
# 5853 Leon Street, Tampa, 33605
# df_cities
#
# city	state
# Salt Lake City	Utah
# Kansas City	Missouri
# Detroit	Michigan
# Tampa	Florida
# San Francisco	California
# Write a function complete_address to create a single dataframe with complete addresses in the format of street, city, state, zip code.

import pandas as pd

addresses = {"address": ["4860 Sunset Boulevard, San Francisco, 94105", "3055 Paradise Lane, Salt Lake City, 84103", "682 Main Street, Detroit, 48204", "9001 Cascade Road, Kansas City, 64102", "5853 Leon Street, Tampa, 33605"]}

cities = {"city": ["Salt Lake City", "Kansas City", "Detroit", "Tampa", "San Francisco"], "state": ["Utah", "Missouri", "Michigan", "Florida", "California"]}

df_addresses = pd.DataFrame(addresses)
df_cities = pd.DataFrame(cities)



def complete_address(df_addresses,df_cities):
    df_addresses[['street', 'city', 'zipcode']] = df_addresses['address'].str.split(', ', expand=True)
    df_addresses = df_addresses.drop(['address'], axis=1)
    df_addresses = df_addresses.merge(df_cities, on="city")
    df_addresses['address'] = df_addresses[['street', 'city', 'state', 'zipcode']].apply(lambda x: ', '.join(x), axis=1)
    df_addresses = df_addresses.drop(['street', 'city', 'state', 'zipcode'], axis=1)

    return df_addresses

full_address = complete_address(df_addresses,df_cities)
print(full_address)