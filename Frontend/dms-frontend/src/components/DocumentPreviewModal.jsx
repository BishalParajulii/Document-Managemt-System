import "../css/DocumentPreviewModal.css";

const DocumentPreviewModal = ({ fileUrl, onClose }) => {
  if (!fileUrl) return null;

  return (
    <div className="preview-overlay">
      <div className="preview-container">
        <button className="close-btn" onClick={onClose}>✕</button>

        <iframe
          src={fileUrl}
          title="Document Preview"
          className="preview-iframe"
        />
      </div>
    </div>
  );
};

export default DocumentPreviewModal;