# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:26:51 2019

@author: hibbep01
"""

################################################################################

### Load required packages ###
import requests, json
import sys

ATIbit = True
Slackbit = True
rowsPerCall = 10000


apikey = '<API-Key here>'

if(ATIbit):

    ##### Check call is valid
    if rowsPerCall > 10000:
        print("ERROR: Maximum 10,000 rows for ATI calls.")
        sys.exit(1)
    print("Pull data from ATI...")
    
    urlData = "https://api.atinternet.io/data/v2/json/getData?&" \
              "columns={m_uv}&sort={-m_uv}&space={s:598255}&" \
              "period={R:{D:'-1'}}&max-results=" + str(rowsPerCall) + "&page-num=1&" \
              "api-key=" + str(apikey)

    responseData = requests.get(urlData)
    print("...done.")
    j=json.loads(responseData.content)
    a = j.get('DataFeed')
    c = a[0]
    d = c["Rows"]
    list_len = len(d)
    visitor_num = d[0]["m_uv"]
    print (visitor_num)
    


    ##### Check call is valid
    if rowsPerCall > 10000:
        print("ERROR: Maximum 10,000 rows for ATI calls.")
        sys.exit(1)
    print("Pull data from ATI...")
    
    urlData = "https://api.atinternet.io/data/v2/json/getData?&" \
              "columns={cl_461489,cl_461485,m_visits}&sort={-m_visits}&space={s:598255}&" \
              "period={R:{D:'-1'}}&max-results=" + str(rowsPerCall) + "&page-num=1&" \
              "api-key=" + str(apikey)

    responseData = requests.get(urlData)
    print("...done.")
    j=json.loads(responseData.content)
    a = j.get('DataFeed')
    c = a[0]
    d = c["Rows"]
    list_len = len(d)
    url = d[0]["cl_461485"]
    title = d[0]["cl_461489"]
    title = title[:-10]
    visits = d[0]["m_visits"]
    print (visits)


image1 = "https://amp.businessinsider.com/images/5aa94e7542e1cc03fc5c520d-750-500.jpg"
image2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxWam3IqIjicKtHbOsaK9hv5pnZ4sEmSi_XsC_IDnr-x-UNkSTkQ"
image3 = "https://scugogarts.ca/wp-content/uploads/2018/07/dogdays.jpg"
image4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC0lBkmD6h7l5wrZQxlRybsLrWLAVrIdF9d1F3IqRhuOANk7XYng"
image5 = "https://amp.thisisinsider.com/images/5b22bda45e48ec22008b46b5-960-720.jpg"
image6 = "https://static01.nyt.com/images/2012/04/17/blogs/well-fatpetsub/well-fatpetsub-tmagArticle.jpgg"
image7 = "https://www.petguide.com/wp-content/uploads/2015/01/fat-dog.jpg"
image8 = "https://i.kinja-img.com/gawker-media/image/upload/s--UYWaK5eN--/c_scale,f_auto,fl_progressive,q_80,w_800/kxrrj90hprbpcd1pco4p.jpg"
image9 = "https://d1w9csuen3k837.cloudfront.net/Pictures/480xany/5/1/1/123511_fat-dog-250_tcm18-74998.jpg"
image10 = "https://i.redd.it/vzsr5bd6hx421.jpg"
image11 = "https://i.pinimg.com/236x/4e/17/88/4e1788791490fce3267aa450985bc897--im-fat-fat-animals.jpg"


if visitor_num < 50000:
    chosen_image = image1
    chosen_text = "Chonk free"
elif  50000 <= visitor_num < 100000:
    chosen_image = image2
    chosen_text = "Chonk Zero"
elif  100000 <= visitor_num < 150000:
    chosen_image = image3
    chosen_text = "Diet Chonk"
elif  150000 <= visitor_num < 200000:
    chosen_image = image4
    chosen_text = "Lean and Mean"
elif  200000 <= visitor_num < 250000:
    chosen_image = image5
    chosen_text = "Pleasant Chonk"
elif  250000 <= visitor_num < 300000:
    chosen_image = image6
    chosen_text = "Chonk medium"
elif  300000 <= visitor_num < 350000:
    chosen_image = image7
    chosen_text = "A Fine Boi"
elif  350000 <= visitor_num < 400000:
    chosen_image = image8
    chosen_text = "A Heckin Chonk"
elif  400000 <= visitor_num < 450000:
    chosen_image = image9
    chosen_text = "HEFTY CHONK"
elif  450000 <= visitor_num < 500000:
    chosen_image = image10
    chosen_text = "MEGACHONKER"
elif  500000 <= visitor_num:
    chosen_image = image11
    chosen_text = "OH LAWD HE COMIN"


channel_webhook = '<Slack channel webhook here>'

if(Slackbit):
    value = 100
# Send to slack
    whUrl = channel_webhook
    payload = {"text":"Look how many UVs we had yesterday: " + str(visitor_num),
             "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#2eb886",
            "pretext": "The Top article was _" + str(title) + "_ with " + str(visits) + " visits",
#            "author_name": "Chonky Boi",
#            "author_link": "http://flickr.com/bobby/",
#            "author_icon": "http://flickr.com/icons/bobby.jpg",
            "title": "Visual representation of yesterday's traffic: " + str(chosen_text),
            "title_link": url,
#            "text": "Optional text that appears within the attachment",
            "image_url": chosen_image,
#            "ts": 123456789
        }
    ]}


    r = requests.post(whUrl, data = json.dumps(payload))
