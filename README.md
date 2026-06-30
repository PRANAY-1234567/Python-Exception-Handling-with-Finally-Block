# Python Exception Handling with Finally Block

## 📌 Overview

This project demonstrates the use of **exception handling** and the **finally block** in Python. The program accepts two integers from the user, performs integer division, handles common exceptions, and ensures that a result is displayed regardless of whether an exception occurs.
The example showcases how `try`, `except`, and `finally` work together to make Python programs more robust and reliable.

---

## 🚀 Features

* Accepts two integer inputs from the user
* Performs integer division (`//`)
* Handles invalid input errors
* Handles division by zero errors
* Uses a `finally` block for guaranteed execution
* Demonstrates structured exception handling

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
├── exception_finally.py
├── README.md
```

---

## 💻 Source Code

```python
print("Program starts...")

a = 0
b = 0
c = 0

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a // b

except ValueError:
    print("Error in data : Number not provided correctly")

except ZeroDivisionError:
    print("Error in data : Divisor should not be zero")

except Exception as e:
    print("Error in data :", e)

finally:
    print("The division of", a, "and", b, "is", c)

print("Program ends...")
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-exception-finally.git
cd python-exception-finally
```

### Run the Program

```bash
python exception_finally.py
```

---

## 📋 Sample Output

### Successful Execution

```text
Program starts...
Enter first number : 20
Enter second number : 5
The division of 20 and 5 is 4
Program ends...
```

### Invalid Input

```text
Program starts...
Enter first number : abc
Error in data : Number not provided correctly
The division of 0 and 0 is 0
Program ends...
```

### Division by Zero

```text
Program starts...
Enter first number : 20
Enter second number : 0
Error in data : Divisor should not be zero
The division of 20 and 0 is 0
Program ends...
```

---

## 🧠 Concepts Covered

* Exception Handling
* `try` Block
* `except` Block
* `finally` Block
* `ValueError`
* `ZeroDivisionError`
* User Input Validation
* Integer Division

---

## 🔍 Understanding the Finally Block

The `finally` block executes **whether an exception occurs or not**.

```python
finally:
    print("The division of", a, "and", b, "is", c)
```

This makes it useful for:

* Cleanup operations
* Closing files
* Releasing resources
* Executing mandatory code

---

## ⚠️ Note

In this program, the variables `a`, `b`, and `c` are initialized to `0`. Therefore, if an exception occurs before division is completed, the `finally` block still prints their current values.

---

## 🔮 Future Improvements

* Display result only when division is successful
* Add support for floating-point calculations
* Create a menu-driven calculator
* Log exceptions to a file
* Add custom exception handling

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software & Embedded Systems Engineer

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="507" height="240" alt="image" src="https://github.com/user-attachments/assets/0e0b3daa-ffd4-485c-a7a3-099cda3bf5fd" />

<img width="593" height="185" alt="image" src="https://github.com/user-attachments/assets/e1a8432a-ea10-4ccb-9784-ab590f7377ee" />
