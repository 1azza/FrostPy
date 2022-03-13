import requests
from pprint import pprint
class Frost:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.s = requests.Session()
        self.s.headers = {
            "authority": "www.drfrostmaths.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "sec-ch-ua-mobile": "?0",
            "upgrade-insecure-requests": "1",
            "origin": "https://www.drfrostmaths.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://www.drfrostmaths.com/login.php?url=%2F",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        self.login()
        
        
    def login(self):
        url = "https://www.drfrostmaths.com/process-login.php"
        querystring = {"url": "/"}
        payload = f"login-email={self.email}&login-password={self.password}"

        response = self.s.request(
            "POST", url, data=payload, params=querystring)
        print(response)
    def Answers(self, aaid):
        import requests


        url = "https://www.drfrostmaths.com/homework/util-getassessmentattempt2.php"

        querystring = {"aaid": aaid, "": ""}
        payload = ""
        response = self.s.request(
            "GET", url, data=payload, params=querystring)
        print(response.text)
        
        
        
frost = Frost('017437@brgsmail.org.uk', 'larry1102')
frost.Answers()