from setuptools import setup, find_packages

setup(
    name="digital-pick",
    version="1.0.0",
    description="Home Service Business Management System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn[standard]>=0.24.0",
        "sqlalchemy>=2.0.23",
        "alembic>=1.12.1",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "httpx>=0.25.2",
        "schedule>=1.2.0",
        "twilio>=8.10.3",
        "sendgrid>=6.10.0",
        "stripe>=7.8.0",
        "aiofiles>=23.2.1",
        "jinja2>=3.1.2",
        "python-dotenv>=1.0.0",
        "pandas>=2.1.4",
        "plotly>=5.17.0",
        "redis>=5.0.1",
        "celery>=5.3.4",
        "apscheduler>=3.10.4",
        "websockets>=12.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "httpx>=0.25.2",
            "black>=23.0.0",
            "flake8>=6.0.0"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
