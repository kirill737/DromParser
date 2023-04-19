import requests
class Downloader:
    # def __init__(self, url, method="GET"):
    #     self.urls = url
    #     #self.paramss = params
    #     self.methods = method
    #
    # def get_html(self):
    #     if self.methods == "GET":
    #         return requests.get(self.urls).text

    def __init__(self, url, params=None, method="GET"):
        self.url = url
        self.params = params
        self.method = method

    def get_html(self):
        response = requests.request(self.method, self.url, params=self.params)
        return response.text

    def save(self, path):

        file = open(path, "w+")
        file.write(self.get_html())
        file.close()