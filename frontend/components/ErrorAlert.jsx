export default function ErrorAlert({ message, onRetry }) {
  if (!message) return null

  return (
    <div className="error-alert" role="alert">
      <strong>Something went wrong , Try Practically Possible Value.</strong>
      <p>{message}</p>
      {onRetry && (
        <button type="button" className="btn btn-secondary" onClick={onRetry}>
          Try again
        </button>
      )}
    </div>
  )
}
