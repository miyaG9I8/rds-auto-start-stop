# rds-auto-start-stop
AWS Lambda + EventBridge による RDS 自動起動・停止スクリプト

## 1.機能概要
EventBridgeで指定したスケジュールに基づいて、Lambdaを呼び出し、RDSインスタンスを自動で起動・停止する。

## 2.開発背景・目的
実業務において、RDSのコスト最適化が課題となり、「毎朝自動で起動し、夜に自動で停止する」仕組みが求められた。  
最終的にはOpswitchを利用して実装されたが、  Opswitchを使わずにLambda + EventBridgeで同様の仕組みを構築できるかを学習目的で検証した。

業務での課題を自分なりにコードで再現し、  
AWS運用自動化の理解を深めることを目的としている。

## 3.使用技術
- AWS Lambda(Python 3.13)：RDSの起動・停止処理をPythonで記述  
- Amazon EventBridge：スケジュール（cron式）による定期実行  
- AWS RDS (MySQL)：起動・停止の対象  

## 4.構成
![Architecture](./docs/architecture.svg)

1. ローカル環境でPythonベースのLambda関数（start/stop）を作成。
2. Lambda関数をAWSにデプロイし、実行ロールを設定。
3. EventBridgeルールでスケジュール実行を設定
・起動：月曜から金曜の9:00(0 0 ? * MON-FRI *)
・停止：月曜から金曜の21:00(0 12 ? * MON-FRI *)
4. Lambda関数内でRDSを起動・停止。
