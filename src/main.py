from ApiConnector.ApiConnector import getToken
from Utils.Utils import favoriteArtists,favoriteAlbum, extractData, extractDataAlbum
from RedShiftConnector.RedShiftConnector import CreateTableArtists, InsertTableArtists


def main():
   CreateTableArtists()
   InsertTableArtists(extractData(getToken(),favoriteArtists()))
   extractDataAlbum(getToken(),favoriteAlbum())

if __name__ == "__main__":
    main()