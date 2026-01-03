import { useState } from "react";
import api from "../api/axios";
import "../css/UploadModal.css";

const UploadModal = ({ onClose, onSuccess }) => {
  const [title, setTitle] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (!title) {
      setError("Title is required");
      return;
    }

    const formData = new FormData();
    formData.append("title", title);
    if (file) formData.append("file", file);

    try {
      setLoading(true);
      await api.post("docs/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      onSuccess(); // reload docs
      onClose();   // close modal
    } catch (err) {
      console.error("Upload error:", err);
      setError("Upload failed. Check console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-overlay">
      <div className="upload-modal">
        <h2>Upload Document</h2>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Document Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
          />

          {error && <p className="error">{error}</p>}

          <div className="actions">
            <button type="button" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" disabled={loading}>
              {loading ? "Uploading..." : "Upload"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default UploadModal;
