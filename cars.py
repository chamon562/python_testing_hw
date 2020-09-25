class Cars:
    """A sample Cars class"""

    def __init__(self, maker, model, networth):
        self.maker = maker
        self.model = model
        self.networth = networth


    @property
    def full_car(self):
        return '{} {}'.format(self.maker, self.model)


