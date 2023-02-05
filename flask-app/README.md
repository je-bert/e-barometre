## How to install a package

   MacOS & Linux:
   ```bash
   $ pip3 install {PACKAGE_NAME}
   $ pip3 freeze > requirements.txt
   ```

   Windows:
   ```bash
   $ pip install {PACKAGE_NAME}
   $ pip freeze > requirements.txt
   ```

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd flask-app
   ```

4. Create a new virtual environment

   MacOS & Linux:
   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate

   ```
   Windows:
   ```bash
   $ py -m venv venv
   $ venv/Scripts/activate.bat
   ```


5. Install the requirements

   MacOS & Linux:
   ```bash
   $ pip3 install -r requirements.txt
   ```

   Windows:
   ```bash
   $ pip install -r requirements.txt
   ```

6. Run the app

   MacOS & Linux:
   ```bash
   $ python3 app.py
   ```

   Windows:
   ```bash
   $ py app.py
   ```

   OR

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!