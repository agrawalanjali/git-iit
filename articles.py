import unittest
from selenium import webdriver

class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user ="like"
		pwd= "cool123456"
		driver = webdriver.Firefox()
		driver.get("http://127.0.0.1:8000/login/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://127.0.0.1:8000/articles/")
		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
