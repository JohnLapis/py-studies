sequence = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

def isstraight(hand):
    h = []
    for c in sorted(hand):
        try:
            h.append(int(c[0]))
        except:
            if c[0] == 'J':
                h.append(11)
            elif c[0] == 'Q':
                h.append(12)
            elif c[0] == 'K':
                h.append(13)
            elif c[0] == 'A':
                h.append(14)

        for i in range(4):
            if h[i+1] - h[i] != 1:
                return False
            
        return True
        

def points(hand):
    if [card[1] for card in hand].count(hand[0][1]) == 5:
        p = 6
    if isstraight(hand):
        if p == 6:
            p = 9
            hh = [card[0] for card in hand]
            if '10' in hh and 'J' in hh and 'Q' in hh and 'K' in hh and 'A' in hhh:
                p = 10
        else:
            p = 5
        return p

    
    pairs = {}
    for card in hand:
        pairs[card[0]] = hand.count(card[0])


    if 2 == pairs.values().count(2):
        p = (3,())
    elif 2 in pairs.values() and 4 in pairs.values():
        p

    return p
    
    
def main(hands):
    wins = 0
    for h1, h2 in hands:
        h1 = p(h1)
        h2 = p(h2)
        if h1[0] > h2[0]:
            wins += 1
        elif h1[0] == h2[0]:
            if h1[1] > h2[1]:
                wins += 1


    
if __name__ == '__main__':
    print(main())
