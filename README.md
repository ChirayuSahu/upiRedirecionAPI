
<img src="https://socialify.git.ci/ChirayuSahu/upiRedirectionAPI/image?language=1&name=1&owner=1&stargazers=1&theme=Dark" alt="upiRedirectionAPI"/>

![cover](https://github.com/user-attachments/assets/a7779007-b4e3-4fd3-92ee-52b84a766f8e)

# UPI Payment API

A simple API that generates UPI payment links and QR codes for easy transactions. This web application allows users to generate UPI payment links by providing the Virtual Payment Address (VPA) and the payment amount. The generated UPI link can be used to redirect users to their UPI apps like Google Pay, PhonePe, etc.

## Features

- **Generate UPI Links:** Users can generate UPI links for specific VPAs and amounts.
- **QR Code Generation:** A QR code is generated for easy scanning to make payments.
- **Customizable UPI Links:** Allows users to customize payment details, like VPA and amount, using the generated URL.

## Technologies Used

- **Frontend:** HTML, CSS (Tailwind CSS)
- **Backend:** Python (Flask)
- **QR Code Generation:** Python's `qrcode` library
- **Payment Redirection:** Custom UPI links for Google Pay, PhonePe, etc.

## Installation

To run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChirayuSahu/upiRedirectionAPI.git
   cd upiRedirectionAPI
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application:**
   ```bash
   flask run
   ```

6. **Visit the App:**
   Open a browser and go to `http://127.0.0.1:5000/` to use the application locally.

## Usage

1. **Enter the VPA (Virtual Payment Address):**
   Example: `vpa@bank`

2. **Enter the Amount:**
   Enter the payment amount in INR (e.g., `100`).

3. **Click "Generate UPI Link":**
   Upon submission, the app will generate a UPI link and QR code for the payment.

4. **Payment Options:**
   You can select your preferred payment method (e.g., Google Pay, PhonePe) to initiate the payment.

## Direct UPI Link Format

You can directly generate a UPI link by visiting the following URL format:

```
https://upi-redirection-api.vercel.app/upi/vpa@bank&amount
```

Replace `vpa@bank` with the actual VPA and `amount` with the payment amount.

## Contributing

If you have suggestions or want to contribute, feel free to create an issue or a pull request. Contributions are welcome!

## License

This project is open-source and available under the MIT License.
