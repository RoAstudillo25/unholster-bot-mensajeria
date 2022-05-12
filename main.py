from pip._vendor import requests

if __name__ == "__main__":
    url = "https://hooks.slack.com/services/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"
    msg = input("introducir mensaje -> ")
    result = requests.post(url, json = {'text': msg})

    if(result.text == "ok"):
        print("Successful")
    else:
        print(result.text)  