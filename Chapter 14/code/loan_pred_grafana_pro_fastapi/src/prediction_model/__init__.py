import os
from prediction_model.config import config

with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

# __version__ = 0.1