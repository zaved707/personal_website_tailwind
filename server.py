import os
import flask

app = flask.Flask(__name__)




 
@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/index.js')
def script():
    return flask.render_template('index.js')


if __name__ == '__main__':
    extra_files = [
        os.path.join(app.root_path, 'templates/index.html'),  # Single file
        os.path.join(app.root_path, 'static/style/style.css'), 
        os.path.join(app.root_path, 'static\scripts\index.js'),                                                        # Another file
    ]

    # Optionally, watch an entire directory
    
    app.run(host='0.0.0.0',debug=True, extra_files=extra_files)