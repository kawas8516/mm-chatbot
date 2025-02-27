# CookingBot

CookingBot is a Django-based web application designed to help users manage and discover recipes. It leverages Django for the backend and includes REST API capabilities for easy integration with other services.

## Features

- Recipe management
- Ingredient tracking
- User authentication and authorization
- REST API for integration with other services

## Requirements

- Python 3.9+
- Django 4.0+
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cookingbot.git
    cd cookingbot
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Use the admin interface at `http://127.0.0.1:8000/admin/` to manage recipes and ingredients

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License.
