class Job:
    def __init__(self, company_name, job_link, job_location, job_description):
        self._company_name = company_name
        self._job_link = job_link
        self._job_location = job_location
        self._job_description = job_description

    # Getter for company_name
    @property
    def company_name(self):
        return self._company_name

    # Setter for company_name
    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    # Getter for job_link
    @property
    def job_link(self):
        return self._job_link

    # Setter for job_link
    @job_link.setter
    def job_link(self, value):
        self._job_link = value

    # Getter for job_location
    @property
    def job_location(self):
        return self._job_location

    # Setter for job_location
    @job_location.setter
    def job_location(self, value):
        self._job_location = value

    # Getter for job_description
    @property
    def job_description(self):
        return self._job_description

    # Setter for job_description
    @job_description.setter
    def job_description(self, value):
        self._job_description = value

    # toString function (__str__)
    def __str__(self):
        return f"Company Name: {self._company_name}\nJob Link: {self._job_link}\nJob Location: {self._job_location}\nJob Description: {self._job_description}"



