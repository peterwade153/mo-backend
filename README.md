[![Django CI](https://github.com/peterwade153/mo-backend/actions/workflows/django.yml/badge.svg)](https://github.com/peterwade153/mo-backend/actions/workflows/django.yml)
# mo-backend

Track service providers locations

Requires Postgres, Postgis and built with Python 3.8 

### Installation

1. Create and activate a virtual environment and Clone the project `https://github.com/peterwade153/mo-backend.git`

2. Move into the project folder
   ```
   $ cd mo-backend
   ```

3. Create a postgres database, and Create Extensions to enable handling of Geospatial storage and requests. Connect to the database created and run the commands below.
    ```
    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;
    ```

4. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

5. Create a `.env` file from the `.env.sample` file.  Replace the variables in the sample file with the actual variables, such the database credentials, secret key etc.

6. Run migrations
   ```
   python manage.py migrate
   ```

7. Start server
   ```
   python manage.py runserver
   ```

8.  The application can be accessed via swagger docs here http://127.0.0.1:8000/

9. To run tests
   ```
   python manage.py test
   ```

