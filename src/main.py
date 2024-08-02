from ApiConnector.ApiConnector import getToken, callApi
from Utils.Utils import favoriteArtists, extractData

def main():
   print(extractData(getToken(),favoriteArtists()))

if __name__ == "__main__":
    main()