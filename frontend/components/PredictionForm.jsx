const defaultValues = {
  store: 1,
  item: 1,
  year: 2017,
  month: 1,
  day: 1,
  daysofweek: 1,
  weekofyear: 1,
  quarter: 1,
  is_weekend: 0,
  lag_1: 15,
  lag_7: 14,
  lag_30: 16,
  rolling_mean_7: 14.8,
  rolling_std_7: 1.2,
  rolling_mean_30: 15.2,
  rolling_std_30: 1.3,
}

const fields = [
  { name: "store", label: "Store ID", type: "number" },
  { name: "item", label: "Item ID", type: "number" },
  { name: "year", label: "Year", type: "number" },
  { name: "month", label: "Month", type: "number" },
  { name: "day", label: "Day", type: "number" },
  { name: "daysofweek", label: "Day of Week (0-6)", type: "number" },
  { name: "weekofyear", label: "Week of Year", type: "number" },
  { name: "quarter", label: "Quarter", type: "number" },
  { name: "is_weekend", label: "Is Weekend (0/1)", type: "number" },
  { name: "lag_1", label: "Lag 1", type: "number", step: "0.01" },
  { name: "lag_7", label: "Lag 7", type: "number", step: "0.01" },
  { name: "lag_30", label: "Lag 30", type: "number", step: "0.01" },
  { name: "rolling_mean_7", label: "Rolling Mean 7", type: "number", step: "0.01" },
  { name: "rolling_std_7", label: "Rolling Std 7", type: "number", step: "0.01" },
  { name: "rolling_mean_30", label: "Rolling Mean 30", type: "number", step: "0.01" },
  { name: "rolling_std_30", label: "Rolling Std 30", type: "number", step: "0.01" },
]

export default function PredictionForm({ onSubmit, loading }) {
  const handleSubmit = (event) => {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const payload = {}

    fields.forEach(({ name }) => {
      const value = formData.get(name)
      payload[name] = name.includes("lag") || name.includes("rolling")
        ? parseFloat(value)
        : parseInt(value, 10)
    })

    onSubmit(payload)
  }

  return (
    <form className="card prediction-form" onSubmit={handleSubmit}>
      <div className="card-header">
        <h2>Demand Prediction</h2>
        <p>Enter store, item, and engineered features to forecast sales.</p>
      </div>
      <div className="form-grid">
        {fields.map((field) => (
          <label key={field.name} className="form-field">
            <span>{field.label}</span>
            <input
              name={field.name}
              type={field.type}
              step={field.step || "1"}
              defaultValue={defaultValues[field.name]}
              required
            />
          </label>
        ))}
      </div>
      <button type="submit" className="btn btn-primary" disabled={loading}>
        {loading ? "Predicting..." : "Run Prediction"}
      </button>
    </form>
  )
}
