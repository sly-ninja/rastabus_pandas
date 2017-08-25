from dataframe_class import Rasta_Dataframe

rasta_df = Rasta_Dataframe()

file_name = '2017-07-26-35057.xls'
cities = ['Beverly Hills', 'Century City', 'Hollywood', 'LAX', 'Marina Del Rey', 'North Hollywood', 'Santa Monica', 'Venice', 'West Hollywood', 'Westwood']
drop_columns = ['Conf.', 'Comments', 'Balance Owing', 'Drivers/Veh/Cap', 'Pickup Address']
tour_name = 'City Tour 1'


df = rasta_df.create_dataframe(file_name, drop_columns)
tour_df, tour_count = rasta_df.total_guests_per_tour('City Tour 1')
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


def assign_buses(bus_capacities, pickup_buses):

    number_in_bus = 0
    current_bus = 0
    bus_assignments = {key:[] for key in pickup_buses}
    
    total_bus_count = len(pickup_buses)
    total_groups = len(tour_df_pickup)
    bus_capacity = bus_capacities[pickup_buses[current_bus]]
    
    for i in range(total_groups):
        
            if tour_df_pickup.loc[:, 'Pax'][i] + number_in_bus <= bus_capacity:
                bus_assignments[pickup_buses[current_bus]].append(tour_df_pickup.loc[:, 'Guest Name'][i])
                number_in_bus += tour_df_pickup.loc[:, 'Pax'][i]

            else:
                if current_bus < total_bus_count:
                    current_bus += 1
                    number_in_bus = 0
                    i += 1
                else:
                    print('all buses are full')
                    return bus_assignments
    
    return bus_assignments

#print(assign_buses(bus_capacities, pickup_buses))

