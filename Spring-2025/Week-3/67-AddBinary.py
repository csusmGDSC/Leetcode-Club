# Modular Solution.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        a = a[::-1]
        b = b[::-1]

        maximum = max(len(a), len(b))

        for i in range(maximum):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digitA + digitB + carry 
            result = str(total % 2) + result
            carry = total // 2 

        if carry:
            result = '1' + result
        return result

# Bit Manipulation.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        return bin(x)[2:]

# Another Solution.
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    res = a + b
    res = bin(res)
    return res[2:]
