ゼロ電の請求金額確認 自動化

<背景>
光熱費を一か所に集計して管理したい思いがあり、
まずは、現在電気で利用しているゼロ電の請求金額をプログラム内から取得できる
プログラムを作成検討しました。

<準備・実行>
1.ゼロ電のマイページで、F12を押下し、以下の情報を取得する。

ネットワークタブから、
ApiKey、Systemdivisionを取得する
![image](https://github.com/Shuhey1102/getZeroDenUtilityBill/assets/68799081/c6f9158b-5853-4ff6-84a9-9d6db29f95c2)

2.各Jsonファイルに設定値を入力する

<login.json>
ゼロ電にログインするためのID情報をセットする
![image](https://github.com/Shuhey1102/getZeroDenUtilityBill/assets/68799081/1fa9dcaa-a611-441f-aed3-feb746d0fdaa)

<config.json>
1.で取得した情報をセットする
![image](https://github.com/Shuhey1102/getZeroDenUtilityBill/assets/68799081/a23bd41d-5678-4798-b156-49af12dfeaca)

3.main.pyを実行する

実行結果例(※現状はCUIベースで出力が確認できるのみ)
![image](https://github.com/Shuhey1102/getZeroDenUtilityBill/assets/68799081/d7378b67-bbf5-495d-847a-30c70a0ec5d8)
