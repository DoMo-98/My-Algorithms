# -*- coding: utf-8 -*-

class Airport():
    def __init__(self, name, dests_in_scope, dest_map = {}):
        self.name = name
        self.dests_in_scope = dests_in_scope
        self.dest_map = dest_map