"""
         Umeozo C Valentine

    7Shifts Technical Interview

        20th January 2019
"""

import unittest

import StringCalculator as Calc
import Bonus as Bonus


class TestStringCalc(unittest.TestCase):
    def testQ1(self):
        """
        Tests StringCalculator Q1: checks if the commas are removed and numbers are added properly
        :return:
        """
        print('\n------------Testing Question 1----------------\n')
        with open("TestFiles/testQ1.txt") as file:
            for line in file.readlines():
                items = line.split("#")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Calc.Q1(items[0]).add()), "\n")

                self.assertEqual(Calc.Q1(items[0]).add(), int(items[1]), items[2])
            file.close()

    def testQ2(self):
        """
        Tests String Calculator Q2: checks if the newline characters are dealt with
        :return:
        """
        print('\n------------Testing Question 2----------------\n')
        with open("TestFiles/testQ2.txt") as file:
            for line in file.readlines():
                items = line.split("#")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Calc.Q2(items[0]).add()), "\n")
                self.assertEqual(Calc.Q2(items[0]).add(), int(items[1]), items[2])
            file.close()

    def testQ3(self):
        """
        Tests String Calculator Q3: checks if the correct delimeters are used to split the string and
        numbers are added properly. This should accept negative numbers
        :return:
        """
        print('\n------------Testing Question 3----------------\n')
        with open("TestFiles/testQ3.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Calc.Q3(items[0]).add()), "\n")
                self.assertEqual(Calc.Q3(items[0]).add(), int(items[1]), items[2])

            file.close()

    def testQ4(self):
        """
        Tests String Calculator Q4: checks if the correct delimeters are used to split the string and if negative
        numbers exist, it checks if negative numbers are listed
        :return:
        """
        print('\n------------Testing Question 4----------------\n')
        with open("TestFiles/testQ4.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Calc.Q4(items[0]).add()), "\n")

            file.close()

    def testQ5(self):
        """
        Tests Bonus Q1: checks if numbers > 1000 are ignored and if negative numbers are reported
        :return:
        """
        print('\n-------------Testing Bonus Question 1----------------\n')
        with open("TestFiles/testBonusQ1.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Bonus.Q1(items[0]).add()), "\n")
            file.close()

    def testQ6(self):
        """
        Tests Bonus Q2: checks if delimeters of any length can be used. It also checks if numbers > 1000 are ignored and
        if negative numbers are reported.
        :return:
        """
        print('\n-------------Testing Bonus Question 2----------------\n')
        with open("TestFiles/testBonusQ2.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Bonus.Q2(items[0]).add()), "\n")
            file.close()

    def testQ7(self):
        """
        Tests Bonus Q3: checks if multiple delimeters can be used. It also checks if numbers > 1000 are ignored and
        if negative numbers are reported.
        :return:
        """
        print('\n-------------Testing Bonus Question 3----------------\n')
        with open("TestFiles/testBonusQ3.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Bonus.Q3(items[0]).add()), "\n")
            file.close()

    def testQ8(self):
        """
        Tests Bonus Q4: checks if multiple delimeters of any length can be used. It also checks if numbers > 1000
        are ignored and if negative numbers are reported.
        :return:
        """
        print('\n-------------Testing Bonus Question 4----------------\n')
        with open("TestFiles/testBonusQ4.txt") as file:
            for line in file.readlines():
                items = line.split("\t")
                print('input=>>', (items[0]))
                print('Expected=>>', (items[1]), '||', 'Result=>>', (Bonus.Q4(items[0]).add()), "\n")
            file.close()


if __name__ == '__main__':
    unittest.main()
