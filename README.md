# Django Savings Goals Application

## Requirements

- Django 3.0 or higher
- Python 3.6 or higher

## Setup

1. Clone the repository:

   ```sh
   git clone <repository-url>
   
 2. Create and Activate a Virtual Environment
    python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install Dependencies
   pip install -r requirements.txt
   
5.Apply Migrations
   python manage.py migrate
   
6.Create a Superuser
   python manage.py createsuperuser
   
7.Run the Development Server
   python manage.py runserver

8. if the code above doesnt work, access  the Application
by Opening your web browser and navigate to http://127.0.0.1:8000/.

# Additional Information
To access the Django admin, navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## Usage
- Home Page: Navigate to the home page to see the welcome message and general information.
- user login / regsitering new users
- Goal List: View the list of goals.
- Create Goal: Add new goals.
- Goal Detail: View detailed information about a specific goal.
- Add Contribution: Contribute towards a specific goal.
- View Contributions: View all contributions for a specific goal.
  
