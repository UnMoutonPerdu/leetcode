class Solution:
    def monoFizzBuzz(self, n: int) -> str:
        output = ""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        
        return output if len(output) > 0 else str(n)
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [self.monoFizzBuzz(i+1) for i in range(n)]
        return answer