A simple, cronable script that checks whether the computer's public IP address matches the IP address of a domain name hosted in AWS Route 53, and updates the record with the new public IP address if it has changed.

## Usage

    cp config_secrets.template config_secrets.py
    nano config_secrets.py
    sudo pip install -r requirements.txt
    ./update_ddns_record.py

## Credits

Based on https://gist.github.com/willtrking/736875ad128a6d9b10dd
