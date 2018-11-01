"""


VERY Simple Web App
illya kovarik



"""

from flask import Flask, render_template
#%%

app = Flask(__name__)
#%%

@app.route('/')
def index():
    return render_template('illya_page.html')

#%%

if __name__ == '__main__':
    app.run(debug=True)