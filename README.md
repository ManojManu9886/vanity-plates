# vanity-plates
Making valid vanity plates
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

1. “All vanity plates must start with at least two letters.”

2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

3. “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

4. “No periods, spaces, or punctuation marks are allowed.”

In plates.py, I implemented a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assuming that any letters in the user’s input will be uppercase. Structured by program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assumed that s will be a str.

