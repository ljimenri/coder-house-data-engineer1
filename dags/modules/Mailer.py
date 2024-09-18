import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmailBeginning(**context):
    subject = "Inicio de proceso ETL"
    from_address = "email.de.ch.ljimenez@gmail.com"
    password = "dfhhveivyfjrlcec"
    to_address = "artybandy@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Plantilla de Correo Electrónico</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding:   
        20px;
        }}

        .header {{
            background-color: #4CAF50; /* Verde */
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }}

        .body {{
            padding: 20px;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <div class="header">
            <h1>¡Hola! Te escribo para informar sobre el estado del Pipeline</h1>
        </div>
        <div class="body">
            <p>Te informamos que se ha dado <strong>inicio</strong> al proceso de ETL utilizando la Spotify API.</p>
        </div>
        <div class="footer">
            <p><strong>Luis Jimenez Rivas</strong><br>
            Dirección: Data Engineer Coder House<br>
            Teléfono: (123) 456-7890<br>
            Email: email.de.ch.ljimenez@gmail.com</p>
        </div>
    </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")



def sendEmailEnd(**context):
    subject = "Inicio de proceso ETL"
    from_address = "email.de.ch.ljimenez@gmail.com"
    password = "dfhhveivyfjrlcec"
    to_address = "artybandy@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Plantilla de Correo Electrónico</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding:   
        20px;
        }}

        .header {{
            background-color: #4CAF50; /* Verde */
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }}

        .body {{
            padding: 20px;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <div class="header">
            <h1>¡Hola! Te escribo para informar sobre el estado del Pipeline</h1>
        </div>
        <div class="body">
            <p>Te informamos que el proceso de ETL utilizando la Spotify API ha <strong>finalizado</strong> con éxito.</p>
        </div>
        <div class="footer">
            <p><strong>Luis Jimenez Rivas</strong><br>
            Dirección: Data Engineer Coder House<br>
            Teléfono: (123) 456-7890<br>
            Email: email.de.ch.ljimenez@gmail.com</p>
        </div>
    </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")