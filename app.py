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

    amount = round(float(amount), 2)
    
    # Construct the UPI link
    upi_link = f"/upi/{vpa}&{amount}"
    
    return redirect(upi_link)

@app.route('/upi/<vpa_and_amount>')
def upi_redirect(vpa_and_amount):
    # Process the URL parameters
    try:
        vpa, amount = vpa_and_amount.split('&')
        
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
        
        # Render a new page to show payment details and QR code
        return render_template('upi_payment_page.html', vpa=vpa, amount=amount, qr_code=qr_code_base64)
    
    except Exception as e:
        return f"Error: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)
