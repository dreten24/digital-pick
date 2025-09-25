# Digital Pick - Home Service Business Management System

Digital Pick is a comprehensive backend monitoring system designed specifically for home service businesses like junk removal, roofing, plumbing, and other service-based companies. It provides complete lead lifecycle management from acquisition to service completion.

## Features

### Lead Management
- Multi-source lead capture (website forms, Google Ads, Facebook, referrals)
- Advanced lead tracking and status management
- Automated lead scoring and prioritization
- Follow-up scheduling and reminders
- Lead conversion analytics

### Service Management
- Service catalog management
- Service request scheduling
- Team assignment and dispatch
- Service completion tracking
- Customer feedback collection

### Business Intelligence
- Real-time dashboard with key metrics
- Revenue analytics and forecasting
- Team performance tracking
- Conversion funnel analysis
- Custom reporting

### Monitoring & Alerts
- System health monitoring
- Business metric tracking
- Automated alerts for urgent leads
- Performance analytics
- Error tracking and resolution

## Quick Start

### Development Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Copy environment file:
   cp .env.example .env

3. Run the application:
   uvicorn app.main:app --reload

4. Access API documentation:
   http://localhost:8000/docs

### Production Deployment

1. Configure environment variables in .env
2. Deploy with Docker Compose:
   docker-compose up -d

## API Endpoints

- /api/v1/businesses/ - Business management
- /api/v1/leads/ - Lead management
- /api/v1/services/ - Service management
- /api/v1/monitoring/ - System monitoring
- /api/v1/webhooks/ - Webhook endpoints
- /api/v1/dashboard/ - Analytics dashboard

## Technology Stack

- Backend: FastAPI (Python)
- Database: SQLite (development)
- Caching: Redis
- Containerization: Docker
- Web Server: Nginx (production)

## License

Proprietary software. All rights reserved.
