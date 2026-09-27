# 🔡 Wordlist-Tool

A fast, interactive Python CLI tool for generating targeted, pattern-based wordlists for security assessments, pentesting, OSINT, and password auditing.

Unlike heavy, complex rule-based engines like John the Ripper or Hashcat rules, **Wordlist-Tool** focuses on rapid, targeted dictionary generation: enter keywords with OR-patterns, configure depth and separators, preview sample outputs in real-time, and generate millions of combinations in seconds.

---
<img width="1239" height="694" alt="image" src="https://github.com/user-attachments/assets/3a058489-c71c-450b-923b-d720e53a8c15" />

---

## ⚡ Highlights & Key Advantages

* **Interactive Live Preview**: Preview sample combinations and view total combination counts *before* writing to disk.
* **On-the-Fly Tweaking**: Don't like the format or separator? Tweak your settings instantly without starting over.
* **High Throughput (~3,000,000+ words/sec)**: Buffered streaming I/O generates massive wordlists with minimal CPU and memory overhead.
* **Zero Dependencies**: Pure standard-library Python (requires Python 3.8+).
* **Cross-Platform**: Works smoothly on Windows (PowerShell/CMD), Linux, and macOS.

---

## 🥊 Wordlist-Tool vs. John the Ripper / Hashcat Rules

| Feature | Wordlist-Tool | John the Ripper (`john`) |
| :--- | :--- | :--- |
| **Primary Use Case** | Targeted, contextual OSINT & custom wordlists | Massive cracking & rule mutation |
| **Setup & Dependencies** | Pure Python, `pip install wordlist-tool`, no compile | C / GCC / OpenCL / GPU drivers |
| **Configuration** | Interactive prompts with instant preview | Complex rule syntax (`[List.Rules:...]`) |
| **Feedback Loop** | Shows sample preview & total count before running | Generates blindly based on rule file |
| **Disk Efficiency** | Streamed directly with 1MB write buffer | Rule-driven pipe / stdout |

---

## 📦 Installation

From PyPI:

```bash
pip install wordlist-tool
```

From source:

```bash
git clone https://github.com/RMNO21/wordlist-tool.git
cd wordlist-tool
pip install .
```

---

## 🚀 Usage

Run the tool from your terminal:

```bash
wordlist-tool
```

### Interactive Workflow

1. **Enter target keywords / patterns**: Enter base words, using commas `,` for OR-options (e.g. `admin,root` or `2024,2025,2026`). Press Enter on a blank line or type `done`.
2. **Set loop / depth level**: Specify permutation depth.
3. **Choose separator**: Add characters like `@`, `_`, `-`, or leave empty.
4. **Review & Tweak**: Check the live sample preview and total estimated combinations. Confirm (`Y`), tweak (`T`), or cancel (`N`).
5. **Output**: Specify destination file (default: `wordlist.txt`).

### Example Run

```text
Enter target keywords / patterns (use ',' for OR options, e.g. 'admin,user')
[1]: admin,root
[2]: 2025,2026
[3]: pass,secret
[4]: 

=======================================================
 [*] SETTINGS & SAMPLE PREVIEW
=======================================================
  * Loop Depth     : 2
  * Separator      : '@'
  * Estimated Words: 24 combinations
  * Sample Output  :
     1. admin
     2. root
     3. 2025
     4. 2026
     5. pass
     6. secret
     ... (18 more)
=======================================================
Proceed to generate? [Y = Yes / T = Tweak settings / N = Cancel]: y

Enter output filename (e.g. wordlist.txt): wordlist.txt

[+] Generating 24 words...
[OK] Success! Generated 24 words in 0.001s (24,000 words/sec).
[OK] Saved to: wordlist.txt
```

---

## 🛠 Development

```bash
git clone https://github.com/RMNO21/wordlist-tool.git
cd wordlist-tool
pip install -e .
```

---

## 📜 License

This project is licensed under the **GNU General Public License v2.0 or later**.  
See the [LICENSE](LICENSE) file for details.
