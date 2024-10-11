# 🎯 **Chainsaw Human Typing**

Welcome to the **Chainsaw Human Typing** repository! This tool simulates **human-like typing** on a keyboard when you can’t, or don’t want to, paste directly. It's especially useful for simulating human typing in a video!

---

<div align="center">

💻 **Getting Started** 🚀

</div>

| Supported OS | Build Status |
|--------------|--------------|
| Windows      | Since 1.0.0  |
| Linux        | Since 1.5.0  |
| MacOS        | Not yet*     |
| FreeBSD      | Not yet      |

Download one of the binaries from the [releases page](https://github.com/LyubomirT/chainsaw-human-typing/releases) or build it yourself by cloning the repository and running:

```bash
python main.py
```

*The app technically should work on MacOS, but we don't have any pre-built binaries for it yet.

---

<div align="center">

⚙️ **Usage** 🛠

</div>

It’s very **simple** to use! Input the text you want to simulate, then hit **"Start Typing"**. Your text will appear in the lower input field as it's typed out, with a **progress bar** to monitor the process.

---

<div align="center">

📝 **Capabilities** ⌨️

Chainsaw Human Typing allows for several tweaks to be made about how the typing is done. Users can choose the:
    <ul>
    <li>Delay until typing starts</li>
    <li>Interval</li>
    <li>Chars per stroke</li>
    <li>Mistake Percentage</li>
    </ul>
along with being able to randomize the interval and choose whether enter is typed all in a GUI. 
Users are also able to create different presets that save their typing settings. Current preset settings allow for unlimited presets to be created and for presets to be renamed or deleted.


---

<div align="center">

🏗 **Run from Source**

</div>

Ensure you have **Python 3.6+** installed. Install the dependencies:

```bash
pip install -r requirements.txt
```

Navigate to the `src` folder and run:

```bash
python main.py
```

To **build** the project, use **PyInstaller**. The `build.ps1` script automates this for **Windows**:

```bash
.\build.ps1
```

The output will be in the `dist` folder.

---

<div align="center">

🤝 **Contributing**

</div>

Feel free to fork this project and submit a **pull request**. I’d be more than happy to review your contributions. If you have any questions, open an **issue**!

See the [CONTRIBUTING](CONTRIBUTING.md) file for more details.

---

<div align="center">

📝 **License**

</div>

This project is licensed under **GPL-3.0**. See the [LICENSE](LICENSE) file for more information.

---

<div align="center">

🎌 **Translations Available**

</div>

- 中文/Chinese README: [README-ZHCN](https://github.com/LyubomirT/chainsaw-human-typing/blob/main/readmes/README-Chinese.md)
- Norwegian README: [README-NO](https://github.com/LyubomirT/chainsaw-human-typing/blob/main/readmes/README-Norwegian.md)
- Turkish README: [README-TR](https://github.com/LyubomirT/chainsaw-human-typing/blob/main/readmes/README-Turkish.md)

---

<div align="center">

🙏 **Acknowledgements**

</div>

- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyInstaller](https://pypi.org/project/pyinstaller/)
- [PyNput](https://pypi.org/project/pynput/)