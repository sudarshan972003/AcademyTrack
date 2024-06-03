# AcademyTrack: Student Management & API Integration ( REST Framework and External APIs )

AcademyTrack is a web application designed to empower class incharges for seamless student management. It provides features for adding, updating, deleting, and viewing student records, along with a user-friendly interface for navigation. It also displays location and weather information for logged-in users and a random motivational quote fetched from a custom API built using REST Framework.

## Description

This project consist of a simple client-server architecture where:
- The server hosts an API that returns a motivativational quote.
- The AcademyTrack(Student Management System) which is a client displays a random motivativational quote in its Home Page by making a request to the server's API.

## Features

- **User Authentication**: Users can log in and log out.
- **User Registration**: New users can sign up for an account.
- **Student Management**:
  - Add new student records.
  - View a list of all students.
  - Update existing student records.
  - Delete student records.
- **Location and Weather Information**: Displays the current location and temperature for the logged-in user.
- **Custom API**: Displays a Motivational Quote fetched from a custom API built using REST Framework.

### Installation for this project :
```
pip install django
pip install requests
pip install djangorestframework
```

## How to Run

**Running the Server**:
    
    cd mm_project

1) Create a Superuser:
    ```
    python manage.py createsuperuser
    ```
    
2) Set Up the Database:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

3) Start the server:
   ```
   python manage.py runserver
   ```
   The server will be running at http://127.0.0.1:8000/.
   


**Running the Client**:
    
    cd sms_project
    
1) Create a Superuser:
    ```
    python manage.py createsuperuser
    ```
    
2) Set Up the Database:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

3) Start the server:
   ```
   python manage.py runserver
   ```
   The server will be running at http://127.0.0.1:8000/.

## Technologies Used
- **Backend Framework**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (by default in Django)
- **API Integration**:- **IPify** for providing the IP address, **ipapi** for location data, **OpenWeatherMap API** for weather information, **Custom API Built using REST Framework** for motivational quotes
- **User Authentication**: Django's built-in authentication system


## Important Files

**Server**
- settings.py: Django settings file.
- urls.py: URL routing file.
- mmapp/: The main Django app for the project.
- models.py: Defines the QuoteModel model.
- views.py: Contains the logic for the views.
- ser.py: Serializer for the QuoteModel.

**Client**
- settings.py: Django settings file.
- templates/: Contains all HTML templates for the project.
- static/: Contains static files like CSS.
- smsapp/: The main Django app for the project.
- views.py: Contains the views for handling the HTTP requests.
- models.py: Defines the database models.
- urls.py: Contains the URL configurations for the app.
- styles.css: Contains the styles for the project.

## Usage
- Upon accessing the application, users will be directed to the login page.
- New users can sign up for an account.
- After logging in, users will be directed to the home page, where they can view weather information, location details, and a random motivational quote fetched from the custom API built using REST Framework.
- Users can navigate to different sections of the application using the provided buttons.
- In the student management section, users can add, view, update, and delete student records.

## Dependencies

- Django
- Django REST Framework
- Requests (for fetching IP and weather data)

## Acknowledgements

- **IPify**: For providing the IP address.
- **ipapi**: For location data.
- **OpenWeatherMap**: For weather data.
- **Custom API**: Created by Sudarshan Thiruppathi using Django REST Framework, providing motivational quotes for the project.

## Contributing
Contributions are welcome! 
Please fork this repository and submit pull requests for any features, enhancements, or bug fixes.

## License
This project is licensed under the MIT License. 
See the LICENSE file for details.

## Author
Sudarshan Thiruppathi
