# 🔡 Wordlist-Tool

A flexible Python CLI tool for generating wordlists from user‑defined inputs.  
It supports **permutations, product combinations, separators, and OR‑options**, making it useful for automation, security research, or custom scripting.

---

## 📦 Installation

From PyPI:

```bash
pip install wordlist-tool
```

From source:

Linux:

```bash
git clone https://github.com/RMNO21/wordlist-tool.git
cd wordlist-tool
pip install .
```
Windows:

```bash
git clone https://github.com/RMNO21/wordlist-tool.git
cd wordlist-tool
python -m venv venv 
source venv/bin/activate
pip install .
```

---

## 🚀 Usage

After installation, run:

```bash
wordlist-tool
```

The tool will:

1. Ask you to enter possible words (you can use `,` for OR options).  
2. Let you specify the loop number (between 1 and 10).  
3. Ask for a separator (optional).  
4. Generate all permutations and product combinations.

### Example Run

```text
1: admin,user
2: pass,1234
3: done
enter the loop number: 2
enter the separator: @
```

Output:

```
admin@pass
admin@1234
user@pass
user@1234
...
```

---

## ⚙️ Features

- Accepts multiple word inputs with OR options (`word1,word2`)  
- Generates permutations up to user‑defined loop count  
- Supports custom separators (`@`, `$`, `&`, etc.)  
- Prints results directly to stdout (redirect to file if needed)  

---

## 🛠 Development

Editable install for development:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

---

## 📜 License

This project is licensed under the **GNU General Public License v2.0 or later**.  
See the [LICENSE](LICENSE) file for details.
```
