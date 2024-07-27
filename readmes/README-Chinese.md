# chainsaw-human-typing

欢迎来到 chainsaw-human-typing 仓库！Chainsaw Human Typing 是一种工具，允许你在键盘上模拟人类输入（如果你不想或不能的话）。例如，这对于模拟视频中的人类打字非常有用。

## 快速上手 🚀

只需从 [releases](https://github.com/LyubomirT/chainsaw-human-typing/releases) 页面下载一个二进制文件并运行它。你也可以通过克隆存储库并运行`python main.py`来自己构建它。

## 用法 🛠

实际上，非常简单，只需在输入字段中输入你想要模拟输入的文本，然后按“开始打字”按钮。文本将在下面的输出字段中输出出来。你可以在进度条中看到进度。

## 从源代码运行 🏗

要从源代码运行项目，你需要安装 Python 3.6 或更高版本。你还必须通过运行`pip install -r requirements.txt`来安装依赖项。之后，你可以通过运行`python main.py`来运行项目。

要构建项目，你可以使用 PyInstaller。 `build.ps1`是一个 PowerShell 脚本，用于使用 PyInstaller 生成项目。你可以通过运行`.\build.ps1`来运行它。输出将位于“dist”文件夹中，请注意，该脚本配置为构建 Windows 可执行文件，并且你需要安装 PyInstaller。
## 贡献 🤝
如果你想为这个项目做出贡献，可以大方的fork并提交一个pr。我很乐意审阅，如果你有任何issue，请随时open一个。有关更多信息，请查看[CONTRIBUTING](CONTRIBUTING.md)文件。

## 许可证 📝

此项目遵从 GPL-3.0 许可 - 查看 [LICENSE](LICENSE) 文件获得更多信息

## 使用的项目 🙏

- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyInstaller](https://pypi.org/project/pyinstaller/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
