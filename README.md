# [@holyshiitbot](https://twitter.com/holyshiitbot)

[@holyshiitbot](https://twitter.com/holyshiitbot) is a Twitter bot that tweets "this is fine" meme with a random word in the sentence.


## How to Install
This script is wrote in [Python](https://www.python.org)

You need to:

1. Install [Pillow](https://pypi.org/project/Pillow/)

    `pip install Pillow`
2. Install [Tweepy](https://pypi.org/project/tweepy/)

    `pip install tweepy`
3. Create an apps in your developer Twitter account
4. Download the holy\_shiit_bot repository
5. In the repository, creat a conf.py file and write this following code and replace that is in between double quote by your API Key and token
```python
API_key = "API_KEY"
API_secret_key = "API_SECRET_KEY"
Access_token = "ACCESS_TOKEN"
Access_token_secret = "ACCESS_TOKEN_SECRET"
```
6. Open a terminal in the holy\_shiit_bot repository and write the following line to execute the bot

    `python holy_shiit_bot_script.py`

## Algorithme
1. Get a word from this [noun list](http://www.desiquintans.com/downloads/nounlist/nounlist.txt)
    * Delete the word from the list.
    * If the word is too large, get another.

2. Creat the image out with the icecremex3's [Cees Hand Regular](https://www.dafont.com/fr/cees-hand.font) font
    * Creat the midle sentence.
    * Center the midle sentence in the comic strip bubble.
    * Generate the image out.

3. Tweet.
    * Tweeter authentification key API
    * Tweet the image out.

## License
The source code of this bot is available under the terms of the [MIT license](http://www.opensource.org/licenses/mit-license.php)