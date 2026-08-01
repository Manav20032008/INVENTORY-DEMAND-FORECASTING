import { useState } from "react";
import PredictionForm from "../components/PredictionForm";
import PredictionResult from "../components/PredictionResult";
import ErrorAlert from "../components/ErrorAlert";
import { createPrediction } from "../services/predictionService";

export default function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (payload) => {
    setLoading(true);
    setError("");
    try {
      const data = await createPrediction(payload);
      setResult(data);
    } catch (err) {
      setError(err.message);
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="page">
      <div className="page-header">
        <h2>Forecast Sales Demand</h2>
        <p>
          Submit engineered features to the XGBoost model and store the result in
          PostgreSQL prediction history.
        </p>
      </div>
      <ErrorAlert message={error} onRetry={() => setError("")} />
      <div className="home-grid">
        <PredictionForm onSubmit={handleSubmit} loading={loading} />
        <PredictionResult result={result} />
      </div>
    </section>
  );
}
