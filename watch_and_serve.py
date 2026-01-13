#!/usr/bin/env python3
"""
Watch script that auto-regenerates the chart when files change.
Serves the chart on http://localhost:8000/benchmark_chart.html
"""
import os
import sys
import time
import subprocess
import threading
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

def generate_chart():
    """Run the plotting script to regenerate the chart."""
    print("\n🔄 Regenerating chart...")
    try:
        result = subprocess.run(
            [sys.executable, "plot_ai_benchmarks.py"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print("✅ Chart regenerated successfully!")
        else:
            print(f"❌ Error regenerating chart:\n{result.stderr}")
    except Exception as e:
        print(f"❌ Error: {e}")

def watch_files():
    """Watch for file changes and regenerate chart."""
    watched_files = ["AI_benchmarks_2025.csv", "plot_ai_benchmarks.py"]
    last_modified = {f: os.path.getmtime(f) if os.path.exists(f) else 0
                     for f in watched_files}

    print(f"👀 Watching files: {', '.join(watched_files)}")

    # Generate initial chart
    generate_chart()

    while True:
        time.sleep(1)  # Check every second

        for filepath in watched_files:
            if not os.path.exists(filepath):
                continue

            current_mtime = os.path.getmtime(filepath)
            if current_mtime != last_modified[filepath]:
                print(f"📝 Detected change in: {filepath}")
                last_modified[filepath] = current_mtime
                generate_chart()
                break

def start_server(port=8000):
    """Start HTTP server in a separate thread."""
    class QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            # Only log errors, not every request
            if args[1] != '200':
                super().log_message(format, *args)

    server = HTTPServer(('', port), QuietHTTPRequestHandler)

    def serve():
        print(f"🌐 Server running at http://localhost:{port}/benchmark_chart.html")
        print("   Press Ctrl+C to stop\n")
        server.serve_forever()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()

if __name__ == "__main__":
    try:
        start_server(8000)
        watch_files()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        sys.exit(0)
