

class CellType(object):

    def __init__(self):
        print 'this is Cell Type1'
        self.peat = None
        self.biomass = None
        self.climate_zone = None

    def add_properties(self, peat, biomass, climate_zone):
        self.peat = peat
        self.biomass = biomass
        self.climate_zone = climate_zone

        print 'Adding properties to this cell'

    def calculate_output(self):

        print 'Calculating output'
        print self.peat * self.biomass + self.climate_zone
