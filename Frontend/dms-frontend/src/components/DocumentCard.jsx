import "../css/DocumentCard.css";

const DocumentCard = ({ doc, onOpen }) => {
  const handleDoubleClick = () => {
    if (!doc.file) {
      alert("No file attached");
      return;
    }
    onOpen(doc);
  };

  return (
    <div
      className="document-card"
      onDoubleClick={handleDoubleClick}
      title="Double click to open"
    >
      <div className="doc-header">
        <h3>{doc.title}</h3>
        {doc.is_locked && <span className="lock-badge">🔒</span>}
      </div>

      <p className="created-by">Created by: {doc.created_by}</p>
      <small className="date">
        {new Date(doc.created_at).toLocaleString()}
      </small>
    </div>
  );
};

export default DocumentCard;
