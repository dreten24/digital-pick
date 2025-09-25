# Digital Pick Deployment Guide

## Quick Start

1. **Prerequisites**
   - Docker and Docker Compose installed
   - 8000 port available

2. **Setup Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Deploy**
   ```bash
   docker-compose up -d --build
   ```

4. **Verify**
   - API Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health
   - Test: python test_system.py

## Configuration

Edit `.env` file with your:
- Database settings
- External service API keys (Twilio, SendGrid, Stripe)
- Security keys

## Management Commands

```bash
# View logs
docker-compose logs -f digital-pick

# Stop system
docker-compose down

# Restart
docker-compose restart

# Update
docker-compose pull && docker-compose up -d
```

## Support

Check `/docs` endpoint for API documentation
Review system health at `/health`
