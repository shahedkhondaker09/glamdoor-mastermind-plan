# Chatbot Deployment Guide

## Step 1: Prerequisites
- OpenAI API key (GPT-4o-mini access)
- Twilio account with WhatsApp Business API
- Cal.com account with API key
- Base44 backend function access

## Step 2: Backend Function
Create a Base44 backend function `glamdoorChatbot` that:
1. Receives incoming WhatsApp messages from Twilio webhook
2. Detects language (EN/AR) via GPT-4o-mini
3. Determines intent (booking, support, info, cancel)
4. Executes appropriate flow (booking -> Cal.com API)
5. Saves conversation to Base44 entities
6. Returns response to Twilio

## Step 3: WhatsApp Setup
1. Create Twilio WhatsApp Business account
2. Set webhook URL to Base44 function endpoint
3. Configure message templates (EN/AR) for notifications
4. Test with personal number

## Step 4: Web Widget
1. Build React component (chat widget)
2. Embed on landing page via script tag
3. Connect to same backend function via HTTP

## Step 5: Cal.com Integration
1. Create Cal.com account
2. Connect each partner salon as an event type
3. Use Cal.com API to check availability + create bookings
4. Sync booking IDs to Base44 Booking entity

## Step 6: Testing
1. Test EN booking flow (service -> area -> time -> confirm)
2. Test AR booking flow (same in Arabic)
3. Test mixed language input
4. Test cancellation flow
5. Test reschedule flow
6. Test human handoff
7. Test with 5 beta users before going live

## Step 7: Go Live
1. Enable Twilio webhook in production
2. Deploy web widget to landing page
3. Announce on social media
4. Monitor conversations for first 48 hours
5. Fix any dead-end flows
