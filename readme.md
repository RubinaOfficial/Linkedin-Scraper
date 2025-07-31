# LinkedIn Name Scraper

This project is an automated Python script that logs into LinkedIn, searches for a specific term (e.g., "Hospitals"), filters results by "People", and scrapes only user names from the search results. The names are saved to a CSV file.

## Features
- Automated login to LinkedIn
- Searches for a given term
- Filters results by the "People" category
- Extracts clean, valid names (ignores job posts, ads, etc.)
- Random delays for anti-bot detection
- Saves results in `linkedin_names_only.csv`

## Requirements
- Python 3.7+
- Google Chrome browser
- ChromeDriver (must match your Chrome version)

## Python Libraries Used
- selenium
- time
- random
- csv
- re

Install selenium via pip:
```bash
pip install selenium
```

## Configuration
In the script, replace these with your LinkedIn credentials:
```python
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
```

## How It Works
1. Opens LinkedIn login page
2. Logs in with provided credentials
3. Searches for "Hospitals"
4. Clicks on the "People" filter
5. Extracts names from search results (up to 100 pages or until no more pages)
6. Applies basic validation to ensure the scraped text is a real name
7. Writes the names into a CSV file called `linkedin_names_only.csv`

## Output
A CSV file containing:
```
Full Name
John Smith
Emily Davis
...
```

## Notes
- Always respect LinkedIn's Terms of Service.
- This script is intended for educational use only.
- Do not run this on your main LinkedIn account to avoid risk of suspension.

## To-Do / Future Enhancements
- Add support for scrolling and dynamic loading
- Extract job titles and profile URLs
- Export to Excel format

---
Feel free to modify and extend this project based on your specific requirements.

