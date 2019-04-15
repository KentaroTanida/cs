<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>form</title>
</head>
<body>

<!-- php -S localhost:8000 form.php -->


<h2>お問い合わせ</h2>

<form method="post">
  <p>name</p>
  <input type="text" name="name">

  <p>age</p>
  <select name="age">
  <option value="未選択">選択してください。</option>
    <?php
        for ($i=6; $i <= 100; $i++) {
            echo "<option value='${i}'>$i</option>";
    }
    ?>
  </select>

  <p>type</p>
   <?php
     $types = array('サイトについて',
                    'サイトについての意見',
                    'サポート方法',
                    '実装依頼',
                    'その他')
  ?>
  <select name="category">
  <option value="未選択">選択してください。</option>
  <?php
    foreach ($types as $type) {
      echo "<option value='$type'>$type</option>";
     }
  ?>
  </select>

  <p>text</p>
  <textarea type="text" name="body"></textarea>

  <input type="submit" value="送信">
</form>


<?php
$name = $_POST['name'];
$age = $_POST['age'];
$category = $_POST['category'];
$body = $_POST['body'];
echo $name.'<br>';
echo $age.'<br>';
echo $category.'<br>';
echo $body.'<br>';
?>

</body>
