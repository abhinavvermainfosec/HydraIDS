# 🛡️ HydraIDS

> A modular Python-based Intrusion Detection System (IDS) that captures live network traffic and detects suspicious activity through real-time packet analysis.

HydraIDS is an open-source IDS built from scratch using Python and Scapy. It is designed with a modular architecture, making it easy to add new detection modules while maintaining clean and scalable code.

---

## ✨ Features

- Live packet capture
- TCP, UDP and ICMP packet parsing
- TCP SYN Port Scan Detection
- Modular detection engine
- Centralized alert management
- Alert logging
- Configurable debug mode
- Rich CLI interface

---

## 🏗️ Architecture

```text
                 ┌─────────────────┐
                 │ Packet Capture  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Packet Parser   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Detection Engine│
                 └────────┬────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
 ┌─────────────────┐             ┌─────────────────┐
 │ Port Scan       │             │ Future Modules  │
 │ Detection       │             │ (SYN, UDP, ...) │
 └────────┬────────┘             └────────┬────────┘
          └───────────────┬───────────────┘
                          ▼
                 ┌─────────────────┐
                 │ Alert Manager   │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ Logger          │
                 └─────────────────┘
```

---

## 📦 Project Structure

```text
HydraIDS/
│
├── core/
│   ├── alerts.py
│   ├── capture.py
│   ├── detector.py
│   ├── interface.py
│   ├── logger.py
│   └── parser.py
│
├── detections/
│   ├── __init__.py
│   └── port_scan.py
│
├── logs/
├── utils/
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/abhinavvermainfosec/HydraIDS.git
cd HydraIDS
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run HydraIDS:

```bash
sudo .venv/bin/python main.py
```

Run in debug mode:

```bash
sudo .venv/bin/python main.py --debug
```

---

## 📸 Preview

<p align="center">
<img width="450" alt="HydraIDS" src="https://github.com/user-attachments/assets/b110aed5-e22a-470e-b377-8be7410811d5">
</p>

---

## ✅ Current Capabilities

- [x] Live packet capture
- [x] TCP packet parsing
- [x] UDP packet parsing
- [x] ICMP packet parsing
- [x] TCP SYN Port Scan Detection
- [x] Modular detection engine
- [x] Alert manager
- [x] Alert logging
- [x] Configurable debug mode

---

## 🚧 Roadmap

- [ ] TCP SYN Flood Detection
- [ ] UDP Scan Detection
- [ ] FIN Scan Detection
- [ ] NULL Scan Detection
- [ ] XMAS Scan Detection
- [ ] ICMP Flood Detection
- [ ] ARP Spoof Detection
- [ ] Dynamic detector loading
- [ ] Statistics dashboard
- [ ] YAML configuration support

---

## 📄 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

HydraIDS is intended for educational purposes and authorized defensive security testing only. Always obtain permission before monitoring or testing networks that you do not own or administer.

---

## 🤝 Contributing

Contributions, bug reports, feature requests, and pull requests are welcome.

If you have ideas for new detection modules or improvements, feel free to open an issue or submit a pull request.