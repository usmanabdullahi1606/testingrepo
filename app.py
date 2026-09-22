from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)



products = [
    {
        'id' : 1,
        'name' : 'Studio Microphone',
        'price' : 10000,
        'description' : 'sensitive and detailed, great for vocals and acoustic instruments in a treated room',
        'image' : 'images/microphone.jpg'

    },
    {
        'id' : 2,
        'name' : 'Audio Interface',
        'price' : 70000,
        'description' : "converts analog signals (your voice, instruments) into digital data your computer can process, and vice versa. It's the central hub connecting microphones, instruments, and speakers to your DAW (Digital Audio Workstation).",
        'image' : 'images/audio interface.avif',
    
    },

    {
        'id' : 3,
        'name' : 'Studio Headphones',
        'price' : 15000,
        'description' : 'closed-back headphones are used for tracking (recording) since they isolate sound and prevent bleed into the mic; open-back headphones are often used for mixing since they offer a more natural, spacious sound.',
        'image' : 'images/headphone.avif'

    }
]
cart = [

]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    for item in products:
        if item['id'] == id:
            return render_template('product.html', product=item)
@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    for item in products:
        if item['id'] == id:
            cart.append(item)
    return redirect(url_for("add_to_cart"))
            

    
if __name__ == '__main__':
    app.run(debug=True)
