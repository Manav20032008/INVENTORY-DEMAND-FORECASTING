import { useCallback, useEffect, useState } from "react";
import { fetchPredictions } from "../services/predictionService";

export default function usePredictions({ page = 1, limit = 20, store = null } = {}) {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadPredictions = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const params = { page, limit };
      if (store != null && store !== "") {
        params.store = Number(store);
      }
      const data = await fetchPredictions(params);
      setPredictions(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err.message);
      setPredictions([]);
    } finally {
      setLoading(false);
    }
  }, [page, limit, store]);

  useEffect(() => {
    loadPredictions();
  }, [loadPredictions]);

  return { predictions, loading, error, reload: loadPredictions };
}
