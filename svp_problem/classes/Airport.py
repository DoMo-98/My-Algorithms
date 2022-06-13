# -*- coding: utf-8 -*-

class Airport():
    def __init__(self, name, dests_in_scope, dest_map = {}):
        self.name = name
        self.dests_in_scope = dests_in_scope
        self.dest_map = dest_map
        
    def get_name(self):
        return self.name
        
    def get_dests_in_scope(self):
        return self.dests_in_scope
        
    def get_dest_map(self):
        return self.dest_map
        
    def print_info(self):
        print(self.name)
        print(self.dests_in_scope)
        print(self.dest_map)
        print("")