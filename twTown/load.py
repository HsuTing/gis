import os
from django.contrib.gis.utils import LayerMapping
from models import TwTown

twtown_mapping = {
    'townsn' : 'TOWNSN',
    'townid' : 'TOWNID',
    'countyname' : 'COUNTYNAME',
    'townname' : 'TOWNNAME',
    'name' : 'name',
    'geom' : 'UNKNOWN',
}

twtown_data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'twTown1982.geojson'))

def run(verbose=True):
    lm = LayerMapping(TwTown, twtown_data, twtown_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)
