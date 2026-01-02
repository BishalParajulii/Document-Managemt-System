import { useEffect, useState } from "react";
import api from "../api/axios";
import DocumentCard from "../components/DocumentCard";
import "../css/MyDocuments.css";

const MyDocuments = () => {
  const [docs, setDocs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadMyDocs();
  }, []);

  const loadMyDocs = async () => {
    try {
      const res = await api.get("my-docs/");
      setDocs(res.data);
    } catch (err) {
      console.error("Failed to load my documents", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mydocs-container">
      <h2 className="mydocs-title">My Documents</h2>

      {loading && <p className="status">Loading...</p>}

      {!loading && docs.length === 0 && (
        <p className="status">You have not uploaded any documents yet.</p>
      )}

      <div className="mydocs-grid">
        {docs.map((doc) => (
          <DocumentCard key={doc.id} doc={doc} />
        ))}
      </div>
    </div>
  );
};

export default MyDocuments;
