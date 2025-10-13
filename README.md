# rds-auto-start-stop
AWS Lambda + EventBridge による RDS 自動起動・停止スクリプト

# rds-auto-start-stop
Lambda + EventBridge による RDS 自動起動・停止スクリプト

## 1.機能概要
EventBridgeで指定したスケジュールに基づいて、Lambdaを呼び出し、RDSインスタンスを自動で起動・停止する。

## 2.開発背景・目的
RDSは一度停止しても、7日間経つと自動で起動される。停止するのを忘れていると多額のコストが発生してしまうことがあり、
実業務にてRDSのコスト最適化が課題に上がり、自動起動・停止の方法が検討された。    
最終的にはopswitchが採用されたが、Lambdaでの自動化にも可能性を感じ、自習環境で実装に挑戦した。  
業務での課題を自分なりにコードで再現し、運用自動化の理解を深めることが目的である。

## 3.使用技術
- AWS Lambda(Python 3.13)：RDSの起動・停止処理をPythonで記述  
- Amazon EventBridge：スケジュール（cron式）による定期実行  
- AWS RDS (MySQL)：起動・停止の対象  


## 4.構成
