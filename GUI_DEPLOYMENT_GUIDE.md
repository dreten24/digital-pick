# Digital Pick - Step-by-Step GUI Deployment Guide

This guide will walk you through deploying Digital Pick using graphical interfaces (no command line required!).

## 📋 Prerequisites Checklist

### ✅ Step 1: Install Docker Desktop
1. **Download Docker Desktop**:
   - Visit: https://www.docker.com/products/docker-desktop/
   - Click "Download for Windows" or "Download for Mac"
   - Run the installer and follow the setup wizard

2. **Start Docker Desktop**:
   - Open Docker Desktop from your applications
   - Wait for the Docker icon in system tray to show "Docker Desktop is running"
   - You should see a green dot next to the Docker whale icon

### ✅ Step 2: Download Digital Pick
1. **Download the ZIP file** (from the link provided earlier)
2. **Extract the ZIP**:
   - Right-click on `digital-pick-system.zip`
   - Select "Extract All..." (Windows) or double-click (Mac)
   - Choose a location like your Desktop or Documents folder
   - Click "Extract"

## 🚀 Deployment Steps

### Step 3: Configure Environment Settings

1. **Navigate to the extracted folder**:
   - Open File Explorer (Windows) or Finder (Mac)
   - Go to where you extracted Digital Pick
   - You should see files like `docker-compose.yml`, `README.md`, etc.

2. **Copy environment file**:
   - Find the file named `.env.example`
   - Right-click on `.env.example`
   - Select "Copy"
   - Right-click in empty space → "Paste"
   - Rename the copied file from `.env.example - Copy` to `.env`
   
3. **Edit configuration** (Optional for basic setup):
   - Right-click on `.env` file
   - Select "Open with" → "Notepad" (Windows) or "TextEdit" (Mac)
   - For now, you can leave the default settings
   - Save and close the file

### Step 4: Deploy with Docker Desktop

1. **Open Docker Desktop**:
   - Make sure Docker Desktop is running (green whale icon)
   - Click on the Docker Desktop application

2. **Navigate to your project**:
   - In Docker Desktop, you might see a "Browse" or "Open" option
   - Or continue with the next step using file explorer

3. **Deploy using File Explorer**:
   - Open File Explorer/Finder to your Digital Pick folder
   - Look for the file named `docker-compose.yml`
   - **Double-click** on `docker-compose.yml`
   - This should open Docker Desktop and start the deployment

   **Alternative method:**
   - In Docker Desktop, look for a "+" or "Create" button
   - Select "From docker-compose.yml"
   - Navigate to your Digital Pick folder
   - Select the `docker-compose.yml` file

4. **Wait for deployment**:
   - Docker Desktop will show progress bars
   - You'll see messages like "Building..." and "Creating..."
   - Wait until you see "digital-pick" container running (green status)
   - This may take 5-10 minutes the first time

### Step 5: Verify Deployment

1. **Check Docker Desktop**:
   - In Docker Desktop, go to "Containers" tab
   - You should see containers running:
     - `digital-pick-digital-pick-1` (green/running)
     - `digital-pick-redis-1` (green/running)
     - `digital-pick-nginx-1` (green/running)

2. **Test the application**:
   - Open your web browser
   - Go to: `http://localhost:8000/docs`
   - You should see the Digital Pick API documentation page
   - Go to: `http://localhost:8000/health`
   - You should see a health status message

## 🎯 Using Digital Pick

### Access Points
- **📚 API Documentation**: http://localhost:8000/docs
- **❤️ Health Check**: http://localhost:8000/health
- **📊 System Status**: http://localhost:8000/api/v1/monitoring/health

### Testing Your System

1. **Run the test script**:
   - Navigate to your Digital Pick folder
   - Find `test_system.py`
   - **Right-click** → "Open with" → "Python"
   - Or if you have Python installed, double-click the file
   - This will test that everything is working correctly

## 🔧 Managing Your System

### Using Docker Desktop Interface

1. **View Logs**:
   - In Docker Desktop → "Containers" tab
   - Click on `digital-pick-digital-pick-1`
   - Click "Logs" tab to see system activity

2. **Stop the System**:
   - In Docker Desktop → "Containers" tab
   - Click the "Stop" button (square icon) next to digital-pick

3. **Restart the System**:
   - Click the "Start" button (play icon) next to digital-pick

4. **Update the System**:
   - Stop the containers first
   - Replace files in your Digital Pick folder with new versions
   - In Docker Desktop, click "Restart" or "Recreate"

## 📊 Configuration Guide

### Basic Configuration (.env file)

Open the `.env` file with Notepad/TextEdit and customize:

```
# Change this to a secure secret key
SECRET_KEY=your-very-secure-secret-key-here

# Email settings (for notifications)
SENDGRID_API_KEY=your-sendgrid-api-key
SENDGRID_FROM_EMAIL=noreply@yourbusiness.com

# SMS settings (for notifications)
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+1234567890

# Payment processing (optional)
STRIPE_SECRET_KEY=sk_test_your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=pk_test_your-stripe-publishable-key
```

### External Service Setup

1. **SendGrid (Email)**:
   - Go to: https://sendgrid.com
   - Create free account
   - Get API key from Settings → API Keys
   - Add to `.env` file

2. **Twilio (SMS)**:
   - Go to: https://twilio.com
   - Create account
   - Get Account SID, Auth Token from Console
   - Buy a phone number
   - Add to `.env` file

3. **Stripe (Payments)**:
   - Go to: https://stripe.com
   - Create account
   - Get API keys from Developers → API Keys
   - Add to `.env` file

## 🆘 Troubleshooting

### Common Issues

**Problem**: "Docker Desktop is not running"
- **Solution**: Start Docker Desktop application and wait for green whale icon

**Problem**: "Port 8000 is already in use"
- **Solution**: 
  - Stop other applications using port 8000
  - Or edit `docker-compose.yml` to use different port (like 8080:8000)

**Problem**: "Cannot access http://localhost:8000"
- **Solution**:
  - Check Docker Desktop shows containers as "Running" (green)
  - Wait a few minutes for full startup
  - Try http://127.0.0.1:8000 instead

**Problem**: Web browser shows "This site can't be reached"
- **Solution**:
  - Verify containers are running in Docker Desktop
  - Check Windows Firewall/Mac Firewall isn't blocking
  - Try restarting Docker Desktop

### Getting Help

1. **Check Logs**:
   - Docker Desktop → Containers → digital-pick → Logs tab
   - Look for error messages in red

2. **Restart Everything**:
   - Stop all containers in Docker Desktop
   - Wait 30 seconds
   - Start containers again

3. **Clean Restart**:
   - In Docker Desktop, delete the containers
   - Double-click `docker-compose.yml` again to recreate

## 🎉 Success!

When everything is working:
- ✅ Docker Desktop shows green containers
- ✅ http://localhost:8000/docs loads the API documentation
- ✅ http://localhost:8000/health shows system status
- ✅ You can create businesses and leads via the API

Your Digital Pick system is now ready to manage leads and services for your home service business! 🏠🔧

## 📞 API Usage Examples

### Creating Your First Business (via web browser)

1. Go to: http://localhost:8000/docs
2. Find "businesses" section
3. Click "POST /api/v1/businesses/"
4. Click "Try it out"
5. Replace the example with your business info:
```json
{
  "name": "ABC Junk Removal",
  "business_type": "junk_removal",
  "email": "contact@abcjunk.com",
  "phone": "555-123-4567",
  "city": "Your City",
  "state": "CA",
  "address": "123 Business St"
}
```
6. Click "Execute"
7. See your business created with an ID number!

### Capturing Your First Lead

1. In the API docs, find "leads" section
2. Click "POST /api/v1/leads/"
3. Click "Try it out"
4. Use your business ID from step above:
```json
{
  "business_id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@email.com",
  "phone": "555-987-6543",
  "service_address": "456 Customer St",
  "service_city": "Your City",
  "service_state": "CA",
  "service_zip": "12345",
  "source": "website",
  "service_type": "junk_removal",
  "description": "Need old furniture removed"
}
```
5. Click "Execute"
6. Your first lead is captured! 🎯

Now you're ready to build your home service empire with Digital Pick! 🚀
