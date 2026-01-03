import { useEffect, useState } from "react";
import api from "../api/axios";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import DocumentCard from "../components/DocumentCard";
import UploadModal from "../components/UploadModal";
import "../css/Documents.css";

const Documents = () => {
  const [docs, setDocs] = useState([]);
  const [active, setActive] = useState("all");
  const [showUpload, setShowUpload] = useState(false);

  useEffect(() => {
    loadDocs();
  }, [active]);

  const loadDocs = async () => {
    try {
      const endpoint = active === "mine" ? "my-docs/" : "docs/";
      const res = await api.get(endpoint);
      setDocs(res.data);
    } catch (err) {
      console.error("Failed to load documents:", err);
    }
  };

  return (
    <div className="documents-layout">
      <Sidebar active={active} setActive={setActive} />

      <div className="documents-main">
        <Topbar onUpload={() => setShowUpload(true)} />

        <div className="documents-grid">
          {docs.length > 0 ? (
            docs.map((doc) => <DocumentCard key={doc.id} doc={doc} />)
          ) : (
            <p className="empty-text">No documents found</p>
          )}
        </div>
      </div>

      {showUpload && (
        <UploadModal
          onClose={() => setShowUpload(false)}
          onSuccess={loadDocs}
        />
      )}
    </div>
  );
};

export default Documents;
