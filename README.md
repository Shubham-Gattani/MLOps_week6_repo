# **MLOps CI/CD Pipeline with GitHub Actions & DVC**

## **🎯 Assignment Objective**

This assignment demonstrates the implementation of a professional MLOps workflow by integrating **Continuous Integration/Continuous Deployment (CI/CD)** with **Data Version Control (DVC)**. The goal is to transform a basic machine learning pipeline into a production-ready system with automated testing, quality gates, and team collaboration features.

## **📁 Repository Structure**

```
MLOps_week2_repo/
├── .github/workflows/          # GitHub Actions CI/CD pipelines
│   ├── ci-dev.yml              # Development branch workflow
│   └── ci-main.yml             # Production branch workflow
├── tests/                      # Automated test suite
│   ├── test_data_validation.py # Data quality tests
│   └── test_model_evaluation.py # Model performance tests
├── data/                       # Dataset directory (DVC tracked)
│   └── data.csv                # Iris dataset
├── get_data.py                 # Data version management
├── train.py                    # Model training pipeline
├── model.joblib                # Trained model (DVC tracked)
├── requirements.txt            # Python dependencies
├── data.dvc                    # DVC pointer for dataset
├── model.joblib.dvc           # DVC pointer for model
└── README.md                   # This file
```

## **🔄 Workflow Summary**

### **Branch Strategy**
- **`dev` branch**: Development and experimentation
- **`main` branch**: Production-ready, stable code

### **CI/CD Pipeline**
1. **Development Phase**: Code changes pushed to `dev` branch
2. **Automated Testing**: GitHub Actions triggers on push to `dev`
   - Fresh Ubuntu environment creation
   - DVC initialization and data/model pull from GCS
   - Data validation tests (schema, missing values)
   - Model evaluation tests (loading, performance metrics)
   - CML report generation with confusion matrix
3. **Code Review**: Pull Request from `dev` → `main`
   - Automated CI runs on PR
   - CML report posted as PR comment
   - Team reviews both code changes AND model metrics
4. **Production Merge**: After approval, merge to `main`
   - Final validation CI run on production branch
   - Production-ready artifact confirmation

## **🔑 Key MLOps Concepts Demonstrated**

### **1. Ephemeral Environments**
- Every CI run starts with a clean Ubuntu VM
- Dependencies installed from scratch each time
- Ensures true reproducibility and complete environment documentation

### **2. Data Versioning with DVC**
- `.dvc` files act as pointers to actual data in Google Cloud Storage
- `dvc pull` fetches exact data versions in CI environments
- Enables reproducible experiments across team members

### **3. ML-Specific Testing**
- **Data Validation**: Schema consistency, missing values, data types
- **Model Evaluation**: Performance thresholds, prediction consistency
- **Integration Testing**: End-to-end pipeline validation

### **4. Quality Gates**
- Development and production have separate CI pipelines
- Tests must pass before merging to main
- Automated checks prevent broken models from reaching production

### **5. Automated ML Reporting**
- CML generates model performance reports
- Confusion matrices and accuracy scores in PR comments
- ML metrics become first-class citizens in code review

### **6. Branch Strategy for ML**
- `dev` branch for experimentation and new features
- `main` branch always production-deployable
- Clear separation between research and production code

## **🚀 Scope for Improvement**

### **Immediate Improvements**
1. **Remove Hardcoded Data Versions** in model tests
   - Current: Tests always use "v1" data regardless of actual workspace state
   - Improved: Tests should use whatever data version is currently checked out

2. **Parameterized Testing**
   - Test multiple data versions automatically
   - Validate model performance across different data distributions

3. **Enhanced Data Validation**
   - Statistical distribution tests
   - Data drift detection between versions
   - Feature correlation validation

### **Medium-term Enhancements**
1. **Model Registry Integration**
   - Version trained models automatically
   - Model performance tracking over time
   - Automated model promotion/demotion

2. **Advanced CI/CD Triggers**
   - Auto-trigger retraining on data changes
   - Performance-based deployment gates
   - A/B testing infrastructure

3. **Monitoring & Alerting**
   - Data quality monitoring in production
   - Model performance degradation detection
   - Automated rollback mechanisms

### **Long-term Vision**
1. **Multi-environment Deployment**
   - Staging, production, canary deployments
   - Feature flag management for ML models
   - Blue-green deployment strategies

2. **Automated Experiment Tracking**
   - Hyperparameter optimization in CI
   - Model comparison and selection
   - Experiment reproducibility at scale

3. **ML Pipeline Orchestration**
   - End-to-end workflow automation
   - Data preprocessing → Training → Validation → Deployment
   - Conditional execution based on test results

## **💡 Key Takeaways**

This implementation demonstrates that **MLOps is not just about tools**, but about **processes and guarantees**:
- **Reproducibility**: Same code + same data = same results
- **Collaboration**: Clear processes for team development
- **Quality**: Automated checks prevent production issues
- **Visibility**: ML metrics are as important as code quality

The pipeline ensures that machine learning systems can be developed, tested, and deployed with the same rigor and reliability as traditional software systems.

---

**Status**: ✅ All core MLOps CI/CD objectives completed  
**Next Steps (immediate)**: Address hardcoded version issues and implement parameterized testing