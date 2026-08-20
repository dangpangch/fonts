# Zira Fonts

基于 [Iosevka](https://github.com/be5invis/Iosevka) 的自定义构建计划（`private-build-plans.toml`）生成 Zira 系列字体：**Zira Mono**、**Zira Sans**、**Zira Serif**。

## 构建流程

推送到 `main` 分支（且改动涉及 `private-build-plans.toml` 或 `.github/workflows/**`），或在 Actions 页面手动触发 **Build Zira Fonts** workflow，GitHub Actions 会自动：

1. 克隆 Iosevka 源码（默认 tag `v34.8.0`，手动触发时可用 `iosevka_ref` 输入覆盖）；
2. 读取 `private-build-plans.toml` 中声明的所有 `[buildPlans.*]` 计划并构建（TTF + WOFF2，提示后）；
3. 将产物整理提交到本仓库：

| 目录 | 内容 |
| --- | --- |
| `zira/ttf` | 提示后的 TTF 字体（取自 Iosevka 构建产物 `dist/*/TTF/*.ttf`） |
| `zira/woff2` | WOFF2 网页字体（取自 `dist/*/WOFF2/*.woff2`） |

> 由于自动提交只改动 `zira/`，不会再次触发构建，避免循环。
