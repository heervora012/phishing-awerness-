#!/usr/bin/env python3
"""
Phishing Awareness Training Module
Interactive educational tool to teach users about phishing attacks, 
social engineering tactics, and best practices to stay safe.
"""

import random
import json
from typing import List, Dict, Tuple
from datetime import datetime


class PhishingTraining:
    """Main class for the phishing awareness training program."""

    def __init__(self):
        self.user_score = 0
        self.total_questions = 0
        self.quiz_results = []
        self.user_name = ""
        self.modules_completed = []
        self.training_start_time = datetime.now()
        
    def display_banner(self):
        """Display the training program banner."""
        banner = """
        ╔════════════════════════════════════════════════════════════════╗
        ║        PHISHING AWARENESS TRAINING PROGRAM                     ║
        ║     Learn to Recognize and Avoid Phishing Attacks              ║
        ╚════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        print("Welcome to the Cybersecurity Training Platform!")
        print("=" * 70)
    
    def display_menu(self):
        """Display main menu options."""
        menu = """
        MAIN MENU
        ─────────────────────────────────────────────────────────────────
        📚 LEARNING MODULES
        1. Learn: What is Phishing?
        2. Recognize: Identify Phishing Emails
        3. Explore: Fake Website Indicators
        4. Understand: Social Engineering Tactics

        🧪 INTERACTIVE TRAINING
        5. Quiz: Test Your Knowledge
        6. Email Simulator: Analyze Real Emails
        7. Interactive Scenarios: Real-World Situations
        8. Vulnerability Assessment: Self-Test

        📖 REFERENCE & RESOURCES
        9. Best Practices Guide
        10. Case Studies: Real-World Examples
        11. Resources & Learning Materials
        12. View Progress

        13. Exit

        Enter your choice (1-13): """
        return menu
    
    def learn_phishing_basics(self):
        """Module 1: Basic phishing education."""
        content = """
        WHAT IS PHISHING?
        ═════════════════════════════════════════════════════════════════
        
        Phishing is a cyber attack method where criminals attempt to steal
        sensitive information by impersonating trustworthy entities.
        
        KEY FACTS:
        ─────────────────────────────────────────────────────────────────
        • Origin: The term "phishing" emerged in the 1990s
        • Method: Typically uses deceptive emails, websites, or messages
        • Goal: Steal passwords, credit card numbers, personal data
        • Statistics: Phishing accounts for 90% of data breaches
        
        TYPES OF PHISHING:
        ─────────────────────────────────────────────────────────────────
        1. EMAIL PHISHING
           - Mass emails sent to many recipients
           - Example: "Confirm your PayPal account immediately"
        
        2. SPEARPHISHING
           - Targeted attacks using personal information
           - More sophisticated and harder to detect
        
        3. WHALING
           - Targets high-value individuals (CEOs, executives)
           - Uses company-specific information
        
        4. CLONE PHISHING
           - Legitimate emails are duplicated with malicious links
           - Attacker may claim email was resent
        
        5. SMISHING & VISHING
           - SMS (text message) phishing
           - Voice call phishing
        
        THE PHISHING ATTACK FLOW:
        ─────────────────────────────────────────────────────────────────
        1. Research     → Attacker researches target organization
        2. Craft        → Deceptive email/message is created
        3. Send         → Malicious content distributed
        4. Capture      → User clicks link or enters credentials
        5. Exploit      → Attacker gains unauthorized access
        6. Damage       → Data theft, financial loss, system compromise
        
        WHY PHISHING IS EFFECTIVE:
        ─────────────────────────────────────────────────────────────────
        • Exploits human trust and psychology
        • Appears to come from legitimate sources
        • Creates sense of urgency
        • Easy and cost-effective for attackers
        • High success rate (3-5% is profitable for criminals)
        
        Press Enter to continue...
        """
        print(content)
        input()
    
    def recognize_phishing_emails(self):
        """Module 2: Identify phishing emails."""
        content = """
        RECOGNIZE PHISHING EMAILS
        ═════════════════════════════════════════════════════════════════
        
        RED FLAGS IN PHISHING EMAILS:
        ─────────────────────────────────────────────────────────────────
        
        ⚠️  SUSPICIOUS SENDER
            • Generic greetings ("Dear Customer" vs "Dear John")
            • Slight variations in email address (amaz0n.com instead of amazon.com)
            • Mismatched display name and email address
        
        ⚠️  URGENT LANGUAGE
            • "Act now!" "Verify immediately!" "Account suspended!"
            • Creates panic to bypass rational thinking
            • Artificial time pressure
        
        ⚠️  SUSPICIOUS LINKS
            • Hover over links to see actual URL (don't click!)
            • URL doesn't match the organization name
            • Shortened URLs (bit.ly, tinyurl) hiding destination
            • HTTPS doesn't guarantee legitimacy
        
        ⚠️  REQUESTS FOR PERSONAL INFO
            • Legitimate companies never ask for:
              - Passwords
              - Social Security Numbers
              - Credit card information
              - Login credentials
            • Banks will never ask to "confirm" accounts via email
        
        ⚠️  POOR GRAMMAR & SPELLING
            • Professional companies proofread communications
            • Multiple spelling/grammar errors = red flag
            • Awkward phrasing or unusual language patterns
        
        ⚠️  SUSPICIOUS ATTACHMENTS
            • Unexpected file attachments
            • Files with double extensions (.doc.exe)
            • Macro-enabled documents (.docm, .xlsm)
        
        ⚠️  MISMATCHED INFORMATION
            • Logo quality issues or old logos
            • Inconsistent branding
            • Wrong company colors or fonts
        
        EMAIL ANALYSIS CHECKLIST:
        ─────────────────────────────────────────────────────────────────
        Before clicking any link or providing information:
        
        □ Do I recognize the sender?
        □ Does the email address match the organization?
        □ Is the greeting personalized?
        □ Is there urgent/threatening language?
        □ Is there a request for personal information?
        □ Does the email have spelling/grammar errors?
        □ Do the links match where they claim to go?
        □ Are there unexpected attachments?
        □ Does the offer seem too good to be true?
        
        If you answered NO or SUSPICIOUS to any question, it's likely phishing!
        
        Press Enter to continue...
        """
        print(content)
        input()
    
    def fake_website_indicators(self):
        """Module 3: Identify fake websites."""
        content = """
        FAKE WEBSITE INDICATORS
        ═════════════════════════════════════════════════════════════════
        
        WARNING SIGNS OF FAKE WEBSITES:
        ─────────────────────────────────────────────────────────────────
        
        🔗 SUSPICIOUS URL
            ✗ www.ammzon.com (missing 'a')
            ✗ www.paypa1.com (number instead of letter)
            ✗ www.secure-amazon.login.com (subdomain tricks)
            ✓ Legitimate sites use exact domain names
        
        🔒 LACK OF HTTPS
            ✗ Site URL starts with HTTP (not HTTPS)
            ✓ Legitimate sites use HTTPS encryption
            ⚠️  Note: HTTPS alone doesn't guarantee legitimacy
        
        🏢 POOR WEBSITE DESIGN
            • Misaligned elements or broken layout
            • Low-quality images or pixelated logos
            • Inconsistent colors or fonts
            • Outdated or broken styling
            • Poorly organized content
        
        📋 MISSING INFORMATION
            • No "About Us" or company information
            • Missing contact information
            • No physical address or business details
            • Lack of legitimate business certifications
        
        🛒 ODD CHECKOUT PROCESS
            • Unusual payment methods only
            • No standard credit card option
            • Asking for excessive personal information
            • No order confirmation or receipt
        
        ⚡ SUSPICIOUS FORMS
            • Asking for password to "verify account"
            • Requesting social security number
            • Forms that don't use secure submission
            • Auto-filling sensitive fields
        
        📱 MOBILE EXPERIENCE
            • Website not optimized for mobile
            • Links don't work on mobile devices
            • Different content than desktop version
        
        🎫 EXCESSIVE POPUPS
            • Intrusive ads or popups
            • Popups asking to enable plugins
            • Download prompts without clicking
        
        WEBSITE VERIFICATION CHECKLIST:
        ─────────────────────────────────────────────────────────────────
        Before entering any information:
        
        □ Does URL exactly match the official domain?
        □ Is the site using HTTPS?
        □ Does the design match official website?
        □ Can you find company contact information?
        □ Does the site have proper branding?
        □ Can you find privacy policy and terms?
        □ Are there customer reviews from trusted sources?
        □ Does the company have social media presence?
        
        BEST PRACTICE:
        Type the official website directly in the browser rather than
        clicking links from emails or search results!
        
        Press Enter to continue...
        """
        print(content)
        input()
    
    def social_engineering_tactics(self):
        """Module 4: Social engineering tactics."""
        content = """
        SOCIAL ENGINEERING TACTICS
        ═════════════════════════════════════════════════════════════════
        
        Social engineering exploits human psychology rather than technology.
        Understanding these tactics helps you recognize manipulation.
        
        COMMON TACTICS:
        ─────────────────────────────────────────────────────────────────
        
        1. AUTHORITY
           • Attacker impersonates boss, IT support, or authority figure
           • Claims urgent action required
           • Example: "This is CEO - transfer $50k immediately"
           • Prevention: Verify through known contact methods
        
        2. URGENCY & SCARCITY
           • Creates pressure to act without thinking
           • "Limited time offer!" "Account expires today!"
           • "Only 3 items left!"
           • Prevention: Take time to verify before responding
        
        3. FEAR & INTIMIDATION
           • Threats of account closure or legal action
           • "Your account has been compromised!"
           • "Suspicious activity detected - confirm identity NOW"
           • Prevention: Contact organization directly (don't use provided number)
        
        4. TRUST & LIKEABILITY
           • Attacker builds rapport before attacking
           • Uses flattery or common interests
           • Appears helpful and friendly
           • Prevention: Maintain professional distance
        
        5. RECIPROCITY
           • Giving free offers or discounts first
           • "We value you as a customer - click here for reward"
           • Creates obligation to reciprocate
           • Prevention: Be skeptical of unsolicited offers
        
        6. CURIOSITY & BAITING
           • "Click to see what you've been missing"
           • "Download this report everyone is talking about"
           • Appeals to human curiosity
           • Prevention: Verify source before clicking unknown links
        
        7. CONSENSUS & SOCIAL PROOF
           • "Thousands of people have already verified their account"
           • "Join the millions using this service"
           • Uses peer pressure psychology
           • Prevention: Don't be influenced by false popularity
        
        PRETEXTING TECHNIQUES:
        ─────────────────────────────────────────────────────────────────
        Attacker creates fake scenario to build credibility:
        
        • Call pretending to be IT support needing password
        • Email posing as vendor requesting invoice payment
        • Text claiming to be bank requiring verification
        • Social media contact from "friend" needing help
        
        DEFENSE AGAINST SOCIAL ENGINEERING:
        ─────────────────────────────────────────────────────────────────
        
        • Think before you act (never rush)
        • Verify identities through official channels
        • Don't share sensitive info over email/phone
        • Be skeptical of emotional appeals
        • Check with colleagues before sensitive actions
        • Trust your instincts (if it feels wrong, it probably is)
        
        Press Enter to continue...
        """
        print(content)
        input()
    
    def run_quiz(self):
        """Interactive quiz to test knowledge."""
        questions = [
            {
                "question": "Which is a red flag for phishing emails?",
                "options": [
                    "Generic greeting like 'Dear Customer'",
                    "Asking to verify your password",
                    "Suspicious sender email address",
                    "All of the above"
                ],
                "correct": 3,
                "explanation": "All of these are red flags. Phishing emails often use generic greetings, ask for passwords, and come from suspicious email addresses."
            },
            {
                "question": "What should you do if you receive an urgent email from your bank?",
                "options": [
                    "Click the link in the email immediately",
                    "Close the email and call your bank using the number on your card",
                    "Reply to the email asking for verification",
                    "Forward it to your IT department"
                ],
                "correct": 1,
                "explanation": "Always call the official number on your card. Never use contact info from suspicious emails."
            },
            {
                "question": "Which URL is most likely phishing?",
                "options": [
                    "https://www.amazon.com/account",
                    "https://www.amaz0n.com/login",
                    "https://amazon.com/secure",
                    "https://www.amazon.com/signin"
                ],
                "correct": 1,
                "explanation": "The '0' replacing 'o' is a common phishing tactic. Scammers use look-alike domains."
            },
            {
                "question": "What is 'spearphishing'?",
                "options": [
                    "Random phishing emails sent to many people",
                    "Targeted phishing using personal information about the victim",
                    "Phishing through text messages",
                    "Phishing targeting senior executives"
                ],
                "correct": 1,
                "explanation": "Spearphishing is highly targeted and uses personal information to appear legitimate."
            },
            {
                "question": "How can you safely check a suspicious link before clicking?",
                "options": [
                    "Click it and use the back button if it looks wrong",
                    "Ask the sender if it's safe",
                    "Hover over the link to see the actual URL destination",
                    "Use a VPN before clicking"
                ],
                "correct": 2,
                "explanation": "Hover over links (don't click!) to see the actual URL destination. Never click first and check later."
            },
            {
                "question": "Which is legitimate company practice?",
                "options": [
                    "Asking you to confirm password via email",
                    "Requesting SSN via email link",
                    "Sending invoice for services used (via verified email)",
                    "Sending urgent account warning without personalization"
                ],
                "correct": 2,
                "explanation": "Legitimate companies send invoices but never ask for passwords, SSN, or sensitive info via unsecured email."
            },
            {
                "question": "What's the best defense against social engineering?",
                "options": [
                    "Memorizing all social engineering tactics",
                    "Thinking critically and verifying before acting",
                    "Using the same password everywhere",
                    "Only communicating via email"
                ],
                "correct": 1,
                "explanation": "Critical thinking and verification are your best defenses. Never rush when something seems urgent."
            },
            {
                "question": "Which statement about HTTPS is correct?",
                "options": [
                    "HTTPS websites are always safe",
                    "HTTPS only encrypts data in transit; it doesn't verify legitimacy",
                    "You should avoid HTTPS websites",
                    "HTTPS prevents phishing"
                ],
                "correct": 1,
                "explanation": "HTTPS encrypts your connection but doesn't guarantee the site is legitimate. Fake sites can have HTTPS too."
            },
            {
                "question": "What should you do if you clicked a phishing link?",
                "options": [
                    "Nothing, just don't enter information",
                    "Immediately change your password from a secure device",
                    "Contact your IT department and monitor accounts",
                    "Change your password from the infected device"
                ],
                "correct": 2,
                "explanation": "Change passwords from a secure device, contact IT, and monitor your accounts for suspicious activity."
            },
            {
                "question": "Which is an example of 'whaling'?",
                "options": [
                    "Fishing for phishing victims randomly",
                    "Targeting whale organizations only",
                    "Phishing emails targeting high-level executives using company information",
                    "Phishing through text messages"
                ],
                "correct": 2,
                "explanation": "Whaling targets C-level executives and uses company-specific information to appear legitimate."
            }
        ]
        
        print("\n" + "="*70)
        print("PHISHING AWARENESS QUIZ")
        print("="*70)
        print(f"Test your knowledge! You'll get {len(questions)} questions.\n")
        
        correct = 0
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}/{len(questions)}")
            print(f"{q['question']}\n")
            
            for j, option in enumerate(q['options'], 1):
                print(f"  {j}. {option}")
            
            while True:
                try:
                    answer = int(input("\nYour answer (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("Please enter 1-4")
                except ValueError:
                    print("Please enter a valid number")
            
            if answer - 1 == q['correct']:
                print("✓ CORRECT!")
                correct += 1
            else:
                print(f"✗ INCORRECT. The correct answer is {q['correct'] + 1}")
            
            print(f"Explanation: {q['explanation']}")
        
        score_percentage = (correct / len(questions)) * 100
        self.user_score = correct
        self.total_questions = len(questions)
        
        print("\n" + "="*70)
        print("QUIZ RESULTS")
        print("="*70)
        print(f"You got {correct} out of {len(questions)} questions correct!")
        print(f"Score: {score_percentage:.1f}%\n")
        
        if score_percentage >= 90:
            print("🏆 EXCELLENT! You're a phishing expert!")
        elif score_percentage >= 70:
            print("✓ GOOD! You know how to spot phishing.")
        elif score_percentage >= 50:
            print("△ FAIR. Review the materials for areas you missed.")
        else:
            print("✗ NEEDS IMPROVEMENT. Study the materials more carefully.")
        
        input("\nPress Enter to continue...")
    
    def case_studies(self):
        """Real-world case studies."""
        cases = [
            {
                "title": "Target Data Breach (2013)",
                "description": """
                WHAT HAPPENED:
                Hackers stole 40 million credit card numbers from Target.
                
                HOW:
                • Phishing email sent to Target supplier
                • Supplier clicked malicious link and compromised
                • Attacker accessed Target's network through supplier account
                • Installed malware to capture credit card data
                
                LESSON:
                Third-party vulnerabilities can compromise large organizations.
                Never trust links even from known vendors without verification.
                """,
                "impact": "$18.5 million settlement"
            },
            {
                "title": "Google & Facebook Whaling (2013-2015)",
                "description": """
                WHAT HAPPENED:
                A man convinced Google and Facebook to transfer $122 million!
                
                HOW:
                • Attacker impersonated equipment suppliers
                • Created fake invoices and communication
                • Used social engineering to build trust
                • Targeted specific individuals in accounting
                
                LESSON:
                Even tech giants fell for sophisticated social engineering.
                Always verify large transactions through multiple channels.
                """,
                "impact": "$122 million transferred"
            },
            {
                "title": "CEO Fraud at Snapchat (2015)",
                "description": """
                WHAT HAPPENED:
                An attacker impersonated Snapchat's CEO and requested employee data.
                
                HOW:
                • Email spoofed CEO's email address
                • Requested payroll information urgently
                • Created sense of authority and urgency
                • Targeted HR employees
                
                LESSON:
                Always verify urgent requests from leadership through
                alternative communication channels.
                """,
                "impact": "Potential employee data exposure"
            },
            {
                "title": "Healthcare Phishing (2021)",
                "description": """
                WHAT HAPPENED:
                Hospital employees fell for phishing, compromising patient data.
                
                HOW:
                • Email appeared to be from IT support
                • Requested password reset due to "security update"
                • Attackers accessed patient records
                • Medical information exposed
                
                LESSON:
                Healthcare is heavily targeted. Never provide credentials via email.
                IT won't ask for your password.
                """,
                "impact": "Patient data of 100,000+ compromised"
            }
        ]
        
        print("\n" + "="*70)
        print("REAL-WORLD CASE STUDIES")
        print("="*70 + "\n")
        
        for i, case in enumerate(cases, 1):
            print(f"{i}. {case['title']}")
        
        print(f"{len(cases) + 1}. Back to Menu")
        
        try:
            choice = int(input("\nSelect a case study (1-5): "))
            if 1 <= choice <= len(cases):
                case = cases[choice - 1]
                print(f"\n{'='*70}")
                print(case['title'].upper())
                print(f"{'='*70}")
                print(case['description'])
                print(f"Impact: {case['impact']}\n")
                input("Press Enter to continue...")
            elif choice == len(cases) + 1:
                return
        except ValueError:
            print("Invalid input")
    
    def view_progress(self):
        """Display user progress and statistics."""
        print("\n" + "="*70)
        print("YOUR PROGRESS")
        print("="*70)

        if self.total_questions == 0:
            print("You haven't taken the quiz yet.\n")
        else:
            percentage = (self.user_score / self.total_questions) * 100
            print(f"Quiz Score: {self.user_score}/{self.total_questions} ({percentage:.1f}%)")

            # Progress bar
            filled = int(percentage / 5)
            print(f"Progress: [{'█' * filled}{'░' * (20 - filled)}] {percentage:.1f}%\n")

        print("MODULES COMPLETED:")
        print("✓ Module 1: What is Phishing? - Completed")
        print("✓ Module 2: Recognize Phishing Emails - Completed")
        print("✓ Module 3: Fake Website Indicators - Completed")
        print("✓ Module 4: Social Engineering Tactics - Completed")
        print("\nKEY TAKEAWAYS:")
        print("• Never click links in suspicious emails")
        print("• Always verify URLs before entering credentials")
        print("• Think before you act - urgency is a red flag")
        print("• When in doubt, contact the organization directly")

        input("\nPress Enter to continue...")

    def email_simulator(self):
        """Interactive email analysis simulator."""
        emails = [
            {
                "from": "security@paypal-verify.com",
                "subject": "URGENT: Confirm Your Account Now!",
                "body": "Dear Valued Customer,\n\nYour account has been limited. Click here immediately to restore access.\n\nBest regards,\nPayPal Security Team",
                "red_flags": ["Suspicious domain (paypal-verify.com not paypal.com)", "Urgent language", "Generic greeting", "Requests to click link"],
                "verdict": "PHISHING"
            },
            {
                "from": "noreply@amazon.com",
                "subject": "Order #123-4567890-1234567 has shipped",
                "body": "Your package from Amazon has been dispatched and is on its way. Track your package using your account.",
                "red_flags": ["None - legitimate email"],
                "verdict": "LEGITIMATE"
            },
            {
                "from": "hr@companyx.com",
                "subject": "Update Your Direct Deposit Information",
                "body": "Please click the link below to update your banking information due to system changes.",
                "red_flags": ["Request for sensitive financial info via email", "Unusual from HR"],
                "verdict": "SUSPICIOUS"
            },
            {
                "from": "billing@app-store.io",
                "subject": "Subscription Renewal Failed - Action Required",
                "body": "Your subscription payment failed. Update your payment method immediately or your account will be suspended.",
                "red_flags": ["Threatening language", "Suspicious domain", "Request to update payment"],
                "verdict": "PHISHING"
            }
        ]

        print("\n" + "="*70)
        print("EMAIL SIMULATOR - Analyze Real-Looking Emails")
        print("="*70 + "\n")

        for i, email in enumerate(emails, 1):
            print(f"Email #{i}")
            print("-" * 70)
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Body: {email['body']}\n")

            print("Analyze this email. Is it LEGITIMATE, SUSPICIOUS, or PHISHING?")
            user_verdict = input("Your analysis (L/S/P): ").upper().strip()

            # Map input to verdict
            verdict_map = {'L': 'LEGITIMATE', 'S': 'SUSPICIOUS', 'P': 'PHISHING'}
            user_answer = verdict_map.get(user_verdict, "")

            if user_answer == email['verdict']:
                print("✓ CORRECT!\n")
            else:
                print(f"✗ INCORRECT. The correct answer is: {email['verdict']}\n")

            print("Red Flags:")
            for flag in email['red_flags']:
                print(f"  • {flag}")
            print("\n")

        input("Press Enter to continue...")

    def best_practices_guide(self):
        """Comprehensive best practices guide."""
        practices = """
        CYBERSECURITY BEST PRACTICES GUIDE
        ═════════════════════════════════════════════════════════════════

        1. PASSWORD SECURITY
        ─────────────────────────────────────────────────────────────────
        ✓ Use strong passwords (12+ characters, mixed case, numbers, symbols)
        ✓ Never reuse passwords across different accounts
        ✓ Use password managers (LastPass, 1Password, Bitwarden)
        ✓ Enable two-factor authentication (2FA) whenever possible
        ✗ Don't share passwords with anyone (even IT staff)
        ✗ Don't write passwords on sticky notes
        ✗ Don't use common words or personal information

        2. EMAIL SAFETY
        ─────────────────────────────────────────────────────────────────
        ✓ Enable email filtering and spam protection
        ✓ Verify sender before responding to requests
        ✓ Check email headers for suspicious information
        ✓ Report suspicious emails to IT
        ✓ Keep email addresses private
        ✗ Don't click links in unsolicited emails
        ✗ Don't download attachments from unknown senders
        ✗ Don't reply to phishing emails

        3. BROWSING SAFELY
        ─────────────────────────────────────────────────────────────────
        ✓ Keep browser and plugins updated
        ✓ Use reputable antivirus/anti-malware software
        ✓ Enable browser security features
        ✓ Use HTTPS websites only for sensitive transactions
        ✓ Clear cookies and cache regularly
        ✗ Don't visit suspicious websites
        ✗ Don't download files from untrusted sources
        ✗ Don't disable security warnings

        4. DEVICE SECURITY
        ─────────────────────────────────────────────────────────────────
        ✓ Keep operating system updated
        ✓ Enable firewall protection
        ✓ Lock your device when leaving it
        ✓ Use encrypted storage for sensitive files
        ✓ Regularly backup important data
        ✗ Don't leave devices unattended
        ✗ Don't use public WiFi for sensitive transactions
        ✗ Don't connect to untrusted networks

        5. SOCIAL MEDIA SAFETY
        ─────────────────────────────────────────────────────────────────
        ✓ Use strong privacy settings
        ✓ Be cautious about friend requests
        ✓ Verify accounts before connecting
        ✓ Limit personal information shared
        ✓ Review privacy policies regularly
        ✗ Don't accept friend requests from strangers
        ✗ Don't share sensitive information online
        ✗ Don't click links from unknown accounts

        6. INCIDENT RESPONSE
        ─────────────────────────────────────────────────────────────────
        If you suspect a phishing attack:

        1. STOP - Don't enter any information
        2. ISOLATE - Disconnect from network if compromised
        3. REPORT - Contact your IT department immediately
        4. DOCUMENT - Save the email/screenshot
        5. MONITOR - Watch accounts for suspicious activity
        6. CHANGE - Update passwords from secure device

        Emergency Contacts:
        • IT Support: ext. 5555
        • Security Team: security@company.com
        • Help Desk: helpdesk@company.com

        Press Enter to continue...
        """
        print(practices)
        input()

    def vulnerability_test(self):
        """Self-assessment vulnerability test."""
        questions = [
            {
                "question": "You receive an email asking you to confirm your password. What do you do?",
                "options": [
                    "Immediately click the link and update password",
                    "Call IT using the number on your badge, never from email",
                    "Reply to the email asking for verification"
                ],
                "correct": 1,
                "risk": "HIGH"
            },
            {
                "question": "A colleague asks for your password to access a file. Your response?",
                "options": [
                    "Share it since they're a colleague",
                    "Tell them to contact IT for proper access",
                    "Create a temporary password for them"
                ],
                "correct": 1,
                "risk": "HIGH"
            },
            {
                "question": "You notice unfamiliar activity on your account. What's your first step?",
                "options": [
                    "Wait and see if it continues",
                    "Change your password and report to IT",
                    "Ask colleagues if they accessed it"
                ],
                "correct": 1,
                "risk": "HIGH"
            },
            {
                "question": "An email claims your Amazon account will be closed unless you verify immediately.",
                "options": [
                    "Click the link immediately",
                    "Go directly to amazon.com (don't use email link) to check",
                    "Call Amazon using a number from the email"
                ],
                "correct": 1,
                "risk": "MEDIUM"
            },
            {
                "question": "What should you do with confidential documents?",
                "options": [
                    "Leave them on your desk",
                    "Lock them away and dispose of securely",
                    "Email them to yourself at home"
                ],
                "correct": 1,
                "risk": "MEDIUM"
            }
        ]

        print("\n" + "="*70)
        print("VULNERABILITY SELF-ASSESSMENT TEST")
        print("="*70)
        print("Evaluate your cybersecurity behavior and identify risks.\n")

        vulnerabilities = 0
        for i, q in enumerate(questions, 1):
            print(f"Question {i}/{len(questions)}")
            print(f"{q['question']}\n")

            for j, option in enumerate(q['options'], 1):
                print(f"  {j}. {option}")

            while True:
                try:
                    answer = int(input("\nYour answer (1-3): "))
                    if 1 <= answer <= 3:
                        break
                    print("Please enter 1-3")
                except ValueError:
                    print("Please enter a valid number")

            if answer - 1 == q['correct']:
                print("✓ SECURE BEHAVIOR\n")
            else:
                print(f"✗ VULNERABILITY DETECTED (Risk: {q['risk']})\n")
                vulnerabilities += 1

        print("="*70)
        print("ASSESSMENT RESULTS")
        print("="*70)
        print(f"Vulnerabilities Found: {vulnerabilities}/{len(questions)}")

        if vulnerabilities == 0:
            print("🏆 Excellent! Your cybersecurity practices are strong.")
        elif vulnerabilities <= 2:
            print("✓ Good awareness. Minor improvements needed.")
        else:
            print("△ Significant vulnerabilities. Review the training materials.")

        input("\nPress Enter to continue...")

    def resources_and_links(self):
        """Provide additional resources and learning materials."""
        resources = """
        ADDITIONAL RESOURCES & LEARNING MATERIALS
        ═════════════════════════════════════════════════════════════════

        ONLINE COURSES & TRAINING
        ─────────────────────────────────────────────────────────────────
        • Coursera: Cybersecurity Fundamentals
        • edX: Introduction to Cybersecurity
        • LinkedIn Learning: Security Awareness Training
        • SANS Cyber Academy: Security Fundamentals

        CERTIFICATION PROGRAMS
        ─────────────────────────────────────────────────────────────────
        • CISSP (Certified Information Systems Security Professional)
        • CEH (Certified Ethical Hacker)
        • CompTIA Security+
        • CISM (Certified Information Security Manager)

        TESTING & TRAINING PLATFORMS
        ─────────────────────────────────────────────────────────────────
        • Phishing Simulator: www.phishingsimulator.com
        • KnowBe4: Security Awareness Training
        • Gophish: Open-source phishing simulation
        • Social-Engineer: Professional testing

        REPORTING PHISHING
        ─────────────────────────────────────────────────────────────────
        • FBI: ic3.gov (Internet Crime Complaint Center)
        • APWG: apwg.org (Anti-Phishing Working Group)
        • Your IT Department
        • Your Email Provider

        SECURITY ORGANIZATIONS
        ─────────────────────────────────────────────────────────────────
        • NIST: Cybersecurity Framework
        • OWASP: Web Application Security
        • CIS: Center for Internet Security
        • ISSA: Information Systems Security Association

        SECURITY NEWS & UPDATES
        ─────────────────────────────────────────────────────────────────
        • SecurityWeekly.com
        • DarkReading.com
        • BleepingComputer.com
        • KrebsOnSecurity.com

        TOOLS & SOFTWARE
        ─────────────────────────────────────────────────────────────────
        • Bitwarden: Password Manager
        • Authy: Two-Factor Authentication
        • ProtonMail: Encrypted Email
        • Signal: Secure Messaging
        • VPN Services: ExpressVPN, NordVPN, Proton VPN

        GOVERNMENT RESOURCES
        ─────────────────────────────────────────────────────────────────
        • CISA (Cybersecurity & Infrastructure Security Agency)
        • NIST Cybersecurity Resource Center
        • NSA Cybersecurity Center
        • Stop.Think.Connect Campaign

        Press Enter to continue...
        """
        print(resources)
        input()

    def interactive_scenario(self):
        """Interactive real-world scenario simulator."""
        scenarios = [
            {
                "title": "The Urgent CEO Request",
                "description": """
                You receive an email from your CEO that reads:

                "Hi John, I need you to process an urgent wire transfer of $50,000
                to our new vendor immediately. Please handle this confidentially.
                Reply with details. - CEO"

                The email came from a Gmail address that looks similar to the
                company domain but is slightly different.
                """,
                "steps": [
                    ("Do you process the transfer?", "NO - Verify via known communication channel"),
                    ("Should you tell others?", "YES - Inform your manager and IT immediately"),
                    ("What's the real threat?", "CEO fraud / Business Email Compromise (BEC)")
                ]
            },
            {
                "title": "The IT Support Scam",
                "description": """
                Your phone rings. The caller claims to be from "Microsoft Support"
                and says your computer has been compromised. They ask you to:
                1. Go to a website
                2. Download software
                3. Give them remote access
                """,
                "steps": [
                    ("Do you comply?", "NO - Hang up immediately"),
                    ("What should you do?", "Contact your real IT department"),
                    ("What's this called?", "Tech Support Scam / Vishing")
                ]
            },
            {
                "title": "The Password Reset Email",
                "description": """
                You get an email saying your Microsoft password expires in 24 hours.

                The email looks professional with the Microsoft logo and directs
                you to click a link to reset your password.

                However, when you hover over the link, it shows a different URL.
                """,
                "steps": [
                    ("Should you click the link?", "NO - Go directly to microsoft.com"),
                    ("How to verify legitimacy?", "Type the official URL manually"),
                    ("What was the red flag?", "URL mismatch - hover before clicking")
                ]
            }
        ]

        print("\n" + "="*70)
        print("INTERACTIVE SCENARIO TRAINER")
        print("="*70 + "\n")

        for i, scenario in enumerate(scenarios, 1):
            print(f"SCENARIO {i}: {scenario['title']}")
            print("-" * 70)
            print(scenario['description'])
            print("\nStep-by-step Analysis:")

            for step_num, (question, answer) in enumerate(scenario['steps'], 1):
                print(f"\n{step_num}. {question}")
                input("   Press Enter to reveal answer...")
                print(f"   → {answer}")

            print("\n")

        input("Press Enter to continue...")
    
    def run(self):
        """Main program loop."""
        self.display_banner()

        # Get user name for personalization
        self.user_name = input("Enter your name for this training: ").strip() or "Employee"
        print(f"\nWelcome, {self.user_name}!\n")

        while True:
            print(self.display_menu(), end='')

            try:
                choice = input().strip()

                if choice == '1':
                    self.learn_phishing_basics()
                elif choice == '2':
                    self.recognize_phishing_emails()
                elif choice == '3':
                    self.fake_website_indicators()
                elif choice == '4':
                    self.social_engineering_tactics()
                elif choice == '5':
                    self.run_quiz()
                elif choice == '6':
                    self.email_simulator()
                elif choice == '7':
                    self.interactive_scenario()
                elif choice == '8':
                    self.vulnerability_test()
                elif choice == '9':
                    self.best_practices_guide()
                elif choice == '10':
                    self.case_studies()
                elif choice == '11':
                    self.resources_and_links()
                elif choice == '12':
                    self.view_progress()
                elif choice == '13':
                    print("\n" + "="*70)
                    print(f"Thank you for completing Phishing Awareness Training, {self.user_name}!")
                    print("Stay safe and vigilant online!")
                    print("="*70 + "\n")
                    break
                else:
                    print("Invalid choice. Please select 1-13.\n")

            except KeyboardInterrupt:
                print("\n\nTraining interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")


def export_certificate(user_name: str = "Employee"):
    """Generate a completion certificate."""
    certificate = f"""
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                         CERTIFICATE OF COMPLETION                        ║
    ║                                                                          ║
    ║                  PHISHING AWARENESS TRAINING PROGRAM                     ║
    ║                                                                          ║
    ║  This certifies that                                                     ║
    ║                                                                          ║
    ║  {user_name:<60}  ║
    ║                                                                          ║
    ║  has successfully completed the Phishing Awareness Training Program      ║
    ║                                                                          ║
    ║  Date: {datetime.now().strftime('%B %d, %Y'):<52}  ║
    ║                                                                          ║
    ║  This training covers:                                                   ║
    ║  • Understanding phishing attacks and tactics                            ║
    ║  • Recognizing phishing emails                                           ║
    ║  • Identifying fake websites                                             ║
    ║  • Detecting social engineering attempts                                 ║
    ║  • Best practices for staying safe                                       ║
    ║                                                                          ║
    ║  Awarded by: Cybersecurity Awareness Team                                ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """
    return certificate


if __name__ == "__main__":
    training = PhishingTraining()
    training.run()
    
    # Optional: Generate certificate
    show_cert = input("\nWould you like a completion certificate? (y/n): ").lower()
    if show_cert == 'y':
        name = input("Enter your name: ").strip() or "Employee"
        print(export_certificate(name))
