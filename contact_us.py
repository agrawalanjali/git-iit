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
		driver.get("http://127.0.0.1:8000/contact_us/")
		name="anj"
		email= "agrawal41@gmail.com"
		issue_type= "anjali gtre"
		message= "gen"
		elem = driver.find_element_by_id("id_name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("id_Email")
		elem.send_keys(email)
		elem = driver.find_element_by_id("id_Issue_type")
		elem.send_keys(issue_type)
		elem = driver.find_element_by_id("id_message")
		elem.send_keys(message)
		driver.findElement(By.id("uploadbutton")).click;
		driver.find_element_by_class_name('btn-block').click()
		#driver.find_element_by_class_name("btn btn-primary").text
		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()

