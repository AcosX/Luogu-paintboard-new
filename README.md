# Luogu-paintboard-new

洛谷冬日绘板脚本，采用Token进行绘制。

## 准备

- GIMP
- Python3 (需安装requests和pillow库)

## 使用方法

1. 将图片转为绘板可用的颜色
   > 引用自 [ouuan/LuoguPaintBoard](https://github.com/ouuan/LuoguPaintBoard)
   1. 将 `LuoguPaintBoard.gpl` 复制到 `GIMP安装路径\share\gimp\2.0\palettes`。
   2. 用 GIMP 打开原始图片。
   3. 图像 → 缩放图像。
   4. 图像 → 模式 → 索引，Use custom palette：LuoguPaintBoard，**不要** 勾选“从颜色表中移除无用和重复的颜色”。“递色”选项可以自己试试看哪种效果比较好。
   5. 文件 → 导出为 → 选一个路径 → 选择文件类型：**bmp** → 导出
   
   2.将图片转为JSON列表（转换方法源自ouuan的脚本）
   
   在data文件夹下执行
   
   `python ImageToData.py 图片路径 左上角X坐标 左上角Y坐标`
   
   依次对每张图片运行（此脚本为增量更新），完成后可通过 preview.html 查看效果。
   
   3.修改tokens.json文件中列表内容为自己的token。
   
   4.运行main.py。
   
   `python main.py`
   
   <br/>

   
