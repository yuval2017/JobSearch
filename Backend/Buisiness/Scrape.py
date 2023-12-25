from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from Backend.Buisiness.Job import Job


class Scrape:
    def __init__(self, path=None, key_search = ""):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_window_size(1120, 1000)
        url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + key_search + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
        self.driver.get(url)

    from selenium.common.exceptions import NoSuchElementException



    def get_jobs(self, verbose=True):
        li_elements = []
        button_locator = (By.CLASS_NAME, "button-base_Button__9SPjH")
        try:
            ul_element = self.driver.find_element(By.CSS_SELECTOR, 'ul[class^="JobsList_jobsList"]')
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        except NoSuchElementException:
            pass
        bool_break = True
        while bool_break:
            try:
                container = self.driver.find_element(By.CLASS_NAME,"JobsList_buttonWrapper__haBp5")
                # Wait for the button to be present (not necessarily clickable)
                button = WebDriverWait(container, 10).until(EC.element_to_be_clickable(button_locator))
                button.click()
                while button.get_attribute("data-loading") == "true":
                    continue
                # Click the button

                button_locator = (By.CLASS_NAME, "button-base_Button__9SPjH")
                try:
                    ul_element = self.driver.find_element(By.CSS_SELECTOR, 'ul[class^="JobsList_jobsList"]')
                    new_li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
                    if len(new_li_elements) <= len(li_elements):
                        bool_break = False
                    else:
                        li_elements = new_li_elements

                except NoSuchElementException:
                    pass

                # Wait for 4 seconds
                time.sleep(3)

                # Click on an empty space (move to coordinates (0, 0) and click)
                action_chains = ActionChains(self.driver)
                action_chains.move_by_offset(0, 0).click().perform()

            except TimeoutException:
                # If the button is not present, break out of the loop
                break
        jobs = []



        # Iterate over each list item and print its text content
        for li_element in li_elements:
            try:
                company_name = li_element.find_element(By.CSS_SELECTOR,
                                                       'span[class^="EmployerProfile_employerName"]').text
            except NoSuchElementException:
                company_name = "Company Name not found"

            try:
                job_link = li_element.find_element(By.CSS_SELECTOR, 'a[class^="JobCard_seoLink"]').text
            except NoSuchElementException:
                job_link = "Job Link not found"

            try:
                job_location = li_element.find_element(By.CSS_SELECTOR, 'div[class^="JobCard_location"]').text
            except NoSuchElementException:
                job_location = "Job Location not found"

            try:
                job_decription = li_element.find_element(By.CSS_SELECTOR,
                                                         'div[class^="JobCard_jobDescriptionSnippet"]').text
            except NoSuchElementException:
                job_decription = "Job Description not found"

            job = Job(company_name, job_link, job_location, job_decription)
            jobs.append(job)
            if verbose:
                print(job)
                print('----------------------')
        return jobs

