def Quiz():
    Score = 0
    welcome_msg = "HI! WELCOME TO PYTHON QUIZ"
    print(welcome_msg.center(100, '*'))
    print()
    
    Q1 = {
        "question": "What is Python?",    
        "A": "A type of snake",
        "B": "A compiled programming language",
        "C": "A high-level, interpreted programming language",
        "D": "A low-level assembly language"
    }
    
    print("Question 1:", Q1["question"])
    print("A:", Q1["A"])
    print("B:", Q1["B"])
    print("C:", Q1["C"])
    print("D:", Q1["D"])
    print()
    
    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    
    if choice == 'C':
        Score += 1
        print("Correct! Python is indeed a high-level, interpreted programming language.")
    else:
        print('The Correct Answer is C: "A high-level, interpreted programming language"')
    
    print(f"\nYour Score: {Score}/1")
    print("-" * 50)
    
    Q2 = {
        "question": "What is the difference between lists and tuples?",
        "A": "Lists are immutable, tuples are mutable",
        "B": "Lists are unordered, tuples are ordered",
        "C": "Lists are mutable, tuples are immutable",
        "D": "Lists and tuples are the same"
    }

    print("Question 2:", Q2["question"])
    print("A:", Q2["A"])
    print("B:", Q2["B"])
    print("C:", Q2["C"])
    print("D:", Q2["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    
    if choice == 'C':
        Score += 1
        print("Correct! Lists are mutable, tuples are immutable.")
    else:
        print('The Correct Answer is C: "Lists are mutable, tuples are immutable"')
    
    print(f"\nYour Score: {Score}/2")
    print("-" * 50)
    
    Q3 = {
        "question": "What is the Global Interpreter Lock (GIL)?",
        "A": "A lock for securing global variables",
        "B": "A mutex that allows only one thread to execute at a time in Python",
        "C": "A way to prevent memory leaks",
        "D": "A method to lock files during reading"
    }

    print("Question 3:", Q3["question"])
    print("A:", Q3["A"])
    print("B:", Q3["B"])
    print("C:", Q3["C"])
    print("D:", Q3["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    
    if choice == 'B':
        Score += 1
        print("Correct! The GIL is a mutex that allows only one thread to execute at a time in Python.")
    else:
        print('The Correct Answer is B: "A mutex that allows only one thread to execute at a time in Python"')
    
    print(f"\nYour Score: {Score}/3")
    print("-" * 50)

    Q4 = {
        "question": "What are Python decorators?",
        "A": "Functions that decorate strings",
        "B": "Functions that modify the behavior of other functions",
        "C": "Loops with advanced formatting",
        "D": "Debugging tools"
    }

    print("Question 4:", Q4["question"])
    print("A:", Q4["A"])
    print("B:", Q4["B"])
    print("C:", Q4["C"])
    print("D:", Q4["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    
    if choice == 'B':
        Score += 1
        print("Correct! Functions that modify the behavior of other functions.")
    else:
        print('The Correct Answer is B: "Functions that modify the behavior of other functions"')
    
    print(f"\nYour Score: {Score}/4")
    print("-" * 50)

    Q5 = { 
        "question": "What is the difference between shallow copy and deep copy?",
        "A": "No difference at all",
        "B": "Deep copy is faster than shallow copy",
        "C": "Shallow copy copies everything recursively",
        "D": "Deep copy copies all nested objects, shallow copy only top-level"
    }

    print("Question 5:", Q5["question"])
    print("A:", Q5["A"])
    print("B:", Q5["B"])
    print("C:", Q5["C"])
    print("D:", Q5["D"])
    print()
    
    choice = input("Enter Your Answer (A, B, C, or D): ").upper()

    if choice == 'D':
        Score += 1
        print("Correct! Deep copy copies all nested objects, shallow copy only top-level.")
    else:
        print('The Correct Answer is D: "Deep copy copies all nested objects, shallow copy only top-level"')
    
    print(f"\nYour Score: {Score}/5")
    print("-" * 50)

    Q6 = {
        "question": "What are *args and **kwargs?",
        "A": "Used to define class attributes",
        "B": "Used to pass variable number of arguments to a function",
        "C": "Used in list comprehension",
        "D": "Used to create decorators"
    }

    print("Question 6:", Q6["question"])
    print("A:", Q6["A"])
    print("B:", Q6["B"])
    print("C:", Q6["C"])
    print("D:", Q6["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! Used to pass variable number of arguments to a function.")
    else:
        print('The Correct Answer is B: "Used to pass variable number of arguments to a function"')
    
    print(f"\nYour Score: {Score}/6")
    print("-" * 50)

    Q7 = {
        "question": "What is the with statement/context manager?",
        "A": "A loop to iterate through a block",
        "B": "Used to define global variables",
        "C": "A way to automatically manage resources like files",
        "D": "Used only in class definitions"
    }

    print("Question 7:", Q7["question"])
    print("A:", Q7["A"])
    print("B:", Q7["B"])
    print("C:", Q7["C"])
    print("D:", Q7["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! A way to automatically manage resources like files.")
    else:
        print('The Correct Answer is C: "A way to automatically manage resources like files"')
    
    print(f"\nYour Score: {Score}/7")
    print("-" * 50)

    Q8 = {
        "question": "What are generators?",
        "A": "Functions that create random numbers",
        "B": "Loops that never end",
        "C": "Functions that yield items one at a time using yield",
        "D": "Built-in data types"
    }

    print("Question 8:", Q8["question"])
    print("A:", Q8["A"])
    print("B:", Q8["B"])
    print("C:", Q8["C"])
    print("D:", Q8["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Functions that yield items one at a time using yield.")
    else:
        print('The Correct Answer is C: "Functions that yield items one at a time using yield"')
    
    print(f"\nYour Score: {Score}/8")
    print("-" * 50)

    Q9 = {
        "question": "What is list comprehension?",
        "A": "A concise way to create lists",
        "B": "A type of function",
        "C": "A debugging method",
        "D": "A built-in Python module"
    }

    print("Question 9:", Q9["question"])
    print("A:", Q9["A"])
    print("B:", Q9["B"])
    print("C:", Q9["C"])
    print("D:", Q9["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'A':
        Score += 1
        print("Correct! A concise way to create lists.")
    else:
        print('The Correct Answer is A: "A concise way to create lists"')
    
    print(f"\nYour Score: {Score}/9")
    print("-" * 50)

    Q10 = {
        "question": "What is the difference between == and is operators?",
        "A": "No difference",
        "B": "== compares values, is compares identity",
        "C": "is is used in loops only",
        "D": "== checks type, is checks value"
    }

    print("Question 10:", Q10["question"])
    print("A:", Q10["A"])
    print("B:", Q10["B"])
    print("C:", Q10["C"])
    print("D:", Q10["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! == compares values, is compares identity.")
    else:
        print('The Correct Answer is B: "== compares values, is compares identity"')
    
    print(f"\nYour Score: {Score}/10")
    print("-" * 50)

    Q11 = {
        "question": "What are lambda functions?",
        "A": "Anonymous one-liner functions",
        "B": "Loops inside functions",
        "C": "Named recursive functions",
        "D": "Built-in sorting tools"
    }

    print("Question 11:", Q11["question"])
    print("A:", Q11["A"])
    print("B:", Q11["B"])
    print("C:", Q11["C"])
    print("D:", Q11["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'A':
        Score += 1
        print("Correct! Anonymous one-liner functions.")
    else:
        print('The Correct Answer is A: "Anonymous one-liner functions"')
    
    print(f"\nYour Score: {Score}/11")
    print("-" * 50)

    Q12 = {
        "question": "What is inheritance in Python?",
        "A": "Copying variables between scripts",
        "B": "One class acquiring properties of another class",
        "C": "Encrypting a function",
        "D": "A way to optimize memory"
    }

    print("Question 12:", Q12["question"])
    print("A:", Q12["A"])
    print("B:", Q12["B"])
    print("C:", Q12["C"])
    print("D:", Q12["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! One class acquiring properties of another class.")
    else:
        print('The Correct Answer is B: "One class acquiring properties of another class"')
    
    print(f"\nYour Score: {Score}/12")
    print("-" * 50)

    Q13 = {
        "question": "How does Python handle exceptions?",
        "A": "Using if statements",
        "B": "Using exit() function",
        "C": "Using try, except, finally blocks",
        "D": "Automatically retries the code"
    }

    print("Question 13:", Q13["question"])
    print("A:", Q13["A"])
    print("B:", Q13["B"])
    print("C:", Q13["C"])
    print("D:", Q13["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Using try, except, finally blocks.")
    else:
        print('The Correct Answer is C: "Using try, except, finally blocks"')
    
    print(f"\nYour Score: {Score}/13")
    print("-" * 50)

    Q14 = {
        "question": "What is the __init__ method?",
        "A": "A variable",
        "B": "Constructor method in a class",
        "C": "Built-in list function",
        "D": "Loop initializer"
    }

    print("Question 14:", Q14["question"])
    print("A:", Q14["A"])
    print("B:", Q14["B"])
    print("C:", Q14["C"])
    print("D:", Q14["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! Constructor method in a class.")
    else:
        print('The Correct Answer is B: "Constructor method in a class"')
    
    print(f"\nYour Score: {Score}/14")
    print("-" * 50)

    Q15 = {
        "question": "What is a KeyError and how to handle it?",
        "A": "A syntax error",
        "B": "Error raised when a dictionary key is not found; handle with try-except",
        "C": "Issue with strings",
        "D": "Related to index out of range"
    }

    print("Question 15:", Q15["question"])
    print("A:", Q15["A"])
    print("B:", Q15["B"])
    print("C:", Q15["C"])
    print("D:", Q15["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! Error raised when a dictionary key is not found; handle with try-except.")
    else:
        print('The Correct Answer is B: "Error raised when a dictionary key is not found; handle with try-except"')
    
    print(f"\nYour Score: {Score}/15")
    print("-" * 50)

    Q16 = {
        "question": "How does Python's memory management work?",
        "A": "Automatic using reference counting and garbage collection",
        "B": "Manual like in C",
        "C": "Memory is never freed",
        "D": "Through a memory stack only"
    }
    
    print("Question 16:", Q16["question"])
    print("A:", Q16["A"])
    print("B:", Q16["B"])
    print("C:", Q16["C"])
    print("D:", Q16["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'A':
        Score += 1
        print("Correct! Automatic using reference counting and garbage collection.")
    else:
        print('The Correct Answer is A: "Automatic using reference counting and garbage collection"')
    
    print(f"\nYour Score: {Score}/16")
    print("-" * 50)

    Q17 = {
        "question": "What is Method Resolution Order (MRO)?",
        "A": "A way to sort methods alphabetically",
        "B": "The order in which Python looks for methods in a hierarchy",
        "C": "The order methods are written",
        "D": "The order functions are compiled"
    }

    print("Question 17:", Q17["question"])
    print("A:", Q17["A"])
    print("B:", Q17["B"])
    print("C:", Q17["C"])
    print("D:", Q17["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! The order in which Python looks for methods in a hierarchy.")
    else:
        print('The Correct Answer is B: "The order in which Python looks for methods in a hierarchy"')
    
    print(f"\nYour Score: {Score}/17")
    print("-" * 50)

    Q18 = {
        "question": "What is PEP 8?",
        "A": "A debugging tool",
        "B": "Python style guide for code formatting",
        "C": "A performance engine",
        "D": "A package manager"
    }

    print("Question 18:", Q18["question"])
    print("A:", Q18["A"])
    print("B:", Q18["B"])
    print("C:", Q18["C"])
    print("D:", Q18["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! Python style guide for code formatting.")
    else:
        print('The Correct Answer is B: "Python style guide for code formatting"')
    
    print(f"\nYour Score: {Score}/18")
    print("-" * 50)

    Q19 = {
        "question": "What are sets and dictionaries?",
        "A": "Both are lists",
        "B": "Set stores unique items; dictionary stores key-value pairs",
        "C": "Both store only numbers",
        "D": "Dictionary is an ordered set"
    }

    print("Question 19:", Q19["question"])
    print("A:", Q19["A"])
    print("B:", Q19["B"])
    print("C:", Q19["C"])
    print("D:", Q19["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'B':
        Score += 1
        print("Correct! Set stores unique items; dictionary stores key-value pairs.")
    else:
        print('The Correct Answer is B: "Set stores unique items; dictionary stores key-value pairs"')
    
    print(f"\nYour Score: {Score}/19")
    print("-" * 50)

    Q20 = {
        "question": "What is the difference between Python 2 and Python 3?",
        "A": "Python 3 is faster",
        "B": "Python 2 has more features",
        "C": "Python 3 uses print() as a function; Python 2 uses it as a statement",
        "D": "No difference"
    }

    print("Question 20:", Q20["question"])
    print("A:", Q20["A"])
    print("B:", Q20["B"])
    print("C:", Q20["C"])
    print("D:", Q20["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Python 3 uses print() as a function; Python 2 uses it as a statement.")
    else:
        print('The Correct Answer is C: "Python 3 uses print() as a function; Python 2 uses it as a statement"')
    
    print(f"\nYour Score: {Score}/20")
    print("-" * 50)

    Q21 = {
        "question": "What is slicing in Python?",
        "A": "Extracting a portion of a sequence",
        "B": "Sorting a list",
        "C": "Removing duplicates",
        "D": "Encrypting data"
    }

    print("Question 21:", Q21["question"])
    print("A:", Q21["A"])
    print("B:", Q21["B"])
    print("C:", Q21["C"])
    print("D:", Q21["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'A':
        Score += 1
        print("Correct! Extracting a portion of a sequence.")
    else:
        print('The Correct Answer is A: "Extracting a portion of a sequence"')
    
    print(f"\nYour Score: {Score}/21")
    print("-" * 50)

    Q22 = {
        "question": "What is enumerate() used for?",
        "A": "For adding items to a list",
        "B": "For reversing strings",
        "C": "Iterates with index and value in a loop",
        "D": "Converts string to number"
    }

    print("Question 22:", Q22["question"])
    print("A:", Q22["A"])
    print("B:", Q22["B"])
    print("C:", Q22["C"])
    print("D:", Q22["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Iterates with index and value in a loop.")
    else:
        print('The Correct Answer is C: "Iterates with index and value in a loop"')
    
    print(f"\nYour Score: {Score}/22")
    print("-" * 50)

    Q23 = {
        "question": "What is pickling and unpickling?",
        "A": "Serializing and deserializing Python objects",
        "B": "Encrypting passwords",
        "C": "Backing up data",
        "D": "Compressing files"
    }

    print("Question 23:", Q23["question"])
    print("A:", Q23["A"])
    print("B:", Q23["B"])
    print("C:", Q23["C"])
    print("D:", Q23["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'A':
        Score += 1
        print("Correct! Serializing and deserializing Python objects.")
    else:
        print('The Correct Answer is A: "Serializing and deserializing Python objects"')
    
    print(f"\nYour Score: {Score}/23")
    print("-" * 50)

    Q24 = {
        "question": "What are modules and packages?",
        "A": "Same as loops",
        "B": "Used for GUI",
        "C": "Modules are .py files; packages are collections of modules",
        "D": "Python built-in data types"
    }

    print("Question 24:", Q24["question"])
    print("A:", Q24["A"])
    print("B:", Q24["B"])
    print("C:", Q24["C"])
    print("D:", Q24["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Modules are .py files; packages are collections of modules.")
    else:
        print('The Correct Answer is C: "Modules are .py files; packages are collections of modules"')
    
    print(f"\nYour Score: {Score}/24")
    print("-" * 50)

    Q25 = {
        "question": "How do you reverse a string in Python?",
        "A": "Using sort()",
        "B": "Using .reverse()",
        "C": "Using slicing: string[::-1]",
        "D": "Using reversed() function directly on string"
    }

    print("Question 25:", Q25["question"])
    print("A:", Q25["A"])
    print("B:", Q25["B"])
    print("C:", Q25["C"])
    print("D:", Q25["D"])
    print()

    choice = input("Enter Your Answer (A, B, C, or D): ").upper()
    if choice == 'C':
        Score += 1
        print("Correct! Using slicing: string[::-1]")
    else:
        print('The Correct Answer is C: "Using slicing: string[::-1]"')
    
    print(f"\nYour Score: {Score}/25")
    print("-" * 50)

    # Final score display
    print("\n" + "="*50)
    print(f"🎉 Quiz Completed! Your Final Score: {Score}/25")
    if Score == 25:
        print("🏆 Perfect score! You're a Python Pro!")
    elif Score >= 20:
        print("👏 Great job! Solid Python knowledge.")
    elif Score >= 10:
        print("🙂 Good attempt, keep practicing!")
    else:
        print("📘 Don't worry, review the basics and try again.")
    print("="*50)
    
    return Score

# Run the quiz
if __name__ == "__main__":
    Quiz()