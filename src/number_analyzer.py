def get_numbers():
    numbers = []
    while True:
        try:
                    
            quantity_numbers = int(input("How many numbers would you like to enter?: "))
            while quantity_numbers <= 0:
                print("The quantity of numbers cannot be 0 or negative")
                quantity_numbers = int(input("How many numbers would you like to enter?: "))
            break
        except ValueError:
            print("wrong value, enter an integer")
    
    count = 0
    while count < quantity_numbers:
        try:        
            number = int(input("Enter a number: "))
            print("number entered")
            numbers.append(number)
            count += 1
        
        except ValueError:
            print("wrong value, Enter a number")
            

        
    
    return numbers
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
def average(numbers):
    total_of_numbers = 0
    for number in numbers:

        total_of_numbers += number
        
    avg = total_of_numbers/ len(numbers)
    return avg
def positive_count(numbers):
    positive_numbers = 0
    for number in numbers:
        if number > 0:
            positive_numbers += 1
    return positive_numbers
def negative_count(numbers):
    negative_numbers = 0
    for number in numbers:
        if number < 0:
            negative_numbers += 1
    return negative_numbers
def zero_count(numbers):
    zeros = 0
    for number in numbers:
        if number == 0:
            zeros += 1
    return zeros
def display_report(largest, smallest, avg, positive_numbers, negative_numbers, zeros):
    print("The largest number is: ", largest, "\nThe smallest number is: ", smallest,"The average value is: ", avg, "\nThe positive numbers are: ", positive_numbers,"\nThe negative numbers are: ", negative_numbers,"\nThe number of zeroes are: ", zeros)
def main():
    print("\n=== NUMBER ANALYZER ===")
    numbers = get_numbers()
    while True:
        
        print("1. FIND LARGEST NUMBER")
        print("2. FIND SMALLEST NUMBER")
        print("3. FIND AVERAGE")
        print("4. FIND POSITIVE COUNT")
        print("5. FIND NEGATIVE COUNT")
        print("6. FIND ZEROS COUNT")
        print("7. EXIT")
        while True:
            try: 
                choice = int(input("What operation would you like to proceed with? "))
                break
            except ValueError:
                print("Wrong Value.\nEnter an integer.")
        if choice == 1:
            largest = largest_number(numbers)
            print("The largest number is: ", largest)
        elif choice == 2:
            smallest = smallest_number(numbers)
            print("The smallest number is: ", smallest)
        elif choice == 3:
            avg = average(numbers)
            print("The average number is: ", avg)
        elif choice == 4:
            positive_numbers = positive_count(numbers)
            print("The positive numbers is(are): ", positive_numbers)
        elif choice == 5:
            negative_numbers = negative_count(numbers)
            print("The negative numbers is(are): ", negative_numbers)
        elif choice == 6:
            zeros = zero_count(numbers)
            print("The zeros number is(are): ", zeros)
            
        elif choice == 7:
            print("EXITING THE PROGRAM, THANK YOU!")
            break
        else:
            print("Wrong option.")    
if __name__ == "__main__":
    main()