from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))

application = app

@app.route("/")
def hello():
return "Hello HostPark！\n"

if __name__ == "__main__":
app.run()