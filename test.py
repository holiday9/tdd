class TestCase:
	def __init__(self, name):
		self.name = name
	
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def run(self):
		result = TestResult()
		result.testStarted()
		self.setUp()
		method = getattr(self,self.name)
		method()
		self.tearDown()
		return result

class TestResult:
	def __init__(self):
		self.runCount = 1
	
	def testStarted(self):
		self.runCount = self.runCount + 1

	def summary(self):
		return "%d run, 0 failed" %self.runCount

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
	
class TestCaseTest(TestCase):
	def testResult(self):
		test = WasRun("testMethod")
		result = test.run()
		assert("1 run, 0 failed" == result.summary())

	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		result = test.run()
		assert("1 run, 1 failed", result.summary)

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown" == test.log)
		
	
if __name__ == "__main__":
	TestCaseTest("testTemplateMethod").run()
