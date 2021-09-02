from threading import Thread
import requests, time

class HtmlGetter(Thread):
    def __init__(self, url):
        # super().__init__()
        Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)

t = HtmlGetter('https://google.com')
t.start()
print("### End ###")
