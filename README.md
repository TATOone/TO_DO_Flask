# 📝 Flask To-Do API

Простой REST API на Flask для управления задачами (to-do), без базы данных — всё хранится в памяти.

---

## 🚀 Возможности

- Получить список всех задач (`GET /tasks`)
- Добавить новую задачу (`POST /tasks`)
- Обновить задачу (`PUT /tasks/<id>`)
- Удалить задачу (`DELETE /tasks/<id>`)

---

## 🧱 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/TO_DO_Flask.git
cd TO_DO_Flask
```
### 2. Установи зависимости

```bash
python -m venv .venv
source .venv/bin/activate        # для Linux/macOS
 .venv\Scripts\activate         # для Windows
```
### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```
### 4. Запуск
После установки зависимостей можно запустить сервер Flask:

```bash
python app.py
```
Сервер будет работать на http://127.0.0.1:5000/ и готов принимать запросы.
