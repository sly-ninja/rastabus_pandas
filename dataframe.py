import pandas as pd
import numpy as np

file_name = '2017-07-26-35057.xls'



def create_dataframe(file_name):
    df = pd.read_html(file_name)
    df = df[6]
    df = df.drop(['Conf.', 'Comments', 'Balance Owing'], axis=1)
    return df

df = create_dataframe(file_name)

# ======================================================================= #


def split_dataframe(df):
    tour_types = df.Activity.unique().tolist()
    tour_types = [ x for x in tour_types if str(x) != 'nan' ]
    
    df_dict = {}
    for item in tour_types:
        df_dict[item] =  df.loc[df.Activity == item].reset_index() 

    return df_dict

df_dict = split_dataframe(df)    

# ======================================================================= #


def sum_pax_rows(tour):
    
    pax_column = df_dict[tour].loc[0:, 'Pax']
    
    for row in range(len(df_dict[tour])):
        pax_column[row] = sum([ int(x) for x in pax_column[row] if x.isdigit() ])
        
    
def total_guests_per_tour(df_dict):
    total_guests = dict.fromkeys( df_dict.keys(), 0 )
    
    for tour in list( df_dict.keys() ):
        sum_pax_rows(tour)
        total_guests[tour] = df_dict[tour].Pax.sum()
    
    return total_guests

total_guests = total_guests_per_tour(df_dict)
#df_dict['City Tour 1'].loc[:, ['Pax']][1] = sum([ int(x) for x in df_dict['City Tour 1'].loc[:, ['Pax']][1] if x.isdigit() ])

# ======================================================================= #


def split_for_pickup(tour):
        #Only Bus 5, 11 and 12 have a luggage compartment.
        #Bus 10 (16 with a wheelchairs). 
        
    pick_up_buses = ['10', '2', '8', 'Van']
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

    tour_total = total_guests['City Tour 1']
    pax_column = df_dict[tour].loc[0:, 'Pax']
    name_column = df_dict[tour].loc[0:, 'Guest Name']
    
    for i in range(len(pax_column)):
        
    

split_for_pickup('City Tour 1')

# ======================================================================= #









#==============================================================================
# westside = ['LAX', 'Marina Del Rey', 'Malibu', 'Venice']
# sm = ['Santa Monica', 'Malibu']
# hollywood = ['Hollywood', 'West Hollywood']
# bh =['Beverly Hills', 'Century City', 'Culver City', 'Westwood']
# 
# df_pickup = df['Pickup Location'].fillna('')
# 
# group_westside = []
# group_sm = []
# group_hollywood = []
# group_bh = []
# 
# 
# for item in range(len(df_pickup)):
# #    print(df_pickup[item])
#     group_westside = [item for item in df_pickup[item] if x for x in westside in df_pickup[item]]
# #    [group_westside.append(item) for x in westside if any(x in df_pickup[item])]
# print(group_westside)    
# #print(df['Comments'])
# 
# #df.to_excel('test.xlsx')
#==============================================================================




test = 0/1/2


















#==============================================================================
# df['Pickup Location'] = df['Pickup Location'].str.replace("\*Check-in Hollywood - You'll meet us in Los Angeles, CA @", 'Hollywood - ')
# df['Pickup Location'] = df['Pickup Location'].str.replace("\*Check-in Santa Monica - You'll meet us in Santa Monica @", 'Santa Monica - ')
# df['Pickup Location'] = df['Pickup Location'].str.replace('9-9:30 AM', '')
#  
# 
# print(df['Pickup Location'])
#==============================================================================

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


#==============================================================================
# test = []
# test2 = []
# for location in range(len(df['Pickup Location'])):
#     if 'Hollywood' in (df['Pickup Location'].fillna(''))[location]:
#         test.append(location)
#     if 'West Hollywood' in (df['Pickup Location'].fillna(''))[location]:
#         test.append(location)
#         
#         
#     if 'Westwood' in (df['Pickup Location'].fillna(''))[location]:
#         test2.append(location)
#     if 'Westwood' in (df['Pickup Location'].fillna(''))[location]:
#         test2.append(location)
#     if 'Westwood' in (df['Pickup Location'].fillna(''))[location]:
#         test2.append(location)
# 
# print(test, test2)   
# 
# 
#     [item for item in westside if item in westside]
#         print("ok")
#     else:
#         print('nope')
# 
# list(df['Pickup Location'])
#==============================================================================

