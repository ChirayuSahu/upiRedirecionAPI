import qrcode
from flask import Flask, render_template, request, redirect
import io
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_upi', methods=['POST'])
def generate_upi():
    vpa = request.form['vpa']
    amount = request.form['amount']
    
    # Construct the UPI link
    upi_link = f"upi://pay?pa={vpa}&am={amount}&cu=INR"
    
    # Generate QR code for the UPI link
    qr = qrcode.make(upi_link)
    
    # Save the QR code as an image in memory
    img = io.BytesIO()
    qr.save(img, format='PNG')
    img.seek(0)  # Reset the pointer to the beginning
    
    # Convert image to base64 encoding
    qr_code_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    # Pass the base64-encoded image to the template
    return render_template('index.html', qr_code=qr_code_base64, upi_link=upi_link)

@app.route('/upi/<vpa_and_amount>')
def upi_redirect(vpa_and_amount):
    # Process the URL parameters
    try:
        vpa, amount = vpa_and_amount.split('&')
        amount = amount  # Get the amount after the `=`
        
        upi_link = f"upi://pay?pa={vpa}&am={amount}&cu=INR"
        return redirect(upi_link)
    except Exception as e:
        return f"Error: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)
