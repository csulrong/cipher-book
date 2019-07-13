# 深入浅出密码技术

## 准备编译环境

### 安装TeX

MacBook操作系统上，下载并安装[MacTeX 2019](https://www.tug.org/mactex/)。

```
  TEXDIR (the main TeX directory):
     /usr/local/texlive/2019
   TEXMFLOCAL (directory for site-wide local files):
     /usr/local/texlive/texmf-local
   TEXMFSYSVAR (directory for variable and automatically generated data):
     /usr/local/texlive/2019/texmf-var
   TEXMFSYSCONFIG (directory for local config):
     /usr/local/texlive/2019/texmf-config
   TEXMFVAR (personal directory for variable and automatically generated data):
     ~/.texlive2019/texmf-var
   TEXMFCONFIG (personal directory for local config):
     ~/.texlive2019/texmf-config
   TEXMFHOME (directory for user-specific files):
     ~/texmf
```

### 配置中文字体

本书所使用的中文字体基于zhfonts包。

```
git clone git://github.com/liyanrui/zhfonts
```

然后，将下载的zhfonts文件夹拷贝到下面的目录下：

```
cp -rf zhfonts /usr/local/texlive/2019/texmf-dist/tex/context/third/
```

最后，使用如下命令更新库文件

```
luatools -generate
```

这样，就完成了zhfonts包的安装。

### 字体文件

## 编译



