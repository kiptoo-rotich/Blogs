from .models import Quotes
import urllib.request, json

#Get the url
# quote_url=app.config["quote_url"]
quote_url='http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    quotes_list=[]
    new_quote_url=quote_url.format()
    with urllib.request.urlopen(new_quote_url) as url:
        get_data=url.read()
        get_responce = json.loads(get_data)
        id=get_responce['id']
        quote=str(get_responce['quote'])
        author=str(get_responce['author'])
        new_list=[id, quote, author]
        quotes_list.append(new_list)
    return quotes_list[0]
