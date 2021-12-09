This website will act as a platform where the user will interact with an intention to check the credibility of news. The user enters a news article in the space provided. This text is passed on to the machine learning model to predict the credibility or sentiment of the article. After backend processing, the final results are displayed to the users. 
We chose a web-based presentation with the hope that it will enable many users to view our results. The statistical analysis and machine learning module will make the judgements about a given article. 

Tools Used : PyCharm.

Libraries used: Pandas, sklearn, Flask, vaderSentiment, BeautifulSoup, TextBlob, urllib.request

Data Structures used: lists, dictionaries, files and dataframes.
 
Step 1: Predicting News Authenticity
•	Made necessary imports
•	Read dataset into data frames
•	Extracted text and labels from the data, and divided the whole dataset into test and train subsets.
•	Trained Passive Aggressive Classifier model and predicted results.
•	Calculated accuracy for test data.
•	Generated outputs for user data.

Step 2: News Sentiment Analysis
•	Made necessary imports
•	Used Vader Sentiment to analyze text/news, and TextBlob to find polarity of web-scraped news articles.
•	Categorized results as ‘positive’, ‘negative’ or ‘neutral’ based on polarity values.

Step 4: Developing Flask web application and implementing the first 3 steps       
•	Made the necessary imports.
•	Created 3 HTML pages for the web application.
o	The Home Page
o	News Authenticity Page, where user would get to know the authenticity of news entered into the textbox, and its sentiment as well.
o	Sentiment Analysis Page, where user would get to know the sentiment of text entered into the textbox, or the sentiment of news posted on either of the two websites: thehindu.com or thestar.com.
•	Implemented logic to trigger python functions and generate required results.
•	Used stylesheet and bootstrap to improve the visuals of web application.

     Evaluation and Analysis:

We evaluated our model using two metrices: accuracy and confusion matrix. The model scored an accuracy of >90%. It was observed that model was working very well with the data from our dataset, though we were getting some false postives and false negatives for the actual news articles since the data in our dataset seemed to be have collected in the past and needs to be updated for better results.
We are using the confusion matrix to depict the overall performance of our model while testing our test data.




