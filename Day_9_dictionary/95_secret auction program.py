# from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {} # bids 디렉토리 형성
bidding_finished = False # while 무한 loop를 위한 False문

def find_highest_bidder(bidding_record): # bids dic. -> bidding_record로
    highest_bid = 0
    winner = ""
    for bidder in bidding_record: # dic.에서 for loop는 key값만 반복
        bid_amount = bidding_record[bidder] # bid_amount가 value 값을 얻도록. int
        if bid_amount > highest_bid: # 둘 다 int
            highest_bid = bid_amount # 최상위 값을 도출하기 위해, highest_bid가 bid_amount와 같게 되도록 설정
            winner = bidder   # winner는 bidder(key)로 표기되도록
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $")) # integer 값으로 변경
    bids[name] = price # 비어있는 bids 디렉토리 내에 key = name, value = price 값을 형성해줌.
    should_continue = input("Are there any ohter bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True # 여기서 ==처럼 2개의 =을 사용하니 해당 부분을 건너뛰는 듯..! while문 밖에서는 error로 뜨는데, while문 내에서 오류로 인식을 하지 않고 건너뛰는 현상을 발견함. 추후 확인.
        find_highest_bidder(bids) # find_highest_bidder() 함수로 가게 함


# Answer
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        print(bids)