""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """

    return render_template('index.html')


@app.route("/error")
def error():
    """Эта функция запуская и отвечает за процесс возврата результата index.html."""
    cmd = ["./scriptsh/error.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/ui_tests")
def ui_tests():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/ui_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/ui_test_header")
def ui_test_header():

    cmd = ["C:/Program Files/Git/bin/bash.exe","./scriptsh/ui_test_header.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/ui_test_footer")
def ui_test_footer():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["C:/Program Files/Git/bin/bash.exe","./scriptsh/ui_test_footer.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/ui_test_search")
def ui_test_search():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/ui_test_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/api_tests")
def api_test():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/api_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/allure_ui")
def allure_ui():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/allure_ui.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/allure_api")
def allure_api():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/allure_api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/allure_summary")
def allure_summary():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/allure_summary.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/run_ui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["./scriptsh/run_aut_lk.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
