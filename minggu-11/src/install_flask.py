                                                                       (base) PS C:\Users\ianma\Desktop\flask> cd examples/tutorial                                                            (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> python3 -m venv .venv                                         Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.                                                                                         (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> python3 -m venv .venv                                         (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> .venv\Scripts\activate.bat                                    (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> pip install -e .                                              Obtaining file:///C:/Users/ianma/Desktop/flask/examples/tutorial                                                          Installing build dependencies ... done                                                                                  Checking if build backend supports build_editable ... done                                                              Getting requirements to build editable ... done                                                                         Installing backend dependencies ... done                                                                                Preparing editable metadata (pyproject.toml) ... done                                                                 Requirement already satisfied: flask in c:\users\ianma\anaconda3\lib\site-packages (from flaskr==1.0.0) (2.2.2)         Requirement already satisfied: Werkzeug>=2.2.2 in c:\users\ianma\anaconda3\lib\site-packages (from flask->flaskr==1.0.0) (2.2.2)                                                                                                                Requirement already satisfied: Jinja2>=3.0 in c:\users\ianma\anaconda3\lib\site-packages (from flask->flaskr==1.0.0) (3.1.2)                                                                                                                    Requirement already satisfied: itsdangerous>=2.0 in c:\users\ianma\anaconda3\lib\site-packages (from flask->flaskr==1.0.0) (2.0.1)                                                                                                              Requirement already satisfied: click>=8.0 in c:\users\ianma\anaconda3\lib\site-packages (from flask->flaskr==1.0.0) (8.0.4)                                                                                                                     Requirement already satisfied: colorama in c:\users\ianma\anaconda3\lib\site-packages (from click>=8.0->flask->flaskr==1.0.0) (0.4.6)                                                                                                           Requirement already satisfied: MarkupSafe>=2.0 in c:\users\ianma\anaconda3\lib\site-packages (from Jinja2>=3.0->flask->flaskr==1.0.0) (2.1.1)                                                                                                   Building wheels for collected packages: flaskr                                                                            Building editable for flaskr (pyproject.toml) ... done                                                                  Created wheel for flaskr: filename=flaskr-1.0.0-0.editable-py3-none-any.whl size=4062 sha256=3c09a119b2bf49f7cc8cc3876b6a5b3018b2cc0c6b27e2f617b53997c7d360af                                                                                   Stored in directory: C:\Users\ianma\AppData\Local\Temp\pip-ephem-wheel-cache-89ewhy20\wheels\3c\cb\8e\8389e3fdd3ca0862488ae40fde937d63c4533aab5aed5b38c7                                                                                      Successfully built flaskr                                                                                               Installing collected packages: flaskr                                                                                   Successfully installed flaskr-1.0.0                                                                                     (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> flask --app flaskr init-db                                    Initialized the database.                                                                                               (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> flask --app flaskr run --debug                                Usage: flask run [OPTIONS]                                                                                              Try 'flask run --help' for help.                                                                                                                                                                                                                Error: No such option: --debug (Possible options: --debugger, --no-debugger)                                            (base) PS C:\Users\ianma\Desktop\flask\examples\tutorial> flask --app flaskr run                                         * Serving Flask app 'flaskr'                                                                                            * Debug mode: off                                                                                                      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.   * Running on http://127.0.0.1:5000                                                                                     Press CTRL+C to quit                                                                                                    127.0.0.1 - - [11/Jul/2023 18:26:58] "GET / HTTP/1.1" 200 -                                                             127.0.0.1 - - [11/Jul/2023 18:26:58] "GET /static/style.css HTTP/1.1" 200 -                                             127.0.0.1 - - [11/Jul/2023 18:26:58] "GET /favicon.ico HTTP/1.1" 404 -                                                  127.0.0.1 - - [11/Jul/2023 18:27:34] "GET /auth/register HTTP/1.1" 200 -                                                127.0.0.1 - - [11/Jul/2023 18:27:34] "GET /static/style.css HTTP/1.1" 304 -                                             127.0.0.1 - - [11/Jul/2023 18:27:49] "POST /auth/register HTTP/1.1" 302 -                                               127.0.0.1 - - [11/Jul/2023 18:27:49] "GET /auth/login HTTP/1.1" 200 -                                                   127.0.0.1 - - [11/Jul/2023 18:27:49] "GET /static/style.css HTTP/1.1" 304 -                                             127.0.0.1 - - [11/Jul/2023 18:27:59] "POST /auth/login HTTP/1.1" 302 -                                                  127.0.0.1 - - [11/Jul/2023 18:27:59] "GET / HTTP/1.1" 200 -                                                             127.0.0.1 - - [11/Jul/2023 18:27:59] "GET /static/style.css HTTP/1.1" 304 -                                             127.0.0.1 - - [11/Jul/2023 18:28:05] "GET /create HTTP/1.1" 200 -                                                       127.0.0.1 - - [11/Jul/2023 18:28:05] "GET /static/style.css HTTP/1.1" 304 -                                             127.0.0.1 - - [11/Jul/2023 18:28:21] "POST /create HTTP/1.1" 302 -                                                      127.0.0.1 - - [11/Jul/2023 18:28:21] "GET / HTTP/1.1" 200 -                                                             127.0.0.1 - - [11/Jul/2023 18:28:21] "GET /static/style.css HTTP/1.1" 304 - 