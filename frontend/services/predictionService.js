import api from "./api"

export const createPrediction = async (payload) => {
  const response = await api.post("/api/v1/predict", payload)
  return response.data
}

export const fetchPredictions = async (params = {}) => {
  const response = await api.get("/api/v1/predictions", { params })
  return response.data
}
