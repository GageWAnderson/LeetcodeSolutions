#Remember that strings are immutable in python, if you want to build up a result you will have to use a char array
#Kept getting confused implementing the dynamic programming solution, had to look at the solution...
#Didn't try the brute force, so I got hung up trying to implement the harder solution first!
class Solution:  
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add parens when you know it will make a valid sequence
        #You can tell isValid by keeping track of the number of parens placed so far!
        solutions = []
        #Declare recursive helper functions inside the main 'wrapper' function to save space!
        def genPar(S='',opens=0,closes=0): #S is the result we are building, opens,closes = num open/close parens in S
            #When writing this, use default arguments to save space
            if len(S) == 2*n: #base case, don't need to return tho
                solutions.append(S)
            if opens < n: #NOT elif, you want to run this whenever opens < n
                genPar(S+'(',opens+1,closes)
            if opens > closes: #Need to re-balance with closing parens
                genPar(S+')',opens,closes+1)
        genPar()
        return solutions
            