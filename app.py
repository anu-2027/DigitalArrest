"""
DigitalArmour — Detection Engine v3
====================================
Multi-factor risk scoring algorithm with 4 named, explainable components.

ALGORITHM DESIGN
─────────────────
Score = KDS + UPS + IMS + ITS   (capped at 100)

  Factor                     Max pts  What it measures
  ─────────────────────────────────────────────────────
  KDS  Keyword Density Score    40    Weighted scam-specific phrase matching
  UPS  Urgency & Pressure Score 25    Time-pressure and fear language
  IMS  Impersonation Score      20    Authority body / official impersonation
  ITS  Isolation Tactic Score   15    Secrecy demands, victim isolation

Each factor is scored independently, then combined.
A severity floor prevents under-reporting on high-danger categories.

SCORING RATIONALE
─────────────────
Keyword weights (1-10) reflect exclusivity:
  10 = phrase almost never appears outside scam context ("digital arrest")
   7 = high-signal but occasionally legitimate ("money laundering" in news)
   4 = moderate-signal, needs supporting context ("narcotics")
   1 = low-signal alone ("tax")

UPS captures the psychological pressure mechanism all scams share:
immediate deadlines, consequences, fear of inaction.

IMS captures impersonation of the three most-abused authorities in India:
government agencies (CBI/ED/NCB), telecom (TRAI/DoT), banks.

ITS captures the isolation tactic — keeping victims from family/friends
so they cannot verify the scam before paying.
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ═══════════════════════════════════════════════════════════════════
#  FACTOR 1: KEYWORD DENSITY SCORE (KDS)  —  max 40 points
#  Weighted phrase matching per scam category.
#  Score = min(40, matched_weight_sum / top5_max_weight * 40)
# ═══════════════════════════════════════════════════════════════════

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
            "kyc expired":                      10,
            "update your kyc":                  10,
            "kyc pending":                       9,
            "your account will be deactivated":  9,
            "account will be suspended":         9,
            "your upi blocked":                  9,
            "sbi kyc":                           8,
            "hdfc kyc":                          8,
            "paytm kyc":                         8,
            "google pay kyc":                    8,
            "phonepe kyc":                       8,
            "re-kyc":                            8,
            "video kyc":                         7,
            "kyc update":                        7,
            "kyc verification":                  6,
            "bank account blocked":              6,
            "click link to update":              6,
            "pan card verification":             5,
            "aadhaar otp":                       5,
            "link expired":                      4,
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


# ═══════════════════════════════════════════════════════════════════
#  FACTOR 2: URGENCY & PRESSURE SCORE (UPS)  —  max 25 points
#  Scammers always create artificial time pressure.
#  Each phrase matched adds points; capped at 25.
# ═══════════════════════════════════════════════════════════════════

URGENCY_PHRASES = {
    # Extreme time pressure (8 pts each)
    "within 2 hours":         8,
    "within 24 hours":        8,
    "immediately":            7,
    "urgent":                 6,
    "last chance":            8,
    "expires today":          8,
    "final warning":          8,
    # Consequence language (6 pts)
    "or else":                6,
    "failure to comply":      8,
    "ignore at your own risk":8,
    "legal action":           6,
    "consequences":           5,
    "penalty":                5,
    # Action pressure (5 pts)
    "act now":                6,
    "do not delay":           6,
    "respond immediately":    6,
    "verify now":             5,
    "call back immediately":  6,
    "limited time":           5,
    "offer expires":          5,
    "click now":              5,
}


# ═══════════════════════════════════════════════════════════════════
#  FACTOR 3: IMPERSONATION SCORE (IMS)  —  max 20 points
#  Claiming to be a known authority body adds credibility for scammers.
# ═══════════════════════════════════════════════════════════════════

IMPERSONATION_PHRASES = {
    # Government / Law enforcement (high weight)
    "central bureau of investigation": 10,
    "cbi":                              8,
    "enforcement directorate":          9,
    "narcotics control bureau":         9,
    "ncb":                              7,
    "cyber crime police":               8,
    "cybercrime cell":                  8,
    "supreme court":                    8,
    "high court":                       7,
    # Telecom regulators
    "telecom regulatory authority":     9,
    "trai":                             7,
    "department of telecom":            8,
    "dot":                              5,
    # Financial / Tax
    "income tax department":            8,
    "income tax officer":               8,
    "enforcement directorate":          9,
    "reserve bank of india":            8,
    "rbi":                              7,
    "sebi":                             7,
    # Banks (impersonation)
    "sbi":                              5,
    "hdfc bank":                        5,
    "icici bank":                       5,
    "axis bank":                        5,
    "kotak bank":                       5,
}


# ═══════════════════════════════════════════════════════════════════
#  FACTOR 4: ISOLATION TACTIC SCORE (ITS)  —  max 15 points
#  Scammers isolate victims so they can't verify / get help.
# ═══════════════════════════════════════════════════════════════════

ISOLATION_PHRASES = {
    "do not tell anyone":    15,
    "don't tell anyone":     15,
    "do not inform anyone":  15,
    "keep this confidential":12,
    "do not share":           8,
    "stay on call":          10,
    "do not disconnect":     10,
    "remain on the line":    10,
    "do not contact":         8,
    "do not call police":    12,
    "this is confidential":  10,
    "secret":                 6,
    "between us":             6,
}


# ═══════════════════════════════════════════════════════════════════
#  FACTOR SCORING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def score_kds(matched_weights: dict, all_weights: dict) -> int:
    """
    Keyword Density Score (KDS) — max 40 points.
    Normalises matched weight sum against top-5 keyword maximum.
    """
    if not matched_weights:
        return 0
    top5_max = sum(sorted(all_weights.values(), reverse=True)[:5])
    raw = sum(matched_weights.values())
    return int(min(40, (raw / top5_max) * 40))


def score_ups(text_lower: str) -> tuple[int, list]:
    """
    Urgency & Pressure Score (UPS) — max 25 points.
    Returns (score, matched_phrases).
    """
    matched = {ph: wt for ph, wt in URGENCY_PHRASES.items() if ph in text_lower}
    score = int(min(25, sum(matched.values())))
    return score, list(matched.keys())


def score_ims(text_lower: str) -> tuple[int, list]:
    """
    Impersonation Score (IMS) — max 20 points.
    Returns (score, matched_phrases).
    """
    matched = {ph: wt for ph, wt in IMPERSONATION_PHRASES.items() if ph in text_lower}
    score = int(min(20, sum(matched.values())))
    return score, list(matched.keys())


def score_its(text_lower: str) -> tuple[int, list]:
    """
    Isolation Tactic Score (ITS) — max 15 points.
    Returns (score, matched_phrases).
    """
    matched = {ph: wt for ph, wt in ISOLATION_PHRASES.items() if ph in text_lower}
    score = int(min(15, sum(matched.values())))
    return score, list(matched.keys())


# ═══════════════════════════════════════════════════════════════════
#  SEVERITY FLOOR — ensures CRITICAL scams always reflect real danger
# ═══════════════════════════════════════════════════════════════════

SEVERITY_FLOOR = {"CRITICAL": 70, "HIGH": 50, "MEDIUM": 30}


# ═══════════════════════════════════════════════════════════════════
#  MAIN DETECTION FUNCTION
# ═══════════════════════════════════════════════════════════════════

def detect_scam(text: str) -> dict:
    """
    Run all 4 scoring factors against the input text.
    Returns the highest-scoring scam category with full factor breakdown.
    """
    text_lower = text.lower()

    # Compute cross-cutting factors once (same for all categories)
    ups_score, ups_matched = score_ups(text_lower)
    ims_score, ims_matched = score_ims(text_lower)
    its_score, its_matched = score_its(text_lower)

    scores = {}

    for scam_type, data in SCAM_PATTERNS.items():
        kw_map  = data["keywords"]
        matched = {kw: wt for kw, wt in kw_map.items() if kw in text_lower}

        if not matched:
            continue  # category not triggered at all

        kds = score_kds(matched, kw_map)

        # Combined raw score
        raw_total = kds + ups_score + ims_score + its_score
        final_score = max(
            min(100, raw_total),
            SEVERITY_FLOOR.get(data["severity"], 0)
        )

        scores[scam_type] = {
            "matched_keywords": list(matched.keys()),
            "keyword_weights":  matched,
            "risk_score":       final_score,
            "explanation":      data["explanation"],
            "action":           data["action"],
            "severity":         data["severity"],
            # Factor breakdown (sent to frontend for visualization)
            "factors": {
                "kds": {"score": kds,       "max": 40, "label": "Keyword Density",     "matched": list(matched.keys())},
                "ups": {"score": ups_score, "max": 25, "label": "Urgency & Pressure",  "matched": ups_matched},
                "ims": {"score": ims_score, "max": 20, "label": "Impersonation",       "matched": ims_matched},
                "its": {"score": its_score, "max": 15, "label": "Isolation Tactics",   "matched": its_matched},
            },
        }

    if not scores:
        return {
            "status":  "SAFE",
            "message": "No known scam patterns detected.",
            "tip": (
                "Stay alert — scammers constantly evolve their language. "
                "When in doubt: never share OTPs, never pay unknown callers, "
                "and always verify through official channels."
            ),
            "factors": {
                "kds": {"score": 0, "max": 40, "label": "Keyword Density",    "matched": []},
                "ups": {"score": 0, "max": 25, "label": "Urgency & Pressure", "matched": []},
                "ims": {"score": 0, "max": 20, "label": "Impersonation",      "matched": []},
                "its": {"score": 0, "max": 15, "label": "Isolation Tactics",  "matched": []},
            },
        }

    ranked = sorted(scores.items(), key=lambda x: x[1]["risk_score"], reverse=True)
    pname, pdata = ranked[0]

    return {
        "status":           "SCAM_DETECTED",
        "primary_scam":     pname,
        "severity":         pdata["severity"],
        "risk_score":       pdata["risk_score"],
        "matched_keywords": pdata["matched_keywords"],
        "keyword_weights":  pdata["keyword_weights"],
        "explanation":      pdata["explanation"],
        "action":           pdata["action"],
        "factors":          pdata["factors"],
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
            {"type": "Digital Arrest", "pct": 64, "color": "#ff4560"},
            {"type": "KYC Fraud",      "pct": 18, "color": "#f5c400"},
            {"type": "IT Dept Scam",   "pct":  9, "color": "#ff9800"},
            {"type": "TRAI Scam",      "pct":  6, "color": "#0096ff"},
            {"type": "Prize Scam",     "pct":  3, "color": "#00d4aa"},
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
                "This is Officer Rajiv Sharma from the Central Bureau of Investigation (CBI). "
                "Your Aadhaar number is linked to a money laundering case. "
                "You are under digital arrest effective immediately. A warrant has been issued. "
                "Stay on this video call and do not disconnect. Do not tell anyone about this call "
                "or you will be taken into physical custody within 2 hours. Failure to comply "
                "will result in legal action."
            ),
        },
        {
            "id": 2, "label": "KYC Fraud — SBI Account Block", "tag": "HIGH",
            "message": (
                "Dear SBI customer, your SBI KYC has expired as of today. "
                "Your account will be deactivated within 24 hours if KYC is not updated. "
                "Click to update your KYC immediately: sbi-kyc-update.net/verify "
                "Enter your Aadhaar OTP to complete re-KYC. Ignore at your own risk."
            ),
        },
        {
            "id": 3, "label": "TRAI Scam — SIM Disconnection", "tag": "HIGH",
            "message": (
                "URGENT: TRAI notice — illegal use of your number has been detected. "
                "Your SIM card will be disconnected within 2 hours by the Department of Telecom. "
                "Your mobile connection is suspended pending verification. "
                "Press 9 to speak with a DoT officer immediately to avoid disconnection."
            ),
        },
        {
            "id": 4, "label": "Prize Scam — KBC Lucky Draw", "tag": "MEDIUM",
            "message": (
                "Congratulations! You have won Rs 25,00,000 in the KBC Lucky Draw 2025. "
                "You are our lucky winner selected from 2 crore participants. "
                "To claim your prize money, pay a processing fee of Rs 2500 to activate your "
                "KBC winner account. Offer expires today. Act now and call back immediately."
            ),
        },
        {
            "id": 5, "label": "IT Dept Scam — TDS Refund", "tag": "HIGH",
            "message": (
                "Income Tax Department alert: your TDS refund of Rs 18,450 has been approved. "
                "Your PAN card has been flagged for unreported income and financial irregularity. "
                "Click to claim refund: incometax-refund.net/claim — respond immediately. "
                "Failure to comply may result in tax arrest and IT raid proceedings within 24 hours."
            ),
        },
    ])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
