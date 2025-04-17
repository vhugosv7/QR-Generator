# QR Code Generator deploy
QR code generator with different types of data: URL or text, personal card information, and artistic QR codes. This version includes a new artistic QR method that allows the user to select a logo from a list due to access to external internet sites limitation. This project is hosted on PythonAnywhere. Visit https://vhugosv7.pythonanywhere.com/


## Features

- **QR Code with URL or some text.**: The `home_qr` function generates a QR code with the URL, scale, border, and background color given by the user.
- **QR code which encodes contact information.**: The `Vcard()` generates a QR code with the full name, title, email, phone mobile, scale, border, and background color given by the user.
- **Add a logo to a QR code .**: The `artCard()` generates a QR code with a logo in the middle chosen with the URL, background image, scale, border, and background color given by the user.
- **Folder images.** The QR codes generated are saved in the 'static' folder.


## Installation

Follow the steps below to set up and run this project locally.

### Prerequisites

- Flask 3.1.0
- segno 1.6.6
- Python 3.11.7
- Bootstrap 5.02

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/vhugosv7/QR-Generator.git

2. Navigate to the project folder:
   ```bash
   cd QR-Generator

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask application:
   ```bash
   python QR_generator.py

5. Open your browser and navigate to http://127.0.0.1:5000/ to interact with the application.



### Screnshoots


* **Requesting URL QR code**
  
  ![QR code image](https://github.com/user-attachments/assets/8eff5299-a37f-4a46-8404-81446b9074e2)

  **URL QR code Result:**
  ![Result](https://github.com/user-attachments/assets/dbf0e170-84f5-4d48-8699-1b5633de1f27)

  


* **QR Code with contact information**
  
  ![contact information](https://github.com/user-attachments/assets/ea337b43-a07c-4020-a614-9959ab721cf9)
  
  **QR Code with contact information result**
  ![info result](https://github.com/user-attachments/assets/04d547b5-757d-4527-8fc7-9f26da4f5ce0)



* **Artistic QR Code**
  
  ![artistic QR](https://github.com/user-attachments/assets/2d0598bd-7432-45d4-b808-2a896039b795)

  **Artistic QR Code result**
  ![result artistic](https://github.com/user-attachments/assets/3dd667dd-843f-468d-a610-078b7af2feef)

  

## To consider
- To generate another QR, the user must press the reset button
![reset](https://github.com/user-attachments/assets/599ed07d-c30e-4238-bd1f-f2a0d392a57c)


