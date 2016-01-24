import os
from django.contrib.gis.utils import LayerMapping
from models import TwVillage

twvillage_mapping = {
    'villagesn' : 'VILLAGESN',
    'villageid' : 'VILLAGEID',
    'countyname' : 'COUNTYNAME',
    'townname' : 'TOWNNAME',
    'villagenam' : 'VILLAGENAM',
    'name' : 'name',
    'geom' : 'UNKNOWN',
}

twvillage_data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'twVillage1982.geojson'))

def run(verbose=True):
    lm = LayerMapping(TwVillage, twvillage_data, twvillage_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)
