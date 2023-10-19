from test.testing import print_name

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)
# logger = logging.getLogger(__main__)


print_name()

