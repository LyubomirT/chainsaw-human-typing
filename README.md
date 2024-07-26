# chainsaw-human-typing

⌨️ Chainsaw Human Typing 是一个允许你在键盘上模拟人类打字的工具，如果你不想或不能直接粘贴 ，这对于模拟人类在视频中打字很有用

## 快速上手 🚀

简单！从这个release页面里下载 [releases](https://github.com/LyubomirT/chainsaw-human-typing/releases) 然后运行即可. 你也可以通过克隆git仓库和运行 `python main.py`自行构建

## 用法 🛠

其实很简单的, 实际上! 只需要把你想模拟打字的文字输入进“输入”框然后点 "开始打字" 按钮. 文字会直接输出在输出框里. 你可以进度条内看到进度

## 从源文件运行 🏗

要从源文件运行, 你需要安装 Python 3.6 或更高版本. 你还需要通过运行 `pip install -r requirements.txt`安装依赖。 之后，你可以通过运行 `python main.py`来运行

要构建项目，你可以使用PyInstaller， `build.ps1` 是一个通过PyInstaller构建项目的PowerShell脚本。 你可以用如下命令运行脚本： `.\build.ps1`. 输出会在 `dist` 文件夹, 注意脚本会构建Windows可执行文件【.exe】且依赖PyInstaller

## 贡献 🤝

如果你想为项目做贡献, 大方的fork它然后提交pr. 我会很高兴去审阅的! 如果你有任何疑问, 大方的提交一个issue。 请查看 [CONTRIBUTING](CONTRIBUTING.md) 文件获得更多内容

## 执照 📝

此项目遵从GPL-3.0 执照 - 查看 [LICENSE](LICENSE) 文件获得更多细节.

## 基于 🙏

- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyInstaller](https://pypi.org/project/pyinstaller/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
