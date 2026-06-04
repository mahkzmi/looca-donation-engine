markdown
# 🐾 Looca | Transparent Donation Platform for Animal Shelters

**For Looca. Forever free. For every creature without a voice.**

Looca is an open-source, completely free donation platform that helps animal shelters collect public contributions to save more lives.

---

## ✨ Why Looca?

- 🆓 **Forever Free** – Shelters will never be charged
- 🔓 **Open Source** – Full code on GitHub under GPL v3 license
- 🎯 **Transparent** – Every donor receives a unique tracking code
- 🐱 **Dedicated to Looca** – My cat, who taught me that love without action is just a feeling

---

## 🚀 Current Features

- [x] Shelter registration and management
- [x] Create donation campaigns with financial goals
- [x] Real-time campaign progress percentage
- [x] Donation form with unique tracking code generation
- [x] Post-donation tracking page
- [x] Full admin panel for management

## 🔜 Coming Soon

- [ ] ZarinPal payment gateway integration
- [ ] Telegram notifications for shelters after each donation
- [ ] Dedicated shelter dashboard
- [ ] Excel export of transactions
- [ ] Public transparency report page
- [ ] Cloud deployment

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Database:** SQLite (upgradable to PostgreSQL)
- **Frontend:** Django Templates + HTML/CSS
- **Payment:** ZarinPal (in progress)
- **Version Control:** Git & GitHub

---

## 📦 Local Development Setup

```bash
# Clone the project
git clone https://github.com/mahkzmi/looca-donation-engine.git
cd looca-donation-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
Then visit http://127.0.0.1:8000/admin and log in.

📁 Project Structure
text
looca-donation-engine/
├── looca/          # Project settings
├── shelters/       # Shelter management
├── campaigns/      # Campaign management
├── payments/       # Transactions & payments
├── templates/      # HTML templates
└── manage.py
🤝 How to Contribute
⭐ Star the project

🐛 Report bugs

💡 Share ideas

🔧 Submit Pull Requests

📢 Share the project with shelters

📜 License
GNU General Public License v3.0

This project will never become commercial or paid. No one may use Looca's code to build a closed-source or paid product.

💝 Dedicated to
Looca – My cat, who reminds me every day that even the smallest act of kindness can change a creature's world.

And to every cat and animal still waiting for a second chance.

📬 Contact
Built with love by a backend developer for their own heart.

GitHub Repository

<p align="center"> <img src="https://img.shields.io/badge/forever-free-brightgreen" alt="forever free"> <img src="https://img.shields.io/badge/license-GPLv3-blue" alt="license"> <img src="https://img.shields.io/badge/made%20with-%E2%9D%A4%20for%20Looca-red" alt="made with love"> </p> ```
