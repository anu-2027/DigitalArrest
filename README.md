# 🛡️ DigitalArmour — Digital Arrest & Scam Detector

> A real-time web app that detects **Digital Arrest scams, KYC Fraud, TRAI impersonation, Prize scams, and IT Department fraud** using a weighted keyword pattern engine.

Built for Hackathon 2025 · Team Project · KSIT College

---

## 🚀 Quick Start

```bash
# Clone or download the project
cd DigitalArmour

# Install the only dependency
pip install flask

# Run the server
python app.py

# Open in browser
http://localhost:5000
```

That's it. No database, no API keys, no complex setup.

---

## 🧠 How It Works

### Detection Engine (app.py)

Every keyword in the database carries a **weight from 1 to 10** based on how exclusively it appears in scam communications:

| Weight | Meaning | Example |
|--------|---------|---------|
| 10 | Extremely high-signal — almost never legitimate | `"digital arrest"`, `"pay processing fee"` |
| 7–9 | High-signal — rarely used legitimately | `"warrant issued"`, `"sim card blocked"` |
| 4–6 | Medium-signal — needs other keywords for context | `"money laundering"`, `"trai"` |
| 1–3 | Low-signal — common word, adds minor weight | `"automated call"` |

**Risk Score formula:**
```
top5_max = sum of top 5 keyword weights in the category
raw      = sum of matched keyword weights
score    = min(100, raw / top5_max × 100)
final    = max(score, severity_floor)
```

**Severity floors** ensure the bar reflects real danger:
- CRITICAL (Digital Arrest) → always ≥ 70%
- HIGH (KYC, TRAI, IT Dept) → always ≥ 50%
- MEDIUM (Prize Scam) → always ≥ 30%

---

## 📁 Project Structure

```
DigitalArmour/
├── app.py               ← Flask backend + weighted detection engine
├── requirements.txt     ← Just Flask
├── templates/
│   └── index.html       ← Full frontend (HTML + CSS + JS, single file)
└── README.md
```

---

## 🎯 Scam Categories

| Category | Severity | Trigger Example |
|----------|----------|----------------|
| 🚔 Digital Arrest | CRITICAL | "digital arrest", "stay on call", "warrant issued" |
| 🏦 KYC Fraud | HIGH | "kyc expired", "account will be deactivated" |
| 📡 TRAI Scam | HIGH | "sim card blocked", "press 9 to speak" |
| 🎰 Prize / Lottery | MEDIUM | "you have won", "pay processing fee" |
| 📋 IT Department | HIGH | "click to claim refund", "tax arrest" |

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the frontend |
| POST | `/analyze` | Analyse a message for scam patterns |
| GET | `/analytics` | Dashboard stats (scams today, breakdown) |
| GET | `/test-cases` | 5 preloaded demo test cases |

### POST /analyze — Request
```json
{ "message": "Your SBI KYC has expired. Click to update." }
```

### POST /analyze — Response
```json
{
  "status": "SCAM_DETECTED",
  "primary_scam": "KYC Fraud",
  "severity": "HIGH",
  "risk_score": 85,
  "matched_keywords": ["kyc expired", "sbi kyc"],
  "keyword_weights": { "kyc expired": 10, "sbi kyc": 8 },
  "explanation": "...",
  "action": ["...", "..."],
  "other_matches": []
}
```

---

## 🧪 Demo Test Cases (Copy-Paste for Judges)

**1. Digital Arrest — CRITICAL**
```
This is Officer Rajiv Sharma from the Central Bureau of Investigation.
Your Aadhaar number is linked to a money laundering case worth 4 crore rupees.
You are under digital arrest effective immediately. A warrant has been issued.
Stay on this video call and do not disconnect. Do not tell anyone.
```

**2. KYC Fraud — HIGH**
```
Dear SBI Customer, your SBI KYC has expired as of today.
Your account will be deactivated within 24 hours if KYC is not updated.
Click to update your KYC: sbi-kyc-update.net/verify
Enter your Aadhaar OTP to complete re-KYC.
```

**3. TRAI Scam — HIGH**
```
URGENT TRAI Notice: Illegal use of your number has been detected.
Your SIM card will be disconnected within 2 hours by the Department of Telecom.
Press 9 to speak with a DoT officer to avoid disconnection.
```

**4. Prize Scam — MEDIUM**
```
Congratulations! You have won Rs 25,00,000 in the KBC Lucky Draw 2025.
You are our lucky winner. To claim your prize money,
pay a processing fee of Rs 2500 to activate your winner account.
```

**5. IT Department Scam — HIGH**
```
Income Tax Department Alert: Your TDS refund of Rs 18,450 has been approved.
Your PAN card has been flagged for unreported income.
Click to claim refund: incometax-refund.net/claim
Failure to comply may result in tax arrest proceedings.
```

---

## 📊 Dashboard Features

- **Scams Detected Today:** Live KPI cards
- **Money Protected:** Estimated value saved
- **Scam Breakdown:** Animated bar chart by category
- **Recent Detections:** Live feed with city & scam type
- **Risk Score:** Animated 0–100% meter with color coding
- **Trigger Phrases:** Highlighted keywords with weight labels

---

## 🔴 Color Coding

| Color | Meaning | Risk Score |
|-------|---------|-----------|
| 🟢 Green | SAFE — no patterns found | — |
| 🟡 Yellow | MEDIUM — possible scam | 30–60% |
| 🟠 Orange | HIGH — likely scam | 60–85% |
| 🔴 Red | CRITICAL — confirmed scam pattern | 70–100% |

---

## 🛠️ Tech Stack

- **Backend:** Python 3 + Flask (zero external ML dependencies)
- **Frontend:** Vanilla HTML + CSS + JavaScript (single file, no frameworks)
- **Fonts:** IBM Plex Mono + Outfit (Google Fonts)
- **Detection:** Custom weighted keyword engine with severity flooring

---

## 📞 Important Helplines

- **1930** — National Cybercrime Helpline (India)
- **cybercrime.gov.in** — Online complaint portal
- **cert-in.org.in** — CERT-In India
- **report.phishing@cert-in.org.in** — Phishing reports

---

## 👥 Team

Built at KSIT College for Hackathon 2025.

*"No Indian law permits digital arrest. When in doubt — hang up and call 1930."*
