import "./DocumentCard.css"; // we’ll create this next

const DocumentCard = ({ doc }) => {
  if (!doc) return null;

  return (
    <div className="doc-card">
    <h3>{doc.title}</h3>
    <p>Created by: {doc.created_by}</p>
    <small>{new Date(doc.created_at).toLocaleString()}</small>
    </div>

  );
};


export default DocumentCard;
