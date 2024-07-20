# Happy Pets Web Application
Happy Pet Portfolio is a web application built with Python Flask framework. This application allows users to create and manage profiles for their pets, including photos, descriptions, and other details. It connects Pet owners to Vet doctors and enables vet doctors to easily track the health records of a pet to know the right approach when treating a pet due to its medical records. Happy provides an all round solution to enable pet owners easily care for their pets, document and follow up details of their pets. This project aims to provide an alll round care solution for pets in Nigeria, Kenya, Ghana and South Africa.


## Table of Contents
-[Installation](#installation)
-[Usage](#usage)
-[Features](#features)
-[Technologies](#technologies)
[Contributing](#contributing)
-[License](#licence)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/happy-pet-portfolio.git
    cd happy-pet-portfolio
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```


## Features
. User authentication
. Profile creation and management
. Uplaod and display pet photos
. Responsive design
. Add Pet Health Records
. Book Vet Appointments

## Usage

To run the project locally, use the following command:
```bash
python3 app.py
```

## Requirements

- Python 3.x
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- email_validator
- Flask-Caching
- Flask-WTF
- Jinja2
- requests
- SQLAlchemy
- Werkzeug
- WTForms

## Technologies
### Frontend Technologies
- HTML
- CSS
- JavaScript
- JQuery
- Jinja2
### Backend Technologies
- Python3
- Flask
- Flask-SQLAlchemy
- Flask-Login
 

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

Licience
This project is licensed under the MIT License. See the LICENSE file for more information.


### Explanation

- **Title and Project Description**: Provides a clear name and a brief overview of what the project does.
- **Table of Contents**: Helps users quickly find the information they need.
- **Installation**: Step-by-step guide on how to set up the project locally.
- **Usage**: Instructions on how to run and use the project.
- **Features**: Highlights the key features of the project.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Specifies the license under which the project is distributed.
