
class SaveLocations:
    def __init__(self):
        self.save_locations = {}
        print(self.save_locations)

    def add_location(self,**location):
        self.save_locations[location.keys()] = location.values()
