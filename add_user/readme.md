# Add user in kubeflow

- Add dex user
    - https://webcache.googleusercontent.com/search?q=cache:codIIO8MtYkJ:https://www.kubeflow.org/docs/distributions/kfctl/multi-user/+&cd=2&hl=en&ct=clnk&gl=sg

    - Download the dex config
        - kubectl get configmap dex -n auth -o jsonpath='{.data.config\.yaml}' > dex-config.yaml

    - Edit the dex config with extra users.
    - The password must be hashed with bcrypt with an at least 10 difficulty level.
        - python generate-pwd-hash.py pwd

    - After editing the config, update the ConfigMap
        - kubectl create configmap dex --from-file=config.yaml=dex-config.yaml -n auth --dry-run -o yaml | kubectl apply -f -

    -  Restart Dex to pick up the changes in the ConfigMap
        - kubectl rollout restart deployment dex -n auth

- Add kubeflow user profile
    - create a new user profile, matching the dex user.
        - kubectl apply -f user-profile.yaml