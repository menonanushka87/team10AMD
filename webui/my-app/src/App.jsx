import React from 'react';
import './App.css'; // Import your CSS file

const App = () => {
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
            title="1. Upload Files: Click 'Upload Files' to select and upload your SARIF and csv files.
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
              <h3>Step 1</h3>
              <p>Upload CSV file</p>
              <input type="file" accept=".csv" />
            </div>
            <div className="step">
              <h3>Step 2</h3>
              <p>Upload SARIF file</p>
              <input type="file" accept=".sarif" />
            </div>
          </div>
          <div className="generate-button">
            <button>Generate</button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
