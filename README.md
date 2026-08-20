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

## License

Zira 系列字体是 [Iosevka](https://github.com/be5invis/Iosevka) 的派生作品
（Modified Version），与 Iosevka 一样采用 **SIL Open Font License 1.1** 发布。

- 完整许可文本与合规说明见 [`LICENSE.md`](LICENSE.md)（含 Iosevka 原始版权声明与 OFL 1.1 全文）。
- 每个构建出的字体都在元数据中内嵌了 Iosevka 版权声明与 OFL 许可（OFL 条件 2），
  同时 workflow 会把 `LICENSE.md` 一并复制到 `zira/` 随字体发布。
- Iosevka 未声明保留字体名（Reserved Font Name），派生字体改名 “Zira …” 发布符合 OFL 要求。
