"""#!/usr/bin/python3"""
# -*- coding: utf-8 -*-

import pickle
from classes.Airport import Airport
# from svp_problem.classes.Airport import Airport

"""
    The variable "data" is a dictionary of Airports
"""

def write_data( data, file_name ):
    """
    TODO
    """
    with open( file_name, 'wb' ) as f:
        # f.write( str( data ) )
        pickle.dump( data, f )
        print( 'Done writing data to file ' + file_name )

def read_data( file_name ):
    """
    TODO
    """
    try:
        with open( file_name, 'rb' ) as f:
            data = pickle.load( f )
            return data
    except:
        return None

def show_data( data ):
    """
    TODO
    """
    for d in data.values():
        d.print_info()

def show_total_route( data ):
    """
    TODO
    """
    total_route = 0
    for d in data.values():
        total_route += d.get_total_route()
    print( 'Total route: ' + str( total_route ) )