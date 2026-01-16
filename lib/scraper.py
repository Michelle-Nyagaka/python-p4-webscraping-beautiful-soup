from bs4 import BeautifulSoup
import requests

# Set headers to mimic a browser
headers = {'user-agent': 'my-app/0.0.1'}

# Scrape the main Flatiron School page
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')

# Grab the main header
main_header = doc.select('.heading-financier')[0].contents[0].strip()
print("Main header:", main_header)

# Scrape the courses page
courses_html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
courses_doc = BeautifulSoup(courses_html.text, 'html.parser')

# Grab all course titles
courses = courses_doc.select('.heading-60-black.color-black.mb-20')

print("\nCourses offered:")
for course in courses:
    print("-", course.contents[0].strip())
