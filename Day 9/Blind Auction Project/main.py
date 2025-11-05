# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
dic = {}
print(art.logo)
def bidding():

    username = input("Enter your name: ")
    bid_amount = int(input("Please enter bid amount $: "))
    dic.update({username : bid_amount})

    # print(dic)

    another_bidder = input(f"Is there any another bidder? 'Yes' or 'No' ")

    if another_bidder.lower() == "yes" :
        print("\n" * 120)
        bidding()
    elif another_bidder.lower() == "no":
        winner = max(dic, key=dic.get)
        print(f"The Winner is {winner} with bid amount of ${dic[winner]}")
bidding()
