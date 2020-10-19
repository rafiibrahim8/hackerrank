<?php
// https://www.hackerrank.com/challenges/birthday-cake-candles/problem

function birthdayCakeCandles($candles) {
    $blow = 0;
    $max = 0;
    for($i=0;$i<count($candles);$i++){
        if($candles[$i]==$max){
            $blow++;
        }else if($candles[$i]>$max){
            $max = $candles[$i];
            $blow=1;
        }
    }
    return $blow;

}

$candles_count = intval(trim(fgets(STDIN)));
$candles_temp = rtrim(fgets(STDIN));
$candles = array_map('intval', preg_split('/ /', $candles_temp, -1, PREG_SPLIT_NO_EMPTY));
echo birthdayCakeCandles($candles)."\n";
?>