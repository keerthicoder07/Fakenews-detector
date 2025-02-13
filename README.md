<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
# Fake News Detection API

## Overview
This project is a Fake News Detection API built with **FastAPI** and a fine-tuned **DeBERTa model**. It predicts the truthfulness of a given statement using natural language processing techniques.

## Features
- Accepts text input for fake news classification
- Uses a **fine-tuned `sileod/deberta-v3-base-tasksource-nli` model**
- Returns predictions as one of six categories: `False`, `Barely True`, `Half True`, `True`, `Mostly True`, `Pants on Fire`

- React frontend for user interaction

---

## Tech Stack
- **Backend**: FastAPI, Transformers (Hugging Face), PyTorch, MongoDB
- **Frontend**: React.js, Axios
- **Database**: MongoDB

---

## Setup Instructions

### Backend Setup (FastAPI)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/fake-news-detection.git
   cd fake-news-detection/backend
   ```

2. **Create a virtual environment & activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB (if required)**
   Ensure MongoDB is running locally or provide a connection string to **MongoDB Atlas** in `.env`.

5. **Run the FastAPI server**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend Setup (React)

1. **Navigate to the frontend folder**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

---

## API Endpoints

### 1. Predict Fake News
- **URL:** `POST /predict`
- **Description:** Accepts a text statement and returns a classification result.
- **Request Body (Form-Data):**
  ```json
  {
    "statement": "NASA is planning to launch a space hotel by 2030."
  }
  ```
- **Response:**
  ```json
  {
    "statement": "NASA is planning to launch a space hotel by 2030.",
    "prediction": "False"
  }
  ```

---

## Required Dependencies

### Backend (Python)
Install these using:
```bash
pip install -r requirements.txt
```

```text
fastapi
pydantic
transformers
torch
uvicorn


### Frontend (React)
Install these using:
```bash
npm install
```

```text
react
axios
```

---

## Contribution
Feel free to contribute by submitting **pull requests** or reporting issues!

---

## License
This project is **MIT Licensed**. See `LICENSE` for details.

>>>>>>> 2f0c20f571c6e673a0566d75d76ee70b5046d56b
