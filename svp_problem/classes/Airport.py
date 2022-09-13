# -*- coding: utf-8 -*-

# TODO change the flux of the program, its better if the airports_list is a dictionary with the airport name as key
class Airport():
    """
        Datos del Aeropuerto:
        - dest: destino a agregar
        - best_route: ruta mas corta para llegar a dest
        - dests_in_scope: lista de destinos en el alcance del aeropuerto
        - best_route_map: mapa de rutas mas cortas para llegar a cada destino
    """
    def __init__( self, name, dests_in_scope, best_route_map = {} ): # name
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
        print( self.dests_in_scope ) # delete "\n" and str()
        print( self.best_route_map )

    def add_dest( self, dest ):
        self.dests_in_scope.append( dest )

    def add_best_route( self, dest, best_route ):
        self.best_route_map[ dest ] = best_route

    def get_total_route( self, final_dest ):
        source = self
        total_route = [ source ]

        while source != None and final_dest != source.name:
            source = self.best_route_map[ source ]
            total_route.append( source )
        
        return total_route
    
    def print_total_route( self, final_dest ):
        total_route = self.get_total_route( final_dest )

        if len( total_route ) == 1:
            print( "No route found" )
            return

        for airport in total_route:
            print( airport.name )

        