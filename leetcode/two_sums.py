# ----------- Minha Solução -------------
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, valor in enumerate(nums):
            resultado = target - valor

            if resultado in nums and i != nums.index(resultado):
                indice = nums.index(resultado)
                
                return [i, indice]
            else:
                i += 1

# ----------- Solução Certa --------------
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        valores = {}
        
        for i, valor in enumerate(nums):
            resultado = target - valor

            if resultado in valores:
                return [valores[resultado], i]

            valores[valor] = i
                

nums = [4,6,4]
target = 8
sol = Solution()
print(sol.twoSum(nums,target))