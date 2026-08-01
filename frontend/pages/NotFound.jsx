import { Link } from "react-router-dom"

export default function NotFound() {
  return (
    <section className="page not-found">
      <div className="card empty-state">
        <h2>404</h2>
        <p>The page you requested does not exist.</p>
        <Link to="/" className="btn btn-primary">
          Back to Predict
        </Link>
      </div>
    </section>
  )
}
