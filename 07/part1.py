# order for alphabetical sort of cards
order = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


# helper function to sort based on type of hands
def get_type(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


# for two level sorting via rank and card strength
def get_rank(hand):
    return (get_type(hand), [order.get(card, card) for card in hand])


hands = []
with open("input.txt", "r") as file:
    for line in file:
        hand, bid = line.strip().split(" ")
        hands.append((hand, int(bid)))

hands.sort(key=lambda hand: get_rank(hand[0]))

out = 0
for i, hand in enumerate(hands):
    out += (i + 1) * hand[1]

print(out)
