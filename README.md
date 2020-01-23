# GPA Calculator 

登录 info.tsinghua.edu.cn 打开中文成绩单，ctrl+s保存html，默认命名为 `清华大学学生课程学习记录表.html`，将它放在当前目录下。参考工程目录结构如下：

```
GPA-Calculator/
├── main.py
├── README.md
└── 清华大学学生课程学习记录表.html
```

计算改革前后的GPA，并未考虑F的情况。

```bash
python main.py --path 清华大学学生课程学习记录表.html
```
