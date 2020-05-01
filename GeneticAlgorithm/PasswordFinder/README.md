# Genetic algorithm to password finder

## Description
A basic genetic algorithm to find a password with characters and digits.

## How it works?
The user need to pass a password (string) as argument to the main file execution:
```
    python3 main.py write_password_here
```
Then the code will generate a POPULATION list, that will contain 20 random elements with the same password size.
Each element have a FITNESS - a element-wise verification and scored by the number of same characters as the password.  
Will be SELECTED the best two elements (bigger fitness) and applyed a CROSS-OVER and MUTATION to generate a new element.  
The program will stop if it find the password or if it passes a NUMBER OF GENERETION, that is a limiar value.

## Cross-over
From two strings with the same size, ex: *'abcd'* and *'wxyz'* will be selected one of them randomely and get the first half and complement with the second half of the other.  
Ex:  
```python
if choice abcd then
    return abyz  
elif choice wxyz then
    return wxcd 
```

## Mutation
Get a element (string), randomely select a character and change for any character or digit randomely selected.  
Ex:
```python
element = 'abyz'
random_idex = 2
element[random_idex] = random.choice(OPTIONS)
```
Being OPTIONS a list of charactes and digits!