from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
	
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app.  She goes 
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

	# She is invited to enter a to-do item straight away

	# She types "Buy peacock feathers" into a text box (Edith's hobby
	# is tying fly-fishing lures

	# When she hits enter, the page updats and now the page lists
	# 1: buy peacock feathers to make fly

	# The page updates again and shows both items on her list

	# Edith wonders if the site will remember her list.  She sees a unique 
	# Url has been generated for her to return to.

	# She visits the url and sees her list is still there.
if __name__ == '__main__':
    unittest.main()
