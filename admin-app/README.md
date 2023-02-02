## How to add a package
pip install {PACKAGE_NAME}
pip freeze > requirements.txt

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd admin-app
   ```

4. Create a new virtual environment

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip3 install -r requirements.txt
   ```

6. Run the app

   ```bash
   $ python3 app.py
   ```

   OR

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!