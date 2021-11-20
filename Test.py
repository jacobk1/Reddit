def gradeTranslator(user)  :
#pair of list storing data
   grades = ['A','B','C','D','F']
   score = [90,80,70,60,50]
   user = str(user) #convert to string so I can use .isnumeric() later
   
   #checks input type
   if (user.isnumeric()) :
   
      user = int(user)#convert input to int
      user = (user // 10) * 10#round to nearest 10s place
      #checks for special cases and adjust accordingly, in programs with alot of special cases this would be its own function
      if(user < 50) : 
         user = 50
      elif(user >= 100) :
         user = 90
         
      return [grades[score.index(user)]] #returns result as a list
      
      
   else :
   
      user = user.upper()#converts string to all uppercase characters
      upperbound = score[grades.index(user)] + 9 # finds the upper bound of all possible scores
      lowerbound = score[grades.index(user)]
      #another special case check
      if (user == 'A') :
         upperbound += 1
      elif (user == 'F') :
         lowerbound = 0
         
      return [lowerbound,upperbound]#returns lower and upper bound as list
      
      
#test
result = gradeTranslator('c')
print("Your score is between ", result[0], " and ", result[1],"\t\t test input was 'c'")
result = gradeTranslator('a')
print("Your score is between ", result[0], " and ", result[1],"\t test input was 'a'")
result = gradeTranslator('F')
print("Your score is between ", result[0], " and ", result[1],"\t\t test input was 'F'")
result = gradeTranslator(73)
print("Your grade is ", result[0],"\t" * 8, "test input was 73")
