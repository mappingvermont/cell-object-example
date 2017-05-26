import CellType1, CellType2, CellType3, CellType4, CellType5, CellType6, CellType7


class Signature(object):

    def __init__(self, peat, biomass, climate):

        self.peat = peat
        self.biomass = biomass
        self.climate = climate

        print 'Creating new pixel with {} peat, {} biomass and {} climate'.format(peat, biomass, climate)

    def classify(self):

        print 'Classifying pixel based on input flags'
        pixel_signature = [self.peat, self.biomass, self.climate]

        if pixel_signature[0:2] == [True, False] and self.climate in [0, 4, 5, 7]:
            return CellType1.CellType()

        elif pixel_signature[0:2] == [True, False] and self.climate in [1, 2, 3, 6, 8, 9, 10]:
            return CellType2.CellType()

        elif pixel_signature[0:2] == [True, True] and self.climate in [0, 4, 5, 7]:
            return CellType3.CellType()

        elif pixel_signature[0:2] == [True, True] and self.climate in [1, 2, 3, 6, 8, 9, 10]:
            return CellType4.CellType()

        elif pixel_signature[0:2] == [False, False] and self.climate in [0, 4, 5, 7]:
            return CellType5.CellType()

        elif pixel_signature[0:2] == [False, False] and self.climate in [1, 2, 3, 6, 8, 9, 10]:
            return CellType6.CellType()

        elif pixel_signature[0:2] == [False, True] and self.climate in [0, 4, 5, 7]:
            return CellType7.CellType()

        else:
            raise ValueError('Cell with {} peat, {} biomass and {} climate did not match any '
                             'known signature'.format(self.peat, self.biomass, self.climate))
