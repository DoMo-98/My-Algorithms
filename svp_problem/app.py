# -*- coding: utf-8 -*-

from classes.Airport import Airport
# from svp_problem.classes.Airport import Airport
from src.svp import *
# from svp_problem.src.svp import *

def run():
    """
    TODO
    """
    airports_dict = {} if read_data( 'airports_dict.obj' ) is None else read_data( 'airports_dict.obj' )
    # dest_map = {} if read_data( 'dest_map.obj' ) is None else read_data( 'dest_map.obj' )
    show_data( airports_dict )
    # print( 'airports_dict: ' + str( airports_dict ) )
    # print( 'dest_map: ' + str( dest_map ) )

    option = -1

    while option != 0:
        # TODO add show data option; add option to update dest_map.obj; add option to show the destination route
        option = int( input("\nChoose your option: \n"
                        +   "1. Create new airport\n"
                        +   "2. Show airports data\n"
                        +   "3. Show total route\n"
                        +   "0. Exit\n") )

        if option == 0:
            return
        if option == 1:
            name = input("Airport name: ")
            airport = Airport( name, input("Airport destinations: ").split(' ') )
            airports_dict[ name ] = airport
            write_data( airports_dict, 'airports_dict.obj' )
        if option == 2:
            show_data( airports_dict )
        if option == 3:
            name = input("Source airport name: ")
            final_dest = input("Final destination: ")
            airports_dict[ name ].print_total_route( final_dest )