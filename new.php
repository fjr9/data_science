<?php
function btcid_query($method, array $req = array()) {
// API settings
$key = ''; // your API-key
$secret = ''; // your Secret-key
$req['method'] = $method;
$req['nonce'] = time();
// generate the POST data string
$post_data = http_build_query($req, '', '&');
$sign = hash_hmac('sha512', $post_data, $secret);
// generate the extra headers
$headers = array(
'Sign: '.$sign,
'Key: '.$key,
);
// our curl handle (initialize if required)
static $ch = null;
if (is_null($ch)) {
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/4.0 (compatible;
BITCOINCOID PHP client; '.php_uname('s').'; PHP/'.phpversion().')');
}
curl_setopt($ch, CURLOPT_URL, 'https://vip.bitcoin.co.id/tapi/');
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
// run the query
$res = curl_exec($ch);
if ($res === false) throw new Exception('Could not get reply:
'.curl_error($ch));
$dec = json_decode($res, true);
if (!$dec) throw new Exception('Invalid data received, please make sure
connection is working and requested API exists: '.$res);
}

curl_close($ch);
$ch = null;
return $dec;
$result = btcid_query('getInfo');
print_r($result);
