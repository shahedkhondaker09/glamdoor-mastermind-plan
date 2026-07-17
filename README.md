# GlamDoor Dubai 7-Day Mastermind Plan

Week 1 launch strategy for **GlamDoor** — a salon booking platform connecting customers with Dubai salons, powered by a bilingual AI chatbot.

## What's New
- **AI Chatbot**: 24/7 booking assistant (English + Arabic)
- Updated timeline with chatbot development milestones (Day 1-7)
- 3 conversation examples (EN, AR, mixed language)
- Chatbot architecture, prompts, FAQ, and deployment guide

## Project Structure
```
glamdoor-mastermind-plan/
├── docs/                               # Full plan documents
│   ├── GlamDoor_Dubai_7Day_Mastermind_Plan.pdf   # Updated plan with chatbot section
│   └── GlamDoor_Dubai_7Day_Mastermind_Plan.py    # Script to regenerate PDF
├── chatbot/                             # NEW - AI Chatbot specs
│   ├── chatbot_architecture.md          # Tech stack + flow diagrams
│   ├── prompts_en.md                    # English system prompt
│   ├── prompts_ar.md                    # Arabic system prompt
│   ├── faq_knowledge_base.md            # Bilingual FAQ (EN/AR)
│   └── chatbot_deployment.md            # Step-by-step deployment guide
├── templates/                           # Copy-paste message templates
│   ├── partner_outreach_whatsapp.txt
│   ├── partner_outreach_email.txt
│   ├── customer_email.txt
│   ├── influencer_dm.txt
│   ├── referral_broadcast.txt
│   └── follow_up_message.txt
├── content/                             # Content strategy
│   ├── social_calendar.csv
│   ├── ai_agent_configs.md
│   └── email_drip_sequence.md
├── tracking/                            # Tracking spreadsheets
│   ├── metrics_tracker.csv
│   ├── launch_checklist.md
│   ├── partner_tracker.csv
│   └── lead_tracker.csv
├── assets/                             # Reference materials
│   └── dubai_zones.md
├── requirements.txt
├── LICENSE                              # MIT
└── README.md
```

## Quick Start
```bash
git clone https://github.com/shahedkhondaker09/glamdoor-mastermind-plan.git
cd glamdoor-mastermind-plan
pip install -r requirements.txt
python3 docs/GlamDoor_Dubai_7Day_Mastermind_Plan.py
```

## AI Chatbot Features
- Bilingual: Auto-detects English / Arabic, responds in user's language
- Smart booking: "I want a manicure in Marina tomorrow 4pm" -> booked
- Salon search with ratings, prices, availability
- 24/7 support: FAQs, reschedule, cancellation
- Lead capture: Saves customer info before booking
- Post-booking: Auto reminders + review collection
- WhatsApp + web widget deployment
- Cost: ~AED 500/mo (GPT-4o-mini + Twilio)

## Week 1 Targets
| Metric | Target |
|--------|--------|
| Leads | 50-80 |
| Partners onboarded | 10-15 |
| Confirmed bookings | 3-5 (incl. bot-driven) |
| Cost per lead | < AED 40 |
| Chatbot live | Day 4 (EN/AR) |
| Social reach | > 50K |

## License
MIT
