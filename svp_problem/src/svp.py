"""#!/usr/bin/python3"""
# -*- coding: utf-8 -*-

import pickle
from classes.Airport import Airport

"""
    The variable "data" is a list of Airports
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
  for d in data:
    d.print_info()