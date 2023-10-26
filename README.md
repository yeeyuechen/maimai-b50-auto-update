# maimai-b50-auto-update
基于Python的舞萌DX b50无人值守更新脚本

在你使用之前，请仔细阅读本文

！注意：在运行该脚本之前，需要配置环境（建议Python 3.7以上）

该程序还使用了`pyautogui`，在运行之前需要在终端吗内输入

    pip install pyautogui

如果你是Windows环境，那么可以直接打开`start.bat`脚本启动程序

针对水鱼查分器，脚本初次运行时，查分器核心会在你的`脚本目录`生成三个文件，就像一开始单独配置水鱼查分器一样

![例图](https://i0.imgs.ovh/2023/10/26/Fsaco.png "例图")

- cert.crt  --需要安装的证书文件
- config.json  --在此文件内填写查分器平台的账户名与密码
- key.pem  --pem密钥，无需操作

需要配置cert证书和填写config才能够正常使用

可参考 https://www.diving-fish.com/maimaidx/prober_guide 文档对以上三个文件进行配置

配置完上述文件后，你可以选择任意一个核心对成绩进行上传

本项目的原理是通过Python的`pyautogui`模块调用鼠标进行移动从而打开舞萌游戏记录页面

如果你的环境是Linux或其他那么可能要对`index.py`文件稍作更改

我不能确保在Linux及其他操作系统上能不能正常运行我写的这个玩意因为我没试过，而且你要在Linux上跑这玩意的话应该需要X11之类的东西，这些就另说了233

我都作这么多说明了，如果你还不会那就只能证明~~你是个白痴~~（并不