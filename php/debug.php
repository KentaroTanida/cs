<?php
function console_log( $data ){
  echo '<script>';
  echo 'console.log('. json_encode( $data ) .')';
  echo '</script>';
}

$myvar = array(1,2,3);
console_log( $myvar ); // [1,2,3]
?>


// 参考
// http://lighthouse-dev.hatenablog.com/entry/2018/03/08/121727
// https://php.net/manual/ja/debugger.php
