class TestStatus():
    resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("Pass")
                else:
                    self.resultList.append("Fail")
            else:
                self.resultList.append("Fail")

        except:
            self.resultList.append("Fail")

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        '''
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        '''
        self.setResult(result, resultMessage)

        if "Fail" in self.resultList:
            self.resultList.clear()
            assert True == False
        else:
            self.resultList.clear()
            assert True == True
