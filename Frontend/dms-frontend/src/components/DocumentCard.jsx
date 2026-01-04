import "../css/DocumentCard.css";

const DocumentCard = ({ doc, onOpen }) => {
  const handleDoubleClick = () => {
    if (!doc.file) {
      alert("No file attached");
      return;
    }
    onOpen(doc.file);
  };

  return (
    <div
      className="document-card"
      onDoubleClick={handleDoubleClick}
      title="Double click to open"
    >
      <h3>{doc.title}</h3>
      <p>Created by: {doc.created_by}</p>
      <small>{new Date(doc.created_at).toLocaleString()}</small>
    </div>
  );
};

export default DocumentCard;
