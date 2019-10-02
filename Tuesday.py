# Imported datetime.
import datetime
# Created two variables.
today = datetime.datetime.today ()
dayofweek = today.weekday()
print ("Lets check is it Tuesday.")
if dayofweek == 1:
    print ("It is Tuesday!")
elif dayofweek == 0:    
else:
    print("Unfortunately, it is not Tuesday.")
    print("Luckily, it will be Tuesday in six days.")

print ("Thanks for checking if it is Tuesday.")

