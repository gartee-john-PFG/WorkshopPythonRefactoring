class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def __str__(self):
        return f'Item: name - {self.name}, sell_in - {self.sell_in}, quality - {self.quality}'
