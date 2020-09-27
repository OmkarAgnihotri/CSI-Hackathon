import requests

def errors(text):
    req = requests.get("https://api.textgears.com/check.php?text=" + text + "&key=NwcdTOgankW0Wt7b")
    no_of_errors = len(req.json()['errors'])
    return no_of_errors