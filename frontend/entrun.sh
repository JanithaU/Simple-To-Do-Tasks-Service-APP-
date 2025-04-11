#!/bin/sh

# Inject API URL into config.js
cat <<EOF > /usr/share/nginx/html/config.js
window.env = {
  API_BASE_URL: "${API_BASE_URL}"
};
EOF

exec "$@"