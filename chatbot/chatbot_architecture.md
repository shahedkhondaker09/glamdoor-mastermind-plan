# GlamDoor AI Chatbot - Architecture

## Overview
24/7 bilingual (EN/AR) chatbot for salon bookings, support, and lead capture.
Deploys on WhatsApp Business API + web widget.

## Tech Stack
- **AI Engine:** OpenAI GPT-4o-mini
- **WhatsApp:** Twilio WhatsApp Business API
- **Web Widget:** React embed component
- **Booking:** Cal.com API
- **Database:** Base44 entities (Bookings, Customers, Partners, Conversations)
- **Backend:** Base44 serverless function

## Architecture Flow
```
User (WhatsApp/Web)
    |
    v
Twilio / Web Widget
    |
    v
Base44 Backend Function
    |
    +---> GPT-4o-mini (language detection + intent + response)
    +---> Cal.com API (booking availability + create appointment)
    +---> Base44 Entities (save conversation, booking, lead)
    +---> Partner Notification (WhatsApp message to salon)
    |
    v
Response to User (EN or AR)
```

## Language Detection
- GPT-4o-mini detects language from first message
- All subsequent responses in detected language
- Mixed input (EN+AR) supported
- Switching: user can type "speak Arabic" / "تكلم عربي" to switch

## Booking Flow
1. User requests service/area/time
2. Bot queries Partner entity for matching salons
3. Bot checks Cal.com availability via API
4. Bot presents 3 options with prices + ratings
5. User selects -> bot creates Cal.com booking
6. Bot saves to Booking entity + notifies partner
7. Reminders: 2hrs before (auto), review request 2hrs after

## Entities Needed
- Bookings (customer_id, partner_id, service, datetime, status, price)
- Customers (name, phone, email, language, zone_preference)
- Partners (salon_name, zone, services, prices, rating, whatsapp, calcom_id)
- Conversations (customer_id, messages[], language, intent, outcome)

## Cost Estimate
- GPT-4o-mini API: ~AED 300/mo (1,000 conversations)
- Twilio WhatsApp: ~AED 200/mo (1,000 messages)
- Total: ~AED 500/mo
