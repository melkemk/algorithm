
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.time = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.time[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.time and currentTime - self.time[tokenId] < self.timeToLive:
            self.time[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = sum(1 for token_time in self.time.values() if currentTime - token_time < self.timeToLive)
        return count
