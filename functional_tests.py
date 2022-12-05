from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight awa
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
         )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])


        # She types "Buy peacock feathers" into a text box (Edith's hobby
	    # is tying fly-fishing lures

	    # When she hits enter, the page updats and now the page lists
	    # 1: buy peacock feathers to make fly

	    # The page updates again and shows both items on her list

	    # Edith wonders if the site will remember her list.  She sees a unique 
	    # Url has been generated for her to return to.

	    # She visits the url and sees her list is still there.
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main()
