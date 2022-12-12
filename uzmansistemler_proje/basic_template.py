import random
class Player:
    def __init__(self, name, numofcards, sumofcards, money):
        self.name = name
        self.numofcards = numofcards
        self.sumofcards = sumofcards
        self.listofcards = []
        self.money = money

    def gain_money(self, amount):
        self.money = self.money + amount

    def lose_money(self, amount):
        self.money = self.money - amount

def deal_cards():
    for player in player_list:
        popped_card = deck_list.pop()
        exposed_cards.append(popped_card)
        player.listofcards.append(popped_card)
        player.numofcards = player.numofcards + 1
        try:
            card_value = int(popped_card[-1])
            if (card_value == 0):
                player.sumofcards = player.sumofcards + 10
            else:
                player.sumofcards = player.sumofcards + card_value
        except:
                player.sumofcards = player.sumofcards + 10

def prepare_deck():
    random.shuffle(deck_list_perm)
    deck_list = deck_list_perm.copy()
    return deck_list

playerU = Player("Sercan", 0, 0, 500)
player1 = Player("Machine", 0, 0, 500)
player2 = Player("Statically", 0, 0, 500)
player3 = Player("Random Dude", 0, 0, 500)

player_list = []
player_list.append(playerU)
player_list.append(player1)
player_list.append(player2)
player_list.append(player3)

deck_list_perm = [] # 3 DECK SHUFFLED
deck_list = []

exposed_cards = []

for idx in range(0,3): # 3 decks
    for type in ("Clubs","Diamonds","Spades","Hearts"):
        for num in ("2","3","4","5","6","7","8","9","10","Jack","Queen","King"):
            deck_list_perm.append(type+num)
            deck_list.append(type+num)


while(deck_list):
    deal_cards()

