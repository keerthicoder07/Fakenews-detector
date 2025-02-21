import React, { useState } from "react";
import "./App.css"; // Import CSS
import "font-awesome/css/font-awesome.min.css"; // Font Awesome for icons

function App() {
  const [statement, setStatement] = useState("");
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("No file chosen"); // Track file name
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);

    const formData = new FormData();

    if (file) {
      formData.append("file", file);
    } else if (statement.trim()) {
      formData.append("text", statement.trim());
    } else {
      setError("Please enter a statement or upload a file.");
      return;
    }

    try {
      const response = await fetch("https://fakenews-detector.vercel.app/api/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        if (response.status === 500) throw new Error("Server error: Internal error");
        if (response.status === 422) throw new Error("Validation error: Invalid input");
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);

      // Reset input fields
      setStatement("");
      setFile(null);
      setFileName("No file chosen");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <h1>📰 Fake News Detector</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={statement}
          onChange={(e) => setStatement(e.target.value)}
          placeholder="Enter news statement..."
        />

        <div className="file-input-wrapper">
          <label htmlFor="file-upload" className="file-label">
            <i className="fa fa-upload"></i> {fileName}
          </label>
          <input
            id="file-upload"
            type="file"
            accept=".txt, .docx, .pdf"
            onChange={(e) => {
              const selectedFile = e.target.files[0];
              setFile(selectedFile);
              setFileName(selectedFile ? selectedFile.name : "No file chosen");
            }}
          />
        </div>

        <button type="submit">
          <i className="fa fa-check"></i> Check
        </button>
      </form>

      {error && <div className="error">❌ {error}</div>}

      {result && (
        <div className="result">
          <strong>Prediction:</strong> {result.label} 
        </div>
      )}
    </div>
  );
}

export default App;
