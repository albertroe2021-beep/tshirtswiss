<?php
$zip_path = '/exports/tshirtswiss-kit.zip';
$zip = new ZipArchive();
$zip->open($zip_path);

echo "Pages in ZIP:\n";
echo str_repeat("-", 80) . "\n";

$pages_found = [];

for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    if (strpos($stat['name'], 'content/page/') === 0 && substr($stat['name'], -5) === '.json') {
        $content = $zip->getFromIndex($i);
        $parsed = json_decode($content, true);
        
        $title = $parsed['title'] ?? 'UNKNOWN';
        $pages_found[] = ['file' => $stat['name'], 'title' => $title];
        
        echo "File: {$stat['name']}\n";
        echo "  Title: $title\n";
        echo "  Content elements: " . (isset($parsed['content']) ? count($parsed['content']) : 'N/A') . "\n";
    }
}

$zip->close();

echo "\n";
echo "Total pages: " . count($pages_found) . "\n";
