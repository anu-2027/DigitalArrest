from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ═══════════════════════════════════════════════════════════
#  DETECTION ENGINE  —  v2 with weighted keyword risk scores
# ═══════════════════════════════════════════════════════════

SCAM_PATTERNS = {
    "Digital Arrest": {
        "severity": "CRITICAL",
        "keywords": {
            "digital arrest":             10,
            "you are under arrest":       10,
            "cyber arrest":               10,
            "warrant issued":              9,
            "enforcement directorate":     9,
            "stay on call":                9,
            "do not disconnect":           9,
            "do not tell anyone":          9,
            "cbi officer":                 8,
            "ncb officer":                 8,
            "ed officer":                  8,
            "video call verification":     8,
            "arrested online":             8,
            "cbcid":                       7,
            "money laundering":            7,
            "your aadhar linked":          7,
            "illegal activity detected":   7,
            "your number is flagged":      6,
            "central bureau":              6,
            "narcotics":                   5,
            "national security":           4,
        },
        "explanation": (
            "This is a 'Digital Arrest' scam — one of India's fastest-growing cyber frauds. "
            "No Indian law permits 'digital arrest'. The CBI, ED, NCB, or police will NEVER "
            "contact you on WhatsApp/Skype to arrest you or demand you stay on a video call. "
            "These scammers impersonate government officers to extort money using fear and urgency."
        ),
        "action": [
            "Hang up immediately — no real officer conducts arrests over video calls.",
            "Do NOT share personal documents, OTPs, or transfer any money.",
            "Report to cybercrime.gov.in or call helpline 1930.",
            "Inform your family — scammers often demand secrecy to isolate victims.",
            "Screenshot the number and report it to your nearest police station.",
        ],
    },

    "KYC Fraud": {
        "severity": "HIGH",
        "keywords": {
            "kyc expired":                10,
            "update your kyc":            10,
            "kyc pending":                 9,
            "your account will be deactivated": 9,
            "account will be suspended":   9,
            "your upi blocked":            9,
            "sbi kyc":                     8,
            "hdfc kyc":                    8,
            "paytm kyc":                   8,
            "google pay kyc":              8,
            "phonepe kyc":                 8,
            "re-kyc":                      8,
            "video kyc":                   7,
            "kyc update":                  7,
            "kyc verification":            6,
            "bank account blocked":        6,
            "click link to update":        6,
            "pan card verification":       5,
            "aadhaar otp":                 5,
            "link expired":                4,
        },
        "explanation": (
            "This is a KYC (Know Your Customer) fraud. Scammers pretend to be from your bank "
            "or payment app and claim your account will be blocked unless you verify. "
            "Legitimate banks NEVER ask for OTPs, passwords, or CVV numbers over phone or SMS. "
            "The link they send leads to a fake phishing page designed to steal your credentials."
        ),
        "action": [
            "Never click links in SMS/WhatsApp messages claiming to be your bank.",
            "Your bank will NEVER ask for OTP, password, or full card number.",
            "Call your bank's official helpline (on the back of your debit card) to verify.",
            "Report phishing links to report.phishing@cert-in.org.in",
            "Block the number and report to 1930 (National Cyber Crime Helpline).",
        ],
    },

    "TRAI Scam": {
        "severity": "HIGH",
        "keywords": {
            "sim card blocked":                 10,
            "sim blocked":                       9,
            "your number will be disconnected":  9,
            "mobile number deactivated":         9,
            "mobile connection suspended":       9,
            "press 9 to speak":                  9,
            "press 1 to avoid":                  9,
            "trai":                              8,
            "dot officer":                       8,
            "department of telecom":             7,
            "illegal use of your number":        7,
            "your number misused":               7,
            "telecom authority":                 6,
            "telecom regulatory":                6,
            "your sim card":                     5,
            "automated call":                    4,
        },
        "explanation": (
            "This is a TRAI (Telecom Regulatory Authority of India) impersonation scam. "
            "Fraudsters use automated calls/messages claiming your SIM will be blocked for "
            "'illegal use'. TRAI never directly contacts individual subscribers. "
            "No telecom authority blocks your number without prior written notice through official channels."
        ),
        "action": [
            "Ignore and block automated calls claiming to be from TRAI or DoT.",
            "TRAI never calls individual subscribers — this is 100% a scam.",
            "Do not press any number on the automated call (it confirms your number is active).",
            "Register your complaint at trai.gov.in or call 1800-110-420.",
            "Report the number to your telecom provider as spam.",
        ],
    },

    "Prize / Lottery Scam": {
        "severity": "MEDIUM",
        "keywords": {
            "pay processing fee":           10,
            "send registration fee":        10,
            "claim fee":                    10,
            "kbc winner":                    9,
            "kaun banega crorepati":         9,
            "amazon lucky draw":             9,
            "flipkart winner":               9,
            "1 crore prize":                 9,
            "you have won":                  8,
            "congratulations you won":       8,
            "lucky winner":                  8,
            "lottery winner":                8,
            "claim your prize":              7,
            "prize money":                   7,
            "lucky draw":                    7,
            "you are selected":              6,
            "you have been selected":        6,
            "scratch and win":               5,
            "reward points redeemable":      4,
        },
        "explanation": (
            "This is a classic Prize/Lottery scam. You cannot win a contest you never entered. "
            "Scammers ask for a small 'processing fee' or 'tax' upfront — once paid, they "
            "vanish or keep demanding more. KBC, Amazon, and Flipkart NEVER announce "
            "winners via unknown WhatsApp numbers or unsolicited SMS messages."
        ),
        "action": [
            "Ignore — if you didn't enter a contest, you cannot have won it.",
            "NEVER pay any 'processing fee', 'tax', or 'registration fee' to claim a prize.",
            "Verify any brand promotion only through their official website or app.",
            "Report to National Consumer Helpline: 1800-11-4000.",
            "Block and report the number immediately.",
        ],
    },

    "IT Department Scam": {
        "severity": "HIGH",
        "keywords": {
            "click to claim refund":         10,
            "income tax refund approved":    10,
            "tax arrest":                    10,
            "it raid":                        9,
            "black money":                    9,
            "unreported income":              9,
            "financial irregularity":         9,
            "income tax notice":              8,
            "tax evasion":                    8,
            "tds refund":                     8,
            "itr refund":                     8,
            "your pan card flagged":          8,
            "income tax officer":             7,
            "income tax":                     6,
            "tax refund":                     6,
            "tax dues":                       6,
            "it department":                  5,
            "tax department":                 5,
        },
        "explanation": (
            "This is an Income Tax / IT Department impersonation scam. The real Income Tax "
            "Department sends all notices through the official portal (incometax.gov.in) or "
            "registered post. They NEVER call to demand immediate payment, threaten arrest "
            "over the phone, or send SMS links to claim refunds."
        ),
        "action": [
            "All genuine IT notices arrive via incometax.gov.in — check there first.",
            "Never click any 'refund' links received via SMS or WhatsApp.",
            "Do not transfer money to any account citing 'tax dues' on a phone call.",
            "Consult a chartered accountant if you receive suspicious tax communication.",
            "Report to cybercrime.gov.in or call 1930.",
        ],
    },
}

SEVERITY_FLOOR = {"CRITICAL": 70, "HIGH": 50, "MEDIUM": 30}


def compute_risk_score(matched_weights, all_weights, severity):
    if not matched_weights:
        return 0
    top5_max = sum(sorted(all_weights.values(), reverse=True)[:5])
    raw = sum(matched_weights.values())
    score = int(min(100, (raw / top5_max) * 100))
    return max(score, SEVERITY_FLOOR.get(severity, 0))


def detect_scam(text):
    text_lower = text.lower()
    scores = {}

    for scam_type, data in SCAM_PATTERNS.items():
        kw_map = data["keywords"]
        matched = {kw: wt for kw, wt in kw_map.items() if kw in text_lower}
        if matched:
            risk = compute_risk_score(matched, kw_map, data["severity"])
            scores[scam_type] = {
                "matched_keywords": list(matched.keys()),
                "keyword_weights":  matched,
                "risk_score":       risk,
                "explanation":      data["explanation"],
                "action":           data["action"],
                "severity":         data["severity"],
            }

    if not scores:
        return {
            "status": "SAFE",
            "message": "No known scam patterns detected.",
            "tip": (
                "Stay alert — scammers constantly evolve their language. "
                "When in doubt: never share OTPs, never pay unknown callers, "
                "and always verify through official channels."
            ),
        }

    ranked = sorted(scores.items(), key=lambda x: x[1]["risk_score"], reverse=True)
    pn, pd = ranked[0]

    return {
        "status":           "SCAM_DETECTED",
        "primary_scam":     pn,
        "severity":         pd["severity"],
        "risk_score":       pd["risk_score"],
        "matched_keywords": pd["matched_keywords"],
        "keyword_weights":  pd["keyword_weights"],
        "explanation":      pd["explanation"],
        "action":           pd["action"],
        "other_matches": [
            {"type": k, "risk_score": v["risk_score"], "severity": v["severity"]}
            for k, v in ranked[1:]
        ],
    }


# ═══════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.get_json()
    if not payload or not payload.get("message", "").strip():
        return jsonify({"error": "No message provided"}), 400
    msg = payload["message"].strip()
    if len(msg) < 5:
        return jsonify({"error": "Message too short to analyse"}), 400
    return jsonify(detect_scam(msg))


@app.route("/analytics", methods=["GET"])
def analytics():
    return jsonify({
        "scams_detected_today": 47,
        "money_protected":      "₹2,34,000",
        "users_warned":         312,
        "breakdown": [
            {"type": "Digital Arrest",  "pct": 64, "color": "#ff4560"},
            {"type": "KYC Fraud",       "pct": 18, "color": "#f5c400"},
            {"type": "IT Dept Scam",    "pct":  9, "color": "#ff9800"},
            {"type": "TRAI Scam",       "pct":  6, "color": "#0096ff"},
            {"type": "Prize Scam",      "pct":  3, "color": "#00d4aa"},
        ],
        "recent": [
            {"time": "2 min ago",  "type": "Digital Arrest", "city": "Bengaluru"},
            {"time": "8 min ago",  "type": "KYC Fraud",      "city": "Mumbai"},
            {"time": "15 min ago", "type": "TRAI Scam",      "city": "Delhi"},
            {"time": "23 min ago", "type": "IT Dept Scam",   "city": "Hyderabad"},
            {"time": "31 min ago", "type": "Prize Scam",     "city": "Chennai"},
        ],
    })


@app.route("/test-cases", methods=["GET"])
def test_cases():
    return jsonify([
        {
            "id": 1, "label": "Digital Arrest — CBI Officer", "tag": "CRITICAL",
            "message": (
                "This is Officer Rajiv Sharma from the Central Bureau of Investigation. "
                "Your Aadhaar number is linked to a money laundering case worth 4 crore rupees. "
                "You are under digital arrest effective immediately. A warrant has been issued. "
                "Stay on this video call and do not disconnect. Do not tell anyone about this call "
                "or you will be taken into physical custody within 2 hours."
            ),
        },
        {
            "id": 2, "label": "KYC Fraud — SBI Account Block", "tag": "HIGH",
            "message": (
                "Dear SBI Customer, your SBI KYC has expired as of today. "
                "Your account will be deactivated within 24 hours if KYC is not updated. "
                "Click to update your KYC: sbi-kyc-update.net/verify "
                "Enter your Aadhaar OTP to complete re-KYC. Ignore at your own risk."
            ),
        },
        {
            "id": 3, "label": "TRAI Scam — SIM Disconnection", "tag": "HIGH",
            "message": (
                "URGENT TRAI Notice: Illegal use of your number has been detected. "
                "Your SIM card will be disconnected within 2 hours by the Department of Telecom. "
                "Your mobile connection is suspended pending verification. "
                "Press 9 to speak with a DoT officer to avoid disconnection."
            ),
        },
        {
            "id": 4, "label": "Prize Scam — KBC Lucky Draw", "tag": "MEDIUM",
            "message": (
                "Congratulations! You have won Rs 25,00,000 in the KBC Lucky Draw 2025. "
                "You are our lucky winner selected from 2 crore participants. "
                "To claim your prize money, pay a processing fee of Rs 2500 "
                "to activate your KBC winner account. Contact our agent to proceed."
            ),
        },
        {
            "id": 5, "label": "IT Dept Scam — TDS Refund", "tag": "HIGH",
            "message": (
                "Income Tax Department Alert: Your TDS refund of Rs 18,450 has been approved. "
                "Your PAN card has been flagged for unreported income and financial irregularity. "
                "Click to claim refund: incometax-refund.net/claim "
                "Failure to comply may result in tax arrest and IT raid proceedings."
            ),
        },
    ])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
