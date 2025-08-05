# 💼 Wuzzuf Job Listings Scraper

This project is a web scraper built with **Python**, **BeautifulSoup**, and **Requests**, designed to collect real-time job listings from [Wuzzuf.com](https://wuzzuf.net), one of Egypt's leading job portals.

## 📌 Summary

- ✅ **Jobs Scraped:** 931  
- 📄 **Pages Scraped:** 64  
- 📁 **Output Format:** Excel (XLSX)  
- 🧰 **Tools Used:** Python, BeautifulSoup, Requests, OpenPyXL

---

## ⚙️ Features

- 🔄 Automatically loops through paginated job listing pages
- 🧠 Extracts:
  - Job Title
  - Company Name
  - Location
  - Occupation/Category
- ❗ Handles missing or incomplete job data
- 📤 Saves clean, structured data in `wuzzuf_jobs.xlsx`
- 🧹 Demonstrates data cleaning and organization best practices

---

## 🧰 Tech Stack

- Python 3.x
- BeautifulSoup4
- Requests
- openpyxl (for writing to Excel)

---

## ▶️ How to Run

1. **Install dependencies**
```bash
pip install requests beautifulsoup4 openpyxl
```

2. Run the script
```bash
python wuzzuf_scraper.py
```


3.Output
The file wuzzuf_jobs.xlsx will be created in the project folder.



📚 Use Cases

Job market analysis and trends

Salary research by title and location

Resume/job alert tools

Data science practice with real job data

⚠️ Disclaimer

This project is for educational and personal use only.
Please respect the terms of service and robots.txt of Wuzzuf.com.
Use scraping responsibly and avoid overloading any server.

🤝 Author
Ali Ahmed
GitHub Profile
