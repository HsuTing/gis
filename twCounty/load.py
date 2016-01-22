
import os
from django.contrib.gis.utils import LayerMapping
from models import TwCounty

twcounty_mapping = {
    'countysn' : 'COUNTYSN',
    'countyname' : 'COUNTYNAME',
    'name' : 'name',
    'geom' : 'Unknown',
}

twcounty_data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'twCounty2010.geojson'))

def run(verbose=True):
    lm = LayerMapping(TwCounty, twcounty_data, twcounty_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)
