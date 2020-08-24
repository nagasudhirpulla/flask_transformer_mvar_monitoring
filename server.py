from flask import Flask, render_template
from transDataFetcher import getTransData

# create a server instance
app = Flask(__name__)

# define a route
@app.route('/')
def home():
    return render_template("home.html")

# define a route
@app.route('/trans_monitor')
def transMonitor():
    objList = getTransData()
    return render_template("trans_monitor.html.j2", data={"ictData": objList})


# start the server at specific port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
