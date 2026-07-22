#!/bin/bash
# Import using wp shell with admin context

COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"
KIT_FILE="/exports/tshirtswiss-kit.zip"

echo ""
echo "================================"
echo "IMPORTING VIA WP SHELL"
echo "================================"
echo ""

# Create PHP code to execute
cat > /tmp/import_code.php << 'PHPEOF'
<?php
// Set admin user context
wp_set_current_user(1);

if (!current_user_can('manage_options')) {
    echo "ERROR: User does not have admin capability\n";
    exit(1);
}

echo "User: " . wp_get_current_user()->user_login . "\n";
echo "Admin: " . (current_user_can('manage_options') ? 'YES' : 'NO') . "\n";
echo "\n";

// Now try to trigger Elementor import
echo "Calling wp elementor kit import...\n";

// Use proc_open to call WP-CLI with this context
$descriptorspec = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w"),
   2 => array("pipe", "w")
);

$process = proc_open(
    'wp elementor kit import /exports/tshirtswiss-kit.zip --allow-root',
    $descriptorspec,
    $pipes
);

if (is_resource($process)) {
    fclose($pipes[0]);
    
    $output = stream_get_contents($pipes[1]);
    $errors = stream_get_contents($pipes[2]);
    
    fclose($pipes[1]);
    fclose($pipes[2]);
    
    $return_code = proc_close($process);
    
    echo "Output:\n" . $output . "\n";
    if ($errors) {
        echo "Errors:\n" . $errors . "\n";
    }
    echo "Return code: " . $return_code . "\n";
} else {
    echo "Could not open process\n";
}
?>
PHPEOF

echo "[1/2] Creating import script..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wordpress /bin/bash -c "cat /dev/null > /tmp/import_code.php"
docker compose -f "$COMPOSE_VALIDATION" cp /tmp/import_code.php tshirtswiss-validation-wordpress:/tmp/import_code.php

echo "[2/2] Executing import in WordPress context..."
docker compose -f "$COMPOSE_VALIDATION" exec wordpress php /tmp/import_code.php

echo ""
echo "================================"
