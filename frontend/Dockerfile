FROM nginx:alpine

# Copy static files
COPY . /usr/share/nginx/html

# Copy custom entrypoint script
COPY entrun.sh /entrun.sh
RUN chmod +x /entrun.sh

ENTRYPOINT ["/entrun.sh"]
CMD ["nginx", "-g", "daemon off;"]