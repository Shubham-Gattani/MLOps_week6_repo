# **MLOps Week 6 Assignment – Continuous Deployment with Docker & Kubernetes**

## **🎯 Assignment Objective**

This assignment demonstrates the implementation of a complete **MLOps CI/CD pipeline** by containerizing the IRIS ML model as a FastAPI service and automating its deployment to Google Kubernetes Engine (GKE) using GitHub Actions.

## **🚀 Complete Workflow Overview**

### **Development Phase (Dev Branch)**
```
Code Changes → Push to Dev → Automated Testing → CML Report → PR Review
```

### **Production Deployment (Main Branch)**
```
PR Merge to Main → Build Docker Image → Push to Artifact Registry → Deploy to GKE → Live API
```

## **🛠️ Technology Stack**

- **ML Framework**: Scikit-learn, FastAPI
- **Version Control**: Git, DVC (Data Version Control)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Orchestration**: Kubernetes (GKE)
- **Cloud Services**: GCP (GCS, Artifact Registry, GKE)
- **Testing**: pytest, CML

## **📁 Repository Structure**

```
MLOps_week6_repo/
├── .github/workflows/
│   ├── ci-dev.yml              # CI: Testing on dev branch
│   └── ci-main.yml             # CI/CD: Testing + Deployment on main
├── tests/
│   ├── test_data_validation.py # Data quality tests
│   └── test_model_evaluation.py # Model performance tests
├── iris_fastapi.py            # FastAPI application
├── Dockerfile                 # Containerization setup
├── requirements.txt           # Python dependencies
├── train.py                   # Model training script
├── get_data.py               # Data version management
├── model.joblib              # Trained model (DVC tracked)
├── data/data.csv             # Dataset (DVC tracked)
└── README.md                 # This file
```

## **🔧 Key Components Explained**

### **1. Data & Model Versioning (DVC)**
```bash
# DVC tracks large files in GCS, not Git
dvc init --no-scm
dvc remote add -d myremote gs://your-bucket/week_2
dvc pull  # Downloads actual data/model files
```
**Concept**: DVC stores data/models in cloud storage while keeping lightweight pointers (`.dvc` files) in Git for version control.

### **2. FastAPI ML Service**
```python
# iris_fastapi.py - Production API
@app.post("/predict/")
def predict_species(data: IrisInput):
    prediction = model.predict(input_df)[0]
    return {"predicted_class": prediction}
```
**Features**: 
- REST API for model predictions
- Input validation with Pydantic
- Health check endpoints

### **3. Containerization (Docker)**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8200
CMD ["uvicorn", "iris_fastapi:app", "--host", "0.0.0.0", "--port", "8200"]
```
**Key Insight**: Docker image contains only the runtime environment - no DVC needed in production.

### **4. Kubernetes Deployment**
```yaml
# GKE Deployment & Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: iris-api-deployment
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: iris-api
        image: us-central1-docker.pkg.dev/.../iris-api:latest

apiVersion: v1
kind: Service
metadata:
  name: iris-api-service
spec:
  type: LoadBalancer
  ports:
  - port: 80           # External port
    targetPort: 8200   # Internal container port
```

## **🔄 CI/CD Pipeline Details**

### **Development Branch CI (`ci-dev.yml`)**
**Triggers**: Push to `dev` + PR to `main`
**Actions**:
- Set up Python environment
- Install dependencies
- Pull data/model from DVC
- Run pytest test suite
- Generate CML report with model metrics
- **NO deployment** - only validation

### **Main Branch CD (`ci-main.yml`)**
**Triggers**: Push to `main` (after PR merge)
**Actions**:
- All CI steps from dev pipeline
- **Build Docker image** with latest code
- **Push to Artifact Registry** with commit SHA tag
- **Deploy to GKE** using `kubectl set image`
- **Verify rollout** status

## **🔐 GCP Setup & Authentication**

### **Required Services**
1. **Google Kubernetes Engine (GKE)**: Cluster for deployment
2. **Artifact Registry**: Docker image repository
3. **Google Cloud Storage (GCS)**: DVC remote storage
4. **Service Account**: CI/CD automation

### **GitHub Secrets**
```yaml
GCP_CREDENTIALS:    # Service account JSON key
GH_PAT:            # GitHub Personal Access Token
```

### **Service Account Roles**
- `artifactregistry.writer` - Push Docker images
- `container.admin` - Deploy to GKE
- `storage.admin` - Access GCS for DVC

## **🎯 Accessing the Deployed Application**

### **Find Your Application URL**
```bash
kubectl get service iris-api-service
```
**Output**: `EXTERNAL-IP` column shows your application URL

### **Test Endpoints**
```bash
# Home page
curl http://[EXTERNAL-IP]

# Prediction endpoint
curl -X POST "http://[EXTERNAL-IP]/predict/" \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## **💡 Key MLOps Concepts Demonstrated**

### **1. Ephemeral Environments**
- GitHub Actions creates fresh VMs for each run
- DVC pulls data/models from scratch every time
- Ensures true reproducibility

### **2. Quality Gates**
- **Dev branch**: Testing and validation only
- **Main branch**: Production deployment after successful PR
- Automated blocking of broken deployments

### **3. Container Best Practices**
- Small base image (`python:3.10-slim`)
- Multi-stage builds (when applicable)
- Environment-specific configurations
- Health checks and graceful shutdowns

### **4. Kubernetes Patterns**
- Deployment for application lifecycle
- Service for network access
- LoadBalancer for external traffic
- Rolling updates for zero-downtime deployments

### **5. Security Considerations**
- Service accounts with minimal permissions
- Secrets management in GitHub
- Private image repositories
- Network security policies

## **✅ Assignment Completion Status**

| Component | Status |
|-----------|--------|
| FastAPI ML Service | ✅ Complete |
| Docker Containerization | ✅ Complete |
| GitHub Actions CI | ✅ Complete |
| GitHub Actions CD | ✅ Complete |
| GKE Deployment | ✅ Complete |
| DVC Integration | ✅ Complete |
| Automated Testing | ✅ Complete |
| CML Reporting | ✅ Complete |