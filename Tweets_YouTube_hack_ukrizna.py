# -*- coding: utf-8 -*-      

import urllib2, json, codecs, re

from time import sleep
from bs4 import BeautifulSoup
import requests_oauthlib
from oauthlib import oauthlib
import tweepy





#Twitter App keys and Access token
Consumer_Key = 'tnvK1M6lAfSerDHnWgB1NA';
Consumer_Secret = 'hRb8QVPAJ2IqlWQhToIZDa0YJ91oewfny3dt6Zjg8';
Access_Token = '76027237-ecsRTfuhF0aIwUHbYgUPJ3zghgLM4GXhEjkj2L20j';
Access_Token_Secret = '8c2t21z2lCQfQynYgZqD5Ee5ArqBgvwwWoVSxVdGfwppS';


# IDs of 5 selected YouTube videos of "classic" movie trailers. These are the first responses in the YouTube search
video_id = ["o4gHCmTQDVI", "6hB3S9bIaco", "zCy5WQ9S4c0", "sY1S34973zA", "UWio-Umb424"];

count =[]
num =[]
for index in range(len(video_id)):
    id = video_id[index];
	#XML format data about the particular video
    url = 'https://gdata.youtube.com/feeds/api/videos/%s?video_id'%id
    u = urllib2.urlopen(url);
    data = u.read(); 
    data_bs = BeautifulSoup(data);
    data_pretty = data_bs.prettify();
    #Extracting the title
    title = data_bs.title.string
	#A wordlist that has stop words and other words to filter
    words_list = ["trailer", "Trailer", "The", "A", "first look", "teaser", "HD", "Official", "Teaser", "First Look", "First look", "first Look"]
    title2 = title.replace("[^a-zA-Z]"," ");
    for word in words_list:
        if word in title2:
            title2 = title2.replace(word, "");
   
    title2 = title2.split();
    if (len(title2)>1):
        title = title2[0]+" "+title2[1]
    else:
        title = title2[0]
    
	#XML format comments data about the video
    comment_url = 'https://gdata.youtube.com/feeds/api/videos/%s?video_id/comments'%id
    comments = urllib2.urlopen(comment_url);
    data2_bs = BeautifulSoup(comments.read());
    data2_pretty = data2_bs.prettify();
    gdata = str(data2_pretty);
	#Storing the info in a file
    fname = 'C:\Python27\gdata'+str(index)+'.txt';
    file = open(fname, 'w');
    file.write(gdata);
    file.close()
    
    
	#Getting the counthint i.e. the number of YouTube comments.
    file = open(fname, 'rU')
    for line in file:
        m = re.findall('counthint=',line)
        if m:
            ct = re.findall('\d+', line)
            print ct[0];
            count.append(int(ct[0]));
            
            
		
    #Establishing connection with Twitter via Tweepy
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)
    api = tweepy.API(auth);
    cursor1 = tweepy.Cursor(api.search, q=title, result_type = "recent").items(100)
    cursor = tweepy.Cursor(api.search, q=title, result_type = "popular")
    tweets = [];
    ctweet = [];
    for items in cursor.items():
        tweet = items.text.encode('ascii', 'ignore');
        tweets.append(tweet);
        sleep(1)
	
	
    #Counting the number of tweets
    if (tweets != None):
        l = len(tweets);
        num.append(l);		
        print l;
        #print tweets;
        
    else:
        l =0;
        
    #Getting the top 5 tweet on the YouTube movie trailer title.
    cursor = tweepy.Cursor(api.search, q=title, result_type = "popular").items(5);
    for items in cursor:
        print items.text.encode('ascii', 'ignore');
        sleep(1)

ratio = [float(ctc)/float(ctt) for ctc,ctt in zip(count, num)]
print "YouTube Comments Count= "
print count
print "Popular Tweet Count="
print num
print "Ratio="
print (ratio) 

#normalizing the count of tweets and count of YouTube comments.
div_mul = 10;
norm_ct = [x/div_mul for x in count]
norm_num = [x*div_mul for x in num]
print "normalized tweet count="
print norm_num
print "normalized comment count="
print norm_ct

#Using Google Chart API to draw the chart
from GChartWrapper import *
G = VerticalBarGroup([norm_num,norm_ct],encoding='simple')
G.color('4d89f9','c6d9fd')
G.size(5,10)

#conversion of list to string for api call of google chart api
def list2String(x):
    data = "";
    for i in x:
        data += str(i)+","
    return data[0:len(data)-1]
	
#For bar graph - querying the right url with the key parameters.
query_url = "http://chart.apis.google.com/chart?chxt=x,y&chxl=0:|Prestige|Shawshank|Titanic|Godfather|RockyBalboa&chs=500x500&cht=bvg&chco=0A8C8A,EBB671&chdl=PopularTweets_Count*10|YouTubeComments_Count/10&chd=t:"
query_url +=list2String(norm_num[0:5])+"|"+list2String(norm_ct[0:5])+"&chxr=1,0,1000&chds=0,1000"
#retrieving the file
chart = urllib2.urlopen(query_url) 
#saving chart to an image file.
f = open('C:/Python27/chart.png',"wb")
f.write(chart.read())
f.close();





 