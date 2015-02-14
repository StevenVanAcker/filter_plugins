from __future__ import absolute_import

import math
from ansible import errors

def lambdafilter(sd, sf, *args, **kw):
    d = eval(str(sd))
    f = eval(sf)
    return f(d)

class FilterModule(object):
    '''
    Ansible lambda filter: allows processing of a variable
    through a python lambda function.
    '''

    def filters(self):
        return {
            'lambdafilter': lambdafilter,
        }

