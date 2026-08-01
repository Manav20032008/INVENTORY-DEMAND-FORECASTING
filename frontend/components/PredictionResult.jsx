export default function PredictionResult({ result }) {
  if (!result) return null

  return (
    <section className="card result-card">
      <div className="card-header">
        <h2>Prediction Result</h2>
        <p>Model forecast for the selected store and item.</p>
      </div>
      <div className="result-grid">
        <div className="metric">
          <span>Predicted Sales</span>
          <strong>{result.predicted_sales.toFixed(2)}</strong>
        </div>
        <div className="metric">
          <span>Store</span>
          <strong>{result.store}</strong>
        </div>
        <div className="metric">
          <span>Item</span>
          <strong>{result.item}</strong>
        </div>
      </div>
    </section>
  )
}
