# Mitigation Plan

1. **Teammate**  
   - Implemented for **Harrison Rowland**.

2. **Current Status**  
   - The microservice is **complete** and has been tested end-to-end with both the console test script and the Tkinter GUI.

3. **Incomplete Work**  
   - N/A – all planned functionality (reading `list.txt`, waiting on `command.txt`, writing `response.txt`) is implemented and verified.

4. **Access Instructions**  
   - **GitHub Repository:** https://github.com/your-username/sort-microservice  
   - **Setup & Run:**  
     ```bash
     git clone https://github.com/your-username/sort-microservice.git
     cd sort-microservice
     python microservice_sort.py      # starts the file-monitoring service
     # (optional) python sort_gui.py   # launches the Tkinter GUI
     ```
   - **Dependencies:** Only Python 3.6+ (standard library).

5. **Fallback / Support**  
   - **Contact:** Slack DM or email at `your.email@osu.edu`  
   - **Availability:** Monday–Friday, 9 AM–5 PM Pacific Time (UTC-7)  
   - I can help troubleshoot via screen-share or by sharing alternative file copies.

6. **Notification Deadline**  
   - If you cannot access or call the microservice, please inform me **by Wednesday, May 20, 2025 at 11:59 PM PST**.

7. **Additional Notes & Assumptions**  
   - Assumes Python 3.6+ installed and in PATH.  
   - Requires read/write permission in working directory.  
   - The service polls `command.txt` every second; adjust `time.sleep(1)` in `microservice_sort.py` for faster response.  
   - For multiple instances, use separate file sets or subdirectories to avoid conflicts.
