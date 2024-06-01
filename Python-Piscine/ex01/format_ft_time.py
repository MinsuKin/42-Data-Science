import time
from datetime import datetime

current_time = time.time()

formatted_time = f"{current_time:.4f}"
scientific_time = f"{current_time:.2e}"

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_time} or {scientific_time} in scientific notation")
print(current_date)