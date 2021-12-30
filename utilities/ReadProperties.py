import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'user_email')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

