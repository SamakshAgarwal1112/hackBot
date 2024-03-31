# hackBot
hackBot is a scraping bot developed in Python using Selenium to gather basic hackathon data from websites such as MLH, devfolio, devpost, and unstop. This README provides detailed information on how to set up and run the hackBot, along with important notes regarding its usage.

## Disclaimer
This project is intended for educational and learning purposes only. It is designed to showcase web scraping techniques using Selenium and Python. I have no intention of stealing data or exploiting websites. Users are advised to comply with the terms of service and robots.txt of the websites being scraped.

## Setup
To set up hackBot, follow these steps:

### Automatic Setup
Run the setup.sh script provided in the repository. This script automates the setup process for you.

```bash
./setup.sh
```

### Manual Setup

Create and activate a virtual environment: Before installing any dependencies, it's a good practice to create a virtual environment to isolate your project's dependencies from other Python projects on your system.

```bash
python -m venv env
source env/bin/activate
```

Navigate to the backend directory: In order to set up the backend of hackBot, you need to navigate to the backend directory where the Django application resides.

```bash
cd backend
```

Install Django dependencies: Use pip to install the required dependencies specified in the requirements.txt file.

```bash
pip install -r requirements.txt
```

Run database migrations: Django uses migrations to manage changes to the models and schema of your database. Run the following command to apply any pending migrations.

```bash
python manage.py migrate
```
Start the Django server: Launch the Django development server, which will serve as the backend for hackBot. By default, the server runs on http://127.0.0.1:8000/.

```bash
python manage.py runserver
```

Wait for the server to start: Allow a few seconds for the Django server to start up before proceeding to set up the frontend.
Now, Navigate to the frontend directory: Now that the backend is set up, switch to the frontend directory to set up the user interface.

```bash
cd ../frontend
```

Install frontend dependencies: Use npm to install the required dependencies for the React frontend.

```bash
npm install
```

Start the React frontend: Launch the React development server, which will serve the frontend of hackBot.

```bash
npm run dev
```

### Running hackBot
Once the setup is complete, you can run hackBot using the run.sh script provided in the repository.

```bash
./run.sh
```

This script will execute the necessary commands to run the hackBot.

### Contributing
Since, hackBot is a personal project made for only learning purposes, Contributions to hackBot are not welcome! Feel free to fork it and learn from it.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
