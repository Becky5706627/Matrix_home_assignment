# Test Automation Project for Demo Web Application

## Objective

This project is a test automation suite designed to automate the interaction with a demo web application. It includes automated tests to perform login operations and to validate the number of successful transactions in a table.

## Technology Stack

This project uses Python with the PyTest framework for automated testing. Selenium WebDriver is used for browser interaction, and all dependencies are managed using a `requirements.txt` file.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip for installing Python packages
- A modern web browser (Chrome, Firefox, etc.)

### Installation

1. Clone the repository to your local machine using:

```sh
git clone [repository-link]
```

2. Navigate to the cloned directory:
```sh
cd [local-repository]
```

3. Install the required Python packages:
```sh
pip install -r requirements.txt
```

### Running the Tests

To run the automated tests, execute the following command in the project's root directory:
```sh 
pytest 
```

This will start the test suite which will automatically:

- Open a web browser.
- Navigate to the demo application: https://demo.applitools.com/.
- Perform login operations using test credentials.
- Count the number of successful transactions in the table.
- Assert the number of successful transactions against an expected value.
### Test Scenarios
The following test scenarios are included:

- test_login.py - Validates the login functionality with correct credentials.
- test_transaction.py - Verifies that the number of successful transactions is as expected.

### Project Structure
- pages/ - Contains Page Object Models for the demo web application.
- tests/ - Contains the test scripts for the automation suite.
- utils/ - Includes utility functions and custom assertions.
- conftest.py - Contains setup and teardown configurations for the tests.


### Clean Up
The automation script ensures that the web browser is closed gracefully after the test execution.

### Evaluation Criteria
The project will be evaluated based on the following criteria:

- Project organization and code structure.
- Effective use of the Page Object Design Pattern.
- Accurate automation of login and transaction counting.
- Appropriate use of assertions and clean code practices.
- Handling of potential exceptions or errors during execution.
