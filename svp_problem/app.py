# -*- coding: utf-8 -*-

from classes.Airport import Airport
from src.svp import *

def run():
    """
    TODO
    """
    airports_list = [] if read_data( 'airports_list.obj' ) is None else read_data( 'airports_list.obj' )
    # dest_map = {} if read_data( 'dest_map.obj' ) is None else read_data( 'dest_map.obj' )
    print( 'airports_list: ' + str( airports_list ) )
    # print( 'dest_map: ' + str( dest_map ) )
    print( '\n' )

    # TODO add show data option; add option to update dest_map.obj; add option to show the destination route
    option = input("Choose your option: \n1. Create new airport\n")
    if option == '1':
        airport = Airport( input("Airport name: "), input("Airport destinations: ").split(' ') )
        airports_list.append( airport )
        write_data( airports_list, 'airports_list.obj' )