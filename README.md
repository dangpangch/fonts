# Zira Fonts

基于 [Iosevka](https://github.com/be5invis/Iosevka) 构建的派生字体：**Zira Mono**、**Zira Sans**、**Zira Serif**。

## 构建

推送到 `main`（改动涉及 `private-build-plans.toml` 或 `.github/workflows/**`）或手动触发 **Build Zira Fonts** workflow 后自动：

1. 克隆 Iosevka 源码（默认 `v34.8.0`，可手动指定 `iosevka_ref`）；
2. 按 `private-build-plans.toml` 中所有 `[buildPlans.*]` 构建（TTF + WOFF2）；
3. 提交产物到 `zira/`：

| 目录             | 内容                     |
| ---------------- | ------------------------ |
| `zira/ttf`       | TTF 字体                 |
| `zira/woff2`     | WOFF2 网页字体           |
| `zira/fonts.css` | 生成的 @font-face 样式表 |

## 网页引用（jsDelivr，仓库需 public）

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/dangpangch/fonts@main/zira/fonts.css"
/>
```

```css
font-family: "Zira Sans"; /* 或 Zira Mono / Zira Serif */
```

或直接引用单个 WOFF2：

```css
@font-face {
  font-family: "Zira Sans";
  src: url("https://cdn.jsdelivr.net/gh/dangpangch/fonts@main/zira/woff2/ZiraSans-Regular.woff2")
    format("woff2");
  font-weight: 400;
  font-style: normal;
}
```

<!--缓存：`@main` 缓存约 12 小时（更新后可到 https://www.jsdelivr.com/tools/purge 清除）；正式使用请在手动触发时填 `tag`（如 `v1.0.0`），用 `@v1.0.0` 固定版本（永久缓存）。-->

## License

Zira 为 Iosevka 的派生作品，采用 **SIL Open Font License 1.1** 发布。全文与合规说明见 [`LICENSE.md`](LICENSE.md)。
