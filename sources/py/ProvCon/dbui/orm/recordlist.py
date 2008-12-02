
class RecordList(list):
    def __init__(self, table, _filter="TRUE", select=['0'], order="objectid", **kkw):
        list.__init__(self)
        self.table = table
        self.filter = _filter
        self.select = select
        self.order = order
        self.filterfunc = kkw.get("filterfunc", lambda r: True)
        self.hash_id = {}
        self.hash_index = {}
    
    def reload(self):
        list.__init__(self)
        self += filter(self.filterfunc, self.table.recordObjectList (self.filter, self.select, self.order))
        self.hash_id.clear()
        self.hash_index.clear()
        for idx, r in enumerate(self): 
            self.hash_id[r.objectid] = r
            self.hash_index[r.objectid] = idx
        return self
    
    def reloadsingle(self, objectid):
        rl = self.table.recordObjectList ( self.filter + " AND o.objectid = %d " % objectid, self.select, self.order)
        self[self.hash_index[objectid]] = rl[0]
            
    def clear(self):
        list.__init__(self)
        self.hash_id.clear()
        
    def getindex(self, objectid):
        return self.hash_index[objectid]

    def getid(self, objectid):
        return self.hash_id[objectid]

    

    