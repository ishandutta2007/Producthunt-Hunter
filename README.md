<p align="center">
  <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDgwMCAyMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMDAiIHJ4PSIxMCIgZmlsbD0iI0RBNTUyRiIvPgogIDxwYXRoIGQ9Ik00MDAgNDBMNDIwIDgwSDM4MEw0MDAgNDBaIiBmaWxsPSJ3aGl0ZSIgb3BhY2l0eT0iMC4zIi8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMTUwIiByPSI1MCIgZmlsbD0id2hpdGUiIG9wYWNpdHk9IjAuMSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjUwIiByPSIzMCIgZmlsbD0id2hpdGUiIG9wYWNpdHk9IjAuMSIvPgogIAogIDx0ZXh0IHg9IjQwMCIgeT0iMTAwIiBmb250LWZhbWlseT0iQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNDgiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UFJPRFVDVEhVTlQgSFVOVEVSPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMTQwIiBmb250LWZhbWlseT0iQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IndoaXRlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBvcGFjaXR5PSIwLjkiPvCfj7kgVHJhY2ssIERpc2NvdmVyICYgQW5hbHl6ZSBUcmVuZGluZyBQcm9kdWN0cyBBdXRvbWFnaWNhbGx5PC90ZXh0PgogIAogIDxwYXRoIGQ9Ik00MCAxNjBMNjAgMTgwTDQwIDIwMCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSI0IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIG9wYWNpdHk9IjAuNSIvPgogIDxwYXRoIGQ9Ik03NjAgMTYMEw3NDAgMTgwTDc2MCAyMDAiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iNCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBvcGFjaXR5PSIwLjUiLz4KPC9zdmc+" alt="ProductHunt Hunter Banner" width="800">
</p>

# ProductHunt Hunter 🏹

<p align="center">
  <strong>The ultimate tool to track, discover, and analyze trending products on Product Hunt.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://api.producthunt.com/v2/docs"><img src="https://img.shields.io/badge/API-Product%20Hunt%20V2-orange.svg" alt="Product Hunt API"></a>
  <a href="https://graphql.org/"><img src="https://img.shields.io/badge/Query-GraphQL-e10098.svg" alt="GraphQL"></a>
  <a href="https://github.com/ishandutta2007">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow&style=for-the-badge&logo=github&logoColor=white"/>
  </a>

</p>

---

## 🌟 Overview

**ProductHunt Hunter** is a powerful Python-based automation tool designed for makers, marketers, and researchers. It seamlessly interfaces with the **Product Hunt API V2** via **GraphQL** to fetch real-time trending data, analyze product topics, and find similar alternatives using **SaaSHub**.

Whether you're doing market research, looking for inspiration, or tracking competitors, ProductHunt Hunter automates the discovery process and stores it all in an easy-to-use CSV format.

---

## ✨ Key Features

- 🚀 **Real-time Trending Discovery**: Automatically fetch the top 20 trending products.
- 🔍 **Deep Insights**: Extract votes, taglines, detailed topics, and direct links.
- 🤖 **Smart Competitor Analysis**: Automatically finds similar products using SaaSHub and PH Topics.
- 💾 **Automated Data Export**: Saves new discoveries to `products.csv` for easy analysis in Excel/Sheets.
- ⚡ **Performance Optimized**: Local file-based caching (24h) to respect API rate limits and speed up repeated runs.
- 🔐 **Secure by Design**: Fully configurable via `.env` variables.

---

## 🛠️ Tech Stack

- **Core:** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) 3.8+
- **API Architecture:** ![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white)
- **Data Source:** ![Product Hunt](https://img.shields.io/badge/Product%20Hunt-DA552F?style=flat-square&logo=product-hunt&logoColor=white)
- **Intelligence:** ![SaaSHub](https://img.shields.io/badge/SaaSHub-Blue?style=flat-square) (Optional)

---

## 🚀 Getting Started

### 📋 Prerequisites

- [Product Hunt Developer Token](https://www.producthunt.com/v2/developer)
- Python 3.8+ installed on your system.

### ⚙️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/ishandutta2007/producthunt-hunter.git
   cd producthunt-hunter
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   # Or manually: pip install requests python-dotenv
   ```

3. **Setup Environment:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your credentials:
   ```env
   ACCESS_TOKEN=your_ph_token_here
   SAASHUB_API_KEY=your_saashub_key_here (optional)
   ```

---

## 📖 Usage

Run the hunter with a single command:

```bash
python fetch_trending.py
```

### 📸 Demo / Example Output

*(Imagine a cool GIF of the CLI running here!)*
<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHIzZ3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z/l41lTfNfR6Z0BfO08/giphy.gif" alt="Searching GIF" width="400">
</div>

```text
--- Fetching fresh data from Product Hunt API ---

1. AI Coder (▲ 1250 votes)
   Tagline: Build apps with natural language
   Topics:  AI, Developer Tools, Software
   Link:    https://www.producthunt.com/products/ai-coder
   Searching for similar products...
   ✅ Appended AI Coder to products.csv
--------------------------------------------------
```

---

## 🗺️ Roadmap

- [ ] Support for fetching top products by specific topics.
- [ ] Email notifications for new trending apps.
- [ ] Weekly summary report generation (PDF/HTML).
- [ ] Integration with Slack/Discord webhooks.

---

## 🤝 Contributing

We love contributions! Whether it's a bug report, a feature request, or a pull request, you are welcome to help make **ProductHunt Hunter** better.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact & Support

**Ishan Dutta** - [GitHub](https://github.com/ishandutta2007)

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

<div align="center">
  <sub>Developed with ❤️ for the maker community.</sub>
</div>
