import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get('common info', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('common info', 'useremail'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('common info', 'password'))
        return password


#Testing above methods - optional Code
'''print(ReadConfig.getApplicationURL())
print(ReadConfig.getUseremail())
print(ReadConfig.getPassword())'''
