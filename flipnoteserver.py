from flask import Flask, Response, request, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURATION ---
BASE_DIR = r"C:\Jeraldmemo-DSi-server\DSi"
UGO_PATH = os.path.join(BASE_DIR, "ds", "v2-us")

def get_dsi_info():
    fsid = request.headers.get('X-Dsi-ConsoleId', 'Unknown-DSi')
    return fsid

# 1. THE HELLO (Conntest)
@app.route('/')
@app.route('/index.html')
def conntest():
    fsid = get_dsi_info()
    print(f"\n[DSi]: Hello! Are you there?")
    print(f"[Server]: Hi {fsid}! Yes, I'm a real Nintendo server. How are you?")
    print(f"[*] DSi {fsid} is having a meeting with conntest!")
    
    content = "<html><head><title>Return Code 200</title></head><body>OK</body></html>"
    resp = Response(content, mimetype='text/html')
    resp.headers['X-Organization'] = 'Nintendo'
    return resp

# 2. THE PERMISSION (NAS)
@app.route('/ac', methods=['POST'])
@app.route('/proto/ac', methods=['POST'])
def nas_login():
    fsid = get_dsi_info()
    print(f"\n[DSi]: May I connect to the Flipnote Gallery?")
    print(f"[Server]: Of course! Checking your credentials now...")
    print(f"[!] DSi {fsid} is having a meeting with NAS!")
    
    nas_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <auth><status>0</status><token>jerald_pass_123</token><datetime>20260326140000</datetime></auth>"""
    print(f"[Server]: Everything looks good. Here is your Entry Pass.")
    return Response(nas_xml, mimetype='text/xml')

# 3. THE ENTRANCE & GOODBYE
@app.route('/ds/v2-us/index.ugo')
def launch_index():
    fsid = get_dsi_info()
    print(f"\n[DSi]: Awesome! I'm heading into the Jeraldmemo server now!")
    print(f"[>] DSi {fsid} is about to launch Jeraldmemo Flipnote server!")
    
    try:
        @Response.force_type
        def generate():
            # Send the file
            yield send_from_directory(UGO_PATH, 'index.ugo', mimetype='application/octet-stream')
            # Once the yield is done, the DSi has the file
            print(f"\n[Server]: Enjoy the gallery, {fsid}!")
            print(f"[SUCCESS] DSi {fsid} has entered the Jeraldmemo Flipnote server!")
            print(f"--- Conversation Finished ---")

        return send_from_directory(UGO_PATH, 'index.ugo', mimetype='application/octet-stream')
    except Exception as e:
        print(f"[ERROR] Connection lost: {e}")
        return "File Not Found", 404

if __name__ == '__main__':
    print("="*40)
    print("  JERALDMEMO SERVER: WAITING FOR KNOCK... ")
    print("="*40)
    app.run(host='0.0.0.0', port=80)
