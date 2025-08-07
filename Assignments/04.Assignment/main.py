import my_programs

def display_menu():
    print("\n------ FUNCTION MENU ------")
    print("1. Reverse a String")
    print("2. Check Even or Odd")
    print("3. Factorial using Recursion")
    print("4. Check Palindrome")
    print("5. Fibonacci Series")
    print("6. Find Max and Min in List")
    print("7. Count Vowels in String")
    print("8. Count Character Occurrence")
    print("9. Swap Two Variables")
    print("10. Remove Duplicates from List")
    print("11. Sum of Elements in List")
    print("12. Frequency of Characters in String")
    print("13. Sort List without sort()")
    print("14. Second Largest in List")
    print("15. Check Prime Number")
    print("0. Exit")
    print("----------------------------")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            my_programs.reverse_string()
        elif choice == '2':
            my_programs.check_even_odd()
        elif choice == '3':
            my_programs.factorial_recursion()
        elif choice == '4':
            my_programs.is_palindrome()
        elif choice == '5':
            my_programs.fibonacci_series()
        elif choice == '6':
            my_programs.find_max_min()
        elif choice == '7':
            my_programs.count_vowels()
        elif choice == '8':
            my_programs.count_char_occurrence()
        elif choice == '9':
            my_programs.swap_variables()
        elif choice == '10':
            my_programs.remove_duplicates()
        elif choice == '11':
            my_programs.sum_of_list()
        elif choice == '12':
            my_programs.frequency_characters()
        elif choice == '13':
            my_programs.sort_without_sort()
        elif choice == '14':
            my_programs.second_largest()
        elif choice == '15':
            my_programs.is_prime()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 15.")

if __name__ == "__main__":
    main()