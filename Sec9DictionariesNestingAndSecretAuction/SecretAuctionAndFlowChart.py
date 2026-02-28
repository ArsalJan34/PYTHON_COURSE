# Asking user for input
bids = {}

# whether if new bids to be added
continue_bidding = True

while continue_bidding:
    name = input("What is your name? : ")
    Price = int(input("What is your bid?  : $"))

    # saving the data into dictionary {name: price}
    bids[name] = Price

    should_continue = input("Are there any other bidders? Type Yes Or No.\n").lower()

    if should_continue == "no":
        continue_bidding = False


def find_highest_bidder(bidding_dcitionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dcitionary:
        bid_amount = bidding_dcitionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


find_highest_bidder(bids)
