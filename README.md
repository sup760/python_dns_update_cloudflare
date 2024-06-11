# Dynamic DNS Updater using Cloudflare API

This script updates a Cloudflare DNS record with your current public IP address. It fetches the current public IP, retrieves the corresponding DNS record ID from Cloudflare, and updates the DNS record with the new IP.

## Prerequisites

- Python 3.x
- Cloudflare account with API token
- `requests` library (`pip install requests`)
- `.env` file with the required environment variables

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dynamic-dns-updater.git
    cd dynamic-dns-updater
    ```

2. Install the required Python packages:
    ```bash
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the project directory with the following variables:
    ```bash
    API_KEY=your_cloudflare_api_token
    ZONE_ID=your_cloudflare_zone_id
    RECORD_NAME=your_dns_record_name
    ```

## Usage

Run the script to update your DNS record with the current public IP:
```bash
python update_dns.py
