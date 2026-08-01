export default function PredictionRangeBar({ analytics }) {
  if (!analytics || analytics.total_predictions === 0) {
    return (
      <div className="chart-empty">
        <p>Run predictions to see the forecast range.</p>
      </div>
    )
  }

  const { lowest_prediction: min, highest_prediction: max, average_prediction: avg } = analytics
  const span = max - min || 1
  const avgPct = ((avg - min) / span) * 100

  return (
    <div className="range-bar">
      <div className="range-bar__labels">
        <span>Low {min.toFixed(2)}</span>
        <span>Avg {avg.toFixed(2)}</span>
        <span>High {max.toFixed(2)}</span>
      </div>
      <div className="range-bar__track">
        <div className="range-bar__fill" />
        <div className="range-bar__marker" style={{ left: `${avgPct}%` }} title={`Average: ${avg.toFixed(2)}`} />
      </div>
      <p className="range-bar__caption">
        Spread of {span.toFixed(2)} units across {analytics.total_predictions} stored predictions
      </p>
    </div>
  )
}
