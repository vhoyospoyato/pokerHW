import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def threekind(self):
        for i in range(5):
            for j in range(i+1, 5):
                for z in range(j + 1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[z].get_rank():
                        return True
        return False


    def fourkind(self):
        for i in range(5):
            for j in range(i+1, 5):
                for z in range(j + 1, 5):
                    for y in range(z+1, 5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[z].get_rank() == self.cards[y].get_rank():
                            return True
        return False

    def twopairs(self):
        twop = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    twop += 1
                if twop == 2:
                    return True
        return False

    #def straight(self):
        #for i in range (5):
            #for j in range (i+1,5):
                #if self.cards[i].get_rank()

    def flush(self):
        for i in range (5):
            if self.cards[0].get_suit()==self.cards[1].get_suit()==self.cards[2].get_suit()==self.cards[3].get_suit()==self.cards[4].get_suit():
                return True
        return False


for i in range(10000):
    new_deck = Deck()
    new_deck.shuffle()
    print(new_deck)
    hand = Hand(new_deck)
    print("\n", hand)

    print("Pairs in hand?", hand.is_pair())
    print("Three of a kind in hand?", hand.threekind())
    print("Four of a kind in hand?", hand.fourkind())
    print("Two pairs in hand?", hand.twopairs())
    print("Flush in hand?", hand.flush())
    #print("Two pairs in hand?", hand.twopairs())
    #print("Two pairs in hand?", hand.twopairs())




