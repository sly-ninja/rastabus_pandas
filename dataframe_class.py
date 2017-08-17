import pandas as pd
import numpy as np

class Rasta_Dataframe(object):
    
    def __init__(self):
        self.df = self.create_dataframe(file_name)
        self.df_clean = self.clean_dataframe(drop_columns)
        self.tour_df, self.tour_count = self.total_guests_per_tour(tour_name)
        self.tour_df_pickup = self.pickup_passengers()
        self.location_groups_count = self.add_location_groups(cities)
 
    
    def create_dataframe(self, file_name):
        """
        takes in tour information file downloaded, a string
        returns pandas dataframe 
        """
        self.df = pd.read_html(file_name)
        self.df = self.df[6]
        
        return self.df
    
    
    def clean_dataframe(self, drop_columns):
        try :
            if self.drop_columns:
                self.df_clean = self.df.drop(drop_columns, axis=1)
                return self.df_clean
        except:
            return self.df
    
    
    def total_guests_per_tour(self, tour_name):
        """
        takes in name of specific tour, a string
        returns number of guests for that specific tour, an integer
        and its respective pandas dataframe
        """
        self.tour_df = self.df[(self.df['Activity'] == tour_name)]
        tour_df_Pax_column = self.tour_df.loc[0:, 'Pax']
        self.tour_count = self.tour_df.Pax.sum()
        
        for row in range(len(self.tour_df)):
            tour_df_Pax_column[row] = sum([ int(x) for x in tour_df_Pax_column[row] if x.isdigit() ])
        
        return (self.tour_df, self.tour_count)
        
    
    
    def pickup_passengers(self):
        # isolate the pickup location column
        pickup_column = self.tour_df.loc[0:, 'Pickup Location']
        # remove those who are going to meet at the visitor center
        to_drop = [ "*Check-in Santa Monica - You'll meet us in Santa Monica @1400 Ocean Ave, 90401 9-9:30 AM" ]
        self.tour_df_pickup = self.tour_df[ ~pickup_column.isin(to_drop) ]
        
        return self.tour_df_pickup
        

    
    def add_location_groups(self, cities):
    
        self.tour_df_pickup['Location Groups'] = np.empty((len(self.tour_df_pickup), 0)).tolist()
        self.location_groups_count = dict.fromkeys(cities, 0)
        
        for city in cities:
            for i in range(len(self.tour_df_pickup)):
                if self.tour_df_pickup[['Pickup Location']].loc[i].str.contains(city).bool():
                    self.tour_df_pickup.loc[:, 'Location Groups'][i] = city
                    self.location_groups_count[city] += self.tour_df_pickup.loc[:, ('Pax')][i]
        
        return self.location_groups_count
    
    

#=============================================================================#

file_name = '2017-07-26-35057.xls'
cities = ['Beverly Hills', 'Century City', 'Hollywood', 'LAX', 'Marina Del Rey', 'North Hollywood', 'Santa Monica', 'Venice', 'West Hollywood', 'Westwood']
drop_columns = ['Conf.', 'Comments', 'Balance Owing', 'Drivers/Veh/Cap', 'Pickup Address']
tour_name = 'City Tour 1'

#rasta_df = Rasta_Dataframe()

#print(rasta_df.create_dataframe(file_name))
#rasta_df.total_guests_per_tour('City Tour 1')
#rasta_df.pickup_passengers()
#rasta_df.add_location_groups()
