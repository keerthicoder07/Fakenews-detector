import React, { useState } from "react";
import "./App.css"; // Import your CSS file

function App() {
  const [statement, setStatement] = useState("");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    
    if (file) {
      formData.append("file", file);
    } else if (statement.trim()) {
      formData.append("statement", statement.trim());
    } else {
      alert("Please enter a statement or upload a file.");
      return;
    }

    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      console.error("Server error:", response.status);
      return;
    }

    const data = await response.json();
    setResult(data);
    setStatement(""); // Clear text input
    setFile(null); // Clear file input
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
        <label htmlFor="file-upload" className="file-label">
  Choose File
</label>
<input 
  id="file-upload"
  type="file" 
  accept=".txt, .docx, .pdf" 
  onChange={(e) => setFile(e.target.files[0])} 
/>

        <button type="submit">Check</button>
      </form>

      {result && (
        <div className="result">
          <strong>Prediction:</strong> {result.prediction}
        </div>
      )}
    </div>
  );
}

export default App;
