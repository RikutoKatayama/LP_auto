# LP_auto
本システムは、大学の教務システムである「LiveCampus」を自動で入力するシステムである。

本研究は、その第一段階として、教務システムの機能の1つである「ラーニング・ポートフォリオ」の自動化のみ行っている。

<br>

# Description
ラーニング・ポートフォリオとは、学生が自身の学生生活の振り返りをする機能である。

「前期の評価」と「今期の目標」の2種類があり、合計20以上の項目を埋めなければならない。

<br>



# Features
本システムは、いくつかの質問に答えることで、入力する内容を決定し、自動で入力することができる。

本システムの具体的な処理の流れは以下の図のようになっている。

<img src="https://user-images.githubusercontent.com/101154269/233535090-e2f62563-61fc-4486-9065-6e4e3fd2b4c9.png" width="400">

<br>

# DEMO
### ①ボタンをクリックする（今回は「評価と目標の両方」をクリック）
<img src="https://user-images.githubusercontent.com/101154269/233531296-3dcd98ac-7fba-435a-afbc-e14224561097.jpg" width="250">


### ②以下の質問に答え、「実行」をクリックする
<img src="https://user-images.githubusercontent.com/101154269/233532087-de084340-4270-445f-855d-b4b1ec6a759d.jpg" width="250">

### ③自動入力完了
<img src="https://user-images.githubusercontent.com/101154269/233551033-a3313349-8c03-4460-971f-8dadae1e1fb3.png" width="180">

<br>
 
# Requirement
 
* Docker 20.10
* Django 4.0.1
* Selenium 3.141.0
 
 
