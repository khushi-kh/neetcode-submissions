class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for string in strs:
            encoded += string
            encoded += "k&k"
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = s.split("k&k")
        return decoded[:-1]