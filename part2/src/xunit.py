class TestResult(object):
    def __init__(self):
        self.run_count = 0
        self.fail_count = 0

    def summary(self):
        return "{} run, {} failed".format(self.run_count, self.fail_count)

    def testStarted(self):
        self.run_count = self.run_count + 1

    def testFailed(self):
        self.fail_count = self.fail_count + 1

    def add(self, result2):
        result = TestResult()
        result.fail_count = self.fail_count + result2.fail_count
        result.run_count = self.run_count + result2.run_count
        return result


class TestCase(object):
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
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def brokenMethod(self):
        raise Exception


class TestSuite():
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self):
        result = TestResult();
        for test in self.tests:
            result = result.add(test.run())
        return result
