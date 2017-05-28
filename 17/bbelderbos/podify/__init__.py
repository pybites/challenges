__title__ = 'podify'
__author__ = 'Bob Belderbos'

import logging
import os
import ssl

# some feeds get 'bozo_exception': URLError(SSLError(1, 
#   '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed 
ssl._create_default_https_context = ssl._create_unverified_context

FORMAT = '%(asctime)-15s :: %(message)s'
logdir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

logging.basicConfig(
    filename=os.path.join(logdir, 'podcast.log'), 
    level=logging.DEBUG, 
    format=FORMAT)
