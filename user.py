class User:
    _instance = None
    _first = True	
    def __init__(self,name, age, sex):
        if self._first :
            self.name = name
            self.age = age
	    self.sex = sex
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
	else:
	    return cls._instance
