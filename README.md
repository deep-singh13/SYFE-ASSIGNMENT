# Selenium Test Automation

## Tasks Performed

- Implemented automated tests for login, inventory, cart, checkout, and logout functionalities.
- Used Selenium WebDriver to interact with the web application.
- Applied Pytest for test execution and reporting.
- Configured WebDriver setup using `webdriver-manager`.
- Utilized `conftest.py` for shared test fixtures.
- Developed a Page Object Model (POM) structure for better maintainability.
- Created reusable page classes: `base_page.py`, `login_page.py`, `inventory_page.py`, `cart_page.py`, `checkout_page.py`, and `logout_page.py`.

## Features

- Automated UI testing for a web-based application.
- Modular test cases for easy maintainability.
- Uses `pytest` for structured and efficient test execution.
- Logs and reports test execution results.
- Implements Page Object Model (POM) to separate test logic from UI elements.

## How to Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/deep-singh13/SYFE-ASSIGNMENT.git
   cd syfr_assignment
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Tests:**

   ```sh
   pytest test_cases -s #for logging task information in terminal
   ```

## Assumptions

- The web application under test is accessible and stable.
- WebDriver is managed automatically via `webdriver-manager`.
- Python 3.9.6 or a compatible version is installed.
- Required browser (Chrome) is installed for Selenium tests.
- The Page Object Model (POM) structure is followed for better code organization.

