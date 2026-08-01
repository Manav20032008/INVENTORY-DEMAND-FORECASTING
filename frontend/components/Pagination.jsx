export default function Pagination({ page, limit, itemCount, onPageChange }) {
  const hasPrev = page > 1;
  const hasNext = itemCount >= limit;

  return (
    <div className="pagination">
      <span className="pagination__info">
        Page {page} · showing {itemCount} record{itemCount === 1 ? "" : "s"}
      </span>
      <div className="pagination__actions">
        <button
          type="button"
          className="btn btn-secondary btn-sm"
          disabled={!hasPrev}
          onClick={() => onPageChange(page - 1)}
        >
          Previous
        </button>
        <button
          type="button"
          className="btn btn-secondary btn-sm"
          disabled={!hasNext}
          onClick={() => onPageChange(page + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}
