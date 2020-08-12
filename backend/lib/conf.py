import os

import ruamel.yaml as yaml
from addict import Dict


def load(environment="common"):
    """Load configuration parameters for an environment, or the common
    configuration shared by all environments.
    """
    basedir = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )
    settingsdir = os.path.join(basedir, "backend", "main", "settings")
    filepath = os.path.join(settingsdir, "%s.yml" % environment)

    # Configuration file doesn't exists
    if not os.path.isfile(filepath):
        valid_environments = []
        for filename in os.listdir(settingsdir):
            filename_splitexted = os.path.splitext(filename)
            if filename_splitexted[-1] == ".yml":
                valid_environments.append(filename_splitexted[0])
        valid_environments.sort()

        valid_environments_msg = ""
        for i, valid_environment in enumerate(valid_environments):
            valid_environments_msg += '"%s"' % valid_environment
            if i == len(valid_environments) - 2:
                valid_environments_msg += " and "
            elif i < len(valid_environments) - 2:
                valid_environments_msg += ", "
        msg_schema = (
            "Attempt to load a configuration for an invalid"
            + ' environment "%s". Valid environments are %s.'
        )
        msg = msg_schema % (environment, valid_environments_msg)
        raise ValueError(msg)

    config = {}
    # Merge common and environment configurations
    if environment != "common":
        common_config_filepath = os.path.join(settingsdir, "common.yml")
        with open(common_config_filepath, "r") as f:
            common_config = yaml.safe_load(f)
        config.update(common_config)

    with open(filepath, "r") as f:
        config.update(yaml.safe_load(f) or {})

    return Dict(config)
