# ProductHunt Hunter 🏹

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Product Hunt API](https://img.shields.io/badge/API-Product%20Hunt%20V2-orange.svg)](https://api.producthunt.com/v2/docs)

**ProductHunt Hunter** is a lightweight, efficient Python utility designed to track and discover the top-voted products on Product Hunt. Leveraging the **Product Hunt API V2 (GraphQL)**, it provides real-time insights into what's trending in the tech ecosystem.

---

## ✨ Features

- 🚀 **Real-time Discovery**: Fetch the top 20 trending apps instantly.
- 📊 **Rich Metadata**: Get votes, taglines, topics, and direct links for every product.
- 🔐 **Secure Configuration**: Uses `.env` for safe management of Developer Tokens.
- ⚡ **Smart Caching**: Local file-based caching (24-hour expiry) to improve performance and respect API rate limits.
- 🛠️ **Modern Stack**: Built with Python 3, GraphQL, and `python-dotenv`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **API:** Product Hunt V2 (GraphQL)
- **Libraries:** `requests`, `python-dotenv`

---

## 🚀 Getting Started

### Prerequisites

- A [Product Hunt Developer Token](https://www.producthunt.com/v2/developer)
- Python 3.8 or higher installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishandutta2007/producthunt-hunter.git
   cd producthunt-hunter
   ```

2. **Install dependencies:**
   ```bash
   pip install requests python-dotenv
   ```

3. **Configure Environment Variables:**
   Duplicate the example environment file and add your credentials:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and insert your `ACCESS_TOKEN`:
   ```env
   ACCESS_TOKEN=your_actual_token_here
   ```

---

## 📖 Usage

Run the hunter script to fetch the latest trending products:

```bash
python fetch_trending.py
```

### Example Output

```text
--- Top 20 Trending Apps on Product Hunt ---

1. Fundraisly (▲ 1093 votes)
   Tagline: AI fundraising agent that finds investors and books meetings
   Topics:  Venture Capital, Artificial Intelligence, Fundraising
   Link:    https://www.producthunt.com/products/fundraisly
--------------------------------------------------
```

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

Project Link: [https://github.com/ishandutta2007/producthunt-hunter](https://github.com/ishandutta2007/producthunt-hunter)

---


## 📈 Star History

<div align="center">
   <a href="https://www.star-history.com/?repos=ishandutta2007%2FProducthunt-Hunter&type=date&legend=bottom-right">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Producthunt-Hunter&type=date&theme=dark&legend=bottom-right" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Producthunt-Hunter&type=date&legend=bottom-right" />
      <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Producthunt-Hunter&type=date&legend=bottom-right" />
    </picture>
   </a>
</div>

---

*Developed with ❤️ for the maker community.*
