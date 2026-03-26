# Variables
PYTHON = python
SERVER_SCRIPT = flipnoteserver.py

# The default action when you just type 'make'
all: setup run

# 1. Prepare the Windows environment (Must run as Admin)
setup:
	@echo "--- Clearing Port 80 and Opening Firewall ---"
	powershell -Command "Stop-Service -Name W3SVC -ErrorAction SilentlyContinue"
	powershell -Command "New-NetFirewallRule -DisplayName 'Jeraldmemo_Flipnote_Server' -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow -ErrorAction SilentlyContinue"

# 2. Start the Handshake Conversation
run:
	@echo "--- Starting Jeraldmemo Flipnote Server ---"
	$(PYTHON) $(SERVER_SCRIPT)

# 3. Clean up (Optional)
clean:
	@echo "--- Cleaning up Python Cache ---"
	powershell -Command "Remove-Item -Path '**/__pycache__' -Recurse -Force -ErrorAction SilentlyContinue"
