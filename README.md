# DOLAR ARGENTO
#### Video Demo:  <https://youtu.be/BOq7gotmVpA>
#### General Description:
I live in Argentina, where everybody is always checking the dolar rate exchange. The thing is that there are so many rate exchanges that it gets really messy... Today, there are 19 different rates, but it changes everyday.
The thing is that not everybody can access to all rate exchanges. So, most of us, are just interested in just 3 or 4. This is how this project comes to life.

Dolar Argento is a twitter bot that tweets twice a day 3 different rate exchanges, available for most people
who want to buy US Dolars with Argentinian Pesos.

#### Twitter:
I chose twitter, because is a social network I use all the time. I have already seen bots like this, so I knew it was doable. I also believe that this info is useful for the Argentinian community.
I had a secondary twitter account, that I wasn't using. I changed its name to @Dolar_Argento, styled it accordingly and then I requested essential access at the Twitter Developer Portal. I created the project, got the proper keys and tokens and was set to code.

#### The script:
The script is written in two .py files and one .env file:
- .env: is a list of my twitter project keys and tokens. 
- dolar.py is in charge of retrieving the exchange rate from 2 different websites, where I usually check this information. To do so, I used the BeatifulSoup library that allowed me to scrap information from these websites.
- tweet.py handles the creation of 2 tweets that should be posted at different hours. The first tweet gets posted every morning at 10 am UTC-3 (when Argentinian market opens), and the other one at 4 pm UTC-3 (when it closes). I set this up using the Schedule library. At each time, the script would call 3 functions from "dolar.py": dolarBlue(), dolarTC() and dolarCripto(), get the updated information and add it to a tweet-template that ends with the time the tweet is meant to be posted.

#### Deployment:
I decided to deploy the bot in Heroku's server, so it would run from there.
To do so, I created a few extra files to my project: 
- .gitignore: copied from [GitHub/Python.gitignore] (https://github.com/github/gitignore/blob/main/Python.gitignore)
- Procfile: where I added a web and worker command.
- requirements.txt: recorded with `pip freeze > requirements.txt` command.
- runtime.txt: where I copied my python version.
All of these files, plus tweet.py and dolar.py where deployed over 30 times before I could make it work.
My major problem here was that my OS is set with local time and Heroku runs with UTC, so I had to get creative to make it work.

And that's all folks!
Thank you for this journey :D
