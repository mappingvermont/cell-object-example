import random

from pixels import signature

# Create bogus pixel
peat = random.randint(0, 1)
biomass = random.randint(0, 400)
climate_zone = random.randint(0, 10)

# build peat flag
if peat == 1:
    has_peat = True
else:
    has_peat = False

# biomass flag
if biomass > 200:
    high_biomass = True
else:
    high_biomass = False

# create a signature for this combination of pixel inputs
sig = signature.Signature(has_peat, high_biomass, climate_zone)

# classify this signature to get a unique pixel type (with a unique pixel formula)
pixel = sig.classify()

# add the real values to this pixel for the purposes of calculation
pixel.add_properties(peat, biomass, climate_zone)

# do the math
pixel.calculate_output()




