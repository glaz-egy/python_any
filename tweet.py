import twitter
import configparser
import re

config = configparser.ConfigParser()
config.read('api.ini')

api = twitter.Api(consumer_key=config['OAuth']['consumer_key'],\
                consumer_secret=config['OAuth']['consumer_secret'],\
                access_token_key=config['OAuth']['access_token_key'],\
                access_token_secret=config['OAuth']['access_token_secret'])

def get_tweet(api, count=200):
    statuse = api.GetUserTimeline(config['User']['user_id'], count=count)
    with open('textdata.txt', 'r', encoding='utf-8') as f:
        ExistData = f.readlines()
    for s in statuse:
        MucthText = re.search(r"@.*\s", s.text)
        texts = s.text if MucthText is None else MucthText.string.replace(" ", "")
        MucthText = re.search(r"http.*", texts)
        texts = texts if MucthText is None else texts.replace(MucthText.group(0), '')
        MucthText = re.search(r"#.*", texts)
        texts = texts if MucthText is None else texts.replace(MucthText.group(0), '')
        if not "RT" in texts and None == s.retweeted_status and re.match(r".*@.*(より|さんから)", texts) is None:
            texts = texts.strip().split('\n')
            print(texts)
            for text in texts:
                if not text == '\n' and not text == '' and re.match(r"\s+", text) is None and not text+'\n' in ExistData:
                    ExistData.append(text)
                    with open('textdata.txt', 'a', encoding='utf-8') as f:
                        f.write(text+'\n')

if __name__=='__main__':
    get_tweet(api)