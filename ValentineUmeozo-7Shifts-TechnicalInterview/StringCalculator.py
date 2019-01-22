"""
         Umeozo C Valentine 

    7Shifts Technical Interview

        20th January 2019
"""
import re


class StringCalc(object):
    def __init__(self, string):
        self.string = string
        self.answer = 0

    def add(self):
        return


class Q1(StringCalc):

    def add(self):
        """
        This function splits a split by a comma.
        :return: the sum of the values in the resultant list.
        """
        for w in self.string.split(","):
            self.answer += int(w)
        return self.answer


class Q2(StringCalc):
    def add(self):
        """
        This function splits a split by a comma and strips a new line off the values
        :return: the sum of the values in the resultant list.
        """
        for w in self.string.split(","):
            """if value in array is digit, add. Else, strip new line and add."""
            if w.isdigit():
                self.answer += int(w)

            else:
                self.answer += int(w.strip("\\n"))
        return self.answer


class Q3(StringCalc):
    @staticmethod
    def match(string):
        """
        This function gets the pattern between '//' and '\\n'
        :param string:
        :return: the pattern found, Else: returns a comma
        """
        delimeter = re.search(r'^//.+', string)
        if delimeter:
            # Split pattern from rest of string, then get piece between '//' and '\\n'
            return delimeter.group().split("\\n")[0][2:]
        return ","

    def add(self):
        """
         Using the pattern found, the string is split and any new line attached to the values are
         stripped.
        :return: the sum of all values in the string
        """
        pattern = self.match(self.string)
        if len(self.string) > 0:
            for w in self.string.split(pattern):
                w = w.strip("\\n")
                if w.isdigit() or w[0] == "-":
                    self.answer += int(w)
        return self.answer


class Q4(Q3):
    def add(self):
        """
         Using the pattern found, the string is split and any new line attached to the values are
         stripped.
        :return: the sum of values in the string if all values are positive.
                If there are negative numbers, it returns the negative number(s)
        """
        negatives = "%s" % ""
        pattern = self.match(self.string)

        if len(self.string) > 0:
            for w in self.string.split(pattern):
                w = w.strip("\\n")
                if w.isdigit():
                    self.answer += eval(w)

                elif w[0] == "-":
                    negatives = "%s %s" % (negatives, w)

            if len(negatives) > 0:
                return "%s" % ("Negatives Not Allowed! -> " + negatives)
        return self.answer
