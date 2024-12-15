import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
import os
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Create the plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, label='Linear Growth', color='blue', linestyle='--', marker='o')
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()

# Save the plot as an image
plot_filename = "line_plot.png"
plt.savefig(plot_filename)
plt.close()

# Serve the plot using a local HTTP server
PORT = 8000
os.chdir(os.path.dirname(os.path.abspath('line_plot.png')))

with TCPServer(("localhost", PORT), SimpleHTTPRequestHandler) as httpd:
    # Automatically open the plot in the browser
    url = f"http://localhost:{PORT}/{plot_filename}"
    webbrowser.open(url)
    print(f"Serving {plot_filename} at {url}")
    httpd.serve_forever()
