import requests
g = requests.get("https://docs.google.com/forms/d/e/1FAIpQLScipsmYg7XxaWYBlAM9jxrH8ywmDDgzH-Bs8Q9RCVycagEqIg/viewform?usp=sf_link")
print(g.text)
