def get_numbers():
    while True:
        try:
            quantity_number = int(input("How many numbers would you like to enter: "))
            while quantity_number <= 0:
                print("Quantity number cannot be less than zero.")
                quantity_number = int(input("How many numbers would you like to enter: "))
            break
        except ValueError:
            print("Wrong value. Please enter a valid integer.")
            
    numbers = []
    i = 0        
    while i < quantity_number:
        try:
            number = int(input(f"Enter number {i + 1}: "))
            numbers.append(number)
            i += 1
        except ValueError:
            print("Wrong input. Please enter an integer.")
            
    return numbers

def display_numbers(numbers):
    """Displays the current collection of numbers."""
    if not numbers:
        print("\nThe list is currently empty.")
    else:
        print("\nCurrent numbers collection:", numbers)

def linear_search(numbers, target):
    """Searches for a target sequentially and returns its index."""
    for idx in range(len(numbers)):
        if numbers[idx] == target:
            return idx
    return -1

def binary_search(numbers, target):
    """Searches for a target using binary search on a sorted list."""
    low = 0
    high = len(numbers) - 1
    comparison_count = 0
    while low <= high:
        found_idx = (low + high) // 2
        comparison_count += 1
        if numbers[found_idx] == target:
            return found_idx, comparison_count
        comparison_count += 1
        if numbers[found_idx] > target:
            high = found_idx - 1
        else:
            low = found_idx + 1
    return -1, comparison_count

def bubble_sort(numbers):
    nums = list(numbers)
    swapped = True
    n = len(nums)
    comparison_performed = 0
    while swapped and n > 1:
        swapped = False
        for i in range(n - 1):
            comparison_performed += 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        n -= 1
    return nums, comparison_performed

def selection_sort(numbers):
    nums = list(numbers)
    n = len(nums)
    comparison_performed = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparison_performed += 1
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums, comparison_performed

def merge_sort(numbers):
    def merge(left, right):
        merged = []
        comparisons = 0
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged, comparisons

    if len(numbers) <= 1:
        return list(numbers), 0

    mid = len(numbers) // 2
    left_sorted, left_comp = merge_sort(numbers[:mid])
    right_sorted, right_comp = merge_sort(numbers[mid:])
    
    merged_list, merge_comp = merge(left_sorted, right_sorted)
    total_comparisons = left_comp + right_comp + merge_comp
    return merged_list, total_comparisons

def main():
    numbers = []
    
    while True:
        print("\n===== SEARCH & SORT TOOLKIT =====")
        print("1. Enter numbers")
        print("2. Display numbers")
        print("3. Linear Search")
        print("4. Binary Search")
        print("5. Bubble Sort")
        print("6. Selection Sort")
        print("7. Merge Sort")
        print("8. Exit")

        try:
            choice = int(input("Enter the operation you would like to execute: "))
            
            if choice == 1:
                numbers = get_numbers()
                print("Numbers successfully saved!")
                
            elif choice == 2:
                display_numbers(numbers)
                
            elif choice == 3:
                if not numbers:
                    print("\nThe list is empty. Please enter numbers first (Option 1).")
                    continue
                target = int(input("Enter the target number: "))
                idx = linear_search(numbers, target)
                print("The index of the target is:", idx) 
                
            elif choice == 4:
                if not numbers:
                    print("\nThe list is empty. Please enter numbers first (Option 1).")
                    continue
                target = int(input("Enter the target number: "))
                # Binary search requires sorted data; we use bubble_sort or merge_sort first
                sorted_nums, _ = bubble_sort(numbers)
                print("Sorted list for binary search:", sorted_nums)
                found_idx, comparison_count = binary_search(sorted_nums, target)
                print(f"The found index is: {found_idx} \nThe number of comparisons performed is: {comparison_count}")
                
            elif choice == 5:
                if not numbers:
                    print("\nThe list is empty. Please enter numbers first (Option 1).")
                    continue
                sorted_numbers, comparison_performed = bubble_sort(numbers)
                print("Sorted numbers (Bubble Sort):", sorted_numbers)
                print("Number of comparisons performed:", comparison_performed)
                
            elif choice == 6:
                if not numbers:
                    print("\nThe list is empty. Please enter numbers first (Option 1).")
                    continue
                sorted_numbers, comparison_performed = selection_sort(numbers)
                print("Sorted numbers (Selection Sort):", sorted_numbers)
                print("Number of comparisons performed:", comparison_performed)
                
            elif choice == 7:
                if not numbers:
                    print("\nThe list is empty. Please enter numbers first (Option 1).")
                    continue
                sorted_numbers, comparison_performed = merge_sort(numbers)
                print("Sorted numbers (Merge Sort):", sorted_numbers)
                print("Number of comparisons performed:", comparison_performed)
                
            elif choice == 8:
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 8.")
                
        except ValueError:
            print("Wrong value. Please enter a valid menu number.")

if __name__ == "__main__":
    main()