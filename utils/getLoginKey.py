import requests
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random


# account="detect usage brick another edge diagram gym sense tube you paddle insect inquiry student token inside multiply olympic jeans lucky client disagree treat license"

def login(account):
    headers = {
        "User-Agent": user_agent,
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "text/plain",
        "Referer": "https://www.creoplay.app/",
    }
    url = f"https://m84784bbba.execute-api.ap-southeast-1.amazonaws.com/production/authentication/wallet/login"
    payload = {"wallet_id": account}
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data["data"]["api_token"]


def get_login_key(api_token):
    headers = {
        "User-Agent": user_agent,
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "text/plain",
        "Authorization": "Bearer " + api_token,
        "Referer": "https://www.creoplay.app/",
    }
    url = f"https://m84784bbba.execute-api.ap-southeast-1.amazonaws.com/production/authentication/login-key"
    response = requests.post(url, headers=headers)
    data = response.json()
    return data["data"]["login_key"]


def createLoginKey(account):
    api_token = login(account)
    loginKey = get_login_key(api_token)
    return loginKey


def main():
    accounts = [
        "ill begin idle modify verify try park arm awesome search ring toast",
        "pole sea prison total stock fluid idle edit indicate hidden weather crime",
        "health close fine stem barely palace real orchard disease useful umbrella eight",
        "position opinion grab cruel onion move return stock warm reunion universe sample",
        "gospel badge rug six gallery jealous own census salad speak meadow spice",
        "base mimic side syrup share scorpion slow senior neglect gravity script rose",
        "vague flower family rival eagle universe frost south adapt exile post void",
        "onion output this sleep analyst dutch dumb ask snake aerobic diagram depart",
        "dragon lemon cradle little census bracket congress modify chronic box unusual satoshi",
        "party obey follow glove hip switch post post hub input divide asset",
        "detect usage brick another edge diagram gym sense tube you paddle insect inquiry student token inside multiply olympic jeans lucky client disagree treat license",
    ]

    loginKeys = []

    for account in accounts:
        loginKeys.append(createLoginKey(account))
    print(loginKeys)


if __name__ == "__main__":
    main()
