
"""
MAP Client Plugin
"""

__version__ = '0.1.3'
__author__ = 'Hugh Sorby'
__stepname__ = 'Multiple File Chooser'
__location__ = 'https://github.com/mapclient-plugins/multiplefilechooser'

# import class that derives itself from the step mountpoint.
from mapclientplugins.multiplefilechooserstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
