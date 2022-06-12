---
marp: true
theme: 386jp
header: MUDS DDoS Web系講座
footer: Copyright 2022 @386jp All Rights Reserved.
---

<!-- _class: lead -->

# Web講座

Faculty of Data Science, Musashino University
Kyosuke Miyamura

> website: [386.jp](https://386.jp)
> twitter: [@386_jp](https://twitter.com/386_jp)
> mail: [ask@386.jp](mailto:ask@386.jp)

---

# 一連の講座の目的

> Webに関する基礎的な知識をつけた上で未来創造プロジェクトなどで製作したPythonアプリをWebアプリとして公開する

---

# 発想とデプロイメントのサイクル

> 1. 発想
> 1. システム構想
> 1. システム構築
> 1. デプロイメント

このサイクルができることによって、テクノロジーを使ってできることの幅が広がる・発信できる

---

# Web概論

> 本講座では、IPアドレスやポートなどのネットワークに関する基礎知識から、現代でよく使われているWebサイトの要素技術などについて解説します。

> **キーワード**: IPアドレス, ドメイン, DNS, ポート番号, TCP, UDP, 5G, World Wide Web, HTML, CSS, JavaScript, API, JSON, WebSocket

---

#  Webセキュリティ基礎

> 本講座では、特にWeb上に公開するアプリケーションを制作する際に必要な、最低限のセキュリティに関する知識と施策について解説します。Webやネットワークに関する事前知識を必要としますので、Web概論を受講することを強くおすすめします。

> **キーワード**: SQLインジェクション, ハッシュ, ブルートフォースアタック, ファイヤウォール, 公開鍵認証, SSH, 踏み台サーバー, SSL, WAF

---

# Webアプリ開発概論

> 本講座では、DockerやAWSなど、Webアプリケーション開発において必要な開発支援技術について解説します。なお、本講座内でGitやDockerについての解説を行いますが、詳しい解説は、別途他の講師によって開催されている別講座を参照してください。また、本講座はWebセキュリティ基礎と共に受講することをおすすめします。

> **キーワード**: Git, GitHub, SSH, Docker, docker-compose, Kubernetes, AWS, EC2, セキュリティグループ, キーペア, CloudFlare, CDN, WAF, CloudFlare Argo Tunnel

---

#  脱初心者ポートフォリオ概論

> 本講座では、ポートフォリオのレベルを1段上げたい方に向けて、JAMStackと呼ばれるコンテンツ管理手法を中心に解説します。一部、Webやネットワークに関する事前知識を必要としますので、Web概論を受講することをおすすめします。

> **キーワード**: JAMStack, Jekyll, Markdown, WordPress, Headless CMS, API, Contentful, ドメイン / 独自ドメイン, DNS, CDN, PageSpeed Insight, Google Analytics, Google Search Console

---

#  Webアプリ開発演習1・2

> 本講座では、PythonのWebフレームワークであるFastAPIを用いて、Webアプリケーションを講座の参加者とともに制作していきます。座学系のWeb関連講座を事前に受講することをおすすめします。また、実際にコードを書いたりしながら講座を進めていきますので、Python開発環境をお手持ちのパソコンに必ず構築した上で受講してください。 (事前準備資料を配布する予定ですが、時間の都合上、基本的にプログラミングなどに関するサポートは講座内では行いませんのでご了承ください)

> キーワード (演習1): FastAPI, Django, Flask, API, React, Docker, docker-compose, SQL, ORM / OR Mapper, PostgreSQL, MySQL / MariaDB, SQLAlchemy, SQLModel, NGINX, プロキシ / リバースプロキシ, CloudFlare Argo Tunnel
> キーワード (演習2, 演習1に加え): WebSocket