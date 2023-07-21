import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def serve_php_file():
    try:
        php_script = 'templates/index.php'
        php_executable = 'php/php.exe'  # Replace with the full path to your PHP executable
        result = subprocess.check_output([php_executable, php_script]).decode('utf-8').strip()
        return result
    except subprocess.CalledProcessError as e:
        return f"Error executing PHP script: {e}"

if __name__ == "__main__":
    # Run the Flask application on port 8080
    app.run(port=8080)
