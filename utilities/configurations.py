import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    return "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"
