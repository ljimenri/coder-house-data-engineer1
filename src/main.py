from ApiConnector.ApiConnector import getToken
from Utils.Utils import favoriteArtists, extractData
from RedShiftConnector.RedShiftConnector import DataBaseConnection


def main():
   #print(extractData(getToken(),favoriteArtists()))
   DataBaseConnection()

if __name__ == "__main__":
    main()