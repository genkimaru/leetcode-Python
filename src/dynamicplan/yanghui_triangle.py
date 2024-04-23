from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[]]
        for i in range(numRows):
            result.append(self.generateNumRows(i+ 1))
        return result

            

    def generateNumRows(self , numRows):
        if numRows < 1:
            raise Exception('numRows need greater than 0')
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1,1]
        if numRows == 3:
            return [ 1, self.generateNumRows(2)[0] + self.generateNumRows(2)[1] ,1 ]
        # if numRows == 4:
        #     return [ self.generateNumRows(numRows - 1)[0] ,self.generateNumRows(numRows - 1)[0] + self.generateNumRows(numRows - 1)[1] ,
        #              self.generateNumRows(numRows - 1)[1] +  self.generateNumRows(numRows - 1)[2] , self.generateNumRows(numRows - 1)[2]]

        else:
            numRows_result = []
            for i in range(numRows):
                # Attention: in python the logical OR use keyword `or` , Not `|`
                if i == 0 or i == numRows - 1:
                    numRows_result.append(1)
                else:
                    numRows_result.append(self.generateNumRows(numRows - 1)[i-1] + self.generateNumRows(numRows - 1)[i] )
            return numRows_result




numRows = 5

result = Solution().generate(numRows)
print(result)