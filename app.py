from flask import Flask, render_template, request
import re
from urlib.parse import urlparse

app = Flask(__name__)

# detection functions
def analyze_email(sender, subject, body):

    score = 0
    warnings = []
    email_text = f"{subject} {body}".lower()
    sender = sender.lower().strip()
# check for urgency, credential words, and threats
    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "action required",
        "final warning",
        "verify now",
        "respond immediately",
        "within 24 hours",
        "account will be closed"
    ]
    urgency_found = [
        word for word in urgency_words
        if word in email_text
    ]
    if urgency_found:
        score += 15
        warnings.append("Urgency or pressure tactics detected")

    credential_words = [
        "password",
        "login",
        "username",
        "social security",
        "credit card",
        "bank account",
        "security code",
        "verification code",
        "one-time password",
        "otp"
    ]
    credential_found = [
        word for word in credential_words
        if word in email_text
    ]
    if credential_found:
        score += 20
        warnings.append("Email requests or references sensitive information")

    threat_words = [
        "suspended",
        "locked",
        "terminated",
        "deactivated",
        "unauthorized activity",
        "fraud detected",
        "account compromised",
        "legal action"
    ]
    threat_found = [
        word for word in threat_words
        if word in email_text
    ]
    if threat_found:
        score += 15
        warnings.append("Threatening or account-related language detected")
# check for urls and analyze
# check sender address
# create score percentage

# connect to flask