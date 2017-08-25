import pandas as pd
import numpy as np

file_name = '2017-07-26-35057.xls'

cities = ['Beverly Hills', 'Century City', 'Hollywood', 'LAX', 'Marina Del Rey', 'North Hollywood', 'Santa Monica', 'Venice', 'West Hollywood', 'Westwood']


def create_dataframe(file_name):
    """
    takes in tour information file downloaded, a string
    returns pandas dataframe 
    """
    df = pd.read_html(file_name)
    df = df[6]
    df = df.drop(['Conf.', 'Comments', 'Balance Owing', 'Drivers/Veh/Cap', 'Pickup Address'], axis=1)
    
    return df

df = create_dataframe(file_name)


def total_guests_per_tour(tour_name):
    """'
    takes in name of specific tour, a string
    returns number of guests for that specific tour, an integer
    and its respective pandas dataframe
    """
    tour_df = df[(df['Activity'] == tour_name)]
    tour_df_Pax_column = tour_df.loc[0:, 'Pax']
    
    for row in range(len(tour_df)):
        tour_df_Pax_column[row] = sum([ int(x) for x in tour_df_Pax_column[row] if x.isdigit() ])
    
    return (tour_df, tour_df.Pax.sum())
    
(tour_df, tour_total_guests) = total_guests_per_tour('City Tour 1')


def pickup_passengers(tour_df):
    # isolate the pickup location column
    pickup_column = tour_df.loc[0:, 'Pickup Location']
    # remove those who are going to meet at the visitor center
    to_drop = [ "*Check-in Santa Monica - You'll meet us in Santa Monica @1400 Ocean Ave, 90401 9-9:30 AM" ]
    tour_df_pickup = tour_df[ ~pickup_column.isin(to_drop) ]
    
    return tour_df_pickup
    
tour_df_pickup =  pickup_passengers(tour_df)


def add_location_groups(tour_df_pickup):

    tour_df_pickup['Location Groups'] = np.empty((len(tour_df_pickup), 0)).tolist()
    location_groups_count = dict.fromkeys(cities, 0)
    
    for city in cities:
        for i in range(len(tour_df_pickup)):
            if tour_df_pickup.loc[:, 'Pickup Location'][i].str.contains(city).bool():
                tour_df_pickup.loc[:, 'Location Groups'][i] = city
                location_groups_count[city] += tour_df_pickup.loc[:, ('Pax')][i]
    
    return location_groups_count


counts_list = add_location_groups(tour_df_pickup)
print(counts_list)
print(tour_df_pickup)
