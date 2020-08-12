import importlib
import os
import sys

sys.path.append(os.path.join("backend", "lib"))

conf = importlib.import_module("conf")
common_config = conf.load("common")

__name__ = common_config.name
if common_config.title is not None:
    __title__ = common_config.title
else:
    inflection = importlib.import_module("inflection")
    __title__ = inflection.humanize(__name__)
__author__ = common_config.author
__description__ = common_config.description
__version__ = common_config.version
__version_info__ = tuple([int(i) for i in __version__.split(".")])
