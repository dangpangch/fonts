# Zira Fonts

基于 [Iosevka](https://github.com/be5invis/Iosevka) 构建的派生字体：**Zira Mono**、**Zira Sans**、**Zira Serif**。

## 发布

推送到 `v*` tag（如 `./release.sh 0.1.0`）或手动触发后，两个 workflow 依次自动执行：

1. **Release Zira Fonts**（`build-fonts.yml`）：先检查 `private-build-plans.toml` 自上个发布 tag 以来是否修改——**未修改则跳过构建**；有修改才克隆 Iosevka 源码（默认 `v34.8.0`，可指定 `iosevka_ref`）→ 按 `private-build-plans.toml` 中所有 `[buildPlans.*]` 构建（TTF + WOFF2）→ 上传 GitHub Release 资产（`zira-ttf.zip`、`zira-woff2.zip`，桌面下载用）；
2. **Publish to npm**（`publish-npm.yml`）：Release 成功后自动触发，**先确认带版本号的 Release 真实存在**（构建被跳过则不发）→ 下载 `zira-woff2.zip` → 发布 npm 包 `zira-font`（Web 用，含 WOFF2 + CSS）。

构建产物不提交进仓库。

## 网页引用（jsDelivr npm CDN）

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/zira-font@latest/zira/fonts.css"
/>
```

```css
font-family: "Zira Mono"; /* 或 Zira Sans / Zira Serif */
```

固定版本（推荐生产使用）：

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/zira-font@0.1.0/zira/fonts.css"
/>
```

## 桌面字体

从 [Releases](https://github.com/dangpang/zira-font/releases) 下载 `zira-ttf.zip` / `zira-woff2.zip`。

## License

Zira 为 Iosevka 的派生作品，采用 **SIL Open Font License 1.1** 发布。全文与合规说明见 [`LICENSE.md`](LICENSE.md)。
