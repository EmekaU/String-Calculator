Umeozo C Valentine

Language used: python 3
IDE: pycharm
Libraries used: re, unittest

To see results for all questions: python Test.py

There are 3 files:
-> StringCalculator.py

QUESTION 1 is constructed with the assumption that all input
would be in the format => 1,2,3 or " "

Example of Output:
------------Testing Question 1----------------
input=>> 1,2,3,4,-5
Expected=>> 5 || Result=>> 5

QUESTION 2 is constructed with the assumption that all input
would be in the format => 1\n,2,3 or " "

Example of Output:
------------Testing Question 2----------------
input=>> 1\n,2,3
Expected=>> 6 || Result=>> 6

QUESTION 3 is constructed with the assumption that all input
would be in the format => //;\n1;3;4 or " "
Example of Output:
------------Testing Question 3----------------

input=>> //$$$$\n1$$$$2$$$$3$$$$-21$$$$1000
Expected=>> 985 || Result=>> 985

QUESTION 4 is constructed with the assumption that all input
would be in the format => //;;\n1;;3;;4 or " ".
Example of Output:
it returns a string of negative values if any exist.
------------Testing Question 4----------------
input=>> //$$$$\n1$$$$2$$$$3$$$$-21$$$$1000
Expected=>> Negatives Not Allowed! ->  -21 ||
Result=>> Negatives Not Allowed! ->  -21

-> Bonus.py

QUESTION 1
This ignores the values > 1000
Example of Output:

-------------Testing Bonus Question 1----------------
input=>> //$\n1$2$3000$21$1000
Expected=>> 1024 || Result=>> 1024

QUESTION 2
Example of Output:

-------------Testing Bonus Question 2----------------
input=>> //**\n25**300**80**55**-21**34**3**-90
Expected=>> Negatives Not Allowed! ->  -21 -90 ||
Result=>> Negatives Not Allowed! -> -21 -90

QUESTION 3
Example of Output:
-------------Testing Bonus Question 3----------------
input=>> //*,#,$\n10$120#40*5
Expected=>> 175 || Result=>> 175

QUESTION 4
Example of Output:
-------------Testing Bonus Question 4----------------
input=>> //$$,****,#@#@\n1$$2****3#@#@4
Expected=>> 10 || Result=>> 10

-> Test.py
Reads from file in the testFile directory. Uses the info to conduct tests.
