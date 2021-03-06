from BasePage                import BasePage
from BasePage                import IncorrectPageException
from oig.Constants           import TT_Constants
from oig.UIMap               import OrganizationalChartPageMap


#this is a page object for the organizational chart page
#accessed after clicking the Organizational Chart link 
class OrganizationalChartPage(BasePage):

    def __init__(self, driver):
        super(OrganizationalChartPage, self).__init__(driver)
  
    def _verify_page(self):
    	try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         OrganizationalChartPageMap['OrganizationalChartXpath']
          )
        except:   
          raise IncorrectPageException
          
    
    
    
    
      