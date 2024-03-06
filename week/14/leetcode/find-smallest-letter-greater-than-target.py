class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if bisect_right(letters,target) <len(letters):
            return letters[bisect_right(letters,target)]
        return letters[0]