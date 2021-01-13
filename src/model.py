class Customer:
    """ Structure for input Customer details"""
    def __init__(self, user_id: int, name: str, location: tuple):
        self.user_id = user_id
        self.name = name
        self.location = location
