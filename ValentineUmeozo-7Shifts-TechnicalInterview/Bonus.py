"""
         Umeozo C Valentine

    7Shifts Technical Interview

        20th January 2019
"""

import StringCalculator as Calc
import re


class Q1(Calc.Q3):

    def add(self):
        """
         Using the pattern found, the string is split and any new line attached to the values are
         stripped. It ignores values > 1000
        :return: the sum of values in the string if all values are positive.
                If there are negative numbers, it returns the negative number(s)
        """
        negatives = "%s" % ""
        pattern = self.match(self.string)

        if len(self.string) > 0:
            for w in self.string.split(pattern):
                w = w.strip("\\n")
                if w.strip().isdigit():
                    if eval(w) <= 1000:
                        self.answer += eval(w)

                elif w[0] == "-":
                    negatives = "%s %s" % (negatives, w)

            if len(negatives) > 0:
                return "Negatives Not Allowed! ->" + negatives
        return self.answer


class Q2(Calc.Q3):
    def add(self):
        return Q1(self.string).add()


class Q3(Calc.Q3):
    @staticmethod
    def match(string):
        """
        This function gets the string between '//' and '\\n', then splits it to get each pattern
        :param string:
        :return: an array containing the patterns found , Else: returns a comma
        """
        delimeter = re.search(r'((.*).*)\\n', string)
        if delimeter:
            return delimeter.group(1)[2:].split(",")
        return ","

    def add(self):
        """
        This function joins the patterns to "|" so that it could be used by the re.split() function to split the other
        half of the string which contains the numbers. It avoids numbers > 1000 and if there are negative values,
        it returns them instead.
        :return:
        """
        negatives = "%s" % ""
        if len(self.string) > 0:
            pattern = self.match(self.string)
            pattern = "|".join(re.escape(x) for x in pattern)
            number_list = re.split(pattern, self.string.split("\\n")[1])
            for num in number_list:
                if 0 <= int(num) <= 1000:
                    self.answer += int(num)
                else:
                    if int(num) < 0:
                        negatives = "%s %s" % (negatives, num)
            if len(negatives) > 0:
                return "%s" % ("Negatives Not Allowed! -> " + negatives)
        return self.answer


class Q4(Q3):
    def add(self):
        return Q3(self.string).add()

