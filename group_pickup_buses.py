from dataframe_class import Rasta_Dataframe


rasta_df = Rasta_Dataframe()

file_name = '2017-07-26-35057.xls'
cities = ['Beverly Hills', 'Century City', 'Hollywood', 'LAX', 'Marina Del Rey', 'North Hollywood', 'Santa Monica', 'Venice', 'West Hollywood', 'Westwood']
drop_columns = ['Conf.', 'Comments', 'Balance Owing', 'Drivers/Veh/Cap', 'Pickup Address']
tour_name = 'City Tour 1'


df = rasta_df.create_dataframe(file_name, drop_columns)
tour_df, tour_count = rasta_df.total_guests_per_tour('City Tour 1')
#clean_df = rasta_df.clean_dataframe(drop_columns)
tour_df_pickup = rasta_df.pickup_passengers()
counts_list = rasta_df.add_location_groups(cities)


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



pickup_buses = ['10', '2', '8', 'Van']

def assign_buses():
#    guest_total = sum(tour_df_pickup.Pax)
    assigned_to_bus = 0
    bus_assignments = dict.fromkeys(pickup_buses, [])
    
    for i in range(len(pickup_buses)):
        print('IIII: ', i)
        print(bus_capacities[pickup_buses[i]])
        while assigned_to_bus < bus_capacities[pickup_buses[i]]:
            
            for j in range(len(tour_df_pickup)):
                print('JJJJ: ', j)
                bus_assignments[pickup_buses[i]].append(tour_df_pickup.loc[:, 'Guest Name'][j])
                assigned_to_bus += tour_df_pickup.loc[:, 'Pax'][j]
                print("assigned_to_bus:", assigned_to_bus)
                j += 1
        else:
#            assigned_to_bus = 0
            i += 1
    
    return bus_assignments
