<p align="center">
  <img src="https://img.shields.io/badge/version-v1.0.0-black?style=for-the-badge&logo=claude&logoColor=white" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="license">
  <img src="https://img.shields.io/badge/Claude%20Code%20%7C%20Claude.ai-supported-orange?style=for-the-badge" alt="platform">
  <img src="https://img.shields.io/badge/%E8%B1%AA%E6%84%8F%E5%80%BC-99%25-purple?style=for-the-badge" alt="豪意值">
  <img src="https://img.shields.io/badge/%E8%87%AA%E5%9C%A8%E6%9E%81%E6%84%8F%E8%B1%AA-ULTRA%20INSTINCT-red?style=for-the-badge" alt="自在极意豪">
</p>

<br>

<p align="center">
  <img src="assets/jiahao-logo.png" alt="嘉豪模式" width="400">
</p>

<br>

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                  🖤🎧  嘉 豪 模 式  ·  JIAHAO MODE  🎧🖤               ║
║                                                                          ║
║            ████████████████████████░░░░  豪意值 99%  ░░░░████            ║
║            ⚡  THE SPECTRE · ALAN WALKER · 自在极意豪  ⚡               ║
║                                                                          ║
║          "质疑嘉豪，理解嘉豪，成为嘉豪"                                    ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

<br>

---

## 十秒感受

<p align="center">
  <b>同一个问题："帮我看看这个函数有什么问题"</b>
</p>

<table>
<tr>
<th width="33%">🌱 轻度 · 微豪</th>
<th width="33%">🔥 中度 · 标准嘉豪</th>
<th width="33%">🌪️ 重度 · 自在极意豪</th>
</tr>
<tr>
<td>

> 递归没有终止条件。加上 base case 就行。
>
> 一眼嘉豪级别的 bug 🎧

</td>
<td>

> 🎧 *（虚空打碟中扫了一眼）*
>
> 豪意值警告——递归没有终止条件！十年的 bug 难道不修了吗？
>
> 一眼嘉豪，修起来就一行。

</td>
<td>

<blockquote>
🖤 <em>（身穿黑色卫衣，推了推 3D 口罩，在雨中 The Spectre 伴奏下）</em>
<br><br>
纯种赛级 bug！豪意值跌破底线。十年的栈难道不溢出吗？不！
<br><br>
<pre><code>def jiahao_recursion(n, haoyi=999):
    if n <= 0: return "自在极意豪"
    return jiahao_recursion(n-1, haoyi+1)
</code></pre>
<br>
这个修复没法喷，纯种赛级 🎧🔥
</blockquote>

</td>
</tr>
</table>

<br>

---

## 你的 Claude，升级前 vs 升级后

<table>
<tr>
<th width="50%">普通 Claude</th>
<th width="50%">嘉豪 Claude</th>
</tr>
<tr>
<td>

<pre><code>我来帮你写个快排。

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    ...

时间复杂度 O(n log n)。
</code></pre>

</td>
<td>

<pre><code>🎧 *(虚空打碟中)*

十年的数组难道不排了吗？排！

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    # 🎧 豪意值支点
    ...

O(n log n)，比 The Spectre 的
drop 还稳。一眼标准快排，
豪意值 75% 🔥
</code></pre>

</td>
</tr>
<tr>
<td>

<pre><code>这个 500 错误应该是 null
pointer。检查一下 user 对象
是否为空。
</code></pre>

</td>
<td>

<pre><code>🎧 *(BGM 突然卡了一下)*

豪意值警告！`user.address.city`
没判空。十年的 null 难道
不判了吗？

`user?.address?.city` ——
一行的事。豪意值回升至 85%。
</code></pre>

</td>
</tr>
<tr>
<td>

<pre><code>git commit -m "fix: null
pointer in user lookup"
</code></pre>

</td>
<td>

<pre><code>🎧 *(虚空打碟中把所有改动
加入暂存区)*

git commit -m "fix: 十年的null
pointer难道不判了吗"
git push

推上去了，豪意值+1 🔥
</code></pre>

</td>
</tr>
</table>

**代码逻辑一样正确。但你的终端从此有了灵魂。**

---

## 快速开始

### 安装

```bash
# 一键安装
claude skills install jiahao-skill

# 或手动
git clone https://github.com/lhao17202-hue/jiahao-skill.git
cp -r jiahao-skill ~/.claude/skills/
```

### 使用

在 Claude Code 中说任意一句：

| 效果 | 你说 |
|------|------|
| 🟢 开启 | `开启嘉豪` / `来点嘉豪` / `变身嘉豪` |
| 🔥 拉满 | `自在极意豪` / `火力全开` / `拉满` |
| 🌱 调低 | `微豪一下` / `轻一点` / `收一收` |
| 🔴 关闭 | `关闭嘉豪` / `别装了` / `够了` |

**零学习成本。说话就能控制。**

---

## 交互演示

不想装？直接看效果：

```bash
python scripts/demo.py           # 完整演示（打字效果）
python scripts/demo.py --quick   # 快速预览
python scripts/demo.py --level 3 # 只看自在极意豪
```

<details>
<summary>📺 点击展开 demo 输出预览</summary>

<pre>
══════════════════════════════════════════════════════════════

场景一：写代码
🧑 用户：帮我写个快速排序

────────────────────────────────────────

🌱 轻度 · 微豪：

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    ...

# O(n log n)，稳稳的。这段代码的豪意值还行 🎧

────────────────────────────────────────

🔥 中度 · 标准嘉豪：

🎧 *(虚空打碟中扫了一眼排序需求)*

十年的数组难道不排了吗？排！接好：
...

────────────────────────────────────────

🌪️ 重度 · 自在极意豪：

🖤 *(身穿黑色卫衣，推了推3D口罩...)*

十年的数组难道不排了吗？十年的O(n²)难道不优化了吗？不！
看我用自在极意豪之力终结乱序：
...
</pre>

</details>

---

## 三层浓度

| 浓度 | 别名 | 语录密度 | 代码影响 | 适合 |
|------|------|:--:|:--:|------|
| 🌱 **轻度** | 微豪 | ~30% | 零影响 | 日常开发，轻调味 |
| 🔥 **中度** | 标准嘉豪 | ~70% | 注释嘉豪化 | 大多数情况（**默认**） |
| 🌪️ **重度** | 自在极意豪 | 100% | 变量名+注释全面嘉豪化 | 深夜 coding、hackathon |

**Claude 每 5-6 轮主动问你要不要调浓度。** 不用记命令。

---

## 项目结构

```
jiahao-skill/
├── README.md                     ← 你在这
├── SKILL.md                      ← 核心指令
├── LICENSE                       ← MIT
├── CONTRIBUTING.md               ← 贡献指南
├── assets/
│   └── jiahao-logo.png           ← 黑袍口罩嘉豪
├── references/
│   └── jiahao-encyclopedia.md    ← 12章嘉豪知识库
├── scripts/
│   ├── aw-logo.py                ← AW签名输出
│   ├── jiahao-news.py            ← 嘉豪日报
│   ├── jiahao-banner.py          ← 终端横幅
│   └── demo.py                   ← 交互演示
└── .github/
    └── ISSUE_TEMPLATE/
```

---

## 社区

### 🏅 在你的 README 里挂豪意值徽章

```markdown
[![豪意值](https://img.shields.io/badge/%E8%B1%AA%E6%84%8F%E5%80%BC-XX%25-purple)](https://github.com/lhao17202-hue/jiahao-skill)
```

把 `XX` 换成你的豪意值分数。**让全世界知道你的代码有多"豪"。**

### 🤝 贡献

十年的 PR 难道不提了吗？提！

- 🐛 [报 Bug](https://github.com/lhao17202-hue/jiahao-skill/issues/new?template=bug_report.md)
- 💡 [提建议](https://github.com/lhao17202-hue/jiahao-skill/issues/new?template=feature_request.md)
- 📖 [贡献新语录/新分支到百科](CONTRIBUTING.md)

<a href="https://github.com/lhao17202-hue/jiahao-skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=lhao17202-hue/jiahao-skill" />
</a>

---

## ⭐ Star 历史

如果嘉豪让你的终端多了点乐子，**点个 star**——豪意值 +1，虚空打碟更带劲。

<a href="https://star-history.com/#lhao17202-hue/jiahao-skill&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=lhao17202-hue/jiahao-mode&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=lhao17202-hue/jiahao-mode&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=lhao17202-hue/jiahao-mode&type=Date" />
  </picture>
</a>

---

## FAQ   # #常见问题解答

<details>   < details>
<summary><b>代码质量会受影响吗？</b></summary><summary><b>代码质量会受影响吗？</   & lt;b></   & lt;summary>

不会。**代码正确性是绝对底线。** 轻度模式代码零影响；中度和重度只影响注释和命名风格。人设是滤镜，不是哈哈镜。
</   & lt;details>

<details>   < details>
<summary><b>和 system prompt 有什么区别？</b></summary><summary><b>和 system prompt 有什么区别？</   & lt;b></   & lt;summary>

System prompt 是死的，改了要重启。嘉豪模式有 **三层浓度 + 主动询问 + 场景感知**——是一个完整的交互系统，不是一段死文字。
</details>   < / details>

<details>   < details>
<summary><b>能只在特定场景用吗？</b></summary><summary><b>能只在特定场景用吗？</   & lt;b></   & lt;summary>

当然。日常轻度，debug 时说"拉满"切到重度，修完说"收一收"回来。浓度切换即时生效。
</details>   < / details>

<details>   < details>
<summary><b>不了解嘉豪梗能用吗？</b></summary><summary><b>不了解嘉豪梗能用吗？</   & lt;b></   & lt;summary>

能。即使不知道梗的背景——"一个中二 DJ 在终端里帮你写代码"本身就是有趣的体验。而且所有嘉豪背景都在 SKILL.md 和百科里有介绍，Claude 读过就懂。
</details>   < / details>

---

## 许可证

MIT © 2025 嘉豪模式 contributorsMIT © 2025 嘉豪模式 contributors

"嘉豪"的文化知识产权属于互联网。把它变成了一个 Claude 能穿上的皮肤。

---

<br>   < br>

<p align="center">   <p align   对齐="center"   "center">
  <b>🖤🎧 穿上黑色卫衣。戴上 3D 口罩。The Spectre 已开始播放。</b>
  <br><br>   <br><br>
  <b>码，写起来。十年的 star 难道不点了吗？点。🎧🖤</b>
</p>   < / p>
