from card import Card

card1 = Card(1, 11)
print(card1)

card2 = Card(1, 3)
print(card2)

print(Card.suits[1]) # access a class attribute directly

card3 = Card(1, 11)

print(card1 < card2) # False
print(card1 > card2) # True
print(card1 == card3) # True
