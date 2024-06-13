import React, { useState } from 'react';
import './styles.css'; // Import your CSS file

const App = () => {
  const [csvFile, setCsvFile] = useState(null);
  const [sarifFile, setSarifFile] = useState(null);

  const handleCsvFileChange = (event) => {
    setCsvFile(event.target.files[0]);
  };

  const handleSarifFileChange = (event) => {
    setSarifFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    // Previous code to handle file uploads
  
    try {
      const response = await fetch('http://localhost:8000/api/upload/', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      alert('Files uploaded and processed successfully!');
      console.log('Server response:', data);
  
      // Optionally update UI based on processed data (csvData and sarifVulnerabilities)
      // Example:
      // setCsvData(data.csvData);
      // setSarifVulnerabilities(data.sarifVulnerabilities);
  
    } catch (error) {
      console.error('Error uploading files:', error);
      alert('Error uploading files. Please try again later.');
    }
  };
s  

  return (
    <div>
      <header>
        <div className="logo">
          <h1>Team 10 Hackathon</h1>
        </div>
        <nav>
          <a href="#">Home</a>
        </nav>
      </header>
      <main>
        <section className="description">
          <h2>
            Are you in a <span className="vulnerable">Vulnerable</span> spot?
          </h2>
          <p>
            Our Code Vulnerability Checker is the ultimate tool to protect your
            code from potential threats. We can analyze the code and detect any
            vulnerability such as bugs, security weaknesses, and possible
            exploits.
          </p>
          <button className="instructions-btn">
            Instructions
          </button>
        </section>
        <section className="upload">
          <h2>Get started by uploading your files</h2>
          <div className="upload-steps">
            <div className="step">
              <h3>Step 1</h3>
              <p>Upload CSV file</p>
              <input type="file" accept=".csv" onChange={handleCsvFileChange} />
            </div>
            <div className="step">
              <h3>Step 2</h3>
              <p>Upload SARIF file</p>
              <input type="file" accept=".sarif" onChange={handleSarifFileChange} />
            </div>
          </div>
          <div className="generate-button">
            <button onClick={handleSubmit}>Generate</button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
