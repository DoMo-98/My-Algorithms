# -*- coding: utf-8 -*-

from classes.Airport import Airport
from src.svp import *

def run():
    """
    TODO
    """
    airports_list = [] if read_data( 'airports_list.obj' ) is None else read_data( 'airports_list.obj' )
    # dest_map = {} if read_data( 'dest_map.obj' ) is None else read_data( 'dest_map.obj' )
    show_data( airports_list )
    # print( 'airports_list: ' + str( airports_list ) )
    # print( 'dest_map: ' + str( dest_map ) )

    option = -1

    while option != 0:
        # TODO add show data option; add option to update dest_map.obj; add option to show the destination route
        option = int( input("\nChoose your option: \n1. Create new airport\n2. Show airports data\n0. Exit\n") )

        if option == 0:
            return
        if option == 1:
            airport = Airport( input("Airport name: "), input("Airport destinations: ").split(' ') )
            airports_list.append( airport )
            write_data( airports_list, 'airports_list.obj' )
        if option == 2:
            show_data( airports_list )