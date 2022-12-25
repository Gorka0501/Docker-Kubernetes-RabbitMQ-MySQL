kubectl apply -f rabbitmq-secrets.yaml
kubectl apply -f mysql-secrets.yaml
kubectl apply -f volumen-persistente.yaml
kubectl apply -f mysql.yaml
kubectl apply -f rabbitmq.yaml
kubectl apply -f app.yaml