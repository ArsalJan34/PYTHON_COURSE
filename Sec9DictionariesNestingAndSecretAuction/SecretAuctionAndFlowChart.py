# Ask user for input
name = input("What is your name? : ")
Price = int(input("What is your bid?  : $"))


bids ={}
# save the data into dictionary {name: , price:}
bids[name] = Price

# whether if new bids to be added
should_continue = input("Are there any other bidders? Type Yes Or No. \n")

continue_bidding = True
while continue_bidding:
  name=input("what is your name? :")
  Price = int(input("What is your bid? : $"))
  bids[name] = Price

