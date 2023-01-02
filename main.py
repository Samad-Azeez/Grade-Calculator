'''This code helps in calculating and printing out what your grade in a course is'''

print('Enter your score below')
score = round(float(input('Input Score: '))) #Takes in the score input as a variable

#Uses the inputed variable to determine the grade
if (score >= 70) and (score <= 100):
	print('This is equivalent to 5 points \n Remark: Excellent')
    
elif (score >= 60) and (score <= 69):
	print('This is equivalent to 4 points \n Remark: Very good')
    
elif (score >= 50) and (score <=59):
	print('This is equivalent to 3 points \n Remark: Good')
    
elif (score >= 45) and (score <= 49):
	print('This is equivalent to 2 points \n Remark: Fair')
    
elif (score >= 40) and (score <= 44):
   	print('This is equivalent to 1 point \n Remark:Pass')
    
elif (score >= 0) and (score <= 39):
	print("This is equivalent to 0 point \n Remark: Fail")
    
elif (score < 0) or (score > 100):
    print('Unable to calculate, please input score within the range of 0 - 100')
