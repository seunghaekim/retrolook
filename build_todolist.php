<?php
    $get_config = file_get_contents('./config.json', 'r');
    $config = json_decode($get_config);

    // mapping the config.json to variable
    $baseurl = $config->{'baseurl'};
    $baseurl = $baseurl.'archives';

    $archives = file_get_contents($baseurl, 'r');

    $dom = new DOMDocument;
    $dom -> loadHTML($archives);
    $todo_lv1 = array();

    // get monthley list of archives page
    foreach($dom -> getElementsByTagName('a') as $todo) {
        $attr = $todo->getAttribute('href');
        $checker = preg_match('/\/archives\/[0-9]{4}$/', $attr);
        if ($checker > 0) {
            $todo_lv1[] = $attr;
        };
    };

    // get article list from monthley list

 ?>
