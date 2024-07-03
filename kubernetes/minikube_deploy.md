
## Local deploy:
1. Build docker img locally:

        docker build --no-cache -t manufacturers/app -f .\manufacturer_service\Dockerfile .\manufacturer_service\

2. Start minikube and load img:

        -> minikube start
        -> minikube image load manufacturers/app

3. Apply deployments:

        -> kubectl apply -f .\kubernetes\manufacturers\fastapi-deployment.yml

        -> kubectl apply -f .\kubernetes\manufacturers\database-deployment.yml

4. Forward port:

        -> kubectl port-forward deployment.apps/cars-microservice 8004:8000
5. Curl locally:

        -> curl http://localhost:8000/api/v1/manufacturers/docs

### Useful commnads:
List:

    kubectl get all

Apply a manifest:

    kubectl apply -f .\kubernetes\manufacturers\fastapi-deployment.yml


Get logs from 1st pod:

    kubectl logs -f $(kubectl get pods -o jsonpath='{.items[0].metadata.name}')
