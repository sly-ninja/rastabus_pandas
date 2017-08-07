import pandas as pd
import numpy as np

file_name = '2017-07-26-35057.xls'



def create_dataframe(file_name):
    df = pd.read_html(file_name)
    df = df[6]
    df = df.drop(['Conf.', 'Comments', 'Balance Owing', 'Drivers/Veh/Cap', 'Pickup Address'], axis=1)
    return df

df = create_dataframe(file_name)

# ======================================================================= #

def total_gets_per_tour(tour):
    tour_df = df[(df['Activity'] == tour)]
    tour_df_Pax_column = tour_df.loc[0:, 'Pax']
    
    for row in range(len(tour_df)):
        tour_df_Pax_column[row] = sum([ int(x) for x in tour_df_Pax_column[row] if x.isdigit() ])
    
    return (tour_df, tour_df.Pax.sum())
    
(tour_df, tour_total_guests) = total_gets_per_tour('City Tour 1')


# ======================================================================= #

def pickup_passengers(tour_df):
    
    # isolate the pickup location column
    pickup_column = tour_df.loc[0:, 'Pickup Location']
    # remove those who are going to meet at the visitor center
    to_drop = [ "*Check-in Santa Monica - You'll meet us in Santa Monica @1400 Ocean Ave, 90401 9-9:30 AM" ]
    tour_df_pickup = tour_df[ ~pickup_column.isin(to_drop) ]
    
    return tour_df_pickup
    
tour_df_pickup =  pickup_passengers(tour_df)

# ======================================================================= #

def split_pickup_buses():
   
    pickup_buses = ['10', '2', '8', 'Van']
    bus_capacities = {
         '2' : 27, 
         '4' : 23,
         '5' : 23,
         '6' : 23,
         '7' : 24,
         '8' : 27,
         '9' : 23,
         '10' : 14,
         '11' : 23,
         '12' : 23,
         'Van' : 8}
    bus_assignments = []
    
    assigned_passengers = 0
    for index, row in tour_df_pickup.iterrows():
        
        
        
       
        for bus in pickup_buses:

            single_bus = []
            capacity = bus_capacities[bus]
#            print(bus, 'assigned_passengers1', assigned_passengers, 'END')
            
            if assigned_passengers <= capacity:
                
                single_bus.append(( tour_df_pickup['Guest Name'][index], tour_df_pickup['Mobile Telephone'][index], tour_df_pickup['Pickup Location'][index] ))
                
                assigned_passengers +=  tour_df_pickup['Pax'][index]
                
                print('SINGLE BUS: ', single_bus, index)
                
            else:
                bus_assignments.append(( bus, single_bus ))
                
                
        return bus_assignments


split_pickup_buses()




#==============================================================================
# remove_string2 = ".inplaceeditor-saving" 
# df['Comments'] = df['Comments'].str.replace(".inplaceeditor-saving { background: url('https://adayinlatours.zaui.net/themes/default/img/ajax-small-trans-loader.gif') bottom right no-repeat; }", '')
# 
# remove_string3 = "background"
# df['Comments'] = df['Comments'].str.replace(remove_string3, '') 
# 
# remove_string4 = 'add/edit notes'
# df['Comments'] = df['Comments'].str.replace(remove_string4, '') 
#==============================================================================
