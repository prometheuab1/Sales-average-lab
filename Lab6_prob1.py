#This program is written by Abdulbasit Adeniji for CIS_105 on 11/9/2022.
#The purpose of this code is to display the min, max and average number of sales inputed by the user.

#day list
days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
sales = [] #empty list
#intro
def intro():
    print('This program is going to display the min, max and average number of sales inputed by you.')


#main function
def main():
    intro()
    print('\n')
    #create a for loop
    for element in days_list:
        sales_amount = float(input(f'Amount of sales for {element} : '))
        sales.append(sales_amount) #append each sales day from the list

    #sales max and sales min using index position.
    salesmax = sales.index(max(sales))
    salesmin = sales.index(min(sales))


    #set the output (min, max and average) for the user after getting all the information needed.
    print('Here is the min, max, and average number of sales for this week')
    print()
    print(f'The day with the most sales amount is {days_list[salesmax]} ')
    print(f'with ${max(sales)}')
    print()
    print(f'The day with the least sales amount is {days_list[salesmin]} ')
    print(f'with ${min(sales)}')
    print()
    print(f'The average number of sales make this week is ${sum(sales)/len(sales):.0f}.') #calculating the average
    
#call to main
if __name__ == "__main__":
    main()
