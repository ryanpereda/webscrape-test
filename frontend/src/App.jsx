import { useState } from "react";


function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");


  const handleUpload = async (event) => {
    event.preventDefault();

    if (!file) {
      setError("Please select a CSV file.");
      return;
    }

    setError("");
    setResult(null);

    const formData = new FormData();

    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/upload/",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(data.error || "Upload failed.");
        return;
      }

      setResult(data);

    } catch (error) {
      setError("Could not connect to the server.");
      console.error(error);
    }
  };


  return (
    <main>
      <h1>Data Miner</h1>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".csv"
          onChange={(event) =>
            setFile(event.target.files[0])
          }
        />

        <button type="submit">
          Upload and Analyze
        </button>
      </form>

      {error && (
        <p>{error}</p>
      )}

      {result && (
        <section>
          <h2>Dataset Analysis</h2>

          <p>
            <strong>File:</strong> {result.filename}
          </p>

          <p>
            <strong>Rows:</strong> {result.rows}
          </p>

          <p>
            <strong>Columns:</strong> {result.columns}
          </p>

          <h3>Column Names</h3>

          <ul>
            {result.column_names.map((column) => (
              <li key={column}>
                {column}
              </li>
            ))}
          </ul>

          <h3>Preview</h3>

          <pre>
            {JSON.stringify(result.preview, null, 2)}
          </pre>
        </section>
      )}
    </main>
  );
}


export default App;