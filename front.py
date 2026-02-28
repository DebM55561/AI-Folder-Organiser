import tkinter as tk
from tkinter import filedialog, messagebox
from filemanager import Filemanager
from PreProc import PreProc
from model import ModelHandler  # Updated class name


class FolderOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI File Organizer")
        self.root.geometry("600x400")
        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="AI-Powered Folder Organizer", font=("Arial", 14, "bold")).pack(pady=10)

        # Source UI
        tk.Label(self.root, text="Select Folder to Organize:").pack(anchor="w", padx=20)
        s_frame = tk.Frame(self.root)
        s_frame.pack(fill="x", padx=20, pady=5)
        tk.Entry(s_frame, textvariable=self.source_path).pack(side="left", fill="x", expand=True)
        tk.Button(s_frame, text="Browse", command=lambda: self.source_path.set(filedialog.askdirectory())).pack(
            side="right")

        # Destination UI
        tk.Label(self.root, text="Select Destination Base Folder:").pack(anchor="w", padx=20)
        d_frame = tk.Frame(self.root)
        d_frame.pack(fill="x", padx=20, pady=5)
        tk.Entry(d_frame, textvariable=self.dest_path).pack(side="left", fill="x", expand=True)
        tk.Button(d_frame, text="Browse", command=lambda: self.dest_path.set(filedialog.askdirectory())).pack(
            side="right")

        self.run_btn = tk.Button(self.root, text="Organize Folder", command=self.process_files, bg="#2ecc71",
                                 fg="white", font=("Arial", 12, "bold"))
        self.run_btn.pack(pady=30)
        self.status_label = tk.Label(self.root, text="Ready", fg="blue")
        self.status_label.pack(side="bottom")

    def process_files(self):
        src, dst = self.source_path.get(), self.dest_path.get()
        if not src or not dst:
            messagebox.showerror("Error", "Select both folders.")
            return

        try:
            self.status_label.config(text="Extracting file content...")
            self.root.update()

            fm = Filemanager(src, dst)
            raw_filenames = fm.getFiles()  #
            if not raw_filenames:
                messagebox.showinfo("Done", "No files found.")
                return

            # Get the content of the files for AI analysis
            content_summaries = fm.getSummary()

            self.status_label.config(text="Preprocessing text...")
            self.root.update()
            pp = PreProc()
            clean_data = pp.preprocessing(content_summaries)

            self.status_label.config(text="Clustering files...")
            self.root.update()
            ai = ModelHandler(dst)
            ai.data = clean_data
            clusters = ai.filemodel()
            ai.save_model()

            self.status_label.config(text="Moving files...")
            fm.moveFilesToCluster(clusters)  #

            self.status_label.config(text="Success!")
            messagebox.showinfo("Success", f"Organized {len(raw_filenames)} files.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = FolderOrganizerGUI(root)
    root.mainloop()