#!/bin/bash
kubectl apply -f webapp-service.yaml
kubectl apply -f webapp-deployment.yaml 
kubectl apply -f nginx-deployment.yaml 
kubectl apply -f nginx-service.yaml 
#kubectl apply -f nginx-ingress.yaml 
kubectl apply -f postgres-deployment.yaml 
kubectl apply -f postgres-service.yaml 

