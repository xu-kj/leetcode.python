class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([stone for stone in stones if stone in jewels])