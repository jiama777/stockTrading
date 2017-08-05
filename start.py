from googlefinance import getQuotes
from googlefinance import getNews
from yahoo_finance import Share
from twilio.rest import Client
import json
import csv


class Stock:
	def __init__(self,  symbol, name, lastSale, marketCap, ipoYear, sector, industry):
		self.symbol = symbol
		self.name = name
		self.lastSale = lastSale
		self.marketCap = marketCap
		self.ipoYear = ipoYear
		self.sector = sector
		self.industry = industry

account = "AC75b0087dabc02d842e690f0d33af1072"
token = "ecaf1b7bfc6304315431bc2917c49861"
client = Client(account, token)

##yahoo = Share('GOOGL')
##print json.dumps(yahoo.get_open(), indent=2)
##print json.dumps(yahoo.get_year_low(), indent=2)
print("\n\n") 
print( "**************************************")
print("     	Ivy, I Love You! 			")
print("**************************************")
print("\n\n")

stockArray = []
csvfile = open('companylist.csv', 'r')
fieldnames = ("Symbol","Name","LastSale", "MarketCap", "IPOyear", "Sector", "industry")
reader = csv.DictReader(csvfile, fieldnames)
reader.next()

for row in reader:
	s = Stock(row["Symbol"], row["Name"], row["LastSale"], row["MarketCap"], row["IPOyear"], row["Sector"], row["industry"])
	stockArray.append(s)

for s in stockArray:
	try:
		quoteFromGoogle = getQuotes(s.symbol)
		shareFromYahoo = Share(s.symbol)
		todaysPrice = quoteFromGoogle[0]["LastTradePrice"]
		yearLow = shareFromYahoo.get_year_low()

		print("Today's price for " + s.symbol + " is " + todaysPrice)
		print("52 Year Low: " + yearLow)

		if float(todaysPrice) <= float(yearLow):
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			body = "Ivy, " + s.symbol + " (" + s.name + ") " +" is now at 52 weeks low!! \n Today's price is at $" + todaysPrice + "; 52 weeks low was $" + yearLow + "\n Love you! \n Jia Ma"
			message = client.messages.create(to="+14152793685", from_="+15109015113", body=body)
			
			print(body)
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	except:
		print("#####################################")
		print(s.symbol + " is not invalid")
		print("#####################################")

print("*************** DONE **************************")


