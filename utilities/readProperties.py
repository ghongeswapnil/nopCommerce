import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")                    # here we need to specify path of the config file
# config.read("E:\Automation\nopcommerceApp\Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
