#!/usr/bin/env python3
"""
Simple test script for Digital Pick system
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test system health check"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_create_business():
    """Test creating a business"""
    try:
        business_data = {
            "name": "Test Junk Removal Co",
            "business_type": "junk_removal",
            "email": "test@testjunk.com",
            "phone": "555-123-4567",
            "city": "Test City",
            "state": "CA",
            "address": "123 Test St"
        }
        
        response = requests.post(f"{BASE_URL}/api/v1/businesses/", json=business_data)
        if response.status_code == 201:
            business = response.json()
            print("✅ Business creation passed")
            print(f"   Business ID: {business['id']}")
            return business['id']
        else:
            print(f"❌ Business creation failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Business creation error: {e}")
        return None

def test_create_lead(business_id):
    """Test creating a lead"""
    try:
        lead_data = {
            "business_id": business_id,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@email.com",
            "phone": "555-987-6543",
            "service_address": "456 Service St",
            "service_city": "Test City",
            "service_state": "CA",
            "service_zip": "12345",
            "source": "website",
            "service_type": "junk_removal",
            "description": "Need old furniture removed",
            "urgency": "medium"
        }
        
        response = requests.post(f"{BASE_URL}/api/v1/leads/", json=lead_data)
        if response.status_code == 201:
            lead = response.json()
            print("✅ Lead creation passed")
            print(f"   Lead ID: {lead['id']}")
            return lead['id']
        else:
            print(f"❌ Lead creation failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Lead creation error: {e}")
        return None

def test_webhook():
    """Test webhook endpoint"""
    try:
        webhook_data = {
            "business_id": 1,
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane@email.com",
            "phone": "555-111-2222",
            "address": "789 Webhook Ave",
            "city": "Test City",
            "state": "CA",
            "service_type": "roofing",
            "message": "Need roof inspection"
        }
        
        response = requests.post(f"{BASE_URL}/api/v1/webhooks/form-submission", json=webhook_data)
        if response.status_code == 200:
            print("✅ Webhook test passed")
            return True
        else:
            print(f"❌ Webhook test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Webhook test error: {e}")
        return False

def main():
    print("🚀 Starting Digital Pick System Tests")
    print("=" * 50)
    
    # Test health check
    if not test_health_check():
        print("\n❌ System is not healthy. Please check if the server is running.")
        return
    
    # Test business creation
    business_id = test_create_business()
    if not business_id:
        print("\n❌ Cannot continue without a business.")
        return
    
    # Test lead creation
    lead_id = test_create_lead(business_id)
    if not lead_id:
        print("\n❌ Lead creation failed.")
    
    # Test webhook
    test_webhook()
    
    print("\n" + "=" * 50)
    print("🎉 Digital Pick System Tests Completed!")
    print(f"\nAPI Documentation: {BASE_URL}/docs")
    print(f"System Health: {BASE_URL}/health")

if __name__ == "__main__":
    main()
