<?php
    $get_config = file_get_contents('./config.json', 'r');
    $config = json_decode($get_config);

    // mapping the config.json to variable
    $baseurl = $config->{'baseurl'};
    $archive_url = $baseurl.'archives';

    $archives = file_get_contents($archive_url, 'r');

    $dom = new DOMDocument;
    $dom -> loadHTML($archives);
    $todoMonth = array();

    // get yeally list of archives page
    foreach($dom -> getElementsByTagName('a') as $todo) {
        $attr = $todo->getAttribute('href');
        $checker = preg_match('/\/archives\/[0-9]{4}$/', $attr);
        if ($checker > 0) {
            for ($i=0; $i < 12; $i++) {
                $month = str_pad($i + 1, 2, '0', STR_PAD_LEFT);
                $todoMonth[] = $attr.$month;
            };
        };
    };

    // get an archive from monthley page
    foreach ($todoMonth as $key => $value) {

        $url = $baseurl . substr($value, 1);
        $a_month = file_get_contents($url, 'r');

        $dom = new DOMDocument;
        $dom -> loadHTML($a_month);
        $an_archives = array();

        foreach ($dom -> getElementsByTagName('a') as $a) {
            $attr = $a -> getAttribute('href');
            $checker = preg_match('/\/archives\/[0-9]{8}?([a-z])/', $attr);
            if ($checker > 0) {
                $an_archives[] = $attr;
                echo $attr.'<br />';
            };
        };
    };

    foreach ($an_archives as $key => $value) {
        $url = $baseurl . substr($value, 1);
        $an_archive = file_get_contents($url, 'r');

        $dom = new DOMDocument;
        $dom -> loadHTML($an_archive);

        $class_name = 'description';
        $query = sprintf('//div[@class="%s"]', $class_name);

        $xpath = new DOMXPath($dom);
        $article = $xpath -> query($query);

        foreach ($article as $key => $value) {
            var_dump($value);
        }
    }

    // rlk_raw_documents
    // | ref_numb | document  | cit | parsed_date   | archive_date
    // | int      | long text | url | datetime      | date
    //
    // TODO
    // dataExtractor.php -> extract initial data from document.
    // daileyParser.php -> dailey parser from neolook.com
    //
