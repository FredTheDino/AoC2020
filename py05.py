import sys

def main():
    seats = set()
    for line in sys.stdin.readlines():
        seatid = line.replace("L", "0") \
                     .replace("R", "1") \
                     .replace("F", "0") \
                     .replace("B", "1")
        seats.add(int(seatid, 2))

    print(max(seats))

    for seat in seats:
        if seat + 1 not in seats and seat + 2 in seats:
            print(seat + 1)

main()
