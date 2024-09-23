<?php

$curl = curl_init();
$api ='https://www.gis.dcnr.state.pa.us/agsprod/rest/services/Parks/State_Parks/MapServer/3/query?where=1%3D1&outFields=PARK_NAME%2CNAVIGATION_LATITUDE%2CNAVIGATION_LONGITUDE%2CNAVIGATION_DESCRIPTION%2CPARK_REGION%2CGEOCACHE%2CGEOCACHE_LINK&outSR=4326&returnGeometry=false&f=json';
curl_setopt_array($curl, array(
  CURLOPT_URL => $api,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
));

$response = curl_exec($curl);
curl_close($curl);
$json = json_decode($response);
$park = array();
 foreach($json as $v){
    if(is_array($v)) {
     foreach($v as $d){
        if(isset($d->attributes->PARK_NAME)){
            $park[$d->attributes->PARK_NAME]['long'] = $d->attributes->NAVIGATION_LONGITUDE;

            $park[$d->attributes->PARK_NAME]['lat'] = $d->attributes->NAVIGATION_LATITUDE;

            $park[$d->attributes->PARK_NAME]['type'] = $d->attributes->NAVIGATION_DESCRIPTION;

            $park[$d->attributes->PARK_NAME]['region'] = $d->attributes->PARK_REGION;

         }
      }
    }
 }

ksort($park);
$region=array();
foreach($park as $park_name => $p) {
    if($park_name == "Big Spring" && $p['region'] == NULL) {
        $p['region'] = "3";
    }
        if($p['region'] == "1") {
            $r = "North";
        }

        if($p['region'] == "2") {
            $r = "West";
        } 

        if($p['region'] == "3") {
            $r = "South";
        }

        if($p['region'] == "4") {
            $r = "East";
        }

         
        //adds type to the array
        //$region[$r][$park_name][$p['type']]  = $p['lat'] . "," . $p['long'];
        $region[$r][$park_name]  = $p['lat'] . "," . $p['long'];
        
    
}
ksort($region);
print_r($region);

