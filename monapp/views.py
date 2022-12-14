from flask import Flask, render_template

app = Flask(__name__)

# Config options â Make sure you created a â config .pyâ file .
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
