from fastapi import FastAPI # type: ignore
import random
app = FastAPI()

#? we will buils to simple endpoints
#*  side_hustles
#*  money_quotes

side_hustles = [
    "Freelance web development",
    "Affiliate marketing",
    "Print-on-demand store",
    "Dropshipping",
    "Selling digital products",
    "Stock photography",
    "YouTube content creation",
    "Blogging",
    "Online tutoring",
    "Social media management",
    "Virtual assistant",
    "App development",
    "Graphic design",
    "Video editing",
    "Copywriting",
    "Podcasting",
    "Selling handmade crafts on Etsy",
    "Reselling products on eBay or Amazon",
    "Flipping domain names",
    "Online course creation",
    "Ghostwriting",
    "T-shirt business",
    "AI automation services",
    "Stock trading or crypto investing",
    "Handyman services",
    "Car rental business (Turo)",
    "Personal training or fitness coaching",
    "Pet sitting or dog walking",
    "Event planning",
    "Voice-over acting"
]

money_quotes = [
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "The best way to predict the future is to create it. – Peter Drucker",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki",
    "Wealth consists not in having great possessions, but in having few wants. – Epictetus",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "Don’t work for money, make money work for you. – Robert Kiyosaki",
    "The stock market is designed to transfer money from the Active to the Patient. – Warren Buffett",
    "Rich people stay rich by living like they’re broke. Broke people stay broke by living like they’re rich. – Unknown",
    "Too many people spend money they haven’t earned, to buy things they don’t want, to impress people they don’t like. – Will Rogers",
    "A budget is telling your money where to go instead of wondering where it went. – Dave Ramsey",
    "Time is more valuable than money. You can get more money, but you cannot get more time. – Jim Rohn"
]

@app.get('/side_hustles')
def get_side_hustles(apikey:str):
    
    '''Return a simple Side Hustle Idea from List'''
    if(apikey != '1234567890'):
        return {'error':'api keys invalid'}
    else:
        return {'side_hustles': random.choice(side_hustles)}
@app.get('/money_quotes')
def get_money_quotes():
    '''Return a simple Money Quotes  from List'''
    return {'money_quotes': random.choice(money_quotes)}

#! (command for running fast api ) fastapi dev [file_name] 