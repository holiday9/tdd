class TestCase:
	def __init__(self, name):
		self.name = name
	
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def run(self, result):
		result.testStarted()
		self.setUp()
		try:
			method = getattr(self,self.name)
			method()
		except:
			result.testFailed()
		self.tearDown()
		return result

class TestResult:
	def __init__(self):
		self.runCount = 0
		self.errorCount = 0
	
	def testStarted(self):
		self.runCount = self.runCount + 1
	
	def testFailed(self):
		self.errorCount = self.errorCount + 1

	def summary(self):
		return "%d run, %d failed" % (self.runCount, self.errorCount)

class WasRun(TestCase):
	def __init__(self, name):
		self.wasRun=None
		TestCase.__init__(self,name)
	
	def setUp(self):
		self.wasRun=None
		self.log = "setUp"

	def testMethod(self):
		self.wasRun = True
		self.log = self.log + " testMethod"

	def tearDown(self):
		self.log = self.log + " tearDown"
	
	def testBrokenMethod(sefl):
		raise Exception

class TestSuite:
	def __init__(self):
		self.tests = []
	def add(self, test):
		self.tests.append(test)
	def run(self, result):
		result = TestResult()
		for test in self.tests:
			test.run(result)
		return result
	
class TestCaseTest(TestCase):
	def testSuite(self):
		suite = TestSuite()
		suite.add(WasRun("testMethod"))
		suite.add(WasRun("testBrokenMethod"))
		result = TestResult()
		suite.run(result)
		print result.summary()
		assert("2 run, 1 failed" == result.summary())

	def testResult(self):
		test = WasRun("testMethod")
		result = TestResult()
		test.run(result)
		assert("1 run, 0 failed" == result.summary())
	
	def testFailedResultFormatting(self):
		result = TestResult()
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())

	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		result = TestResult()
		test.run(result)
		assert("1 run, 1 failed" == result.summary())

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		result = TestResult()
		test.run(result)
		assert("setUp testMethod tearDown" == test.log)
		
	
if __name__ == "__main__":
	suite = TestSuite()
	suite.add(TestCaseTest("testTemplateMethod"))
	suite.add(TestCaseTest("testResult"))
	suite.add(TestCaseTest("testFailedResultFormatting"))
	suite.add(TestCaseTest("testFailedResult"))
	result = TestResult()
	suite.run(result)
	print result.summary()
	
	result = TestResult()
	TestCaseTest("testSuite").run(result)




	
