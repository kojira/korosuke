# ころすけ

<img src="https://cdn.discordapp.com/attachments/402183554588475415/888416831021387806/unknown.png" height="200px"/>

ダイスを振るだけのdiscordボットです。
おまけ音声チャンネルの入退出通知機能があります。


# 設定
.env.example ファイルの名前を .env に書き換えて
以下の項目を埋めてください。
BOT_TOKENはdiscordから発行されるbotのトークン。

NOTICE_CHANNEL_IDSは音声チャットの入退出ログを投稿するチャンネルのIDをカンマ区切りで指定してください。

```
BOT_TOKEN=replace your bot token
NOTICE_CHANNEL_IDS=
```

# 起動方法

```sh
docker compose up -d
```
でbotが起動します


# コマンド書式

```
.[数字]d[数字]
```

例)
```
2d6 6面ダイスを2個
d12 12麺ダイスを1個
d10 10面ダイスを2個
d100 100面ダイスを1個
10d1000 1000面ダイスを10個
```

