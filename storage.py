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

    def remove(self,key):
        self.data.pop(key, None)
        return self

    def set(self, key, new_val):
        if key in self.data:
            self.data[key] = new_val
        else:
            raise Exception("No such key")
        
    def add(self, pair):
        if len(pair) != 2:
            raise Exception
        key, value = pair
        if key in self.data:
            raise Exception("The key is already in storage. To change the stored value, use storage.set")
        self.data[key] = value

