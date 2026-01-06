# Модель прогнозирования диабета — первый MLOps-проект (FastAPI + Docker + K8s)
<img width="726" height="478" alt="{C71083A4-F970-40CB-B5C3-C0AB7566CAB8}" src="https://github.com/user-attachments/assets/4f6ed8f1-0793-4fc8-adac-9699b83162b6" />

#### Этот проект помогает изучить создание и развертывание ML-модели на простом и приближенном к реальности примере: прогнозирование наличия диабета у человека на основе медицинских показателей. Мы пройдем весь путь:
```
✅ Обучение модели
✅ Сборка модели локально
✅ Развертывание API с помощью FastAPI
✅ Контейнеризация с Docker
✅ Развертывание в Kubernetes
```
## Задача

Предсказать, есть ли у человека диабет, на основе следующих параметров:
- Количество беременностей (Pregnancies)
- Уровень глюкозы (Glucose)
- Артериальное давление (Blood Pressure)
- Индекс массы тела — BMI
- Возраст (Age)

Используется классификатор Random Forest, обученный на датасете Pima Indians Diabetes Dataset.

## Быстрый старт
1. Клонировать репозиторий
```bash
git clone https://github.com/iam-veeramalla/first-mlops-project.git
cd first-mlops-project
```

2. Создать виртуальное окружение
```bash
python3 -m venv .mlops
source .mlops/bin/activate
```

4. Установить зависимости
```bash
pip install -r requirements.txt
```

## Обучение модели
```bash
python train.py
```

**Запуск API локально**
```bash
uvicorn main:app --reload
```

Пример входных данных для /predict
```jsonnet
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}
```
## **Контейнеризация API с Docker**
Сборка Docker-образа
```bash
docker build -t diabetes-prediction-model .
```

## **Запуск контейнера**
```bash
docker run -p 8000:8000 diabetes-prediction-model
```

## **Развертывание в Kubernetes**
```bash
kubectl apply -f diabetes-prediction-model-deployment.yaml
```
