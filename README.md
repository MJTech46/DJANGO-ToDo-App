# Django ToDo App

## Overview
Welcome to the Django To-Do App, a simple yet powerful application designed to help you manage your daily tasks efficiently. This application allows users to create, update, read, mark as done, and delete tasks. It also provides account management features such as creating, updating, and deleting user accounts.

## Features
- **User Account Management**: Create, update, and delete your account with ease.
- **Task Management**: Create, update, read, mark as done, and delete tasks. Stay organized and keep track of your tasks.

## Screenshots
Here are some screenshots of the Django To-Do App:

![ToDo-Screenshot (1)](https://github.com/MJTech46/Django-ToDo-App/assets/140804026/e8f5822e-5e09-40ae-bb79-278e3480a2d5)
![ToDo-Screenshot (2)](https://github.com/MJTech46/Django-ToDo-App/assets/140804026/5d2dd75f-f2df-438e-adbd-fc0405effd44)
![ToDo-Screenshot (3)](https://github.com/MJTech46/Django-ToDo-App/assets/140804026/9a06d821-2173-4a08-821c-e8d30e4bc94b)

## Technology Stack
This application is built with the following technologies:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Django)

## Getting Started

These instructions will guide you on how to run the Django To-Do App on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed the latest version of Python and pip.
- You have a Windows/Linux/Mac machine.

### Installation and Setup

1. **Clone the Repository**
    - Open your terminal and run the following command to clone the repository:
    ```bash
    git clone https://github.com/MJTech46/Django-ToDo-App.git
    ```

2. **Navigate to the Project Directory**
    - Change to the project directory with:
    ```bash
    cd Django-ToDo-App
    ```

3. **Create a Virtual Environment**
    - It's recommended to create a virtual environment to keep the dependencies required by different projects separate. To create a virtual environment, run:
    ```bash
    python3 -m venv env
    ```
    - Activate the virtual environment with:
    ```bash
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. **Install Required Packages**
    - Install all the required packages by running:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations**
    - Django uses a SQLite database by default. Run the following command to create the necessary tables:
    ```bash
    python manage.py migrate
    ```

6. **Run the Server**
    - Finally, start the Django server with:
    ```bash
    python manage.py runserver
    ```
    - Open your web browser and visit `http://127.0.0.1:8000/` to see the application running.

Congratulations! You have successfully set up and run the Django ToDo App on your local machine. Enjoy managing your tasks!


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any queries or suggestions, please feel free to reach out to me.

Thank you for visiting my project. I hope my application helps you to manage your tasks efficiently!
