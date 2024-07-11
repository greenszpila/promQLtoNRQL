# promQLtoNRQL
promQL to NRQL translator 

Simple flask app that is utilizing api endpoint for translating promQL to NRQL

1. If you don't already have Flask installed, you can install it using pip:

```sh
pip install Flask
```

2. Run the Flask application:

```sh
python app.py
```

3. Access the web application:

Open your web browser and navigate to http://127.0.0.1:5000. You should see a form where you can paste your PromQL query. When you submit the form, it will display the translated NRQL query below the form.

Make sure to replace "xxxxxx" with your actual API key in the code.

This example provides a simple implementation using Flask. For a production environment, consider adding error handling, validation, and security measures such as input sanitization and HTTPS.
