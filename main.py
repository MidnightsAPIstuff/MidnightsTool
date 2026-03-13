import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import zipfile
import shutil
import webbrowser
import requests
import time
import threading
        # -----------------------------------------------------------------------------
        # Dont Skid  
        # -----------------------------------------------------------------------------

class D4rkzzToolsGUI:
    def __init__(self, master):
        self.master = master
        master.title("D4rkzz Tools GUI")
        master.geometry("800x600")
        master.configure(bg="black")
        master.resizable(False, False) # Disable resizing for a fixed layout

        # Set a custom font for the application
        try:
            self.custom_font_large = ("Comic Sans MS", 18, "bold") # A bold, rounded font for titles
            self.custom_font_medium = ("Comic Sans MS", 12)
            self.custom_font_button = ("Comic Sans MS", 14, "bold")
            self.custom_font_label = ("Comic Sans MS", 10)
        except tk.TclError:
            # Fallback font if 'Comic Sans MS' is not available
            self.custom_font_large = ("Arial", 18, "bold")
            self.custom_font_medium = ("Arial", 12)
            self.custom_font_button = ("Arial", 14, "bold")
            self.custom_font_label = ("Arial", 10)

        # -----------------------------------------------------------------------------
        # Dont Skid  
        # -----------------------------------------------------------------------------

        # --- Webhook Spammer Section ---
        self.webhook_frame = tk.LabelFrame(master, text="Webhook Spammer",
                                           font=self.custom_font_large,
                                           fg="#8A2BE2", # Blue Violet
                                           bg="black", bd=5, relief="solid",
                                           highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=2)
        self.webhook_frame.place(x=50, y=50, width=350, height=400)

        # Webhook Name
        self.webhook_name_label = tk.Label(self.webhook_frame, text="Webhook Name:", bg="black", fg="white", font=self.custom_font_label)
        self.webhook_name_label.pack(pady=(20, 5))
        self.webhook_name_entry = tk.Entry(self.webhook_frame, bg="#333333", fg="white", insertbackground="white", font=self.custom_font_medium, bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=1)
        self.webhook_name_entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)

        # Message
        self.message_label = tk.Label(self.webhook_frame, text="Message:", bg="black", fg="white", font=self.custom_font_label)
        self.message_label.pack(pady=(10, 5))
        self.message_entry = tk.Entry(self.webhook_frame, bg="#333333", fg="white", insertbackground="white", font=self.custom_font_medium, bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=1)
        self.message_entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)

        # Webhook URL
        self.webhook_url_label = tk.Label(self.webhook_frame, text="Webhook URL:", bg="black", fg="white", font=self.custom_font_label)
        self.webhook_url_label.pack(pady=(10, 5))
        self.webhook_url_entry = tk.Entry(self.webhook_frame, bg="#333333", fg="white", insertbackground="white", font=self.custom_font_medium, bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=1)
        self.webhook_url_entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)

        # Start Button
        self.start_button = tk.Button(self.webhook_frame, text="Start", command=self.start_webhook_spam,
                                      bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                      activebackground="#6A0DAD", activeforeground="white",
                                      bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        self.start_button.pack(pady=20)

        self.status_label = tk.Label(self.webhook_frame, text="", bg="black", fg="yellow", font=self.custom_font_label)
        self.status_label.pack(pady=5)

        # --- D4rkzz Tools GUI Section ---
        self.tools_frame = tk.LabelFrame(master, text="D4rkzz Tools GUI",
                                         font=self.custom_font_large,
                                         fg="#8A2BE2", # Blue Violet
                                         bg="black", bd=5, relief="solid",
                                         highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=2)
        self.tools_frame.place(x=450, y=50, width=300, height=400)

        # APK to ZIP Button
        self.apk_to_zip_button = tk.Button(self.tools_frame, text="APK to ZIP", command=self.apk_to_zip,
                                           bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                           activebackground="#6A0DAD", activeforeground="white",
                                           bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        self.apk_to_zip_button.pack(pady=(30, 15), fill=tk.X, padx=30)

        # Grab Metadata Button (now opens a new window)
        self.grab_metadata_button = tk.Button(self.tools_frame, text="Grab metadata", command=self.open_grab_metadata_window,
                                             bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                             activebackground="#6A0DAD", activeforeground="white",
                                             bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        self.grab_metadata_button.pack(pady=15, fill=tk.X, padx=30)

        # Methods Button
        self.methods_button = tk.Button(self.tools_frame, text="methods", command=self.create_methods_file,
                                        bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                        activebackground="#6A0DAD", activeforeground="white",
                                        bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        self.methods_button.pack(pady=15, fill=tk.X, padx=30)

        # Discord Button
        self.discord_button = tk.Button(self.tools_frame, text="Discord", command=self.open_discord_link,
                                        bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                        activebackground="#6A0DAD", activeforeground="white",
                                        bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        self.discord_button.pack(pady=15, fill=tk.X, padx=30)

        # Made by Darkzz The Modder label
        self.creator_label = tk.Label(master, text="Made By Darkzz The Modder", bg="black", fg="#8A2BE2", font=("Comic Sans MS", 10, "bold"))
        self.creator_label.place(relx=0.5, rely=0.03, anchor=tk.CENTER)

        # Custom message box for alerts (replaces messagebox.showinfo, messagebox.showerror)
        self.custom_message_box = None
        self.message_box_label = None
        self.message_box_close_button = None

    def show_custom_message(self, title, message, is_error=False):
        if self.custom_message_box:
            self.custom_message_box.destroy()

        self.custom_message_box = tk.Toplevel(self.master)
        self.custom_message_box.title(title)
        self.custom_message_box.geometry("300x150")
        self.custom_message_box.grab_set() # Make it modal
        self.custom_message_box.transient(self.master) # Make it appear on top of the main window
        self.custom_message_box.resizable(False, False)
        self.custom_message_box.configure(bg="black")

        text_color = "red" if is_error else "green"
        border_color = "red" if is_error else "#8A2BE2"

        frame = tk.Frame(self.custom_message_box, bg="black", bd=2, relief="solid",
                         highlightbackground=border_color, highlightcolor=border_color, highlightthickness=2)
        frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.message_box_label = tk.Label(frame, text=message, bg="black", fg=text_color, font=self.custom_font_label, wraplength=250)
        self.message_box_label.pack(pady=10)

        self.message_box_close_button = tk.Button(frame, text="OK", command=self.close_custom_message,
                                                   bg="#8A2BE2", fg="white", font=self.custom_font_label,
                                                   activebackground="#6A0DAD", activeforeground="white",
                                                   bd=2, relief="raised")
        self.message_box_close_button.pack(pady=5)

        self.custom_message_box.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (self.custom_message_box.winfo_width() // 2)
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (self.custom_message_box.winfo_height() // 2)
        self.custom_message_box.geometry(f"+{x}+{y}")

    def close_custom_message(self):
        if self.custom_message_box:
            self.custom_message_box.grab_release()
            self.custom_message_box.destroy()
            self.custom_message_box = None

    def _send_webhook_message(self, webhook_url, message, webhook_name, file_to_send=None):
        headers = {}
        payload = {}
        files = {}

        if file_to_send:
            # If a file is being sent, content-type for the request becomes multipart/form-data
            # 'content' and 'username' must be sent as form fields, not json payload
            payload["content"] = message
            payload["username"] = webhook_name
            files = {'file': (os.path.basename(file_to_send), open(file_to_send, 'rb'), 'application/octet-stream')}
        else:
            # For text-only messages, use JSON payload
            headers["Content-Type"] = "application/json"
            payload = {
                "content": message,
                "username": webhook_name
            }

        try:
            if file_to_send:
                response = requests.post(webhook_url, data=payload, files=files)
            else:
                response = requests.post(webhook_url, json=payload, headers=headers)
            
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
            return False
        finally:
            if file_to_send and 'file' in files and files['file'][1]:
                files['file'][1].close() # Close the file handle


    def send_messages_thread(self, webhook_name, webhook_url, message_content):
        self.master.after(0, lambda: self.status_label.config(text="Sending messages..."))
        success_count = 0
        for i in range(600):
            if self._send_webhook_message(webhook_url, message_content, webhook_name):
                success_count += 1
                self.master.after(0, lambda i=i: self.status_label.config(text=f"Sent {i+1}/600 messages..."))
            else:
                self.master.after(0, lambda: self.show_custom_message("Webhook Error", "Failed to send some messages. Check URL and permissions.", is_error=True))
                break # Stop if a message fails
            time.sleep(0.1) # Small delay to avoid rate limits

        if success_count == 600:
            self.master.after(0, lambda: self.status_label.config(text="All 600 messages sent!"))
            self.master.after(0, lambda: self.show_custom_message("Success", "All 600 messages sent successfully!"))
        else:
            self.master.after(0, lambda: self.status_label.config(text=f"Finished sending with errors. Sent {success_count} messages."))


    def start_webhook_spam(self):
        webhook_name = self.webhook_name_entry.get()
        webhook_url = self.webhook_url_entry.get()
        message_content = self.message_entry.get()

        if not webhook_url:
            self.show_custom_message("Input Error", "Webhook URL cannot be empty.", is_error=True)
            return
        if not message_content:
            self.show_custom_message("Input Error", "Message cannot be empty.", is_error=True)
            return

        # Start sending messages in a separate thread to keep GUI responsive
        threading.Thread(target=self.send_messages_thread, args=(webhook_name, webhook_url, message_content)).start()


    def apk_to_zip(self):
        file_path = filedialog.askopenfilename(
            title="Select .apk file",
            filetypes=(("APK files", "*.apk"), ("All files", "*.*"))
        )
        if file_path:
            dir_name = os.path.dirname(file_path)
            base_name = os.path.basename(file_path)
            name_without_ext, ext = os.path.splitext(base_name)

            if ext.lower() == ".apk":
                new_file_path = os.path.join(dir_name, name_without_ext + ".zip")
                try:
                    os.rename(file_path, new_file_path)
                    self.show_custom_message("Success", f"Renamed '{base_name}' to '{name_without_ext}.zip'")
                except OSError as e:
                    self.show_custom_message("Error", f"Failed to rename file: {e}", is_error=True)
            else:
                self.show_custom_message("Error", "Selected file is not an .apk file.", is_error=True)
    
    def open_grab_metadata_window(self):
        """Opens a new Toplevel window for grabbing and sending metadata."""
        grab_window = tk.Toplevel(self.master)
        grab_window.title("Grab Metadata & Send to Webhook")
        grab_window.geometry("400x300")
        grab_window.configure(bg="black")
        grab_window.transient(self.master) # Make it appear on top of the main window
        grab_window.resizable(False, False)

        # Center the new window
        grab_window.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (grab_window.winfo_width() // 2)
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (grab_window.winfo_height() // 2)
        grab_window.geometry(f"+{x}+{y}")

        # Webhook URL Input
        webhook_label = tk.Label(grab_window, text="Webhook URL:", bg="black", fg="white", font=self.custom_font_label)
        webhook_label.pack(pady=(15, 5))
        webhook_entry = tk.Entry(grab_window, bg="#333333", fg="white", insertbackground="white", font=self.custom_font_medium, bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=1)
        webhook_entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)
        message_label = tk.Label(grab_window, text="Message (for webhook):", bg="black", fg="white", font=self.custom_font_label)
        message_label.pack(pady=(10, 5))
        message_entry = tk.Entry(grab_window, bg="#333333", fg="white", insertbackground="white", font=self.custom_font_medium, bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=1)
        message_entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)
        grab_status_label = tk.Label(grab_window, text="", bg="black", fg="yellow", font=self.custom_font_label)
        grab_status_label.pack(pady=10)
        click_to_grab_button = tk.Button(grab_window, text="Click To Grab",
                                        command=lambda: self.process_metadata_for_webhook(
                                            webhook_entry.get(),
                                            message_entry.get(),
                                            grab_status_label,
                                            grab_window # Pass the window to close it on completion
                                        ),
                                        bg="#8A2BE2", fg="white", font=self.custom_font_button,
                                        activebackground="#6A0DAD", activeforeground="white",
                                        bd=3, relief="raised", highlightbackground="#BF5FFF", highlightcolor="#BF5FFF", highlightthickness=2, padx=10, pady=5)
        click_to_grab_button.pack(pady=20)
    
    def process_metadata_for_webhook(self, webhook_url, message_content, status_label, parent_window):
        if not webhook_url:
            self.show_custom_message("Input Error", "Webhook URL cannot be empty.", is_error=True)
            return
        if not message_content:
            self.show_custom_message("Input Error", "Message cannot be empty.", is_error=True)
            return

        file_path = filedialog.askopenfilename(
            title="Select .apk file",
            filetypes=(("APK files", "*.apk"), ("All files", "*.*"))
        )
        if not file_path:
            status_label.config(text="File selection cancelled.")
            return

        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        name_without_ext, ext = os.path.splitext(base_name)

        if ext.lower() != ".apk":
            self.show_custom_message("Error", "Selected file is not an .apk file.", is_error=True)
            return

        status_label.config(text="Processing metadata...")

        # Create "Grabbed Stuff" directory if it doesn't exist
        output_folder = os.path.join(dir_name, "Grabbed Stuff")
        os.makedirs(output_folder, exist_ok=True)

        # Rename APK to ZIP temporarily
        zip_file_path = os.path.join(dir_name, name_without_ext + ".zip")
        try:
            os.rename(file_path, zip_file_path)
        except OSError as e:
            status_label.config(text=f"Error: Failed to rename APK to ZIP: {e}")
            self.show_custom_message("Error", f"Failed to rename APK to ZIP: {e}", is_error=True)
            return

        metadata_found = False
        extracted_metadata_path = None
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    if "global-metadata.dat" in member:
                        extracted_metadata_path = zip_ref.extract(member, path=output_folder)
                        new_metadata_name = os.path.join(output_folder, "global-metadata.dat")
                        os.rename(extracted_metadata_path, new_metadata_name)
                        extracted_metadata_path = new_metadata_name # Update to the final path
                        metadata_found = True
                        break
            
            if metadata_found:
                status_label.config(text="Metadata found. Sending...")
                # Use a placeholder username for sending the file if not explicitly asked
                webhook_name = "Metadata Grabber" 
                send_success = self._send_webhook_message(webhook_url, message_content, webhook_name, extracted_metadata_path)
                
                if send_success:
                    self.show_custom_message("Success", f"'global-metadata.dat' extracted and sent to webhook!")
                    status_label.config(text="Metadata sent successfully!")
                    parent_window.destroy() # Close the new window on success
                else:
                    self.show_custom_message("Error", "Failed to send metadata via webhook. Check URL and file size.", is_error=True)
                    status_label.config(text="Failed to send metadata!")
            else:
                self.show_custom_message("Info", "'global-metadata.dat' not found in the APK.", is_error=False)
                status_label.config(text="'global-metadata.dat' not found.")
        except zipfile.BadZipFile:
            status_label.config(text="Error: Invalid ZIP file.")
            self.show_custom_message("Error", "The selected file is not a valid ZIP archive.", is_error=True)
        except Exception as e:
            status_label.config(text=f"An error occurred: {e}")
            self.show_custom_message("Error", f"An error occurred during metadata extraction/sending: {e}", is_error=True)
        finally:
            # Rename ZIP back to APK
            original_apk_path = os.path.join(dir_name, name_without_ext + ".apk")
            try:
                os.rename(zip_file_path, original_apk_path)
            except OSError as e:
                self.show_custom_message("Error", f"Failed to rename ZIP back to APK: {e}", is_error=True)
            
            # Clean up extracted metadata file if it exists and was successfully sent or failed
            if extracted_metadata_path and os.path.exists(extracted_metadata_path):
                try:
                    os.remove(extracted_metadata_path)
                    print(f"Cleaned up temporary metadata file: {extracted_metadata_path}")
                except Exception as e:
                    print(f"Error cleaning up metadata file: {e}")

        # -----------------------------------------------------------------------------
        # Dont Skid  
        # -----------------------------------------------------------------------------
    def create_methods_file(self):
        methods_content = """
-- SS/MDS stick --
metadata

search "Slingshot"
Rename to LBAAK.

-- No name --
metadata

search "gorilla"
rename to "__"

-- longarms --
UABEA APK

level0
search Gameobject GorillaPlayer
click view scene
find localscale
right click
edit asset
change it to 1.5 (all of them)
"""
        file_name = "methodss.txt"
        try:
            with open(file_name, "w") as f:
                f.write(methods_content)
            self.show_custom_message("Success", f"'{file_name}' created successfully in the application directory.")
        except IOError as e:
            self.show_custom_message("Error", f"Failed to create '{file_name}': {e}", is_error=True)

    def open_discord_link(self):
        discord_link = "https://discord.gg/6QZTRjRNHE"
        try:
            webbrowser.open_new_tab(discord_link)
            self.show_custom_message("Info", f"Opening Discord link: {discord_link}")
        except Exception as e:
            self.show_custom_message("Error", f"Failed to open link: {e}", is_error=True)
        # -----------------------------------------------------------------------------
        # Dont Skid 
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Dont Skid 
        # -----------------------------------------------------------------------------
# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    app = D4rkzzToolsGUI(root)
    root.mainloop()
