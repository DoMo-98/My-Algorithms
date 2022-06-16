# -*- coding: utf-8 -*-

# TODO change the flux of the program, its better if the airports_list is a dictionary with the airport name as key
class Airport():
    def __init__( self, name, dests_in_scope, best_route_map = {} ):
        self.name = name
        self.dests_in_scope = dests_in_scope
        self.best_route_map = best_route_map
        
    def get_name( self ):
        return self.name
        
    def get_dests_in_scope( self ):
        return self.dests_in_scope
        
    def get_dest_map( self ):
        return self.best_route_map
        
    def print_info( self ):
        print( "\n" + self.name )
        print( self.dests_in_scope )
        print( self.best_route_map )

    def add_dest( self, dest ):
        self.dests_in_scope.append( dest )

    def add_best_route( self, dest, best_route ):
        self.best_route_map[ dest ] = best_route