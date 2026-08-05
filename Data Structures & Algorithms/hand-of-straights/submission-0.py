class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)

        uniqueHand = list(set(hand))
        uniqueHand.sort(reverse = True)

        start = -1
        while len(uniqueHand) > 0:
            while uniqueHand and (start == -1 or counter[start] == 0):
                start = uniqueHand.pop()
            if len(uniqueHand) == 0 and counter[start] == 0:
                break
            for num in range(start, start + groupSize):
                if counter[num] == 0:
                    return False
                counter[num] -= 1

        return True
        