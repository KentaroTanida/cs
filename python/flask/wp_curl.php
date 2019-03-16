<?php

//API
//$url = 'http://0.0.0.0:5050';
$url = 'http://0.0.0.0:5050/v1/target';

$data = array(
'name'=>$users,
'phone'=>'090-xxxx-xxxx'
);

$data_json = json_encode($data);
echo $data_json;


// curlを初期化
$ch = curl_init();

// 設定!
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-type: application/json'));
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($ch, CURLOPT_URL, $url); // 送り先
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json); // 送信データ
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // 実行結果取得の設定

//echo $url;

// 実行！
$output = curl_exec($ch);
echo $output;
// リソースを閉じる
curl_close($ch);

?>
