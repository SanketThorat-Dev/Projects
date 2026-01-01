terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config" # Points to your local Minikube
}

resource "kubernetes_namespace" "dev_namespace" {
  metadata {
    name = "devops-project-ns"
  }
}