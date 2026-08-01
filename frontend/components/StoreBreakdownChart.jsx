import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

function aggregateByStore(predictions) {
  const map = new Map();

  predictions.forEach((row) => {
    const key = row.store;
    const current = map.get(key) || { store: `Store ${key}`, total: 0, count: 0 };
    current.total += row.prediction;
    current.count += 1;
    map.set(key, current);
  });

  return [...map.values()]
    .map((entry) => ({
      store: entry.store,
      average: Number((entry.total / entry.count).toFixed(2)),
      count: entry.count,
    }))
    .sort((a, b) => a.store.localeCompare(b.store, undefined, { numeric: true }));
}

export default function StoreBreakdownChart({ predictions }) {
  const data = aggregateByStore(predictions);

  if (!data.length) {
    return (
      <div className="chart-empty">
        <p>No store breakdown available yet.</p>
      </div>
    );
  }

  return (
    <ResponsiveContainer width="100%" height={280}>
      <BarChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" vertical={false} />
        <XAxis dataKey="store" tick={{ fontSize: 11 }} />
        <YAxis tick={{ fontSize: 11 }} width={48} />
        <Tooltip
          contentStyle={{
            borderRadius: 10,
            border: "1px solid #e2e8f0",
            boxShadow: "0 8px 24px rgba(15, 23, 42, 0.08)",
          }}
          formatter={(value, name) => {
            if (name === "average") return [value, "Avg prediction"];
            return [value, name];
          }}
        />
        <Bar dataKey="average" fill="#0ea5e9" radius={[8, 8, 0, 0]} maxBarSize={56} />
      </BarChart>
    </ResponsiveContainer>
  );
}
