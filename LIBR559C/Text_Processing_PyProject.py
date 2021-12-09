#Importing alll required libraries
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup as bs, BeautifulSoup
from textblob import TextBlob
from urllib.request import Request, urlopen
from sklearn.metrics import accuracy_score

app = Flask(__name__)

tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)  #initializing Tfid-Vectorizer for english words
dataframe = pd.read_csv('C:\\Users\\manki\\PycharmProjects\\Fake_News_Detection-master\\news.csv')
labels=dataframe.label
text = dataframe['text']

x_train, x_test, y_train, y_test = train_test_split(text, labels, test_size=0.2, random_state=7) #spliting data into test and train datas
tfid_train = tfvect.fit_transform(x_train)     #transforming train data
tfid_test = tfvect.transform(x_test)           #transforming test data
pac = PassiveAggressiveClassifier(max_iter=50)   #initializing model
pac.fit(tfid_train, y_train)

y_pred = pac.predict(tfid_test)
score=accuracy_score(y_test,y_pred)
print(score)


#This function starts the web scraping process, and takes an argument to select which website to scrape from
#It then calls the other functions which all together work to extract the text and perform sentiment analysis
#It creates a soup object and passes to next function
def st(msg):
    newsPaper = {}
    if msg == 'two':
        url = 'https://www.thestar.com/vancouver.html?redirect=true'
    else:
        url = 'https://www.thehindu.com/news/international/?page=1'

    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='html')
    if msg == 'two':
        titles, links = parser2(soup)
    else:

        titles, links = parser1(soup)
    return sentimentAnalysis(newsPaper, titles, links,msg)


#These two functions-parser1 and parser2 finds the required html elements and extract the news titels and their url links
def parser1(soup):
  titles = []
  links = []
  for news in soup.find_all("div", class_= "story-card-news"):
    if news.h3==None:
        continue
    title = news.h3.text
    link = news.find_all('a')
    titles.append(title)
    links.append(link[2]['href'])
  print(titles,links)
  return  titles, links


def parser2(soup):
    titles = []
    links = []
    for news in soup.find_all("a",class_="c-mediacard c-four-story-veritcal-right-hero-medium__story c-mediacard--column"):
        if news.h3.text==None:
            continue
        titles.append(news.h3.text)
        links.append("https://www.thestar.com"+news['href'])
    return titles,links

#This function takes news arrticles url links and extract the text from <p> elements
def newsStoryGrabber(links,msg):
  data=[]
  for i in range(len(links)):
    url = links[i]
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, features='html')
    if msg=='one':
        aa = soup.find('div', class_='article')
        bb = aa.find_all('p')
        cc = bb[1].text + bb[2].text
        data.append(cc)
    else:
        aa = soup.find('div', class_='c-article-body')

        for news in aa.find_all('p'):
            data.append(news.text)
  return data


# take the { title:article } dictionary and runs sentiment
def newsAnalysis(dataDiX):
    sent = []
    sentVal = []
    for news in list(dataDiX.values()):
        analysis = TextBlob(news)
        sentiment = find_Sentiment(analysis.sentiment.polarity)
        qq = analysis.sentiment.polarity
        sentVal.append(qq)
        sent.append(sentiment)
    return sent, sentVal

#This function categorizes polarity values
def find_Sentiment(val):
    if val <= 0.1 and val > -0.1:
        return 'Neutral'
    elif val > 0.1:
        return 'Positive'
    else:
        return 'Negative'

#This function creates list of all news articles scraped from web containing their titles, sentiment and polarity scores
def listMaker(newsPaper, titles, sent, sentVal, lists):
    totalSent = 0
    for i in range(len(newsPaper)):
        sas = titles[i] + ' : ' + sent[i] + ' : ' + str(sentVal[i])
        totalSent += sentVal[i]
        lists.append(sas)
        lists = [x.replace('\n', '') for x in lists]
    return lists, totalSent

#This function requests news article text from newsStoryGrabber function by providing news links
#It then sends this text to newsAnalysis to get the sentiment
#Finally returns list containing dictionary of news titles and thier sentiments
def sentimentAnalysis(newsPaper, titles, links,msg):
    lists = []
    stories = newsStoryGrabber(links,msg)
    newsPaper = dict(zip(titles, stories))
    sent, sentVal = newsAnalysis(newsPaper)
    lists, totalSent = listMaker(newsPaper, titles, sent, sentVal, lists)
    return_list=[]
    for i in range(len(newsPaper)):
        print(lists[i])

        return_list.append({titles[i]:(find_Sentiment( float(lists[i].split(":")[-1])))})
        #a={'result':lists[i].split(":")[1]}
        #return_list.append(a)
    print(return_list)
    return return_list




#Predict news authenticity for user input data
def fake_news_det(news):
    tfid_test = tfvect.transform([news])
    y_pred = pac.predict(tfid_test)
    return y_pred


    #input_data = [news]
    #vectorized_input_data = tfvect.transform(input_data)
    #prediction = loaded_model.predict(vectorized_input_data)
    #return prediction


#Reviews sentiment
def reviewNature(review):
    ob = SentimentIntensityAnalyzer()
    result = ob.polarity_scores(review)


    if result['compound'] >= 0.5 :
        return 1
    elif result['compound'] <=-0.5:
        return -1
    else:
        return 0


#These functions are used to route to an HTML page, and call the above defined functions to get results for user input data
@app.route('/')
def home1():
    return render_template('first.html')
@app.route('/authentic')
def home2():
    return render_template('index.html')
@app.route('/analysis')
def home3():
    return render_template('sentiment.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred = fake_news_det(message)
        nature=reviewNature(message)
        print(pred)
        print(nature)

        return render_template('index.html', prediction=pred,sentiment=nature)
    else:
        return render_template('index.html', prediction="Something went wrong")


@app.route('/sentiment', methods=['POST'])
def sentiment():
    if request.method == 'POST':
        message = request.form['message']

        sentiment=reviewNature(message)
        return render_template('sentiment.html',sentiment=sentiment)
    else:
        return render_template('index.html', prediction="Something went wrong")

@app.route('/webscrape', methods=['POST'])
def webscrape():
    if request.method == 'POST':
        message = request.form['optradio']

        sentiment_dict=st(message)
        return render_template('sentiment.html',websenti=sentiment_dict)
    else:
        return render_template('index.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)