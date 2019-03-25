import unittest
from testCases.test_login import Test_001_Login
from testCases.test_login_ddt import Test_002_DDT_Login

# Get all test methods
tc1=unittest.TestLoader().loadTestsFromTestCase(Test_001_Login)
tc2=unittest.TestLoader().loadTestsFromTestCase(Test_002_DDT_Login)

#creating test suites...

sanitytestsuite=unittest.TestSuite([tc1])
functionaltestsuite=unittest.TestSuite([tc2])


#Run the specific test suite
unittest.TextTestRunner().run(functionaltestsuite)

