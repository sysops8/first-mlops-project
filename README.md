# Модель прогнозирования диабета — MLOps-проект (FastAPI + Docker + K8s)


Этот проект помогает изучить создание и развертывание ML-модели на простом и приближенном к реальности примере: прогнозирование наличия диабета у человека на основе медицинских показателей. Мы пройдем весь путь:
```
✅ Обучение модели
✅ Сборка модели локально
✅ Развертывание API с помощью FastAPI
✅ Контейнеризация с Docker
✅ Развертывание в Kubernetes
```
Этапы проекта:
- Получаем открытые данные с сайта plotly.github.com в формате csv 
- Подгототавливаем данные, берем определенные колонки с данными
- Используем алгоритм случайного леса для обчуения модели (запускаем train.py)
- Сохраняем модель в формат pkl (файл diabetes_model.pkl)
- Даем доступ к модели через fastapi используя конечную точку /predict


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
kubectl apply -f k8s-deploy.yml
```
