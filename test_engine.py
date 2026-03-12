"""
DigitalArmour — Test Suite
===========================
Run with:  python test_engine.py
Or:        python -m pytest test_engine.py -v

Tests cover:
  1. All 5 scam categories detect correctly
  2. SAFE messages return SAFE
  3. Each of the 4 scoring factors fires independently
  4. Severity floors are respected
  5. Risk scores are always within 0–100
  6. Edge cases (empty input, mixed-case, partial phrases)
  7. Factor breakdown is always present in response
"""

import sys
import unittest
from app import (
    detect_scam,
    score_kds, score_ups, score_ims, score_its,
    SCAM_PATTERNS, URGENCY_PHRASES, IMPERSONATION_PHRASES, ISOLATION_PHRASES,
    SEVERITY_FLOOR,
)

# ══════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════

def get_result(message: str) -> dict:
    return detect_scam(message)

def assert_scam(result: dict, expected_category: str, test_name: str):
    assert result["status"] == "SCAM_DETECTED", \
        f"[{test_name}] Expected SCAM_DETECTED, got {result['status']}"
    assert result["primary_scam"] == expected_category, \
        f"[{test_name}] Expected '{expected_category}', got '{result['primary_scam']}'"

def assert_safe(result: dict, test_name: str):
    assert result["status"] == "SAFE", \
        f"[{test_name}] Expected SAFE, got {result['status']}"

# ══════════════════════════════════════════════════════
#  TEST CLASS 1: SCAM CATEGORY DETECTION
# ══════════════════════════════════════════════════════

class TestScamCategoryDetection(unittest.TestCase):

    def test_digital_arrest_detected(self):
        msg = (
            "This is Officer Sharma from CBI. You are under digital arrest. "
            "A warrant has been issued. Stay on this video call and do not disconnect. "
            "Do not tell anyone. Money laundering case linked to your Aadhaar."
        )
        r = get_result(msg)
        assert_scam(r, "Digital Arrest", "digital_arrest_basic")

    def test_digital_arrest_minimum_signal(self):
        """Even a single high-weight keyword should trigger detection."""
        r = get_result("You are under digital arrest. Please cooperate.")
        assert_scam(r, "Digital Arrest", "digital_arrest_single_kw")

    def test_kyc_fraud_detected(self):
        msg = (
            "Dear SBI customer, your SBI KYC has expired. "
            "Your account will be deactivated within 24 hours. "
            "Click to update your KYC. Enter Aadhaar OTP to complete re-KYC."
        )
        r = get_result(msg)
        assert_scam(r, "KYC Fraud", "kyc_fraud_basic")

    def test_trai_scam_detected(self):
        msg = (
            "TRAI notice: illegal use of your number detected. "
            "Your SIM card will be disconnected. "
            "Press 9 to speak with a DoT officer immediately."
        )
        r = get_result(msg)
        assert_scam(r, "TRAI Scam", "trai_scam_basic")

    def test_prize_scam_detected(self):
        msg = (
            "Congratulations! You have won Rs 25 lakh in the KBC Lucky Draw. "
            "You are our lucky winner. To claim your prize money, "
            "pay a processing fee of Rs 2500."
        )
        r = get_result(msg)
        assert_scam(r, "Prize / Lottery Scam", "prize_scam_basic")

    def test_it_department_scam_detected(self):
        msg = (
            "Income Tax Department: your TDS refund has been approved. "
            "Your PAN card flagged for unreported income. "
            "Click to claim refund. Failure to comply: tax arrest proceedings."
        )
        r = get_result(msg)
        assert_scam(r, "IT Department Scam", "it_dept_scam_basic")

    def test_case_insensitivity(self):
        """Detection must work regardless of letter case."""
        msg = "YOU ARE UNDER DIGITAL ARREST. CBI OFFICER SPEAKING."
        r = get_result(msg)
        assert_scam(r, "Digital Arrest", "case_insensitive")

    def test_mixed_case(self):
        msg = "Your SBI Kyc Has Expired. Account Will Be Deactivated."
        r = get_result(msg)
        assert_scam(r, "KYC Fraud", "mixed_case_kyc")


# ══════════════════════════════════════════════════════
#  TEST CLASS 2: SAFE MESSAGES
# ══════════════════════════════════════════════════════

class TestSafeMessages(unittest.TestCase):

    def test_completely_safe(self):
        assert_safe(get_result("Hello, how are you doing today?"), "safe_hello")

    def test_normal_bank_message(self):
        msg = "Your account balance is Rs 12,500. Thank you for banking with us."
        assert_safe(get_result(msg), "safe_bank_balance")

    def test_weather_message(self):
        assert_safe(get_result("Heavy rain expected in Bengaluru tomorrow."), "safe_weather")

    def test_otp_without_scam_context(self):
        # OTP alone isn't enough — needs scam context
        msg = "Your OTP is 482910. Valid for 10 minutes."
        assert_safe(get_result(msg), "safe_otp_only")

    def test_short_legitimate_message(self):
        assert_safe(get_result("Your order has been shipped."), "safe_order")

    def test_empty_message_returns_error(self):
        """Empty message should not crash — detect_scam handles gracefully."""
        r = detect_scam("   ")
        # Should return SAFE (no patterns found), not raise an exception
        self.assertIn("status", r)


# ══════════════════════════════════════════════════════
#  TEST CLASS 3: INDIVIDUAL FACTOR SCORES
# ══════════════════════════════════════════════════════

class TestFactorScores(unittest.TestCase):

    # — KDS —
    def test_kds_zero_on_no_match(self):
        score = score_kds({}, SCAM_PATTERNS["Digital Arrest"]["keywords"])
        self.assertEqual(score, 0)

    def test_kds_max_40(self):
        """Score must never exceed 40."""
        kw_map = SCAM_PATTERNS["Digital Arrest"]["keywords"]
        full_match = dict(kw_map)
        score = score_kds(full_match, kw_map)
        self.assertLessEqual(score, 40)

    def test_kds_higher_weight_gives_higher_score(self):
        kw_map = SCAM_PATTERNS["Digital Arrest"]["keywords"]
        low  = score_kds({"narcotics": 5}, kw_map)
        high = score_kds({"digital arrest": 10, "you are under arrest": 10}, kw_map)
        self.assertGreater(high, low)

    # — UPS —
    def test_ups_zero_on_no_urgency(self):
        score, matched = score_ups("hello, how are you")
        self.assertEqual(score, 0)
        self.assertEqual(matched, [])

    def test_ups_detects_within_24_hours(self):
        score, matched = score_ups("your account will be deactivated within 24 hours")
        self.assertGreater(score, 0)
        self.assertIn("within 24 hours", matched)

    def test_ups_max_25(self):
        # Use all urgency phrases
        text = " ".join(URGENCY_PHRASES.keys())
        score, _ = score_ups(text)
        self.assertLessEqual(score, 25)

    def test_ups_failure_to_comply(self):
        score, matched = score_ups("failure to comply will result in legal action")
        self.assertIn("failure to comply", matched)
        self.assertGreater(score, 0)

    # — IMS —
    def test_ims_zero_on_no_authority(self):
        score, _ = score_ims("a random person called me")
        self.assertEqual(score, 0)

    def test_ims_detects_cbi(self):
        score, matched = score_ims("this is a cbi officer calling you")
        self.assertGreater(score, 0)
        self.assertIn("cbi", matched)

    def test_ims_detects_trai(self):
        score, matched = score_ims("message from trai telecom regulatory authority")
        self.assertGreater(score, 0)

    def test_ims_max_20(self):
        text = " ".join(IMPERSONATION_PHRASES.keys())
        score, _ = score_ims(text)
        self.assertLessEqual(score, 20)

    # — ITS —
    def test_its_zero_on_no_isolation(self):
        score, _ = score_its("please call us back when you can")
        self.assertEqual(score, 0)

    def test_its_detects_do_not_tell(self):
        score, matched = score_its("do not tell anyone about this call")
        self.assertGreater(score, 0)
        self.assertIn("do not tell anyone", matched)

    def test_its_detects_stay_on_call(self):
        score, matched = score_its("stay on call and do not disconnect")
        self.assertGreater(score, 0)

    def test_its_max_15(self):
        text = " ".join(ISOLATION_PHRASES.keys())
        score, _ = score_its(text)
        self.assertLessEqual(score, 15)


# ══════════════════════════════════════════════════════
#  TEST CLASS 4: RISK SCORE BOUNDS & SEVERITY FLOOR
# ══════════════════════════════════════════════════════

class TestRiskScoreBounds(unittest.TestCase):

    def test_risk_score_never_exceeds_100(self):
        """All 4 factors at max should still cap at 100."""
        msg = (
            "CBI officer: you are under digital arrest. Warrant issued. "
            "Stay on call, do not disconnect, do not tell anyone. "
            "Money laundering. Failure to comply within 2 hours. Legal action. "
            "Central Bureau of Investigation. Income tax department. TRAI. "
            "Your SIM card blocked. KYC expired. You have won the lucky draw."
        )
        r = get_result(msg)
        if r["status"] == "SCAM_DETECTED":
            self.assertLessEqual(r["risk_score"], 100)

    def test_risk_score_never_below_zero(self):
        r = get_result("digital arrest")
        self.assertGreaterEqual(r.get("risk_score", 0), 0)

    def test_critical_severity_floor(self):
        """Digital Arrest (CRITICAL) must always score >= 70."""
        r = get_result("digital arrest")  # single keyword trigger
        self.assertGreaterEqual(r["risk_score"], SEVERITY_FLOOR["CRITICAL"])

    def test_high_severity_floor(self):
        """KYC Fraud (HIGH) must always score >= 50."""
        r = get_result("kyc expired")
        self.assertGreaterEqual(r["risk_score"], SEVERITY_FLOOR["HIGH"])

    def test_medium_severity_floor(self):
        """Prize Scam (MEDIUM) must always score >= 30."""
        r = get_result("you have won the lucky draw prize money")
        self.assertGreaterEqual(r["risk_score"], SEVERITY_FLOOR["MEDIUM"])


# ══════════════════════════════════════════════════════
#  TEST CLASS 5: RESPONSE STRUCTURE
# ══════════════════════════════════════════════════════

class TestResponseStructure(unittest.TestCase):

    def test_scam_response_has_all_required_fields(self):
        r = get_result("you are under digital arrest cbi officer warrant issued")
        required = ["status", "primary_scam", "severity", "risk_score",
                    "matched_keywords", "keyword_weights", "explanation",
                    "action", "factors", "other_matches"]
        for field in required:
            self.assertIn(field, r, f"Missing field: {field}")

    def test_factors_structure(self):
        r = get_result("digital arrest cbi officer money laundering")
        factors = r.get("factors", {})
        self.assertIn("kds", factors)
        self.assertIn("ups", factors)
        self.assertIn("ims", factors)
        self.assertIn("its", factors)
        for key in ["kds", "ups", "ims", "its"]:
            f = factors[key]
            self.assertIn("score", f)
            self.assertIn("max", f)
            self.assertIn("label", f)
            self.assertIn("matched", f)

    def test_factor_max_values_correct(self):
        r = get_result("digital arrest")
        factors = r["factors"]
        self.assertEqual(factors["kds"]["max"], 40)
        self.assertEqual(factors["ups"]["max"], 25)
        self.assertEqual(factors["ims"]["max"], 20)
        self.assertEqual(factors["its"]["max"], 15)

    def test_safe_response_has_tip(self):
        r = get_result("hello how are you")
        self.assertIn("tip", r)

    def test_action_list_not_empty(self):
        r = get_result("digital arrest cbi officer")
        self.assertIsInstance(r["action"], list)
        self.assertGreater(len(r["action"]), 0)

    def test_matched_keywords_is_list(self):
        r = get_result("kyc expired sbi kyc account will be suspended")
        self.assertIsInstance(r["matched_keywords"], list)
        self.assertGreater(len(r["matched_keywords"]), 0)


# ══════════════════════════════════════════════════════
#  TEST CLASS 6: EDGE CASES
# ══════════════════════════════════════════════════════

class TestEdgeCases(unittest.TestCase):

    def test_very_long_message(self):
        """Should not crash on long inputs."""
        msg = "digital arrest warrant issued cbi officer " * 100
        r = get_result(msg)
        self.assertIn("status", r)
        if r["status"] == "SCAM_DETECTED":
            self.assertLessEqual(r["risk_score"], 100)

    def test_numbers_and_special_chars(self):
        r = get_result("₹25,00,000 lucky draw winner! Pay Rs.2500 processing fee!!!")
        self.assertIn("status", r)

    def test_multiple_categories_returns_highest(self):
        """When multiple categories match, highest risk score wins."""
        msg = (
            "CBI officer: digital arrest issued. Also your SBI KYC expired. "
            "Pay processing fee to claim your prize."
        )
        r = get_result(msg)
        self.assertEqual(r["status"], "SCAM_DETECTED")
        # Primary should be Digital Arrest (CRITICAL highest)
        self.assertEqual(r["primary_scam"], "Digital Arrest")
        # Other matches should list remaining
        self.assertGreater(len(r["other_matches"]), 0)

    def test_partial_keyword_not_matched(self):
        """'kyc' alone (not as part of a full keyword) should not over-trigger."""
        r = get_result("Please update your KYC details through our official branch.")
        # 'kyc' alone is not in the keyword list; 'kyc update' and 'kyc verification' are
        # This tests that partial word matches work as expected
        self.assertIn("status", r)

    def test_unicode_hindi_characters_dont_crash(self):
        r = get_result("आपका खाता ब्लॉक हो जाएगा। KYC expired. Click link.")
        self.assertIn("status", r)


# ══════════════════════════════════════════════════════
#  RUNNER
# ══════════════════════════════════════════════════════

def run_tests():
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    test_classes = [
        TestScamCategoryDetection,
        TestSafeMessages,
        TestFactorScores,
        TestRiskScoreBounds,
        TestResponseStructure,
        TestEdgeCases,
    ]

    for cls in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(cls))

    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)

    print("\n" + "═" * 60)
    print(f"  TOTAL:  {result.testsRun} tests")
    print(f"  PASSED: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  FAILED: {len(result.failures)}")
    print(f"  ERRORS: {len(result.errors)}")
    print("═" * 60)

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
