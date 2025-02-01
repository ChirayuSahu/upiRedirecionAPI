from flask import Flask, render_template, redirect, request
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML page with instructions
    return render_template('index.html')

@app.route('/upi/<path:params>', methods=['GET'])
def generate_upi(params):
    try:
        # Decode the URL-encoded characters
        decoded_params = urllib.parse.unquote(params)
        vpa, rest = decoded_params.split('@')
        bank, amount = rest.split('&')
        
        # Generate the UPI URL
        upi_url = f"upi://pay?pa={vpa}@{bank}&am={amount}&cu=INR"
        
        # Redirect to the generated UPI URL
        return redirect(upi_url)
    
    except Exception as e:
        return f"Error: Invalid format - {str(e)}", 400

@app.route('/generate_upi', methods=['POST'])
def generate_upi_from_form():
    # Get form data from the user
    vpa = request.form['vpa']
    bank = request.form['bank']
    amount = request.form['amount']
    
    # Generate the UPI URL
    upi_url = f"upi://pay?pa={vpa}@{bank}&am={amount}&cu=INR"
    
    # Redirect to the generated UPI URL
    return redirect(upi_url)

if __name__ == '__main__':
    app.run(debug=True)
