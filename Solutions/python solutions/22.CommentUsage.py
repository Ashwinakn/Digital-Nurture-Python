#define the function totalsal with the parameters base,bonus
def totalsal(base,bonus):
    total=base+bonus #Calculate the total salary
    #by adding up base salary he recieves with the bonus amt
    print("Total Salary: Rs.{:.2f}".format(total))#Print the total salary
    
#Get the input values from the user to calculate totalsal()
base=float(input("Enter the base salary:"))
bonus=float(input("Enter the bonus amount recieved:"))
totalsal(base,bonus)
