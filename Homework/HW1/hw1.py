#  Build a piece of software for a ﬁnancial institution to model one of their clients’ portfolios. 
# Create a portfolio can consist of 3 types of items:
#   • Cash can be added to a portfolio, removed from a portfolio or used to buy stocks/mutual funds. 
#   • Stock can be purchased with existing cash in the portfolio, or sold (adding cash to the portfolio). 
#		Note that stocks can only be purchased or sold as whole units. Stocks have a price and ticker symbol. 
# 		For simplicity’s sake, Stocks can be purchased for $X/share and when sold are sold for a price that 
# 		is uniformly drawn from [0.5X-1.5X] 
# 	• Mutual Funds can be purchased with existing cash in the portfolio, or sold (adding cash to the portfolio). 
#		Note that mutual funds can only be purchased as fractional shares. Mutual funds have a price and ticker 
#		symbol. For simplicity’s sake, Mutual funds can be purchased for $1/share and when sold are sold for a
#		price that is uniformly drawn from [0.9-1.2]
#
# Your program must facilitate managing the correct balance of cash, stocks and mutual funds as the user buys 
# and sells items. Assume that the person using your library will specify the correct buy price so you can 
# trust it and just need to maintain a proper internal state given the speciﬁed buy price (and then compute 
# some sell price using the above formulas). Finally, in order to help with customer service your portfolio
# software needs to keep an audit log of all transactions and make them available to users of your program. 
# You can implement this software however you wish, but a consumer of the application must at a minimum be 
# able to do the following:

#portfolio = Portfolio() #Creates a new portfolio 
#portfolio.addCash(300.50) #Adds cash to the portfolio 
#s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH" 
#portfolio.buyStock(5, s) #Buys 5 shares of stock s 
#mf1 = MutualFund("BRT") #Create MF with symbol "BRT" 
#mf2 = MutualFund("GHT") #Create MF with symbol "GHT" 
#portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT" 
#portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT" 
#print(portfolio) #Prints portfolio 
					#cash: $140.50 #stock: 5 HFH
					#mutual funds: 10.33 BRT # 2 
#GHT portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT 
#portfolio.sellStock("HFH", 1) #Sells 1 share of HFH 
#portfolio.withdrawCash(50) #Removes $50 
#portfolio.history() #Prints a list of all transactions #ordered by time


#Create class for Portfolio
class Portfolio(object): 
	def __init__(self):
		self.Cash = []
		self.Stock = {}
		self.MutualFund = {}
		self.history = {}
	
	# Define functions for Cash transactions
	def addCash (self, value):
		self.Cash.append(value) # Add cash value to the Cash in the portfolio
		self.history.append("Added $%s to the portfolio." % value) # Add cash transaction to history
		print "%d USD cash added to your portfolio." % value 
	def withdrawCash(self, value):
		self.Cash.append(-(value)) # Withdraw cash value to the Cash in the portfolio
		self.history.append("Withdrawn $%d from the portfolio." % value) # Add cash transaction to history
		print "%d USD has been withdrawn from your cash portfolio." % value
	
	# Define functions to manage Stock
	def buyStock(self, s_quantity, s_ticker):
		self.Stock[s_ticker.name] = quantity # Adds ticker name to the Stock dictionary in Portfolio. 
		new_balance = self.Cash.append(-(s_quantity * s_ticker.price)) # Debit the accoount for the purchase of the stock.
		print """
		You have purchased %d shares of %s stock. Your new account balance is %d USD.
		""" % (s_quantity, s_ticker.name, new_balance)
	def sellStock(self, s_quantity, s_ticker):
		self.Stock[s_ticker] -= s_quantity # Delete the sold shares of stock from dictionary in Portfolio
		new_balance = self.Cash.append(s_ticker.price * random.uniform(.5,1.5)) #Add the value of the shares sold to the cash account
		print """
		You have sold %d shares of %s stock at %d USD a share. Your new account balance is %d USD.
		""" % (s_quantity, s_ticker, random.uniform(.5,1.5), 5 * random.uniform(.5,1.5))
		
		
	# Define function to manage Mutual Funds
	def buyMutualFund(self, mf_quantity, mf_ticker): 
		self.MutualFund[mf_ticker.name] = quantity # Adds ticker to the Mutual Fund dictionary in Portfolio
		new_balance2 = self.Cash.append(-(mf_account)) # Debits the account for the purchase of the mutual fund
		print """
		You have purchased %d shares of %s mutual fund. Your account balance is %d USD.
		""" % (mf_quantity, mf_ticker.name, new_balance2)
	def sellMutualFund(self, mf_quantity, mf_ticker):
		self.MutualFund[fund] -= mf_quantity # Delete sold shares of mutual funds from dictionary 
		new_balance2 = self.Cash.append(mf_quantity * random.uniform(.9, 1.2)) # Adds the value of the mutual fund sold to the portfolio
		print """
		You have sold %d shares of %s mutual fund. Your new account balance is %d USD.
		""" % (mf_quantity, mf_ticker, new_balanace2)
	
	def __repr__(self): 
		return "Portfolio ()"
	
	# To print the value of the portfolio
	def __str__(self):
  		return """
  				Portfolio Value:\n
      			\n
      			Cash Balance: $ %s \n
      			Stock(s): %r \n
      			Mutual Fund(s): %r \n 
      			""" % ("%.2f" % sum(portfolio.Cash), portfolio.Stock, portfolio.MutualFund)

# Create class for Stock
class Stock():
	def __init__(self, s_price, s_ticker): # Add  arguments for the class
		self.s_price = s_price # Assign the input for price of the stock
		self.s_ticker = s_ticker # Assign the input for ticker of the stock
		print "%s stock at %d USD a Share" % (s_ticker, s_price) 
  		
# Create class for Mutual Fund
class MutualFund(): 
	def __init__(self, mf_ticker): # Add arguments for the class
		self.mf_ticker = mf_ticker # Assign the input for ticker of the mutual fund 
		print "Mutual Fund - %s." % mf_ticker   

# Required functions/testing
portfolio = Portfolio() # Create the object of the portfolio class		
s = Stock(20, "HFH")
mf_brt = MutualFund("BRT") # Create BRT mutual fund
mf_ght = MutualFund("GHT") # Create GHT mutual fund		
portfolio.addCash(300.50) # Add $300.50  cash
portfolio.withdrawCash(50) # Withdraw $50 cash
portfolio.buyStock(5, s) # Buy 5 shares of the object s which was created
portfolio.sellStock("HFH", 1) # Sell 1 share of HFH stock
portfolio.buyMutualFund(10.3, mf1) # Buy 10.3 shares of BRT mutual fund
portfolio.buyMutualFund(2, mf2) # Buy 2 shares of GHT mutual fund
portfolio.sellMutualFund("BRT", 3) # Sell 3 shares of BRT mutual fund
print(portfolio)
