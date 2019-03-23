import unittest
from testCases.test_Test1 import Test_001_Login
from testCases.test_Test2 import Test_002_DDT_Login

# Get all test methods from LoginTest,SignUpTest,PaymentTest and PaymentReturnsTest
tc1=unittest.TestLoader().loadTestsFromTestCase(Test_001_Login)
tc2=unittest.TestLoader().loadTestsFromTestCase(Test_002_DDT_Login)

#creating test suites...
sanitytestsuite=unittest.TestSuite([tc1])
functionaltestsuite=unittest.TestSuite([tc1,tc2])
#mastertestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

#Run the specific test suite
unittest.TextTestRunner().run(functionaltestsuite)