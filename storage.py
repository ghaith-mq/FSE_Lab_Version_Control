class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self):
        pass

    def set(self):
        pass
    
    def add(self, pair):
        if len(pair) != 2:
	    raise Exception
	key, value = pair
	if key in self.data:
	    raise Exception("The key is already in storage. To change the stored value, use storage.set")
	self.data[key] = value

