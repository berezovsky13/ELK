import time
import random
import socket
import json
from datetime import datetime

# Sample user actions and status codes
actions = ['login', 'logout', 'purchase', 'view_item', 'add_to_cart']
status_codes = [200, 201, 400, 401, 403, 404, 500]
users = ['john_doe', 'jane_smith', 'bob_wilson', 'alice_brown']

def generate_log():
    timestamp = datetime.now().isoformat()
    user = random.choice(users)
    action = random.choice(actions)
    status = random.choice(status_codes)
    duration = random.randint(10, 1000)
    
    log_entry = {
        'timestamp': timestamp,
        'user': user,
        'action': action,
        'status_code': status,
        'duration_ms': duration,
        'host': socket.gethostname()
    }
    
    return json.dumps(log_entry)

def send_logs():
    print("Waiting for Logstash to be ready...")
    time.sleep(10)  # Wait for Logstash to start
    
    while True:
        try:
            # Connect to Logstash
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 5000))
            
            print("Connected to Logstash. Sending logs...")
            while True:
                log = generate_log()
                sock.send((log + '\n').encode())
                print(f"Sent: {log}")
                time.sleep(1)  # Send one log per second
                
        except ConnectionRefusedError:
            print("Could not connect to Logstash. Retrying in 5 seconds...")
            time.sleep(5)
        except ConnectionAbortedError:
            print("Connection to Logstash was lost. Retrying in 5 seconds...")
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nStopping log generation...")
            break
        finally:
            try:
                sock.close()
            except:
                pass

if __name__ == "__main__":
    send_logs() 