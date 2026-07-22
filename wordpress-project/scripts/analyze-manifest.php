<?php
// Get manifest from ZIP
$zip = new ZipArchive();
$zip->open('/exports/tshirtswiss-kit.zip');
$manifest = json_decode($zip->getFromName('manifest.json'), true);

echo "Pages in manifest:\n";
echo str_repeat("=", 80) . "\n";

if (isset($manifest['content']['pages'])) {
    foreach ($manifest['content']['pages'] as $page_id => $page_meta) {
        $title = $page_meta['title'] ?? 'UNKNOWN';
        echo "$page_id: $title\n";
    }
} else {
    echo "No pages in manifest['content']['pages']\n";
}

echo "\n";

// Now list the actual JSON files in the ZIP
echo "JSON files in content/page/:\n";
echo str_repeat("=", 80) . "\n";

for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    if (str_starts_with($stat['name'], 'content/page/') && str_ends_with($stat['name'], '.json')) {
        $data = json_decode($zip->getFromIndex($i), true);
        $title = $data['title'] ?? 'NO TITLE';
        echo $stat['name'] . ": $title\n";
    }
}

$zip->close();
