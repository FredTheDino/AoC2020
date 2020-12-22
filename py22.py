from collections import deque
import sys

def parse_deck(deck):
    return deque(map(int, deck.split("\n")[1:]))

p1, p2 = sys.stdin.read().split("\n\n")

p1 = parse_deck(p1.strip("\n"))
p2 = parse_deck(p2.strip("\n"))

def play_game(p1, p2):
    while p1 and p2:
        a = p1.popleft()
        b = p2.popleft()

        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

    if p1:
        return p1
    return p2

winner = play_game(p1.copy(), p2.copy())


def score(hand):
    hand.reverse()
    return sum((i + 1) * h for i, h in enumerate(hand))


print(score(winner))


def play_recursive(p1, p2, ):
    seen = set()
    while p1 and p2:
        state = tuple(p1), tuple(p2)
        if state in seen:
            return p1, 1
        seen.add(state)

        a = p1.popleft()
        b = p2.popleft()

        if len(p1) >= a and len(p2) >= b:
            p1_copy = deque(card for _, card in zip(range(a), p1))
            p2_copy = deque(card for _, card in zip(range(b), p2))
            _, w = play_recursive(p1_copy, p2_copy)
            a_is_winner = w == 1
        else:
            a_is_winner = a > b

        if a_is_winner:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

    if p1:
        return p1, 1
    return p2, 2

# 31518 Too low

print(score(play_recursive(p1, p2)[0]))
