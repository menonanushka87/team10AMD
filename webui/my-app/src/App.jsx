import React, { useState } from 'react';
import './App.css'; 

const App = () => {
  const [csvFile, setCsvFile] = useState(null);
  const [sarifFile, setSarifFile] = useState(null);
  const [analysisResults, setAnalysisResults] = useState(null); 

  const handleCsvFileChange = (event) => {
    setCsvFile(event.target.files[0]);
  };

  const handleSarifFileChange = (event) => {
    setSarifFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!sarifFile) {
      alert('Please upload both CSV and SARIF files.');
      return;
    }

    const formData = new FormData();
    // formData.append('csvFile', csvFile);
    formData.append('sarifFile', sarifFile);

    try {
      const response = await fetch('http://localhost:8000/api/upload/', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setAnalysisResults(data); 
      alert('Files uploaded successfully!');
      console.log('Server response:', data);
    } catch (error) {
      console.error('Error uploading files:', error);
      alert('Error uploading files. Please try again later.');
    }
  };

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
          <button
            className="instructions-btn"
            aria-describedby="tooltip"
            title="1. Upload Files: Click 'Upload Files' to select and upload your SARIF and CSV files.
                  2. Analyze Commits: The tool will parse the files and identify the commits that introduced new issues.
                  3. View Results: See a list of problematic commits with details such as commit hash, author, date, and issues introduced.
                  4. Visualize Changes: Use the visualization tools to explore the impact of each commit.
                  5. Download Report: Optionally download a report of the analysis."
          >
            Instructions
          </button>
        </section>
        <section className="upload">
          <h2>Get started by uploading your files</h2>
          <div className="upload-steps">
            <div className="step">
              {/* <h3>Step 1</h3> */}
              <p>Upload CSV file</p>
              <input type="file" accept=".csv" onChange={handleCsvFileChange} />
            </div>
            <div className="step">
              {/* <h3>Step 2</h3> */}
              <p>Upload SARIF file</p>
              <input type="file" accept=".sarif" onChange={handleSarifFileChange} />
            </div>
          </div>
          <div className="generate-button">
            <button onClick={handleSubmit}>Generate</button>
          </div>
        </section>
        

        {analysisResults && (
          <section className="analysis-results">
            <h2>Analysis Results</h2>
            <div className="result-item">
              <h3>New Issues:</h3>
              <pre>
                {analysisResults.issues_only_in_file2.map(issue => (
                <div key={issue[0]}>
                <p><strong>File:</strong> {issue[0]}</p>
                <p><strong>Line Number:</strong> {issue[1]}</p>
                <p><strong>Severity:</strong> {issue[2]}</p>
                <p><strong>Type:</strong> {issue[3]}</p>
                <p><strong>Description:</strong> {issue[4]}</p>
                <br />
              </div>
              ))}
              </pre>
            </div>
          </section>
        )}
      </main>
    </div>
  );
};

export default App;