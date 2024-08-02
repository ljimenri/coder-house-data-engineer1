from ApiConnector.ApiConnector import getToken, callApi

def main():
    print(callApi(getToken()))

if __name__ == "__main__":
    main()