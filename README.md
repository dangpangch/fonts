# Zira Fonts

基于 [Iosevka](https://github.com/be5invis/Iosevka) 构建的派生字体：**Zira Mono**、**Zira Sans**、**Zira Serif**。

## 发布

推送到 `v*` tag（如 `./release.sh 0.1.0`）或手动触发 **Release Zira Fonts** workflow（填 `version`）后自动：

1. 克隆 Iosevka 源码（默认 `v34.8.0`，可指定 `iosevka_ref`）；
2. 按 `private-build-plans.toml` 中所有 `[buildPlans.*]` 构建（TTF + WOFF2）；
3. 上传 GitHub Release 资产（`zira-ttf.zip`、`zira-woff2.zip`，桌面下载用）；
4. 发布 npm 包 `@dangpang/zira-fonts`（Web 用，含 WOFF2 + CSS）。

构建产物不提交进仓库。

## 网页引用（jsDelivr npm CDN）

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@dangpang/zira-fonts@latest/zira/fonts.css"
/>
```

```css
font-family: "Zira Mono"; /* 或 Zira Sans / Zira Serif */
```

固定版本（推荐生产使用）：

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@dangpang/zira-fonts@0.1.0/zira/fonts.css"
/>
```

## 桌面字体

从 [Releases](https://github.com/dangpangch/fonts/releases) 下载 `zira-ttf.zip` / `zira-woff2.zip`。

## License

Zira 为 Iosevka 的派生作品，采用 **SIL Open Font License 1.1** 发布。全文与合规说明见 [`LICENSE.md`](LICENSE.md)。
