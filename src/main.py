from ApiConnector.ApiConnector import getToken
from Utils.Utils import favoriteArtists, extractData
from RedShiftConnector.RedShiftConnector import CreateTableArtists, InsertTableArtists


def main():
   CreateTableArtists()
   InsertTableArtists(extractData(getToken(),favoriteArtists()))

if __name__ == "__main__":
    main()