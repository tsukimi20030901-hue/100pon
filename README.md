# 課題14：HTTPステータスコード

## 1. HTTPステータスコードとは

HTTPステータスコードとは、クライアントから送信されたHTTPリクエストに対して、サーバーがどのように処理したかを示す3桁の数字である。

HTTPステータスコードは、以下の5つに分類される。

| 分類 | 意味 |
|---|---|
| 1xx | リクエストの処理状況に関する情報 |
| 2xx | リクエストの成功 |
| 3xx | リダイレクトなど、追加の処理が必要 |
| 4xx | クライアント側のリクエストに関するエラー |
| 5xx | サーバー側で発生したエラー |

## 2. 主なHTTPステータスコード

| コード | 名称 | 意味 |
|---|---|---|
| 200 | OK | リクエストが正常に処理された。 |
| 201 | Created | リクエストが成功し、新しいリソースが作成された。 |
| 204 | No Content | リクエストは成功したが、レスポンスボディは返されない。 |
| 301 | Moved Permanently | リソースのURLが恒久的に変更された。 |
| 302 | Found | リソースが一時的に別のURLに移動している。 |
| 304 | Not Modified | リソースに変更がないため、キャッシュされたデータを利用できる。 |
| 400 | Bad Request | リクエストの形式や内容に問題がある。 |
| 401 | Unauthorized | リクエストを処理するための認証が必要である。 |
| 403 | Forbidden | リソースへのアクセスが拒否された。 |
| 404 | Not Found | 指定されたリソースが見つからない。 |
| 429 | Too Many Requests | 短時間にリクエストを送りすぎたため、制限されている。 |
| 500 | Internal Server Error | サーバー内部で予期しないエラーが発生した。 |
| 503 | Service Unavailable | サーバーが一時的にリクエストを処理できない。 |

## 3. HTTPステータスコードの確認
## 4. 実験結果
`curl -i` コマンドを使用し、httpbinから返されるHTTPステータスコードを確認した。

| リクエストURL | 期待するステータスコード | 確認結果 |
|---|---|---|
| `https://httpbin.org/status/200` | 200 OK | HTTP/2 200 を受信 |
| `https://httpbin.org/status/404` | 404 Not Found | HTTP/2 404 を受信|
| `https://httpbin.org/status/500` | 500 Internal Server Error | HTTP/2 500 を受信 |

```
curl -i https://httpbin.org/status/200
HTTP/2 200 
access-control-allow-credentials: true
access-control-allow-origin: *
access-control-expose-headers: Retry-After, RateLimit, RateLimit-Policy
content-length: 0
content-type: text/html; charset=utf-8
x-content-type-options: nosniff
date: Thu, 29 Oct 2026 15:54:38 GMT
```

## 4. まとめ
HTTPステータスコードは、リクエストの処理結果を把握するために重要である。
ステータスコードの分類と代表的なコードの意味を理解することで、Webサービスの動作確認やエラーの原因調査に役立てられる。