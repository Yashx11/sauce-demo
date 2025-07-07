# 🧪 SauceDemo - Selenium Pytest Automation Framework

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium)]
[![Pytest](https://img.shields.io/badge/Pytest-TestRunner-yellow?logo=pytest)]
[![Allure](https://img.shields.io/badge/Allure-Report-ff69b4?logo=allure)]

This is a Page Object Model (POM) based **Selenium automation framework** for UI testing of [SauceDemo](https://www.saucedemo.com/). Built with **Python + Pytest**, integrated with **Allure Reports**, **screenshot capture on failure**, **data-driven testing**, and structured for real-world CI/CD usage.

---

## 🔧 Features

- ✅ **Page Object Model (POM)** Design Pattern
- ✅ **Pytest** as Test Runner
- ✅ **Cross-browser support** (Chrome, Firefox, Edge)
- ✅ **Configuration-driven** with `.ini` file
- ✅ **Automatic screenshots** on test failure
- ✅ **Allure Report Integration**
- ✅ **Data-Driven Testing** with Excel / JSON
- ✅ **Modular directory structure**
- ✅ CI/CD Ready (GitHub Actions / Jenkins)

---

## 📁 Project Structure

```
sauce-demo/
├── configurations/
│   └── config.ini
├── logs/
│   └── test_log.log
├── pages/
│   ├── BasePage.py
│   ├── LoginPage.py
│   ├── HomePage.py
│   └── ...
├── testcase/
│   ├── test_login.py
│   ├── test_home.py
│   ├── conftest.py
│   └── ...
├── utilities/
│   ├── readproperties.py
│   ├── excel_reader.py
│   └── ...
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🚀 Getting Started

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/Yashx11/sauce-demo.git
cd sauce-demo
```

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Required: Python 3.9+ and ChromeDriver/GeckoDriver in your PATH

---

### 🔹 3. Configure Browser

Update browser in `configurations/config.ini`:
```ini
[Basic Info]
browser = chrome
```

---

## 🧪 Run Tests

```bash
pytest
```

### 🧪 Run with Allure Report
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🖼 Screenshot on Failure

On any test failure, a screenshot is automatically captured and:
- Saved in the `/screenshots/` folder
- Attached inside the Allure Report

---

## 📊 Allure Report Sample

- Shows pass/fail summary
- Test case titles, steps, and descriptions
- Screenshot, exception & stacktrace on failure
- Filter by severity, suite, tags

---

## 📂 Data-Driven Testing Support

Supported via:
- **Excel** (`openpyxl`)
- **JSON** files

Utility methods available in `utilities/`.

---

## 🔐 Future Enhancements

- 🔁 Retry mechanism on flaky failures
- ⛓️ GitHub Actions Integration
- 📩 Email reports post-run
- 🌐 Cross-browser cloud execution (e.g., BrowserStack/SauceLabs)

---

## 🤝 Contributing

If you’d like to contribute or extend this, feel free to fork and raise a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

**Yash Mali**  
🔗 [LinkedIn](https://www.linkedin.com/in/Yashx11)  
📧 yashx11@example.com (replace with your email if public)