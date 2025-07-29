# ☔ Rain Alert Notifier in Python  
A handy little weather bot that checks your local forecast using the OpenWeatherMap API and **sends you an email alert** if it's going to rain — so you can grab your umbrella in time. 🌧️📬

<img width="1536" height="1024" alt="1165d6e1-c126-44df-8658-d502d8e6e94a" src="https://github.com/user-attachments/assets/10c98855-b9e0-4b0f-941f-ae31195002d5" />



---

## 🚀 Features
- Checks short-term weather forecast via OpenWeatherMap  
- Detects upcoming rain conditions using weather codes  
- Sends automated email alerts using secure SMTP login  
- Uses environment variables for password safety  
- Ideal for automation on startup, cron jobs, or Raspberry Pi setups  

---

## 🧠 Built With
- Python 3.7+  
- `requests` for API communication  
- `smtplib` for email notifications  
- `os` for environment variable handling  
- OpenWeatherMap API    

---

## 💻 How It Works
1. The script fetches weather data for the next few hours using OpenWeatherMap.  
2. It checks each forecast block for precipitation indicators (weather code < 700).  
3. If rain is predicted, an email is instantly sent to alert the user.  
4. The script uses `starttls()` for secure SMTP communication.  


---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rain-alert-notifier.git
cd rain-alert-notifier
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Set Environment Variables

#### On Linux/macOS:
```bash
export RAIN_ALERT_EMAIL="your_email@gmail.com"
export RAIN_ALERT_APP_PASSWORD="your_gmail_app_password"
export OPENWEATHER_API_KEY="your_openweathermap_api_key"

```

#### On Windows (CMD):
```cmd
set RAIN_ALERT_EMAIL=your_email@gmail.com
set RAIN_ALERT_APP_PASSWORD=your_gmail_app_password
set OPENWEATHER_API_KEY=your_openweathermap_api_key
```

🛡️ Make sure you use a [Gmail App Password](https://support.google.com/accounts/answer/185833) — not your regular email password.

---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```
📌 Want it to run continuously?
Host your script on PythonAnywhere (or similar platforms) to schedule it and keep it running 24/7 — no local machine needed! 🖥️⏰
You’ll receive an email if rain is expected in the next few hours ☁️.

---

## 🌐 APIs Used

| API                     | Purpose                                     |
|-------------------------|---------------------------------------------|
| OpenWeatherMap	        | 3-hour interval weather forecasts           |

---

## 🧠 What You’ll Learn
- How to fetch and parse weather data via API
- How to securely send emails using Python's smtplib
- Best practices for environment variable usage
- A practical way to combine automation with weather awareness
---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- ☁️ OpenWeatherMap 

---

## 📬 Final Note
If this script reminds even one person to carry an umbrella on a rainy day, it’s already served its purpose. Keep dry — and let Python worry about the skies ☁️🧠


