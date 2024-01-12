from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter, s2_counter = Counter(s1), Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True

        for i in range(len(s1), len(s2)):
            s2_counter[s2[i]] += 1
            s2_counter[s2[i - len(s1)]] -= 1

            if s1_counter == s2_counter:
                return True

        return False
