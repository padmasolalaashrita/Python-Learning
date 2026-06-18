participants = {}
part = input("Do you want to participate in the secret auction?Press 'Y' for yes and 'N' for no.").lower()

def auction(name,bid):
    participants[name] = bid


while part == "y":
    name = input("Enter your name:")
    bid = int(input("Enter your bid: $"))
    auction(name,bid)
    part = input("Is there another bidder?Press 'Y' for yes and 'N' for no.").lower()
    if part == "y":
        print("\n"*100)


participants_list = list(participants)
n = len(participants_list)
highest_bidder = participants_list[0]
highest_bid = participants[highest_bidder]

for bidder in participants:
    current_bid = participants[bidder]

    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    


'''

max_bid = participants_list[0]

for i in range(n):
    if participants_list[i]>max_bid:
        max_bid = participants_list[i]
'''
