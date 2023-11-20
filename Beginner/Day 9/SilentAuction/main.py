import os
clear = lambda: os.system('cls')
# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
	highest_bid = 0
	winner = ""
	#bidding_record = {"Uri": 100, "kingangi": 250}
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"the winner is {winner} with a bid of ${highest_bid} ")

while not bidding_finished:
  name = input("Enter your name?: ")
  price  = int(input("Enter your bid price $"))
  #Adding new values to the bids dictionary with the name as the key and price as value
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or no' ")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == 'yes':
    clear()
