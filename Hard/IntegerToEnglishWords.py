#This question was a challenging, tedious divide and conquer problem
#Got an elegant solution on my first try though
class Solution:
    def numberToWords(self, num: int) -> str:
        tens = {20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
        digits = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
            11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        #All the numbers from 1 to 19 inclusive
        #Unique names stop after 19
        if num == 0:
            return "Zero"
        
        def helper(num):
            if num < 20:
                return digits[num]
            elif num < 100:
                return tens[(num//10)*10] + " " + helper(num%10)
            elif num < 1000:
                return digits[num//100] + " Hundred " + helper(num%100)
            elif num < 1000000:
                return helper(num//1000) + " Thousand " + helper(num%1000)
            elif num < 1000000000:
                return helper(num//1000000) + " Million " + helper(num%1000000)
            else:
                return helper(num//1000000000) + " Billion " + helper(num%1000000000)
        return helper(num).replace("  "," ").strip() #Clean up extra spaces