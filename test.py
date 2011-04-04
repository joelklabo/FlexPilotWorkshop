from selenium import selenium
import unittest, time, re

class test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost:8000/")
        self.selenium.start()
    
    def test_test(self):
        sel = self.selenium
        sel.open("/")
        sel.wait_for_flex_ready("id=example1", "")
        sel.flex_click("id=example1", "chain=id:example1/id:src/name:UITextField*")
        sel.flex_type("id=example1", "text=sdflkjl,chain=id:example1/id:src/name:UITextField*")
        sel.flex_click("id=example1", "chain=id:example1/name:Button*")
        sel.flex_click("id=example1", "chain=id:example1/name:VBox*/id:milkCB")
        sel.flex_click("id=example1", "chain=id:example1/name:VBox*/name:Button*")
        sel.flex_click("id=example1", "chain=id:example1/name:VBox*/name:Button*")
        sel.flex_click("id=example1", "chain=id:example1/name:VBox*/name:Button*")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
