from ApiConnector.ApiConnector import getToken
from Utils.Utils import favoriteArtists, extractData
from RedShiftConnector.RedShiftConnector import CreateTableArtists


def main():
   print(type(extractData(getToken(),favoriteArtists())))
   CreateTableArtists()

if __name__ == "__main__":
    main()