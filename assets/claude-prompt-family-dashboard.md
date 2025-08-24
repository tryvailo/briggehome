# CLAUDE PROMPT: HomeBridge Family Dashboard Interface

Create a complete, production-ready HTML page for the HomeBridge family dashboard. This is the ongoing interface for adult children to monitor their elderly parents' health after initial setup is complete.

## OVERALL DESIGN REQUIREMENTS

**Dashboard Philosophy:**
- Clean, professional healthcare dashboard design
- Data-driven interface with clear health insights
- Family-centric control and monitoring capabilities
- Real-time updates with historical trend analysis
- Medical-grade security and privacy controls
- Mobile-first responsive design for busy family members

**Brand Identity:**
- Product name: HomeBridge
- Primary color: #4f46e5 (medical blue)
- Success color: #10b981 (healthy green)
- Warning color: #f59e0b (attention orange)
- Critical color: #ef4444 (alert red)
- Font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif

## DASHBOARD LAYOUT STRUCTURE

### HEADER SECTION
**Top Navigation Bar:**
- HomeBridge logo with "Family Dashboard" subtitle
- Parent selector dropdown: "[Parent Name] ▼" (if multiple parents)
- Quick actions: "Emergency Contact", "Add Family Member", "Settings"
- User profile with notification bell (number badge if alerts)
- Last updated timestamp: "Last update: 2 minutes ago"

**Health Status Banner:**
- Large health status indicator:
  - Green: "All Good 😊" + health score (8.5/10)
  - Yellow: "Attention Needed 🤔" + specific concerns
  - Red: "Immediate Action Required 🚨" + emergency details
- Quick stats: "14 days healthy", "Last conversation: 2 hours ago", "Response rate: 95%"
- Emergency alert banner (if active): Red background with clear action buttons

### MAIN DASHBOARD CONTENT

### SECTION 1: HEALTH OVERVIEW CARDS
**Layout:** 2x2 grid on desktop, single column on mobile

**Card 1: Today's Status**
- Large parent photo with online/offline indicator
- Current mood: Visual emoji scale (1-10) with today's selection
- Recent conversation summary: "Feeling well, mentioned knee pain"
- Quick actions: "Start Conversation", "Send Message", "Emergency Call"

**Card 2: Key Health Metrics**
- Visual health score: Large circular progress indicator (8.2/10)
- Traffic light indicators:
  - Physical Health: Green ✅
  - Mental Health: Yellow ⚠️ 
  - Social Connection: Green ✅
  - Medication Compliance: Green ✅
- "View detailed analysis" link

**Card 3: Recent Activity**
- Conversation participation: "6/7 days this week"
- Response quality: "Detailed and engaged"
- Sleep quality: "Good (7.5/10 average)"
- Emergency alerts: "0 this month" (with celebration emoji if zero)

**Card 4: AI Insights**
- Latest GPT-4o health analysis summary
- Key concerns detected: "Mild knee discomfort increasing"
- Recommendations: "Consider physiotherapy consultation"
- Confidence level: "High (85% certainty)"

### SECTION 2: HEALTH TRENDS & ANALYTICS
**Interactive Chart Section:**
- Time period selector: "7 days", "30 days", "3 months", "1 year"
- Multi-line chart showing:
  - Mood trends (1-10 scale)
  - Energy levels
  - Sleep quality
  - Social interaction frequency
- Hover tooltips with specific conversation excerpts
- Export data button: "Download Health Report (PDF)"

**Health Parameters Grid:**
- Depression screening (PHQ-9): Score trend with clinical interpretation
- Cognitive assessment: Memory, attention, reasoning scores
- Anxiety monitoring: GAD-7 equivalent tracking
- Voice pattern analysis: Speech clarity, pace, emotional indicators
- Physical activity: Daily movement, exercise mentions
- Social connection: Family contact frequency, loneliness indicators

### SECTION 3: RECENT CONVERSATIONS
**Conversation History Table:**
- Date/time, conversation duration, participation quality
- AI summary of each conversation (1-2 sentences)
- Health flags: Green/yellow/red indicators for concerns
- Full transcript access (privacy-controlled)
- Search and filter functionality

**Conversation Insights Panel:**
- Most discussed topics this week
- Mood pattern analysis
- Medication mention tracking
- Family/social topic engagement
- Health concern frequency

### SECTION 4: ALERT & NOTIFICATION MANAGEMENT
**Active Alerts Section:**
- Emergency alerts (red background)
- Health concerns (orange background)  
- Medication reminders (blue background)
- Missed conversations (gray background)
- Family communication requests (green background)

**Alert Configuration:**
- Health threshold settings:
  - Mood below: 4/10 for 2 consecutive days
  - Missed conversations: 2 days in a row
  - Depression indicators: PHQ-9 score above 10
  - Emergency keywords: "pain", "fall", "help", "hospital"
- Notification preferences:
  - SMS, email, push notifications
  - Family member escalation rules
  - Time-of-day preferences

### SECTION 5: FAMILY COMMUNICATION HUB
**Direct Messaging Interface:**
- Chat-style interface with parent
- Voice message support (play/pause controls)
- Photo/document sharing capability
- Message read receipts and delivery status
- Quick message templates: "How are you?", "Thinking of you", etc.

**Family Coordination:**
- Other family member activity feed
- Care coordination calendar
- Medical appointment sharing
- Task assignment (medication reminders, check-ins)
- Group chat for family members

### SECTION 6: PARENT SETTINGS & CONTROLS
**Authentication Management:**
- Current authentication method display
- "Change authentication method" button
- Recent login attempts log
- Device trust status
- Remote assistance options: "Help [Parent] with login"

**Platform & Preferences:**
- Current platform: WhatsApp/PWA/Email/Phone
- "Switch platform" option with migration wizard
- Conversation schedule: preferred times
- AI personality settings: formal/casual, conversation style
- Language preferences and accessibility options

**Privacy & Data Controls:**
- Granular consent status
- Data sharing preferences with family members
- Conversation retention settings
- Export personal data option
- "Request data deletion" (GDPR compliance)

### SECTION 7: SUPPORT & RESOURCES
**Help & Guidance:**
- Video tutorials: "Understanding Health Insights", "Emergency Procedures"
- Setup guides: "Helping [Parent] with Technology"
- FAQ section with search
- Live chat support availability
- Family success stories and tips

**Medical Integration:**
- "Connect to GP practice" option
- Medical appointment calendar sync
- Medication list management
- Emergency medical information display
- "Share insights with healthcare provider" feature

## TECHNICAL IMPLEMENTATION REQUIREMENTS

### RESPONSIVE DESIGN SPECIFICATIONS
**Desktop Layout (1200px+):**
- Header: 80px height, fixed position
- Main content: CSS Grid, 3-column layout for cards
- Charts: Full-width section, 400px height
- Sidebar: 300px width for notifications

**Tablet Layout (768px-1199px):**
- Header: 70px height, collapsible navigation
- Main content: 2-column grid layout
- Charts: Responsive scaling with touch controls
- Notifications: Collapsible panel

**Mobile Layout (320px-767px):**
- Header: 60px height, hamburger menu
- Single column layout for all sections
- Touch-optimized controls (minimum 44px)
- Swipe gestures for chart navigation
- Bottom navigation for quick actions

### DATA VISUALIZATION REQUIREMENTS
**Chart Library Integration:**
- Use Chart.js or D3.js for interactive charts
- Real-time data updates via WebSocket or polling
- Export functionality (PNG, PDF, CSV)
- Color-blind friendly palettes
- Dark mode support

**Health Score Calculations:**
- Weighted algorithm combining multiple health parameters
- Historical trending with statistical significance
- AI confidence intervals display
- Comparison with age/demographic benchmarks
- Clear explanation of score components

### REAL-TIME FEATURES
**Live Updates:**
- WebSocket connection for real-time parent status
- Push notification integration (Web Push API)
- Real-time conversation monitoring
- Live emergency alert system
- Family member activity synchronization

**Offline Capability:**
- Service worker for offline functionality
- Local storage for recent data caching
- Offline alert queueing
- Sync when connection restored
- Clear offline/online status indicators

### PRIVACY & SECURITY IMPLEMENTATION
**Data Protection:**
- End-to-end encryption for sensitive health data
- Role-based access control for family members
- Audit logging for all data access
- GDPR compliance with consent management
- Secure session management with timeout

**Family Access Controls:**
- Granular permission system
- Parent consent verification for data sharing
- Emergency override capabilities
- Activity logging for transparency
- Data minimization principles

### ACCESSIBILITY REQUIREMENTS
**WCAG 2.1 AA Compliance:**
- Screen reader optimization with ARIA labels
- Keyboard navigation support
- High contrast mode (4.5:1 minimum)
- Focus indicators on all interactive elements
- Alternative text for all charts and images

**Family-Friendly Features:**
- Large text options for older family members
- Voice instructions for complex features
- Simple language in all explanations
- Clear visual hierarchy and spacing
- Error prevention and recovery

### INTEGRATION REQUIREMENTS
**API Integration:**
- REST API for all health data operations
- GraphQL for complex data queries
- WebSocket for real-time updates
- Third-party calendar integration (Google, Outlook)
- SMS/Email gateway integration

**Medical System Integration:**
- HL7 FHIR compatibility for medical data
- NHS API integration capabilities
- Pharmacy medication reminder systems
- GP practice management system connections
- Emergency services notification protocols

### PERFORMANCE REQUIREMENTS
**Loading Performance:**
- Initial page load: < 3 seconds on 3G
- Chart rendering: < 2 seconds for 30-day data
- Real-time updates: < 500ms latency
- Image optimization: WebP format with fallbacks
- CDN integration for global performance

**Scalability Considerations:**
- Support for families with multiple parents
- Historical data handling (2+ years)
- Concurrent family member access
- Peak load handling during emergencies
- Database query optimization

Please implement this as a complete HTML page with embedded CSS and JavaScript. Include realistic health data examples and interactive chart functionality. Add detailed comments explaining the healthcare-specific features and family communication workflows. Ensure all privacy controls are clearly visible and functional.